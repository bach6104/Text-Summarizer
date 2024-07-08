from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DataIngestionConfig:
    def __init__(self, root_dir, source_URL, local_data_file, unzip_dir):
        self.root_dir = root_dir
        self.source_URL = source_URL
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE : str 
    ALL_REQUIRED_FILES : list

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path
