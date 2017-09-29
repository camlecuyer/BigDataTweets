#We are using Tweepy library in order to access Twitter API.
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
###################
#All below tokens & consumer key& secert are from our dev. account on twitter.
access_token = ""
access_token_secret = ""
consumer_key= ""
consumer_secret	=  ""
####################

class Twt_listner(StreamListener):		
   def on_data(self, data):
       try:
           saveFile = open('Twtdata.json','a')
           saveFile.write(data)
           saveFile.write(',  \n')
           saveFile.close()
           return True
       except Except:
           print ("failed ondata")
           time.sleep(1)
           
   def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

TwtStream = Stream(auth, Twt_listner())
#Keywords we are listening for (The current theme is "#Messi")
TwtStream.filter(track=["#Barcelona,#Messi"])
