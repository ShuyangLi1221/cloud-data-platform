from transform.base import BaseTransformer

class OrderItemTransformer(BaseTransformer):
    
    @classmethod
    def transform_row(cls, row):
        return {
            "order_item_id": row["order_item_id"],
            "order_id": row["order_id"],
            "product_id": row["product_id"],
            "quantity": row["quantity"],
            "unit_price": float(row["unit_price"]),
            "line_total": float(row["quantity"] * row["unit_price"])
        }