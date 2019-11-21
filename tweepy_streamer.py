from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials


###TWITTER STREAMER###
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    #def __init__(self):
        #pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        #This handles Twitter authentication and the connection to the Twitter Streaming API.
        listener = TwitterListener()
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

        stream =Stream(auth, listener)

        #This line filter Twitter Streams to capture data by the keywords
        stream.filter(track=hash_tag_list)


###TWITTER STREAM LISTENER###
class TwitterListener(StreamListener):
    """
    This is a basic listener class that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
     #inherits from StreamListener class

     #methods below from StreamListener that are overriden
     def on_data(self, data):
         try:
             print(data)
             with open(self.fetched_tweets_filename, 'a') as tf:
                 tf.write(data)
             return True
        except  BaseException as e:
            print("Error on data: %s" %str(e))
        return True


     def on_error(self, status):
         print(status)


if name__=="__main__":

    hash_tag_list = ["jose mourinho", "lebron james", "cristiano ronaldo", "kababiito"]
    fetched_tweets_filename= "tweets.json"

    twitter streamer = TwitterStreamer()
    twitter streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
