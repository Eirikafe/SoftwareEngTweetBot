# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime as datetime
import tweepy
import datetime
import csv

consumer_key = "0kGfIHzocRGps5A8US0jLK5ck"
consumer_secret = "hlPa3VtgpQ9NmnWHQh1YbF94NmsslgQiYwAYHEvT2GJBOae0tT"
access_token = "1389016192581464064-Gz7fEDktfkCnq7f4CGxGcr76zulX11"
access_token_secret = "Cyflk0XWtUqNjsIn600lo6LDRYRbBd4sKIOBvV6xvdA3w"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = []
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
print(yesterday)


def tweets_to_csv():
    csvFile = open('SoftwareEngTweets.csv', 'a')
    csvWriter = csv.writer(csvFile)
    temptext = "0"
    for tweet in tweepy.Cursor(api.search, q="#SoftwareEngineer",
                               lang="en",
                               since=yesterday).items(100):
        if tweet.text != temptext:
            tweets.append((tweet.created_at, tweet.id, tweet.text))

            print(tweet.id, tweet.created_at, tweet.text)
            csvWriter.writerow([tweet.id, tweet.created_at, tweet.text.encode('utf-8')])
            temptext = tweet.text


tweets_to_csv()
