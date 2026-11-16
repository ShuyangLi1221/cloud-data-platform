from analytics.base import BaseAnalytics
from common.config import (
    GCP_PROJECT,
    BIGQUERY_DATASET,
)


class SalesAnalytics(BaseAnalytics):

    sql = f"""
    MERGE
    `{GCP_PROJECT}.{BIGQUERY_DATASET}.fact_sales` T

    USING (

        SELECT

            o.order_id,

            o.order_date,

            o.customer_id,

            oi.product_id,

            oi.quantity,

            oi.unit_price,

            oi.quantity * oi.unit_price
                AS sales_amount

        FROM
        `{GCP_PROJECT}.{BIGQUERY_DATASET}.orders` o

        JOIN
        `{GCP_PROJECT}.{BIGQUERY_DATASET}.order_items` oi

        ON
        o.order_id = oi.order_id

    ) S

    ON

    T.order_id = S.order_id
    AND
    T.product_id = S.product_id

    WHEN MATCHED THEN

        UPDATE SET

            quantity = S.quantity,

            unit_price = S.unit_price,

            sales_amount = S.sales_amount

    WHEN NOT MATCHED THEN

        INSERT ROW
    """