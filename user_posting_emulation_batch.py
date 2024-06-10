import requests
from time import sleep
import random
from multiprocessing import Process
# import boto3
import json
import sqlalchemy
from sqlalchemy import text

from decouple import config # Calling sensitive information
import yaml # to read .yaml


random.seed(100)

class AWSDBConnector:
    """
    AWSDBConnector is responsible for creating a connection to the AWS database.
    It reads database credentials from a YAML file specified in the environment variables.

    Attributes:
        creds (dict): Dictionary containing the database credentials.
    """
    def __init__(self):
        """
        Initialises the AWSDBConnector class by accessing private credentials from a YAML file for API authentication.
        """
        cred_config_access = config('credentials_env') # refers to .yaml file via decouple import config; to gain access to private credentials for API
         
        with open(cred_config_access, 'r') as db_creds: # extracts the credentials from .yaml file
            self.creds = yaml.safe_load(db_creds)

    def create_db_connector(self):
        """
        Creates a database connector using SQLAlchemy to connect to a MySQL database.

        Returns:
            engine: An SQLAlchemy engine object that is connected to the MySQL database using the credentials provided.
        """
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.creds['AWSDB_USER']}:{self.creds['AWSDB_PASSWORD']}@{self.creds['AWSDB_HOST']}:{self.creds['AWSDB_PORT']}/{self.creds['AWSDB_DATABASE']}?charset=utf8mb4")
        return engine

new_connector = AWSDBConnector()

def run_infinite_post_data_loop():
    """
    Runs an infinite loop that randomly selects a row from each table in the database and posts the data to their respective Kafka topics.
    Designed to be run as a thread.

    Returns:
        None: The function runs indefinitely and doesn't explicitly return any value.
    """
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)

            print("**************************************************\n")
            print("pin result: ", pin_result, "\n")
            print("geo result: ", geo_result, "\n")
            print("user result: ", user_result, "\n")

            pin_payload = json.dumps({
                "records": [
                    {
                        "value": {
                            "index": pin_result["index"],
                            "unique_id": pin_result["unique_id"],
                            "title": pin_result["title"],
                            "description": pin_result["description"],
                            "poster_name": pin_result["poster_name"],
                            "follower_count": pin_result["follower_count"],
                            "tag_list": pin_result["tag_list"],
                            "is_image_or_video": pin_result["is_image_or_video"],
                            "image_src": pin_result["image_src"],
                            "downloaded": pin_result["downloaded"],
                            "save_location": pin_result["save_location"],
                            "category": pin_result["category"]
                            }
                    }
                ]
            }, default=str)
            headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
            invoke_url_pin = "https://2lpziykeee.execute-api.us-east-1.amazonaws.com/prod/topics/0ea287818623.pin"
            pin_response = requests.request("POST", invoke_url_pin, headers=headers, data=pin_payload)
            print("pin status code: ", pin_response.status_code, "\n")

            geo_payload = json.dumps({
                "records": [
                    {
                        "value": {
                            "ind": geo_result["ind"],
                            "timestamp": geo_result["timestamp"],
                            "latitude": geo_result["latitude"],
                            "longitude": geo_result["longitude"],
                            "country": geo_result["country"]
                            }
                    }
                ]
            }, default=str)
            invoke_url_geo = "https://2lpziykeee.execute-api.us-east-1.amazonaws.com/prod/topics/0ea287818623.geo"
            geo_response = requests.request("POST", invoke_url_geo, headers=headers, data=geo_payload)
            print("geo status code: ", geo_response.status_code, "\n")
            
            user_payload = json.dumps({
                "records": [
                    {
                        "value": {
                            "ind": user_result["ind"],
                            "first_name": user_result["first_name"],
                            "last_name": user_result["last_name"],
                            "age": user_result["age"],
                            "date_joined": user_result["date_joined"]
                            }
                    }
                ]
            }, default=str)
            invoke_url_user = "https://2lpziykeee.execute-api.us-east-1.amazonaws.com/prod/topics/0ea287818623.user"
            user_response = requests.request("POST", invoke_url_user, headers=headers, data=user_payload)
            print("user status code: ", user_response.status_code, "\n")

if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    


