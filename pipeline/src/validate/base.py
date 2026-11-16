from validate.validationResult import ValidationResult

class BaseValidator:
    required_fields = []

    @classmethod
    def validate(cls, rows):
        result = ValidationResult()

        for row in rows:
            error = cls.validate_row(row)

            if error is None:
                result.valid_rows.append(row)
            else:
                result.rejected_rows.append({
                "row": row,
                "reason": error,
                })

        return result
    
    
    @classmethod
    def validate_row(cls, row):
        raise NotImplementedError