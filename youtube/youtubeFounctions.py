import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from youtube_transcript_api import YouTubeTranscriptApi

# build for search
apiKey = "AIzaSyDfzzk2bxhsNV4dp47TUjJrCvx3i7zDXMw"
youtube = build('youtube', 'v3', developerKey = apiKey)

# get list by searching with keyword
def getSearchList(youtube, keyword, region):
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
    itemsInList = response['items']
    
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
                relevanceLanguage = "EN",
                videoCaption = "closedCaption",
                #videoCategoryId = 20,
                q = keyword,
                pageToken = nextPageToken
            )
            response = request.execute()
            print(response)
            itemsInList.append(response['items'])
            if 'nextPageToken' in response: nextPageToken = response['nextPageToken']
            else: break
    
    return itemsInList

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
