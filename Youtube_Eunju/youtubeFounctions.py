import io
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from youtube_transcript_api import YouTubeTranscriptApi

# build for search
apiKey = "AIzaSyDfzzk2bxhsNV4dp47TUjJrCvx3i7zDXMw"
youtube = build('youtube', 'v3', developerKey = apiKey)

# get list by searching with keyword
def getSearchList(youtube, keyword, region):
    itemList = []
    
    # request for search list
    request = youtube.search().list(
        part = "snippet",
        maxResults = 50,
        type = "video", # a particular type of resource
        order = "date", # Resources are sorted in reverse chronological order based on the date they were created
        regionCode = region,
        relevanceLanguage = "en",
        videoCaption = "closedCaption", # Only include videos that have captions
        #videoCategoryId = 20, # filtering video search results based on their category (20 = Gaming)
        q = keyword # query term to search for (use the Boolean NOT (-) and OR (|) operators)
    )
    
    # response from the request
    response = request.execute()
    for item in response['items']:
        itemList.append(item)
    
    if 'nextPageToken' in response:
        nextPageToken = response['nextPageToken']
        # get all results from pages
        while nextPageToken != "":
            request = youtube.search().list(
                part = "snippet",
                maxResults = 50,
                type = "video",
                order = "date",
                regionCode = region,
                relevanceLanguage = "en",
                videoCaption = "closedCaption",
                #videoCategoryId = 20,
                q = keyword,
                pageToken = nextPageToken
            )
            
            response = request.execute()
            for item in response['items']:
                itemList.append(item)
            
            if 'nextPageToken' in response:
                nextPageToken = response['nextPageToken']
            else:
                nextPageToken = ""
                break
    
    return itemList

# get descriptions from search list
def getDescriptionFromSearchList(list):
    descriptions = ""

    for item in list:
        if 'snippet' in item:
            item = item['snippet']
        else: 
            continue
        if'description' in item:
            descriptions += item['description']
        else:
            continue
    
    return descriptions

# get titles from search list
def getTitleFormSearchList(list):
    titles = ""

    for item in list:
        if 'snippet' in item: item = item['snippet']
        else: continue
        if 'title' in item: titles += item['title']
        else: continue
    
    return titles

# get video id from search list
def getVideoIdFromSearchList(list):
    ids = []

    for item in list:
        if 'id' in item: item = item['id']
        else: continue
        if 'videoId' in item: ids.append(item['videoId'])
  
    return ids

# get transcripts in videos with video ids
def getTranscriptsFromVideos(videoIds):
    all_transcripts = ""

    for videoId in videoIds:
        transcrip_language_list = YouTubeTranscriptApi.list_transcripts(videoId)
        
        try:
            if(transcrip_language_list.find_transcript(['en'])):
                transcripts = YouTubeTranscriptApi.get_transcript(videoId, languages=['en'])
                for transcript in transcripts:
                    all_transcripts += transcript['text']
                    all_transcripts += " "
        except:
            print("The video (id: " + videoId + ") has no english transcripts.")
            continue

    return all_transcripts

# get transcripts in videos with video ids and save them in the excel file
def getFileOfTranscriptsFromvideos(videoIds, filename):
    all_transcripts = []

    for videoId in videoIds:
        transcrip_language_list = YouTubeTranscriptApi.list_transcripts(videoId)
        text = ""
        
        try:
            if(transcrip_language_list.find_transcript(['en'])):
                transcripts = YouTubeTranscriptApi.get_transcript(videoId, languages=['en'])
                for transcript in transcripts:
                    text += transcript['text']
                    text += " "
                all_transcripts.append([videoId, text])
        except:
            print("The video (id: " + videoId + ") has no english transcript.")
            continue

    transcriptData = pd.DataFrame(all_transcripts, columns=['id','script'])
    transcriptData.to_excel(f'{filename}.xlsx')

# get comments in a video with a video id
def getCommentsInVideos(videoIds):
    comments = []
    
    for videoId in videoIds:
        try:
            print(videoId)
            request = youtube.commentThreads().list(
                part = "snippet",
                videoId = videoId
            )
            response = request.execute()
            commentList = response['items']
        
            for commentItem in commentList:
                comment = commentItem['snippet']['topLevelComment']['snippet']
                comments.append(comment['textDisplay'])
                
                if 'replies' in commentItem:
                    print("replies")
                    replies = commentItem['replies']['comments']
                    print(replies)
                    for reply in replies:
                        reply = reply['snippet']
                        comments.append(reply['textDisplay'])
                        
        except:
            print("The video (id: " + videoId + ") has a problem.")
            continue
        
    return comments