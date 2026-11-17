from google.cloud import bigquery

from common.config import (
    GCP_PROJECT,
    BIGQUERY_DATASET
)
import time

from common.logger import logger

class BaseLoader:
    table = None
    primary_key = None
    client = bigquery.Client(
        project=GCP_PROJECT
    )
    MAX_RETRIES = 3
    BASE_DELAY = 2
    
    @classmethod
    def load(cls, rows):
        if not rows:
            return 0

        dataset = f"{GCP_PROJECT}.{BIGQUERY_DATASET}"
        target = f"{dataset}.{cls.table}"
        staging = f"{dataset}.{cls.table}_staging"

        schema = cls.client.get_table(target).schema
        
        for attempt in range(cls.MAX_RETRIES):
            try:
                cls.client.load_table_from_json(
                    rows,
                    staging,
                    job_config=bigquery.LoadJobConfig(
                        schema=schema,
                        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
                    ),
                ).result()
                key = cls.primary_key
                update_set = ", ".join(
                    f"{f.name} = S.{f.name}" for f in schema if f.name != key
                )
                cls.client.query(f"""
                    MERGE `{target}` T
                    USING (
                        SELECT * FROM `{staging}`
                        WHERE TRUE
                        QUALIFY ROW_NUMBER() OVER (PARTITION BY {key} ORDER BY {key}) = 1
                    ) S
                    ON T.{key} = S.{key}
                    WHEN MATCHED THEN UPDATE SET {update_set}
                    WHEN NOT MATCHED THEN INSERT ROW
                """).result()

                logger.info("%d rows merged into %s", len(rows), cls.table)
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
