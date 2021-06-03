# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime as datetime
import tweepy
import datetime
import csv

# declares keys that are used to verify who is using the Twitter API
consumer_key = "0kGfIHzocRGps5A8US0jLK5ck"
consumer_secret = "hlPa3VtgpQ9NmnWHQh1YbF94NmsslgQiYwAYHEvT2GJBOae0tT"
access_token = "1389016192581464064-Gz7fEDktfkCnq7f4CGxGcr76zulX11"
access_token_secret = "Cyflk0XWtUqNjsIn600lo6LDRYRbBd4sKIOBvV6xvdA3w"

# Authenticates the consumer key and access token and sets up a session with the API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Creates a matrix to store the tweets and declares 24 hours ago
tweets = []
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
print(yesterday)

# read in tweets given a hashtag in the past 24 hours
def tweets_to_csv():
    # sets up the CSV file and writer as well as a temp string to try to avoid copied tweets
    csvFile = open('SoftwareEngTweets.csv', 'a')
    csvWriter = csv.writer(csvFile)
    temptext = "0"

    # iterates through the tweets and searches for the hashtag Software Engineer, up to a total of 100 tweets
    for tweet in tweepy.Cursor(api.search, q="#SoftwareEngineer",
                               lang="en",
                               since=yesterday).items(100):
        # if current tweet is different from the past tweet, append it to the matrix using the timestamp, id and text
        if tweet.text != temptext:
            tweets.append((tweet.created_at, tweet.id, tweet.text))

            print(tweet.id, tweet.created_at, tweet.text)
            csvWriter.writerow([tweet.id, tweet.created_at, tweet.text.encode('utf-8')])
            temptext = tweet.text


tweets_to_csv()
