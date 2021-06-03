# dag_twitter_moon
This is on simple ETL for extract information with string moon in Twitter, clear this data in load in mongoDB platform that aftert we will disponibiliza with fastAPI 

For this project we use airflow and mongoDB in docker 

You can make dowload in the docker-compose in 

https://airflow.apache.org/docs/apache-airflow/2.0.2/docker-compose.yaml

And after, you can run 

```docker-compose up airflow-init```

for mongoDB you can run 

```docker pull mongo```

OBS: don't forget that run configaration for network comunnication. 
For more details 
https://hub.docker.com/_/mongo


For more information about the tools 

[AirFlow](https://airflow.apache.org/)
[MongoDB](https://www.mongodb.com/)
