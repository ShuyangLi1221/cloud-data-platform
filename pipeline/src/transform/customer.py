from transform.base import BaseTransformer
from common.phoneFormater import normalize_phone

PROVINCE_MAP = {
    "Saskatchewan": "SK",
    "Alberta": "AB",
    "Ontario": "ON",
    "British Columbia": "BC",
    "Manitoba": "MB",
}

class CustomerTransformer(BaseTransformer):
    
    @classmethod
    def transform_row(cls, row):
        return {
            "customer_id": row["customer_id"],
            "first_name": row["first_name"].strip().title(),
            "last_name": row["last_name"].strip().title(),
            "full_name": f"{row["first_name"].strip().title()} {row["last_name"].strip().title()}",
            "email": row["email"].lower(),
            "phone": normalize_phone(row["phone"]),
            "city": row["city"].strip().title(),
            "province": PROVINCE_MAP.get(
                row["province"],
                row["province"].strip().title()
            ),
            "created_date": row["created_at"].date().isoformat()
        }