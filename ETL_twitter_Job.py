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
@dag(default_args=default_args, schedule_interval="@daily", start_date=days_ago(2), tags=['elt_twitter'])
def etl_twitter():
    
    bearer_token = '--'


    client = tweepy.Client(bearer_token)
 
    result = client.search_recent_tweets(query=" moon ", max_results=1000,tweet_fields=["text,created_at"])


    @task()
    def extract():
    
        processed_data = list()
        for post_info in result.data:
            processed_data.append(
                {
                    'created_at':str(post_info.created_at),
                    'text':post_info.text
                }
            )
        

        return processed_data

        
    @task()
    def transform(processed_data: list)->list:

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