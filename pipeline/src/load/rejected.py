import json
from datetime import UTC, datetime

from google.cloud import bigquery

from common.config import GCP_PROJECT, BIGQUERY_DATASET
from load.base import BaseLoader


def load_rejected(pipeline_name, rejected_rows):
    if not rejected_rows:
        return
    now = datetime.now(UTC).isoformat()
    rows = [
        {
            "pipeline_name": pipeline_name,
            "reason": r["reason"],
            "row_json": json.dumps(r["row"], default=str),
            "rejected_at": now,
        }
        for r in rejected_rows
    ]
    BaseLoader.client.load_table_from_json(
        rows,
        f"{GCP_PROJECT}.{BIGQUERY_DATASET}.rejected_rows",
        job_config=bigquery.LoadJobConfig(
            write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        ),
    ).result()