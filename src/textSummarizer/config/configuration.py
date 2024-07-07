from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataIngestionConfig
                                   ,DataValidationConfig)
import os 
class ConfigurationManager:
    def __init__(self, 
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH):

        print("Current Working Directory:", os.getcwd())  # Debugging
        print(f"Config File Path: {config_filepath}")
        print(f"Params File Path: {params_filepath}")
        
        if not config_filepath.exists():
            raise FileNotFoundError(f"The config file '{config_filepath}' does not exist.")
        
        if not params_filepath.exists():
            raise FileNotFoundError(f"The params file '{params_filepath}' does not exist.")

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )

        return data_validation_config