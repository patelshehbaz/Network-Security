# Import libraries and modules needed for configuring the pipeline
from datetime import datetime
import os
from networksecurity.constant import training_pipeline

# Print the name of the pipeline and the directory where artifacts will be stored
print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

# Class to configure the training pipeline
class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        # Convert the timestamp into a string format
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        # Set the pipeline name and artifact directory name
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFACT_DIR
        # Create a directory to store artifacts, including a timestamp
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)
        self.timestamp: str = timestamp

# Class to configure data ingestion settings
class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        # Directory for storing data ingestion outputs
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME
        )
        # Path to store the feature store file
        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
        )
        # Path to save the training dataset
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
        )
        # Path to save the testing dataset
        self.testing_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
        )
        # Ratio to split data into training and testing sets
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        # Set the name of the collection and database
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME

            
class DataValidationConfig:
    def __init__(self):
        pass
    

class DataTransformationConfig:
    def __init__(self):
        pass
    
class ModelTrainerConfig:
    def __init__(self):
        pass
    
class ModelEvaluationConfig:
    def __init__(self):
        pass
    
class ModelPusherConfig:
     def __init__(self):
        pass