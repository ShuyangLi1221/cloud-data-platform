from google.cloud import bigquery

from common.config import (
    GCP_PROJECT,
    BIGQUERY_DATASET
)
import time

from common.logger import logger

class BaseLoader:
    table = None
    client = bigquery.Client(
        project=GCP_PROJECT
    )
    MAX_RETRIES = 3
    BASE_DELAY = 2
    
    @classmethod
    def load(cls, rows):
        if not rows:
            return 0

        table_id = (
            f"{GCP_PROJECT}."
            f"{BIGQUERY_DATASET}."
            f"{cls.table}"
        )
        
        for attempt in range(cls.MAX_RETRIES):
            try:
                errors = cls.client.insert_rows_json(
                    table_id,
                    rows
                )
                if errors:
                    raise RuntimeError(
                        f"BigQuery insert failed: {errors}"
                    )
                logger.info(
                    "%d rows loaded into %s",
                    len(rows),
                    cls.table,
                )
                return len(rows)
            
            except Exception as e:
                if attempt ==cls.MAX_RETRIES -1:
                    logger.error(
                        "Load failed after %d attempts: %s",
                        cls.MAX_RETRIES,
                        str(e),
                    )
                    raise
                
                delay = cls.BASE_DELAY*(2**attempt)
                logger.warning(
                    "[%s] Load failed (attempt %d/%d): %s. Retrying in %d sec...",
                    cls.table,
                    attempt + 1,
                    cls.MAX_RETRIES,
                    str(e),
                    delay,
                )
                time.sleep(delay)
