from validate.base import BaseValidator
from common.phoneFormater import normalize_phone

class CustomerValidator(BaseValidator):
    seen = set()
    
    @classmethod
    def validate_row(cls, row):
        if not row["email"]:
            return "Email is missing"
        if not row["first_name"]:
            return "First name is missing"
        if row["email"] in cls.seen:
            return "Duplicated Customer by Email"
        if normalize_phone(row["phone"]) is None:
            return "Invalid Phone Number"
        
        cls.seen.add(row["email"])
        return None
