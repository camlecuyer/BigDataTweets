import json
import sys
import unicodedata

if len(sys.argv) > 1:
    line_generator = open(sys.argv[1], "r")
else:
    line_generator = sys.stdin

#line_generator = open('test_data.txt', "r")

tweets= []
x = ""

for line in line_generator:
#    line = unicodedata.normalize('NFKD', line).encode('utf-8')
    if(line != '\n'):
        tweet = json.loads(line)
        #quoted_status
        if('quoted_status' in tweet):
            if('extended_tweet' in tweet['quoted_status']):
                if(json.dumps(tweet['quoted_status']['extended_tweet']['entities']['hashtags']) != "[]"):
                    for i in range(0, len(tweet['quoted_status']['extended_tweet']['entities']['hashtags'])):
                        print(json.dumps(tweet['quoted_status']['extended_tweet']['entities']['hashtags'][i]['text']))
                if((json.dumps(tweet['quoted_status']['extended_tweet']['entities']['urls'])) != "[]"):
                    for i in range(0, len(tweet['quoted_status']['extended_tweet']['entities']['urls'])):
                        print(json.dumps(tweet['quoted_status']['extended_tweet']['entities']['urls'][i]['url']))
        #retweeted_status
        if('retweeted_status' in tweet):
            if(json.dumps(tweet['retweeted_status']['entities']['hashtags']) != "[]"):
                for i in range(0, len(tweet['retweeted_status']['entities']['hashtags'])):
                    print(json.dumps(tweet['retweeted_status']['entities']['hashtags'][i]['text']))
            if((json.dumps(tweet['retweeted_status']['entities']['urls'])) != "[]"):
                for i in range(0, len(tweet['retweeted_status']['entities']['urls'])):
                    print(json.dumps(tweet['retweeted_status']['entities']['urls'][i]['url']))
        #entities
        if('entities' in tweet):
            if(json.dumps(tweet['entities']['hashtags']) != "[]"):
                for i in range(0, len(tweet['entities']['hashtags'])):
                    print(json.dumps(tweet['entities']['hashtags'][i]['text']))
            if((json.dumps(tweet['entities']['urls'])) != "[]"):
                for i in range(0, len(tweet['entities']['urls'])):
                    print(json.dumps(tweet['entities']['urls'][i]['url']))

line_generator.close()
