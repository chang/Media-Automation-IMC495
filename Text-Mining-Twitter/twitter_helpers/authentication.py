import twitter
from twitter_helpers.API_KEYS_TWITTER import *

def authenticate_twitter():
	"""
	returns an authenticated Twitter object to access the API
	"""
	auth = twitter.oauth.OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
	                           CONSUMER_KEY, CONSUMER_SECRET)

	return twitter.Twitter(auth=auth)