from wordcloud import WordCloud,STOPWORDS

comment_words = ''
stopwords = set(STOPWORDS)

f = open('word cloud.txt','r+')
textData = f.read().replace('\n','')

wordcloud = WordCloud(
	stopwords = stopwords,
	width = 1280,
	height = 720,
	background_color = '#fff',
	min_font_size = 10)
wordcloud.generate(textData)

wordcloud.to_file('WordCloud.png')

print('Successfull')