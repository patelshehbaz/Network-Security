import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant variable for training pipeline
"""
TARGET_COLUMN = "Result"  # The target column we're trying to predict
PIPELINE_NAME: str = "NetworkSecurity"  # Name of the entire pipeline
ARTIFACT_DIR: str = "Artifacts"  # Directory to store generated artifacts
FILE_NAME: str = "NetworkData.csv"  # Name of the data file used

# Filenames for training and testing data
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

# Names of files for storing preprocessing objects and models
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")  # Path to the schema file
SCHEMA_DROP_COLS = "drop_columns"  # Name of the columns to drop
SAVED_MODEL_DIR = os.path.join("saved_models")  # Directory to save trained models

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"  # Name of the collection in the database
DATA_INGESTION_DATABASE_NAME: str = "CyberSecurityDomain"  # Name of the database
DATA_INGESTION_DIR_NAME: str = "data_ingestion"  # Directory name for data ingestion process
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"  # Directory to store features
DATA_INGESTION_INGESTED_DIR: str = "ingested"  # Directory to store ingested data
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2  # Ratio to split data into training and testing


"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""


"""
Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME
"""


"""
Model Trainer related constant start with MODE TRAINER VAR NAME
"""




