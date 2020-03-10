import tweepy
import time

consumer_key = 'O7r4jS9lM1TlTo1cZq0WWUyVt'
consumer_secret = 'tLCxAAJ4LeITmiKS5uJPqU6yUq3HiBBzYt4wU42HGh4WOl6AXQ'
key = '1235093465098317824-vynQuEZSa63PTdd8cBs2L6oB0JI4oz'
secret = 'yu3HrQwOwjfJeRMMCzXRpaPmrubr5LXQW15XhW9X4Krpc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#randomtweet' in tweet.full_text.lower():
            print("Replied To ID - " + str(tweet.id))
            api.update_status("@" + tweet.user.screen_name + " Good Luck For #100DaysOfCode!", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(12)