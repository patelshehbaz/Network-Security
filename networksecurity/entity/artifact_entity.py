# Import necessary libraries to create data structures for storing artifacts
from dataclasses import dataclass

# Data class to store paths for data ingestion artifacts
@dataclass
class DataIngestionArtifact:
    trained_file_path: str  # Path to the training dataset
    test_file_path: str  # Path to the testing dataset

@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str

@dataclass
class ModelTrainerArtifact:
    pass

@dataclass
class ModelEvaluationArtifact:
    pass

@dataclass
class ModelPusherArtifact:
    pass

@dataclass
class ClassificationMetricArtifact:
    pass

