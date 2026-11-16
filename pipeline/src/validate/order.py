from validate.base import BaseValidator

class OrderValidator(BaseValidator):
    
    @classmethod
    def validate_row(cls, row):
        
        if not row["customer_id"]:
            return "Customer ID is missing"
        if not row["order_id"]:
            return "Order DI is missing"
        
        if not row["total_amount"]:
            return "Total Amount is missing"
        if row["total_amount"] < 0:
            return "Invalid Total Amount"
        return None