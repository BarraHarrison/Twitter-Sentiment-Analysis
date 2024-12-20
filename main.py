from textblob import TextBlob
import tweepy
import sys

# Read API keys from the file
my_keys = {}
with open('twitterkeys.txt', 'r') as file:
    for line in file:
        key, value = line.strip().split(" = ")
        my_keys[key] = value

# Assign keys to variables
api_key = my_keys["api_key"]
api_key_secret = my_keys["api_key_secret"]
access_token = my_keys["access_token"]
access_token_secret = my_keys["access_token_secret"]

# Authenticate with Twitter
auth_handler = tweepy.OAuthHandler(api_key, api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

# Connect to the API
api = tweepy.API(auth_handler)

# Verify credentials
try:
    api.verify_credentials()
    print("Authentication successful")
except tweepy.TweepyException as e:
    print("Error during authentication:", e)
    sys.exit(1)

# Search for tweets
search_term = "stocks"
tweet_amount = 20

try:
    tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang="en").items(tweet_amount)
    for tweet in tweets:
        print(tweet.text)
except tweepy.TweepyException as e:
    print("Error fetching tweets:", e)
