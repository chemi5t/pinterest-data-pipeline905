import random
import sqlalchemy # SQL toolkit and Object-Relational Mapping (ORM) library. 
import yaml # to read .yaml and parser and emitter for Python

from decouple import config # Manage settings and environment variables
from multiprocessing import Process
from sqlalchemy import text 
from time import sleep


random.seed(100)

class AWSDBConnector:

    def __init__(self):
         
         cred_config_access = config('credentials_env') # refers to .yaml file via decouple import config; to gain access to private credentials for API
         
         with open(cred_config_access, 'r') as db_creds: # extracts the credentials from .yaml file
            self.creds = yaml.safe_load(db_creds)

    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.creds['AWSDB_USER']}:{self.creds['AWSDB_PASSWORD']}@{self.creds['AWSDB_HOST']}:{self.creds['AWSDB_PORT']}/{self.creds['AWSDB_DATABASE']}?charset=utf8mb4")
        return engine


new_connector = AWSDBConnector()


def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            # print("1. print(pin_selected_row):\n\n", pin_selected_row, "\n") # <sqlalchemy.engine.cursor.CursorResult object at 0x00000253581960B0>
            # print("type: ", type(pin_selected_row)) # type:  <class 'sqlalchemy.engine.cursor.CursorResult'>
           
            for row in pin_selected_row:
                # print("2. row:\n\n", row, "\n") #(2863, '9bf39437-42a6-4f02-99a0-9a0383d8cd70', '25 Super Fun Summer Crafts for Kids - Of Life and Lisa', 'Keep the kids busy this summer with these easy diy crafts and projects. Creative and…', 'Of Life & Lisa | Lifestyle Blog', '124k', 'Summer Crafts For Kids,Fun Crafts For Kids,Summer Kids,Toddler Crafts,Crafts To Do,Diy For Kids,Summer Snow,Diys For Summer,Craft Ideas For Girls', 'image', 'https://i.pinimg.com/originals/b3/bc/e2/b3bce2964e8c8975387b39660eed5f16.jpg', 1, 'Local save in /data/diy-and-crafts', 'diy-and-crafts')
                # print("type: ", type(row)) # type:  <class 'sqlalchemy.engine.row.Row'>
                # print("3. row._mapping:\n\n", row._mapping, "\n")
                # print(type(row._mapping)) #  {'index': 2863, 'unique_id': '9bf39437-42a6-4f02-99a0-9a0383d8cd70', 'title': '25 Super Fun Summer Crafts for Kids - Of Life and Lisa', 'description': 'Keep the kids busy this summer with these easy diy crafts and projects. Creative and…', 'poster_name': 'Of Life & Lisa | Lifestyle Blog', 'follower_count': '124k', 'tag_list': 'Summer Crafts For Kids,Fun Crafts For Kids,Summer Kids,Toddler Crafts,Crafts To Do,Diy For Kids,Summer Snow,Diys For Summer,Craft Ideas For Girls', 'is_image_or_video': 'image', 'image_src': 'https://i.pinimg.com/originals/b3/bc/e2/b3bce2964e8c8975387b39660eed5f16.jpg', 'downloaded': 1, 'save_location': 'Local save in /data/diy-and-crafts', 'category': 'diy-and-crafts'}
                pin_result = dict(row._mapping) # <class 'dict'>


            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
            
            print("**************************************************\npin result: ", pin_result)
            print("\ngeo result: ",geo_result)

            print("\nuser result: ",user_result, "\n**************************************************")


if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    


