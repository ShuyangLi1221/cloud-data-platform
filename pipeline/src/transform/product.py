from transform.base import BaseTransformer


class ProductTransformer(BaseTransformer):
    @classmethod
    def transform_row(cls, row):
        return {
            "product_id": row["product_id"],
            "sku": row["sku"].strip(),
            "brand": row["brand"].strip().upper(),
            "category": row["category"].strip().title(),
            "product_name": row["product_name"].strip(),
            "price": float(row["price"]),
        }
