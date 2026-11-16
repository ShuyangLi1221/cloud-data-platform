import re

def normalize_phone(phone: str) -> str | None:
    
    phone = re.split(r"\s*x\d+", phone, flags=re.IGNORECASE)[0]
    
    digits = re.sub(r"\D", "", phone)
    
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
        
    if len(digits) != 10:
        return None
    
    return digits