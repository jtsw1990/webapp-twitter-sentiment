import tweepy
import os
from dotenv import load_dotenv


load_dotenv()

bearer_token = os.environ['BEARER_TOKEN']

client = tweepy.Client(bearer_token, wait_on_rate_limit=True)

query = 'covid OR covid19 OR covid-19 -is:retweet'

#response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'lang'], user_fields=['profile_image_url'], expansions=['author_id'])


for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=1000):
    print(tweet.id)


#users = { k['id']: k for k in response.includes['users'] }

# for tweet in response.data:
#     if users[tweet.author_id]:
#         user = users[tweet.author_id]
#         print(tweet.id)
#         print(user.profile_image_url)