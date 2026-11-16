from validate.base import BaseValidator

class ProductValidator(BaseValidator):

    @classmethod
    def validate_row(cls, row):

        if not row["sku"]:
            return "SKU is missing"

        if not row["product_name"]:
            return "Product name is missing"

        if row["price"] is None:
            return "Price is missing"

        if row["price"] < 0:
            return "Price cannot be negative"

        return None