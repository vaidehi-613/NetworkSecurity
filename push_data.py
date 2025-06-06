import os 
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL =os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd 
import numpy as np
import pymongo 
from networksecurity.exception.exception import NetworkSecurtiyException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e: 
            raise NetworkSecurtiyException(e, sys)


    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e: 
            raise NetworkSecurtiyException(e, sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            db = self.mongo_client[database]             # Get the database
            collection_obj = db[collection]              # Get the collection
            result = collection_obj.insert_many(records) # Insert data
            return len(result.inserted_ids)

        except Exception as e: 
            raise NetworkSecurtiyException(e, sys)



if __name__=="__main__":
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "VAIDEHIAI"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(no_of_records)
        