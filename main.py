from textblob import TextBlob
import tweepy
import sys
import time

# Read API keys from the file
my_keys = {}
with open('twitterkeys.txt', 'r') as file:
    for line in file:
        key, value = line.strip().split(" = ")
        my_keys[key] = value

# Assign keys to variables
bearer_token = my_keys.get(
    "bearer_token",
    "AAAAAAAAAAAAAAAAAAAAAACWxgEAAAAAlebQUf8mpBcVxHsRdfefusKAmcI%3D34vhR83Jry5H4rhumihkcDdKVVHa2aVe59Wg6N3GGTwGy7aKrr"
)

# Authenticate with API v2
client = tweepy.Client(bearer_token=bearer_token)

# Define search term and max results
search_term = "stocks lang:en"  # Add language filter in the query
tweet_amount = 5  # Reduce number of tweets to avoid rate limit

try:
    # Use search_recent_tweets endpoint
    response = client.search_recent_tweets(
        query=search_term,
        max_results=tweet_amount,
        tweet_fields=["text", "author_id", "created_at"]
    )

    # Check and display tweets
    if response.data:
        for tweet in response.data:
            # Perform sentiment analysis
            sentiment_analysis = TextBlob(tweet.text).sentiment
            print(f"Author ID: {tweet.author_id}")
            print(f"Tweet: {tweet.text}")
            print(f"Created At: {tweet.created_at}")
            print(f"Sentiment: Polarity={sentiment_analysis.polarity}, Subjectivity={sentiment_analysis.subjectivity}\n")
    else:
        print("No tweets found.")
except tweepy.TooManyRequests as e:
    print("Rate limit exceeded. Waiting to retry...")
    time.sleep(900)  # Wait 15 minutes before retrying
except tweepy.TweepyException as e:
    print("Error fetching tweets:", e)
