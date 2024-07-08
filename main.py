from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.logs import logger
import os 

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Failed to execute {STAGE_NAME} pipeline")
    logger.error(str(e))

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Failed to execute {STAGE_NAME} pipeline")
    logger.error(str(e))

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:
    logger.error(f"Failed to execute {STAGE_NAME} pipeline")
    logger.error(str(e))