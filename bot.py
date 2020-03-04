import tweepy

auth = tweepy.OAuthHandler(
'O7r4jS9lM1TlTo1cZq0WWUyVt', 
'tLCxAAJ4LeITmiKS5uJPqU6yUq3HiBBzYt4wU42HGh4WOl6AXQ')
auth.set_access_token('1235093465098317824-vynQuEZSa63PTdd8cBs2L6oB0JI4oz' , 'yu3HrQwOwjfJeRMMCzXRpaPmrubr5LXQW15XhW9X4Krpc')
api = tweepy.API(auth)
api.update_status('tweepy + oauth!')