from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import matplotlib.pyplot as plt

stopWords = set(STOPWORDS)
stopWords.add('video')
stopWords.add('videos')
stopWords.add('game')
stopWords.add('games')
stopWords.add('TV')
stopWords.add('virtual')
stopWords.add('virtual pet')
stopWords.add('pet')
stopWords.add('YouTube')
stopWords.add('channel')
stopWords.add('play')
stopWords.add('Music')
stopWords.add('Oh')
stopWords.add('one')
stopWords.add('good')
stopWords.add('see')
stopWords.add('Yeah')
stopWords.add('will')
stopWords.add('know')
stopWords.add('going')
stopWords.add('think')
stopWords.add('lot')
stopWords.add('well')
stopWords.add('want')

# show WordCloud image from text
def showWordCloudImage(text):
    wordCloud = WordCloud(stopwords = stopWords, max_font_size = 100, background_color = 'white').generate(text)
    #wordCloudImage = wordCloud.to_image()
    #wordCloudImage.show()
    plt.figure()
    plt.imshow(wordCloud, interpolation = "bilinear")
    plt.axis("off")
    plt.show()

def showTop20Words(text):
    wordCloud = WordCloud(stopwords = stopWords)
    text_dictionary = wordCloud.process_text(text)
    frequent_words = {k: v for k, v in sorted(text_dictionary.items(), reverse = True, key = lambda item: item[1])}
    
    top20list = list(frequent_words.items())[:20]
    for index in range(1, len(top20list)):
        print(str(index) + ". " + top20list[index-1][0])