# Schedule Library imported
import schedule
import time
import tweepy
from datetime import date

today = date.today()

# your twitter app keys
consumer_key ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# function setup
def tweet():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(status ="Its 4:20!! \n {} ".format(today.strftime("%B %d, %Y")))

# Task scheduling, Every day at 16:20pm call tweet
schedule.every().day.at("16:20").do(tweet)

# Loop so that the scheduling task
while True:
    # Checks whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)
