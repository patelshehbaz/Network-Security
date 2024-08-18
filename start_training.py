import os
import sys
from networksecurity.exception.exception import NetworkSecurityException  # Import custom exception
from networksecurity.logger.logger import logging  # Import custom logging (though it's not used in this script)

from networksecurity.pipeline import TrainingPipeline

def start_training():
    try:
        pass
    except Exception as e:
        raise NetworkSecurityException(e,sys)

if __name__ == '__main__':
    start_training()