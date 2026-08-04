import time
import traceback

from etl_pipeline.audit import (
    create_audit_table,
    insert_audit_record,
)
from etl_pipeline.config import get_connection
from etl_pipeline.extract import extract_csv
from etl_pipeline.incremental import filter_new_records
from etl_pipeline.load import create_table, load_data
from etl_pipeline.logger import logger
from etl_pipeline.notification import (
    notify_failure,
    notify_success,
)
from etl_pipeline.report import (
    create_metrics,
    generate_report,
)
from etl_pipeline.settings import (
    PROCESSED_CUSTOMERS_FILE,
    RAW_DATA_DIRECTORY,
)
from etl_pipeline.archive import (
    archive_processed_file,
)
from etl_pipeline.transform import transform_data
from etl_pipeline.validation import validate_dataframe


def finalize_pipeline(conn, metrics):
    """
    Generate report and save audit record.
    """

    generate_report(metrics)

    if conn is not None:
        insert_audit_record(conn, metrics)


def run_pipeline():
    """
    Runs the complete ETL pipeline.
    """

    start_time = time.perf_counter()
    conn = None

    logger.info("=" * 60)
    logger.info("ETL PIPELINE STARTED")
    logger.info("=" * 60)

    try:

        # -------------------------
        # Extract
        # -------------------------
        df = extract_csv(RAW_DATA_DIRECTORY)

        # -------------------------
        # Validate
        # -------------------------
        validate_dataframe(df)

        # -------------------------
        # Transform
        # -------------------------
        total_records = len(df)

        df, transform_metrics = transform_data(df)

        cleaned_records = len(df)

        # -------------------------
        # Save Processed Data
        # -------------------------
        PROCESSED_CUSTOMERS_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        df.to_csv(
            PROCESSED_CUSTOMERS_FILE,
            index=False
        )

        archive_processed_file()

        logger.info(
            f"Processed data saved to: "
            f"{PROCESSED_CUSTOMERS_FILE}"
        )

        # -------------------------
        # Database Connection
        # -------------------------
        conn = get_connection()

        create_table(conn)
        create_audit_table(conn)

        # -------------------------
        # Incremental Loading
        # -------------------------
        new_df, existing_records, new_records = (
            filter_new_records(conn, df)
        )

        # -------------------------
        # Load
        # -------------------------
        load_data(conn, new_df)

        execution_time = (
            time.perf_counter() - start_time
        )

        # -------------------------
        # Metrics
        # -------------------------
        metrics = create_metrics(
            total_records=total_records,
            duplicates_removed=transform_metrics[
                "duplicates_removed"
            ],
            missing_names=transform_metrics[
                "missing_names"
            ],
            invalid_ages=transform_metrics[
                "invalid_ages"
            ],
            cleaned_records=cleaned_records,
            existing_records=existing_records,
            new_records=new_records,
            execution_time=execution_time,
            pipeline_status="SUCCESS",
        )

        # -------------------------
        # Finalize
        # -------------------------
        finalize_pipeline(conn, metrics)

        notify_success(metrics)

        logger.info(
            "ETL Pipeline executed successfully."
        )

        return True

    except Exception as e:

        logger.exception("ETL Pipeline Failed!")
        logger.debug(traceback.format_exc())

        execution_time = (
            time.perf_counter() - start_time
        )

        metrics = create_metrics(
            total_records=0,
            duplicates_removed=0,
            missing_names=0,
            invalid_ages=0,
            cleaned_records=0,
            existing_records=0,
            new_records=0,
            execution_time=execution_time,
            pipeline_status="FAILED",
        )

        # -------------------------
        # Finalize
        # -------------------------
        finalize_pipeline(conn, metrics)

        notify_failure(e)

        return False

    finally:

        if conn is not None:
            conn.close()

            logger.info(
                "Database connection closed."
            )

        execution_time = (
            time.perf_counter() - start_time
        )

        logger.info(
            f"Execution Time: "
            f"{execution_time:.2f} seconds"
        )

        logger.info("=" * 60)


if __name__ == "__main__":
    run_pipeline()