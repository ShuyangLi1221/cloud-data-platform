from google.cloud import bigquery

from common.config import GCP_PROJECT
from common.logger import logger

class BaseAnalytics:
    client = bigquery.Client(project=GCP_PROJECT)
    
    @classmethod
    def run(cls):
        logger.info("Running analytics: %s", cls.__name__)
        job = cls.client.query(cls.sql)
        
        job.result()
        logger.info("Analytics completed: %s", cls.__name__)