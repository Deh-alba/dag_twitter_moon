import json
import urllib.parse
import re
from pprint import pprint

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.utils.dates import days_ago
from airflow.decorators import dag, task
import tweepy
from pymongo import MongoClient


# [END import_module]


# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Andre_Alba',
}
@dag(default_args=default_args, schedule_interval=None, start_date=days_ago(2), tags=['elt_twitter'])
def etl_twitter():
 
    @task()
    def extract():
        # consumer_key = 'PJjdcjZ6haAWTe9Uz1Q0yAhnn'
        # consumer_secret = 'nokn6ZTOPf6lfcnZJlMsx1BctTnbC5PRGJtCOy0D0DiU7znn6R'
        bearer_token = 'AAAAAAAAAAAAAAAAAAAAAO8BQQEAAAAA3GQ1%2BF4QuhbiqWhgwBenrxYE2Gs%3DviVybWMsnrEZSOB4O2EoiPhyWi6abmdznxE0SXSTg8JhrFtb3N'

        # auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
        # api = tweepy.API(auth)
        client = tweepy.Client(bearer_token)
 

        result = client.search_recent_tweets(query=" moon ", max_results=10,tweet_fields=["text,created_at"])

        return result 

        
    @task(multiple_outputs=True)
    def transform(t_data: list)->list:
        processed_data = list()
        
        for post_info in t_data.data:
            processed_data.append(
                {
                    'created_at':post_info.created_at,
                    'text':post_info.text
                }
            )
        

        return processed_data

    @task()
    def load(data_inserction: list):

        client = MongoClient("172.19.0.2", 27017)
        db = client.twitter
        twitter_posts = db.twitter_posts
        twitter_posts.insert(data_inserction)
        

    order_data = extract()
    order_summary = transform(order_data)
    load(order_summary)
etl_dag_twitter = etl_twitter()