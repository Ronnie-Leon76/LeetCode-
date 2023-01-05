import tweepy
from decouple import config

consumer_key = config('CONSUMER_KEY')
consumer_secret = config('CONSUMER_SECRET')
bearer_token = config('BEARER_TOKEN')
access_token = config('ACCESS_TOKEN')
access_token_secret = config('ACCESS_TOKEN_SECRET')


# authenticate with Twitter API using consumer key and secret and bearer token
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# get a list of all your followers
followers = api.get_followers()

for follower in followers:
    # send an inbox message to each follower
    api.send_direct_message(user_id=follower.id, text="Hello there. I hope you are holding up well. Let me apologise for the click bait sent to your inbox. A friend of mine whom I trust had fallen victim to a click bait and I clicked it and authorized it to access my account. I realized later it was a click bait and went to settings>account>connected apps and revert the authorization permission. Kindly if you clicked the link and granted permission to it, revert the authorization permission for the safety of your account. Please do not click on any links sent to you by me. I hope you understand. Thank you.")