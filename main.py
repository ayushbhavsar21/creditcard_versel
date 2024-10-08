from credit_default import logger

from credit_default.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from credit_default.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from credit_default.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from credit_default.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from credit_default.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e  


STAGE_NAME =  "Data Validation Stage"
try:
  logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<")
  obj = DataValidationTrainingPipeline()
  obj.main()
  logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation stage "
try:
   logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e