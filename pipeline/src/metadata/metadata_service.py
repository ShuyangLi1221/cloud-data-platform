from datetime import datetime, timedelta, UTC

from sqlalchemy.orm import Session

from common.database import engine
from models.etl_metadata import EtlMetadata


class MetadataService:

    @classmethod
    def get_last_run(cls, pipeline_name: str) -> datetime:

         with Session(engine) as session:

            metadata = (
                session.query(EtlMetadata)
                .filter_by(pipeline_name=pipeline_name)
                .first()
            )

            if metadata is None:
                return None

            return metadata.last_run

    @classmethod
    def start_pipeline(cls, pipeline_name):
        
        with Session(engine) as session:
            metadata = (
                session.query(EtlMetadata)
                .filter_by(
                    pipeline_name = pipeline_name
                )
                .first()
            )
            
            if metadata is None:
                metadata = EtlMetadata(
                    pipeline_name = pipeline_name
                )
                session.add(metadata)
            metadata.status = "RUNNING"
            metadata.error_message = None
            metadata.updated_at = datetime.now(UTC)

            session.commit()
    
    @classmethod
    def finish_pipeline(cls, pipeline_name, last_run, rows_loaded, duration):
        with Session(engine) as session:
            metadata = (
                session.query(EtlMetadata)
                .filter_by(
                    pipeline_name = pipeline_name
                )
                .first()
            )
            
            metadata.last_run = last_run
            metadata.status = "SUCCESS"
            metadata.rows_loaded = rows_loaded
            metadata.duration_seconds = duration
            metadata.updated_at = datetime.now(UTC)
            metadata.error_message = None
            
            session.commit()
    
    @classmethod
    def fail_pipeline(cls, pipeline_name, error_message):
        
        with Session(engine) as session:
            metadata = (
                session.query(EtlMetadata)
                .filter_by(
                    pipeline_name = pipeline_name
                )
                .first()
            )
            
            if metadata is None:
                metadata = EtlMetadata(
                    pipeline_name = pipeline_name
                )
                
                session.add(metadata)
            
            metadata.status = "FAILED"
            metadata.error_message = error_message
            metadata.updated_at = datetime.now(UTC)
            
            session.commit()