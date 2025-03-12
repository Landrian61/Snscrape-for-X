# Script using tweepy with bearer token only

import tweepy
import logging
import sys
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Your Twitter API credentials - only using bearer token
bearer_token = "AAAAAAAAAAAAAAAAAAAAAM8CzwEAAAAAX%2BgOFzmH6aMGamdoyFQ%2Bc1XrUX8%3DRjyZP06xnBUvOfubhQkS3RfENHIqbr7BEnFLhL46ZvOCZsq3Rq"

# Set up username to query (use command line argument if provided)
username = sys.argv[1] if len(sys.argv) > 1 else "nasa"

# Initialize client with Bearer Token only
try:
    logger.info(f"Attempting authentication with Bearer Token for user: {username}...")
    client = tweepy.Client(bearer_token=bearer_token)
    
    # Test the authentication by getting user info
    user = client.get_user(username=username)
    
    if user.data:
        logger.info(f"Successfully authenticated! Found user: {user.data.name}")
        user_id = user.data.id
        logger.info(f"User ID for {username}: {user_id}")
        
        # Get tweets
        tweets = client.get_users_tweets(
            id=user_id,
            max_results=10,
            tweet_fields=["created_at", "public_metrics"]
        )
        
        # Print results
        if tweets.data:
            for tweet in tweets.data:
                print(f"Tweet ID: {tweet.id}")
                print(f"Text: {tweet.text}")
                print(f"Created at: {tweet.created_at}")
                print(f"Retweets: {tweet.public_metrics['retweet_count']}")
                print("---")
            logger.info(f"Successfully retrieved {len(tweets.data)} tweets")
        else:
            logger.warning("No tweets were found for this user")
    else:
        logger.error("Authentication succeeded but no user data returned")
        
except tweepy.errors.Unauthorized as e:
    logger.error(f"Authentication failed: {e}")
    logger.error("Your bearer token may be invalid or expired")
    logger.error("Check the token in your Twitter Developer Portal")
    sys.exit(1)
    
except tweepy.errors.TooManyRequests as e:
    logger.error(f"Rate limit exceeded: {e}")
    logger.error("Try again after the rate limit reset time")
    sys.exit(1)
    
except Exception as e:
    logger.error(f"An unexpected error occurred: {e}")
    sys.exit(1)