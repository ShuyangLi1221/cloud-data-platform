from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from sqlalchemy import inspect

from common.database import engine

class BaseExtractor(ABC):
    model = None
    incremental_column = None
    
    @classmethod
    def extract(cls, window_start, window_end):
        with Session(engine) as session:
            query = session.query(cls.model).filter(
                cls.incremental_column <= window_end
            )
            if window_start is not None:
                query = query.filter(
                    cls.incremental_column > window_start
                )
            return [row.to_dict() for row in query.all()]
    
    @classmethod
    def extract_all(cls):
        
        with Session(engine) as session:
            return session.query(cls.model).all()
        
    @classmethod
    def extract_all_dict(cls):
        return [
            cls.to_dict(row)
            for row in cls.extract_all()
        ]
    
    @classmethod
    def extract_incremental(cls, last_run_time):
        with Session(engine) as session:
            rows = (
                session.query(cls.model)
                .filter(
                    cls.incremental_column > last_run_time
                )
                .all()
            )
            return [
                row.to_dict()
                for row in rows
            ]
    
    
    @staticmethod
    def to_dict(model):
        return {
            c.key: getattr(model, c.key)
            for c in inspect(model).mapper.column_attrs
        }