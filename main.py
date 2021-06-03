
from  Etl_Twitter import *

ETLT = etlTwitter()


# ETLT.test_monog_connection()

query = ETLT.extract_twitter_data()

processe_data = ETLT.transform_twitter_data(query)

ETLT.load_twitter_data_mongoDb(processe_data)

