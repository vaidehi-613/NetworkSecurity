from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        
        logging.info("Initiate the data ingestion pipeline")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)

        datavalidationconfig = DataValidationConfig(trainingpipelineconfig)

        # ✅ FIX: Pass the artifact, not the config
        data_validation = DataValidation(dataingestionartifact, datavalidationconfig)

        logging.info("Initiate the data validation pipeline")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")

    except Exception as e:
        raise NetworkSecurityException(e, sys)
