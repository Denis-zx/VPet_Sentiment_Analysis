from youtube import youtubeFounctions
from youtube import wordCloudFunctions

# Game: Dudde - My Virtual Pet Dog
searchList_dudde = youtubeFounctions.getSearchList(youtubeFounctions.youtube, "Duddu", "US")
print(len(searchList_dudde))
# titles from search list
titles_dudde = youtubeFounctions.getTitleFormSearchList(searchList_dudde)
# wordCloud for YouTube video's title
wordCloudFunctions.showWordCloudImage(titles_dudde)
# Top 20 words from YouTube video's title
wordCloudFunctions.showTop20Words(titles_dudde)
# wordCloud for YouTube video's description 
descriptions_dudde = youtubeFounctions.getDescriptionFromSearchList(searchList_dudde)
wordCloudFunctions.showWordCloudImage(descriptions_dudde)
# Top 20 words from YouTube video's descriptions
wordCloudFunctions.showTop20Words(descriptions_dudde)
# extract video ids from searchList
videoIds_duddes = youtubeFounctions.getVideoIdFromSearchList(searchList_dudde)
# get trascriptions in English with video ids
transcripts_in_English = youtubeFounctions.getTranscriptsFromVideos(videoIds_duddes)
# wordCloud for YouTube video's transcripts
wordCloudFunctions.showWordCloudImage(transcripts_in_English)
# Top 20 words from YouTube video's transcripts
wordCloudFunctions.showTop20Words(transcripts_in_English)
# Comments in the videos
comments = youtubeFounctions.getCommentsInVideos(videoIds_duddes)
print(comments)