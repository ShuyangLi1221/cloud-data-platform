from analytics.base import BaseAnalytics
from common.config import GCP_PROJECT, BIGQUERY_DATASET


class CategorySalesAnalytics(BaseAnalytics):

    sql = f"""
    CREATE OR REPLACE TABLE
    `{GCP_PROJECT}.{BIGQUERY_DATASET}.category_sales`
    AS

    SELECT

        p.category,

        SUM(f.quantity) AS quantity,

        SUM(f.sales_amount) AS revenue

    FROM `{GCP_PROJECT}.{BIGQUERY_DATASET}.fact_sales` f

    JOIN `{GCP_PROJECT}.{BIGQUERY_DATASET}.products` p
      ON f.product_id = p.product_id

    GROUP BY p.category

    ORDER BY revenue DESC
    """