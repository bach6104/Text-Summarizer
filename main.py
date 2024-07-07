from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logs import logger


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Failed to execute {STAGE_NAME} pipeline")
    logger.error(str(e))