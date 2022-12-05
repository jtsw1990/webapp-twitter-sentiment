import tweepy
import os
from dotenv import load_dotenv


load_dotenv()

bearer_token = os.environ['BEARER_TOKEN']

client = tweepy.Client(bearer_token, wait_on_rate_limit=True)

query = 'covid OR covid19 OR covid-19 -is:retweet'

# response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'lang'], user_fields=['profile_image_url'], expansions=['author_id'])


# for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=1000):
#     print(tweet.id)


# users = { k['id']: k for k in response.includes['users'] }

# for tweet in response.data:
#     if users[tweet.author_id]:
#         user = users[tweet.author_id]
#         print(tweet.id)
#         print(user.profile_image_url)




## Getting tweet counts

# counts = client.get_recent_tweets_count(query=query, granularity='day')
# for count in counts.data:
#     print(count)


## Get users timeline
USER_ID = 2244994945

# users = client.get_users(usernames=['twitterdev'])
# for user in users:
#     print(user)

# tweets = client.get_users_tweets(id=USER_ID, tweet_fields=['lang'])
# tweets = client.get_users_mentions(id=USER_ID, tweet_fields=['lang'])


# for tweet in tweets.data:
#     print(tweet.id)
#     print(tweet.text)


## Get users followers and following

#users = client.get_users_followers(id=USER_ID, user_fields=['profile_image_url'])
# users = client.get_users_following(id=USER_ID, user_fields=['profile_image_url'])

# for user in users.data:
#     print(user.profile_image_url)


## Get users liking a tweet
TWEET_ID = '1599605795976777728'
users = client.get_liking_users(id=TWEET_ID)
#users = client.get_retweeters(id=TWEET_ID)
for user in users.data:
    print(user)
