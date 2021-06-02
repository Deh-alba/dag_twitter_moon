import tweepy


class etlTwitter: 
    def __init__(self): 
        self.consumer_key = '--'
        self.consumer_secret = '--'
        self.bearer_token = '--'

        
        self.auth = tweepy.AppAuthHandler(self.consumer_key, self.consumer_secret)
        self.api = tweepy.API(self.auth)
        self.client = tweepy.Client(self.bearer_token)



    def connect_twitter(self):
        result = self.client.search_recent_tweets(query="Moon", max_results=10,leng='en',tweet_fields=['created_at'])
        print(result)
        for twitt in result.data:
            print(twitt.text)
            print(twitt.created_at)
        