from analytics.base import BaseAnalytics
from common.config import GCP_PROJECT, BIGQUERY_DATASET


class TopCustomersAnalytics(BaseAnalytics):

    sql = f"""
    CREATE OR REPLACE TABLE
    `{GCP_PROJECT}.{BIGQUERY_DATASET}.top_customers`
    AS

    SELECT

        c.customer_id,

        c.full_name,

        c.city,

        COUNT(DISTINCT f.order_id) AS orders,

        SUM(f.sales_amount) AS revenue

    FROM `{GCP_PROJECT}.{BIGQUERY_DATASET}.fact_sales` f

    JOIN `{GCP_PROJECT}.{BIGQUERY_DATASET}.customers` c
      ON f.customer_id = c.customer_id

    GROUP BY
        c.customer_id,
        c.full_name,
        c.city

    ORDER BY revenue DESC
    """