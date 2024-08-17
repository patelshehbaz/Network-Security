import os
import sys
import json

from dotenv import load_dotenv  # Import dotenv to load environment variables from a .env file
load_dotenv()  # Load the environment variables from the .env file

# Fetch the MongoDB URL from the environment variables
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
#print(MONGO_DB_URL)  # Print the MongoDB URL for debugging purposes

import certifi  # Import certifi to ensure SSL certificates are verified
ca = certifi.where()  # Get the location of the certifi CA bundle

import pandas as pd  # Import pandas for data manipulation
import numpy as np  # Import numpy for numerical operations (though it's not used in this script)
import pymongo  # Import pymongo to interact with MongoDB
from networksecurity.exception.exception import NetworkSecurityException  # Import custom exception
from networksecurity.logger.logger import logging  # Import custom logging (though it's not used in this script)

class NetworkDataExtract():
    def __init__(self):
        try:
            pass  # Constructor doesn't do anything currently
        except Exception as e:
            # Raise a custom exception if there's an error during initialization
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_convertor(self, file_path):
        try:
            # Read CSV file into a pandas DataFrame
            data = pd.read_csv(file_path)
            
            # Reset index to ensure the DataFrame is in order and no old indices are retained
            data.reset_index(drop=True, inplace=True)
            
            # Convert the DataFrame into a JSON format and then into a list of records (dictionaries)
            records = list(json.loads(data.T.to_json()).values())
            
            return records  # Return the list of records
        except Exception as e:
            # Raise a custom exception if there's an error during CSV to JSON conversion
            raise NetworkSecurityException(e, sys)
    
    def pushing_data_to_mongodb(self, records, database, collection):
        try:
            # Store the database and collection names in instance variables
            self.database = database
            self.collection = collection
            self.records = records
            
            # Create a MongoDB client connection
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            
            # Select the database from the MongoDB client
            self.database = self.mongo_client[self.database]
            
            # Select the collection within the selected database
            self.collection = self.database[self.collection]
                
            # Insert the list of records into the MongoDB collection
            self.collection.insert_many(self.records)
                
            return len(self.records)  # Return the number of records inserted
            
        except Exception as e:
            # Raise a custom exception if there's an error during the MongoDB insertion
            raise NetworkSecurityException(e, sys)
        
if __name__ == '__main__':
    # Define the file path to the CSV file
    FILE_PATH = "./Data/NetworkData.csv"
    
    # Define the database and collection names
    DATABASE = "CyberSecurityDomain"
    COLLECTION = "NetworkData"
    
    # Create an instance of the NetworkDataExtract class
    networobj = NetworkDataExtract()
    
    # Convert the CSV data to a JSON-like list of records
    records = networobj.csv_to_json_convertor(FILE_PATH)
    
    # Push the converted records to MongoDB and get the number of records inserted
    noofrecords = networobj.pushing_data_to_mongodb(records, DATABASE, COLLECTION)
    
    # Print the number of records inserted
    print(noofrecords)
