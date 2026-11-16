from transform.base import BaseTransformer


class OrderTransformer(BaseTransformer):
    
    @classmethod
    def transform_row(cls, row):
        return {
            "order_id": row["order_id"],
            "customer_id": row["customer_id"],
            "status": row["status"],
            "total_amount": float(row["total_amount"]),
            "order_date": row["order_date"].date().isoformat(),
            "created_at": row["created_at"].date().isoformat(),
        }