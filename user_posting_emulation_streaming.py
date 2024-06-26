import json
import random
import requests
import sqlalchemy
import yaml                                         # to read .yaml

from decouple import config                         # Calling sensitive information
from multiprocessing import Process
from sqlalchemy import text
from time import sleep


############################################################################################################################################################
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
    Runs an infinite loop that randomly selects a row from each table in the database and posts the data to their respective Kinesis streams.
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
            
                                                                                                        # print("**************************************************", f"\n", pin_result, f"\n")
                                                                                                        # print(geo_result, f"\n")
                                                                                                        # print(user_result, f"\n")

            pin_payload = json.dumps({
                "StreamName": "streaming-0ea287818623-pin",
                "Data": {
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
                    },
                    "PartitionKey": "pin_pk"
                    })
        
            headers = {'Content-Type': 'application/json'}
            # invoke_url = "https://YourAPIInvokeURL/<YourDeploymentStage>/streams/<stream_name>/record" (invole_url found from deploying the API from API Gateway)
            invoke_url_pin = "https://2lpziykeee.execute-api.us-east-1.amazonaws.com/prod/streams/streaming-0ea287818623-pin/record"
            pin_response = requests.request("PUT", invoke_url_pin, headers=headers, data=pin_payload)
            print("**************************************************\n", "[PIN]\n", "Status code: ", pin_response.status_code, "\n\n", "pin_response.json(): ", pin_response.json(), "\n\n", "pin_payload: ", pin_payload, "\n\n")

            geo_payload = json.dumps({
                "StreamName": "streaming-0ea287818623-geo",
                "Data": {
                    "ind": geo_result["ind"],
                    "timestamp": geo_result["timestamp"].strftime('%Y-%m-%d %H:%M:%S'),
                    "latitude": geo_result["latitude"],
                    "longitude": geo_result["longitude"],
                    "country": geo_result["country"]
                    },
                    "PartitionKey": "geo_pk"
                    })
            
            invoke_url_geo = "https://2lpziykeee.execute-api.us-east-1.amazonaws.com/prod/streams/streaming-0ea287818623-geo/record"
            geo_response = requests.request("PUT", invoke_url_geo, headers=headers, data=geo_payload)
            print("[GEO]\n", "Status code: ", geo_response.status_code, "\n\n", "geo_response.json(): ", geo_response.json(), "\n\n", "geo_payload: ", geo_payload, "\n\n")
            
            user_payload = json.dumps({
                 "StreamName": "streaming-0ea287818623-user",
                "Data": {
                    "ind": user_result["ind"],
                    "first_name": user_result["first_name"],
                    "last_name": user_result["last_name"],
                    "age": user_result["age"],
                    "date_joined": user_result["date_joined"].strftime("%Y-%m-%d %H:%M:%S")
                    },
                    "PartitionKey": "user_pk"
                    })
            
            invoke_url_user = "https://2lpziykeee.execute-api.us-east-1.amazonaws.com/prod/streams/streaming-0ea287818623-user/record"
            user_response = requests.request("PUT", invoke_url_user, headers=headers, data=user_payload)
            print("[USER]\n", "Status code: ", user_response.status_code, "\n\n", "user_response.json(): ", user_response.json(), "\n\n", "user_payload: ", user_payload, "\n\n")

if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    


