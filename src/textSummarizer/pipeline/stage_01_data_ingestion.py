from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logs import logger
import os 

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
        
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
