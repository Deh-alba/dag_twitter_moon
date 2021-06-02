from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from pprint import pprint

default_args = {
    'owner': 'airflow',
}

'''
# For configure mongoDB acess
bucket_name = '<Your_Bucket>'
db_name = '<Database_Name>'
dataset = '<Dataset_Name>'
table_name = '<Table_Name>'
'''


# [START instantiate_dag]
@dag(default_args=default_args, schedule_interval=None, start_date=days_ago(2), tags=['example'])
def taskflow_etl_twitter():

    @task()
    def extract():

        data_string = 'teste'

        order_data_dict = data_string
        return order_data_dict

    # [END extract]

    # [START transform]
    @task(multiple_outputs=True)
    def transform(order_data_dict: dict):

        return {"total_order_value ->": order_data_dict}

    # [END transform]

    # [START load]
    @task()
    def load():

        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    # [END load]

    # [START main_flow]
    order_data = extract()
    order_summary = transform(order_data)
    load()
    # [END main_flow]


# [START dag_invocation]
tutorial_etl_dag = taskflow_etl_twitter()
# [END dag_invocation]

# [END tutorial]