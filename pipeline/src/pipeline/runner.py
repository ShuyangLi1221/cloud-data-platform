from datetime import UTC, datetime, timedelta

from metadata.metadata_service import MetadataService
from common.logger import logger
from load.rejected import load_rejected
from common.alert import send_alert


class PipelineRunner:
    
    SATETY_LAG = timedelta(minutes=5)
    LOOKBACK = timedelta(minutes=10)
    REJECT_THRESHOLD = 0.05

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
            windown_end = datetime.now(UTC) - cls.SATETY_LAG
            last_run = MetadataService.get_last_run(pipeline.name)
            window_start = last_run - cls.LOOKBACK if last_run else None
            
            rows = pipeline.extractor.extract(window_start, windown_end)

            logger.info(
                "Extracted %d rows",
                len(rows),
            )

            validation = pipeline.validator.validate(rows)
            load_rejected(pipeline.name, validation.rejected_rows)
            if rows and (len(validation.rejected_rows) / len(rows)) > cls.REJECT_THRESHOLD:
                send_alert(
                    f"{pipeline.name}: high reject rate",
                    f"{len(validation.rejected_rows)} of {len(rows)} rows rejected.\n"
                    f"See the rejected_rows table in BigQuery.",
                )

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
                last_run=windown_end,
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
            send_alert(
                f"Pipeline {pipeline.name} failed",
                f"Pipeline: {pipeline.name}\nError: {e}",
            )
            
            raise
        
        
       