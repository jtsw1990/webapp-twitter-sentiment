import tweepy
import os
from dotenv import load_dotenv


load_dotenv()

bearer_token = os.environ['BEARER_TOKEN']

client = tweepy.Client(bearer_token, wait_on_rate_limit=True)

query = 'covid OR covid19 OR covid-19 -is:retweet'

response = client.search_recent_tweets(query=query, max_results=100)

print(response)