from datetime import UTC, datetime

from metadata.metadata_service import MetadataService
from common.logger import logger

class PipelineRunner:

    @classmethod
    def run(
        cls,
        pipeline
    ):
        
        MetadataService.start_pipeline(pipeline.name)

        logger.info(
            "========== %s ==========",
            pipeline.name,
        )

        pipeline_start = datetime.now(UTC)
        
        try:
            last_run = MetadataService.get_last_run(
                pipeline.name,
            )
            
            if last_run is None:
                rows = pipeline.extractor.extract_all_dict()
            else:
                rows = pipeline.extractor.extract_incremental(
                    last_run,
                )

            logger.info(
                "Extracted %d rows",
                len(rows),
            )

            validation = pipeline.validator.validate(rows)

            logger.info(
                "Validated %d rows",
                len(validation.valid_rows),
            )

            logger.info(
                "Rejected %d rows",
                len(validation.rejected_rows),
            )

            transformed = pipeline.transformer.transform(
                validation.valid_rows,
            )

            loaded = pipeline.loader.load(
                transformed,
            )

            duration = (datetime.now(UTC) - pipeline_start).total_seconds()
            
            MetadataService.finish_pipeline(
                pipeline_name=pipeline.name,
                last_run=datetime.now(UTC),
                rows_loaded=loaded,
                duration=duration
            )
            logger.info(
                """
==============================
%s

Status      : SUCCESS
Extracted   : %d
Validated   : %d
Rejected    : %d
Loaded      : %d
Duration    : %.2f sec
==============================
                """,
                pipeline.name,
                len(rows),
                len(validation.valid_rows),
                len(validation.rejected_rows),
                loaded,
                duration,
            )
        except Exception as e:
            MetadataService.fail_pipeline(
                pipeline.name,
                str(e)
            )
            logger.exception(
                "Pipeline %s failed",
                pipeline.name
            )
            
            raise
        
        
       