import tweepy

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

tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
for tweet in tweets:
    if '#randomtweet' in tweet.full_text.lower():
        print(str(tweet.id) + ' - ' + tweet.full_text)

        store_last_seen(FILE_NAME, tweet.id)