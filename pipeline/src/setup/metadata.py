from common.database import engine
from models.base import Base

from models.etl_metadata import EtlMetadata

def create_metadata_table():
    Base.metadata.create_all(engine)