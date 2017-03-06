import pandas as pd
from twitter_helpers.authentication import authenticate_twitter


def scrape_tweets(SEARCHTERM, n, progress_messages = True):
    """
    Input: a search term and a number of tweets to grab
    Output: a pandas dataframe of the tweet text and other parameters
    """
    twitter_api = authenticate_twitter()
    data_types = ['id', 'text', 'retweet_count']
    
    tweets_dict = {}
    tweets_dict['id'] = []
    tweets_dict['text'] = []
    tweets_dict['retweet_count'] = []
    max_id = 999999999999999999999999  # choose an arbitrarily big number as the initial max_id
        
    for i in range(n // 100):
        if progress_messages:
            print('Getting tweets', i*100, 'to', (i+1)*100)
        search = twitter_api.search.tweets(q=SEARCHTERM, 
                                           count=100, 
                                           max_id=max_id,
                                           lang = 'en')
        results = list(search.values())

        for data in data_types:
            for i in range(len(results[0])):
                tweets_dict[data].append(results[0][i][data])

        # check if we have less than 100 tweets, signifying all available tweets have scraped
        if not len(results[0]) == 100:
            return pd.DataFrame(tweets_dict)

        max_id = min(tweets_dict['id']) - 1

    # convert to a pandas dataframe and return
    return pd.DataFrame(tweets_dict)
