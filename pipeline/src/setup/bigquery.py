from google.cloud import bigquery
from google.oauth2 import service_account

from common.config import (
    GCP_PROJECT,
    BIGQUERY_DATASET,
    GOOGLE_APPLICATION_CREDENTIALS,
)

from setup.schema import (
    CUSTOMER_SCHEMA,
    PRODUCT_SCHEMA,
    ORDER_SCHEMA,
    ORDER_ITEM_SCHEMA,
    FACT_SALES_SCHEMA,
    DAILY_SALES_SCHEMA,
    TOP_CUSTOMERS_SCHEMA,
    TOP_PRODUCTS_SCHEMA,
    CATEGORY_SALES_SCHEMA
)
from common.logger import logger

TABLES = [
    ("customers", CUSTOMER_SCHEMA),
    ("products", PRODUCT_SCHEMA),
    ("orders", ORDER_SCHEMA),
    ("order_items", ORDER_ITEM_SCHEMA),
    ("fact_sales", FACT_SALES_SCHEMA),
    ("daily_sales_summary", DAILY_SALES_SCHEMA),
    ("top_products", TOP_PRODUCTS_SCHEMA),
    ("top_customers", TOP_CUSTOMERS_SCHEMA),
    ("category_sales", CATEGORY_SALES_SCHEMA),
]

credentials = service_account.Credentials.from_service_account_file(
    GOOGLE_APPLICATION_CREDENTIALS
)

client = bigquery.Client(
    project=GCP_PROJECT,
    credentials=credentials,
)

dataset_id = f"{GCP_PROJECT}.{BIGQUERY_DATASET}"

def create_bigquery_tables():
    # Create Dataset
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"

    client.create_dataset(
        dataset,
        exists_ok=True,
    )

    logger.info("Dataset ready.")
    # Create tables
    for table_name, schema in TABLES:
        table = bigquery.Table(
            f"{dataset_id}.{table_name}",
            schema=schema,
        )

        client.create_table(
            table,
            exists_ok=True,
        )

        logger.info("%s ready.", table_name)
        logger.info(
            "BigQuery initialization completed."
        )
