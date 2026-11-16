from validate.base import BaseValidator

class OrderItemValidator(BaseValidator):
    
    @classmethod
    def validate_row(cls, row):
        
        if not row["product_id"]:
            return "Product ID is missing"
        if not row["order_id"]:
            return "Order DI is missing"
        
        if row["quantity"] < 0:
            return "Invalid Quantity"
        if row["unit_price"] < 0:
            return "Invalid Unit Price"
        if row["line_total"] < 0:
            return "Invalid Line Total"
        return None