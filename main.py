# Python Twitter Sentiment Analysis

from textblob import TextBlob
import tweepy
import sys

my_keys = open('twitterkeys.txt', 'r').read().splitlines()

api_key = my_keys[0]
api_key_secret = my_keys[1]
access_token = my_keys[2]
access_token_secret = my_keys[3]

