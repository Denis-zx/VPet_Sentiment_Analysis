import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
import openpyxl
import math

# Youtube Customization
api_service_name = "youtube"
api_version = "v3"
# Need to generate a youtube API key (Refer to ReadME for instruction)
DEVELOPER_KEY = "AIzaSyA9ppUqUxkEuWQ4mLBuCezDS2jfObxzmQ0"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

#Helper Function
def request_youtube_comment (videoId):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=videoId,
        maxResults=100
    )
    response = request.execute()

    comments = []

    while response:

        for item in response['items']:

            comment = item['snippet']['topLevelComment']['snippet']
            comments.append([
                comment['authorDisplayName'],
                comment['textDisplay']
            ])

        if 'nextPageToken' in response:
            response = youtube.commentThreads().list(
                    part = 'snippet,replies',
                    videoId = videoId,
                    pageToken = response['nextPageToken']
                ).execute()
        else:
            break
    
    df = pd.DataFrame(comments, columns=['author','message'])
    return df

#Customization Parameter
video_list_poki = ["xJXGtCtEB00","xRhz7bMu8GQ","p-28wa_hMRQ"]
video_list_toma = []

youtube_list = video_list_poki
filename = "youtube_pokimon_"

max_comment_summarized = 70 #Adjust this if exceed the token limit for chatgpt (Excel give 400 bad request), currently chatgpt 3.5 accept 4096 token
prompt = "summarized 5 key insights and output in english"

#Fetching Comment
count = 1
for video_key in youtube_list:
    print(video_key)
    comment_df = request_youtube_comment(video_key)
    comment_df.to_excel(f'{filename}{count}.xlsx',engine='xlsxwriter')
    count += 1


# Adding Excel Fomula for OpenAi  
for i in range(2,2+len(youtube_list)):
    current_dataframe = pd.read_excel(f"{filename}{i+1}.xlsx",sheet_name="Sheet1")
    workbook = openpyxl.load_workbook(f'{filename}{i+1}.xlsx')
    worksheet = workbook.create_sheet("formula")
    for n in range(0,math.ceil(current_dataframe.shape[0]/max_comment_summarized)):
        column = chr(ord('A')+n)
        worksheet[f"{column}1"] = f"comment {max_comment_summarized*n+1} - {max_comment_summarized*(n+1)}"
        worksheet[f"{column}2"] = f'=AI.ask({prompt},Sheet1!C{max_comment_summarized*n+1}:C{max_comment_summarized*(n+1)})'
    workbook.save(f"{filename}{i+1}.xlsx")