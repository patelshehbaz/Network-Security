# Import necessary libraries for data ingestion and exception handling
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

import os
import sys
import pandas as pd
import numpy as np
import pymongo  # Library for MongoDB interactions
from typing import List
from sklearn.model_selection import train_test_split  # Function to split data into training and testing sets

from dotenv import load_dotenv  # Library to load environment variables
load_dotenv()  # Load the .env file containing environment variables
MONGO_DB_URL = os.getenv("MONGO_DB_URL")  # Get the MongoDB URL from the environment variables
#print(MONGO_DB_URL)  # Print the MongoDB URL for verification

# Class to handle data ingestion
class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            # Initialize the data ingestion configuration
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            # Raise a custom exception if something goes wrong
            raise NetworkSecurityException(e, sys)

    # Method to export data from MongoDB collection to a pandas DataFrame
    def export_collection_as_dataframe(self):
        try:
            # Retrieve the database and collection names from the configuration
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            
            # Connect to MongoDB using the provided URL
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            # Access the specific collection within the database
            collection = self.mongo_client[database_name][collection_name]
            
            # Convert the collection data into a pandas DataFrame
            df = pd.DataFrame(list(collection.find()))
            # If the "_id" column exists, drop it as it is not needed
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            # Replace any "na" values in the DataFrame with NaN (missing value)
            df.replace({"na": np.nan}, inplace=True)

            return df  # Return the cleaned DataFrame
            
        except Exception as e:
            # Raise a custom exception if something goes wrong
            raise NetworkSecurityException(e, sys)

    # Method to save the DataFrame into the feature store
    def export_data_into_feature_store(self, dataframe: pd.DataFrame):
        try:
            # Get the path to save the feature store file
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            # Create the directory if it does not exist
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            # Save the DataFrame as a CSV file in the feature store
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
            
        except Exception as e:
            # Raise a custom exception if something goes wrong
            raise NetworkSecurityException(e, sys)

    # Method to split the data into training and testing sets
    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        try:

            # Split the DataFrame into training and testing sets based on the ratio
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )
            logging.info("Performed train-test split on the dataframe")

            logging.info("Exited split_data_as_train_test method of Data_Ingestion class")
            
            # Create directories to save the training and testing datasets
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            logging.info(f"Exporting train and test file path.")
            
            # Save the training dataset as a CSV file
            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True
            )
            # Save the testing dataset as a CSV file
            test_set.to_csv(
                self.data_ingestion_config.testing_file_path, index=False, header=True
            )
        
                # Log that the train and test files have been successfully exported
            logging.info(f"Exported train and test file path.")
            
        except Exception as e:
            # Raise a custom exception if something goes wrong
            raise NetworkSecurityException(e, sys)

    # Method to initiate the entire data ingestion process
    def initiate_data_ingestion(self):
        try:
            # Step 1: Export the data from the database into a pandas DataFrame
            dataframe = self.export_collection_as_dataframe()
            # Step 2: Save the DataFrame into the feature store (a place to keep important data)
            dataframe = self.export_data_into_feature_store(dataframe)
            # Step 3: Split the DataFrame into training and testing datasets
            self.split_data_as_train_test(dataframe=dataframe)
            
            # Create a DataIngestionArtifact object to store paths of the training and testing data
            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )
            # Return the artifact containing the paths to the training and testing datasets
            return data_ingestion_artifact
            
        except Exception as e:
            # Raise a custom exception if something goes wrong
            raise NetworkSecurityException(e, sys)
        
    
        

