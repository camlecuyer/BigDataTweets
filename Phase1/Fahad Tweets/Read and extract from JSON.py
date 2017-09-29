import json
from pprint import pprint

#This py code will read from your JSON file the following key(text) & write the output to txt file with ".txt" name.
data_file=open('Twtdata.json','r')
hashtags=open('tweethashtags.txt','w')
urls=open('tweeturls.txt','w')

for x in data_file:

	try:

		tweet=json.loads(x)
		texttt = tweet['text']
		hashsign = '#'

		for word in texttt.split():
			if word[0] in hashsign:
				hashtags.write(word)
				hashtags.write(' ')
			elif "http" in word:
				print(word)
				urls.write(word)
				urls.write(' ')
			else:
				continue
	except:
		hashtags.write(' ')
		urls.write(' ')

