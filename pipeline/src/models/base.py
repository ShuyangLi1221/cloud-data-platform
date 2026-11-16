from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.inspection import inspect

class Base(DeclarativeBase):
    def to_dict(self):
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self).mapper.column_attrs
        }