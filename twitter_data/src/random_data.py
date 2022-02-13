import csv
from operator import index 
import random
import pandas as pd

files = [ "FEB_tweets.csv", "MAR_tweets.csv", "APR_tweets.csv", "MAY_tweets.csv", "JUN_tweets.csv", "JUL_tweets.csv", "AUG_tweets.csv", "SEP_tweets.csv", "OCT_tweets.csv", "NOV_tweets.csv", "DEC_tweets.csv"]


sample = pd.read_csv("JAN_tweets.csv").sample(10)
for m in files:
    month = pd.read_csv(m).sample(10)
    
    sample = pd.concat([sample,month])

sample.to_csv("randomized_tweets.csv", index =False)

