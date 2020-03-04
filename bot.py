import tweepy

consumer_key = 'O7r4jS9lM1TlTo1cZq0WWUyVt'
consumer_secret = 'tLCxAAJ4LeITmiKS5uJPqU6yUq3HiBBzYt4wU42HGh4WOl6AXQ'
key = '1235093465098317824-vynQuEZSa63PTdd8cBs2L6oB0JI4oz'
secret = 'yu3HrQwOwjfJeRMMCzXRpaPmrubr5LXQW15XhW9X4Krpc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

tweets = api.mentions_timeline()
print(tweets[1].text)