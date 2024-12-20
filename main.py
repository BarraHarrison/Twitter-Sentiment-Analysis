# Python Twitter Sentiment Analysis

from textblob import TextBlob
import tweepy
import sys

my_keys = open('twitterkeys.txt', 'r').read().splitlines()
