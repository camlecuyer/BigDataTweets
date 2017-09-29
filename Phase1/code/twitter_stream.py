import tweepy

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "910286108818276353-q9ggMfSGIQxGZzeaqnUh7Q5YGB19rPG"
access_token_secret = "VQ4bQ2GxZ5cegrwsPrLVBU8brd6fsXtgkZitIY4xsHdNK"
consumer_key = "Vd6MWPVnz66RMtbtNerjc2cKL"
consumer_secret = "GUgImfugINchgslKxfDQrTWPIas3D5y188XkAytEnB0MLdAXK4"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filters the Twitter Stream
    #stream.sample()
    stream.filter(track=['#quantum', '#science', '#news', '#puertorico', '#takeaknee', '#taxreform', '#empire'])
