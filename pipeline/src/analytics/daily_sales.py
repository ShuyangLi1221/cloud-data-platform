from analytics.base import BaseAnalytics
from common.config import GCP_PROJECT, BIGQUERY_DATASET


class DailySalesAnalytics(BaseAnalytics):

    sql = f"""
    CREATE OR REPLACE TABLE
    `{GCP_PROJECT}.{BIGQUERY_DATASET}.daily_sales_summary`
    AS

    SELECT

        order_date,

        COUNT(DISTINCT order_id) AS total_orders,

        COUNT(DISTINCT customer_id) AS total_customers,

        SUM(quantity) AS total_quantity,

        SUM(sales_amount) AS revenue,

        AVG(sales_amount) AS avg_order_value

    FROM `{GCP_PROJECT}.{BIGQUERY_DATASET}.fact_sales`

    GROUP BY order_date
    """