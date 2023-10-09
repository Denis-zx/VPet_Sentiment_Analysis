# YouTube Data Analysis
Contributor: Eunju Yoon (eyoo699)


## README Contents
1. Intallation
2. Repository contents


### Installation
The Google APIs Client Library for Python:

> pip install --upgrade google-api-python-client

[Youtube > Dat API > Guides Quickstarts > Python](https://developers.google.com/youtube/v3/quickstart/python)


### Repository contents
1. youtubeFunctions.py
    functions to build, get, and extract data using YouTube APIs
    * getSearchList(youtube, keyword, region) - to get list by searching with keyword
    * getDescriptionFromSearchList(list) - to get descriptions from search list
    * getTitleFormSearchList(list) - to get titles from search list
    * getVideoIdFromSearchList(list) - to get video id from search list
    * getTranscriptsFromVideos(videoIds) - to get transcripts in videos with video ids
    * getFileOfTranscriptsFromvideos(videoIds, filename) - to get transcripts in videos with video ids and save them in the excel file
    * getCommentsInVideos(videoIds) - to get comments in a video with a video id
2. wordCloudFunctions.py
    functions to 
    * showWordCloudImage(text) - to get WordCloud image from text
    * showTop20Words(text) - to get top 20 words from text
3. youtubeAnalysis.py
    * main file to execute with youtubeFunctions and wordCloudFunctions
4. youtubeExample.ipynb
    * an example step by step to execute functions
5. README.md
    * this file (for markdown)
6. features
    * some example pictures
