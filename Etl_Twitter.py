import tweepy
from pymongo import MongoClient
import json
# import pandas as pd
import urllib.parse
import re

class etlTwitter: 
    def __init__(self): 
        self.consumer_key = '--'
        self.consumer_secret = '--'
        self.bearer_token = '--'

 
        self.auth = tweepy.AppAuthHandler(self.consumer_key, self.consumer_secret)
        self.api = tweepy.API(self.auth)
        self.client = tweepy.Client(self.bearer_token)
 
        client = MongoClient("172.19.0.2", 27017)
        
        db = client.twitter
        self.twitter_posts = db.twitter_posts


    def test_monog_connection(self):
        
        post = {"author": "Mike",
                "text": "My first blog post!",
                "tags": ["mongodb", "python", "pymongo"]}

        print(self.twitter_posts.insert_one(post))



    def extract_twitter_data(self):
        result = self.client.search_recent_tweets(query=" moon ", max_results=10,tweet_fields=["text,created_at"])

        return result 

    def transform_twitter_data(self, t_data):
        
        processed_data = list()
        
        for post_info in t_data.data:
            processed_data.append(
                {
                    'created_at':post_info.created_at,
                    'text':post_info.text
                }
            )
        


        return processed_data
        

    def load_twitter_data_mongoDb(self, data_inserction):
        
        data_id = self.twitter_posts.insert(data_inserction)
        print(data_id)