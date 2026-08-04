import time
import traceback

from etl_pipeline.config import get_connection
from etl_pipeline.extract import extract_csv
from etl_pipeline.incremental import filter_new_records
from etl_pipeline.load import create_table, load_data
from etl_pipeline.logger import logger
from etl_pipeline.settings import (
    RAW_DATA_DIRECTORY,
    PROCESSED_CUSTOMERS_FILE,
)
from etl_pipeline.transform import transform_data
from etl_pipeline.validation import validate_dataframe


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
        df = transform_data(df)

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

        logger.info(
            f"Processed data saved to: {PROCESSED_CUSTOMERS_FILE}"
        )

        # -------------------------
        # Database Connection
        # -------------------------
        conn = get_connection()

        create_table(conn)

        # -------------------------
        # Incremental Loading
        # -------------------------
        new_df = filter_new_records(conn, df)

        # -------------------------
        # Load
        # -------------------------
        load_data(conn, new_df)

        logger.info("ETL Pipeline executed successfully.")

        return True

    except Exception:

        logger.exception("ETL Pipeline Failed!")
        logger.debug(traceback.format_exc())

        return False

    finally:

        if conn is not None:
            conn.close()
            logger.info("Database connection closed.")

        execution_time = time.perf_counter() - start_time

        logger.info(
            f"Execution Time: {execution_time:.2f} seconds"
        )

        logger.info("=" * 60)


if __name__ == "__main__":
    run_pipeline()