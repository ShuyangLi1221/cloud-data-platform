from google.cloud import bigquery

CUSTOMER_SCHEMA = [
    bigquery.SchemaField("customer_id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("first_name", "STRING"),
    bigquery.SchemaField("last_name", "STRING"),
    bigquery.SchemaField("full_name", "STRING"),
    bigquery.SchemaField("email", "STRING"),
    bigquery.SchemaField("phone", "STRING"),
    bigquery.SchemaField("city", "STRING"),
    bigquery.SchemaField("province", "STRING"),
    bigquery.SchemaField("created_date", "DATE"),
]

PRODUCT_SCHEMA = [
    bigquery.SchemaField("product_id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("sku", "STRING"),
    bigquery.SchemaField("brand", "STRING"),
    bigquery.SchemaField("category", "STRING"),
    bigquery.SchemaField("product_name", "STRING"),
    bigquery.SchemaField("price", "FLOAT"),
]

ORDER_SCHEMA = [
    bigquery.SchemaField("customer_id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("order_id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("status", "STRING"),
    bigquery.SchemaField("total_amount", "FLOAT"),
    bigquery.SchemaField("order_date", "DATE"),
    bigquery.SchemaField("created_at", "DATE"),
]

ORDER_ITEM_SCHEMA = [
    bigquery.SchemaField("order_item_id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("order_id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("product_id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("quantity", "INTEGER"),
    bigquery.SchemaField("unit_price", "FLOAT"),
    bigquery.SchemaField("line_total", "FLOAT"),
]


FACT_SALES_SCHEMA = [
    bigquery.SchemaField("order_id", "INTEGER"),
    bigquery.SchemaField("order_date", "DATE"),
    bigquery.SchemaField("customer_id", "INTEGER"),
    bigquery.SchemaField("product_id", "INTEGER"),
    bigquery.SchemaField("quantity", "INTEGER"),
    bigquery.SchemaField("unit_price", "FLOAT"),
    bigquery.SchemaField("sales_amount", "FLOAT"),
]

DAILY_SALES_SCHEMA = [
    bigquery.SchemaField("order_date", "DATE"),
    bigquery.SchemaField("total_orders", "INTEGER"),
    bigquery.SchemaField("total_customers", "INTEGER"),
    bigquery.SchemaField("total_quantity", "INTEGER"),
    bigquery.SchemaField("revenue", "FLOAT"),
    bigquery.SchemaField("avg_order_value", "FLOAT"),
]

TOP_PRODUCTS_SCHEMA = [
    bigquery.SchemaField("product_id", "INTEGER"),
    bigquery.SchemaField("product_name", "STRING"),
    bigquery.SchemaField("brand", "STRING"),
    bigquery.SchemaField("category", "STRING"),
    bigquery.SchemaField("quantity_sold", "INTEGER"),
    bigquery.SchemaField("revenue", "FLOAT"),
]

TOP_CUSTOMERS_SCHEMA = [
    bigquery.SchemaField("customer_id", "INTEGER"),
    bigquery.SchemaField("full_name", "STRING"),
    bigquery.SchemaField("city", "STRING"),
    bigquery.SchemaField("orders", "INTEGER"),
    bigquery.SchemaField("revenue", "FLOAT"),
]

CATEGORY_SALES_SCHEMA = [
    bigquery.SchemaField("category", "STRING"),
    bigquery.SchemaField("quantity", "INTEGER"),
    bigquery.SchemaField("revenue", "FLOAT"),
]

REJECTED_SCHEMA = [
    bigquery.SchemaField("pipeline_name", "STRING"),
    bigquery.SchemaField("reason", "STRING"),
    bigquery.SchemaField("row_json", "STRING"),
    bigquery.SchemaField("rejected_at", "TIMESTAMP"),
]