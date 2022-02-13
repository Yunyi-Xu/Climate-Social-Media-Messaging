import pandas as pd
import requests
import os
import json
import csv
import datetime
import dateutil.parser
import unicodedata
import time
import tweepy
from tweepy import tweet
from collections import Counter
from tqdm import tqdm
import random
import math



#Twitter API credentials
consumer_KEY = 'r2ijh0AvsCuBY5O7UtAlE7HbH'
consumer_SECRET = '1MRHE2pTjJYaPdsVf4E6DY2MTbn6Sfsn5ZDqH1IZdMnhQAY8lH'
access_TOKEN = '1463141094657445889-tlpHsp1PFiYHvGddaT7yF6RTFSFhP1'
access_TOKEN_SECRET = 'atEvs2CWsLWJp6GCcr8GZVYylGrXNEUL4TWi6uWkSWeAU'

#Authentication
auth = tweepy.OAuthHandler(consumer_KEY, consumer_SECRET)
auth.set_access_token(access_TOKEN, access_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)




keyword = "(\"climate change\" OR \"global warming\") -is:retweet -is:reply -is:verified lang:en "

######pulling tweets from Twitter
tweets = []
tweet_list = (tweepy.Cursor(api.search_full_archive, label="UndergradProject", query = keyword, fromDate = "202112010001", toDate ="202112312359").items(500))
for i in tqdm(tweet_list):
    tweets.append(i._json)


df = pd.DataFrame(tweets)

output_tweets = (df.drop_duplicates(subset = ["text"], keep='first'))#s.head(20)         #only keep first of the duplicate value
output_tweets.to_csv('DEC_tweets.csv')

