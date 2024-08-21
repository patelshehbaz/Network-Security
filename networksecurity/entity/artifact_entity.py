# Import necessary libraries to create data structures for storing artifacts
from dataclasses import dataclass

# Data class to store paths for data ingestion artifacts
@dataclass
class DataIngestionArtifact:
    trained_file_path: str  # Path to the training dataset
    test_file_path: str  # Path to the testing dataset

@dataclass
class DataValidationArtifact:
    pass

@dataclass
class DataTransformationArtifact:
    pass 

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

