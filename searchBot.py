import tweepy
import time

consumer_key = ''
consumer_secret = ''
key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = "TheHunt"
tweetNumber = 3

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(15)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(15)

searchbot()