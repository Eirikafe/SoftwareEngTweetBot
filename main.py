# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tweepy
import pandas
import time

consumer_key = "0kGfIHzocRGps5A8US0jLK5ck"
consumer_secret = "hlPa3VtgpQ9NmnWHQh1YbF94NmsslgQiYwAYHEvT2GJBOae0tT"
access_token = "1389016192581464064-Gz7fEDktfkCnq7f4CGxGcr76zulX11"
access_token_secret = "Cyflk0XWtUqNjsIn600lo6LDRYRbBd4sKIOBvV6xvdA3w"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = []

username = 'EngGuidebook'
tweet_max = 100


def tweets_to_csv(username, tweet_max):
    for tweet in api.user_timeline(id=username, count=tweet_max):
        tweets.append((tweet.created_at, tweet.id, tweet.text))

        df = pandas.DataFrame(tweets, columns=['Date', 'Tweet_ID', 'Message'])

        df.to_csv('SoftwareEngTweets.csv')


tweets_to_csv(username, tweet_max)