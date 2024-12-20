# Twitter Sentiment Analysis Script
This Python script performs a Twitter sentiment analysis by retrieving recent tweets containing a specific keyword or topic and analyzing the sentiment of the tweet's text.
Sentiment analysis is a powerful tool that helps determine the emotional tone behind a piece of text—whether it's positive, negative, or neutral.

# Features
- Keyword-based Tweet Retrieval: Fetches tweets that include a specific search term.
- Language Filtering: Ensures only English tweets are analyzed by adding a lang:en filter to the query.
- Sentiment Analysis: Uses TextBlob to calculate:
- Polarity: A score between -1 (negative sentiment) and 1 (positive sentiment).
- Subjectivity: A score between 0 (objective) and 1 (subjective).
- Rate Limit Handling: Includes a mechanism to wait and retry if the Twitter API's rate limit is exceeded.

# How the script works

## Authentication:
The script authenticates with the Twitter API using a Bearer Token stored in a separate twitterkeys.txt file for security.
The twitterkeys.txt file should include your API credentials.

## Search for Tweets:
It queries the Twitter API using the search_recent_tweets endpoint to retrieve tweets containing the defined keyword (e.g., "stocks").
The lang:en filter ensures that only English tweets are retrieved.

## Sentiment Analysis:
For each tweet, the script uses TextBlob to analyze the sentiment:
Polarity determines whether the sentiment is positive, neutral, or negative.
Subjectivity indicates the level of opinion or bias in the tweet.

## Output:
The script displays the following information for each tweet:
Author ID
Tweet text
Timestamp
Sentiment scores (Polarity and Subjectivity)

## Rate Limit Handling:
If the rate limit is exceeded, the script waits for 15 minutes before retrying.


# Limitations
- The free tier of the Twitter API has strict rate limits and might require adjustments to the tweet_amount or waiting during execution.
- TextBlob sentiment analysis is basic and may not always capture nuanced sentiment accurately.

