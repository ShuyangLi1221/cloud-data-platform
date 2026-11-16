class BaseTransformer:
    
    @classmethod
    def transform(cls, rows):
        return [
            cls.transform_row(row)
            for row in rows
        ]
    
    
    @classmethod
    def transform_row(cls, row):
        raise NotImplementedError