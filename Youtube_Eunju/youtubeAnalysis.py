from youtube import youtubeFounctions
from common import wordCloudFunctions

# Data about 'Tamagotchi' game
searchList = youtubeFounctions.getSearchList(youtubeFounctions.youtube, "tamagotchi game", "US")
# titles from search list
titles = youtubeFounctions.getTitleFormSearchList(searchList)
# wordCloud for YouTube video's title
wordCloudFunctions.showWordCloudImage(searchList)
# Top 20 words from YouTube video's title
wordCloudFunctions.showTop20Words(searchList)
# wordCloud for YouTube video's description 
descriptions = youtubeFounctions.getDescriptionFromSearchList(searchList)
wordCloudFunctions.showWordCloudImage(descriptions)
# Top 20 words from YouTube video's descriptions
wordCloudFunctions.showTop20Words(descriptions)
# extract video ids from searchList
videoIds = youtubeFounctions.getVideoIdFromSearchList(searchList)
# get trascriptions in English with video ids
transcripts_in_English = youtubeFounctions.getTranscriptsFromVideos(videoIds)
# wordCloud for YouTube video's transcripts
wordCloudFunctions.showWordCloudImage(transcripts_in_English)
# Top 20 words from YouTube video's transcripts
wordCloudFunctions.showTop20Words(transcripts_in_English)
# Comments in the videos
comments = youtubeFounctions.getCommentsInVideos(videoIds)
print(comments)
# create a file of the descriptions from videos
youtubeFounctions.getFileOfTranscriptsFromvideos(videoIds, "video_description_from_youtube")