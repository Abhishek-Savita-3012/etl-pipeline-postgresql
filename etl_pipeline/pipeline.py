from pathlib import Path
import time
import traceback

from etl_pipeline.config import get_connection
from etl_pipeline.extract import extract_csv
from etl_pipeline.load import create_table, load_data
from etl_pipeline.logger import logger
from etl_pipeline.transform import transform_data


def run_pipeline():

    start_time = time.perf_counter()
    conn = None

    logger.info("=" * 60)
    logger.info("ETL PIPELINE STARTED")
    logger.info("=" * 60)

    try:

        # -------------------------
        # Extract
        # -------------------------
        raw_file = Path("data/raw/customers.csv")

        df = extract_csv(raw_file)

        # -------------------------
        # Transform
        # -------------------------
        df = transform_data(df)

        processed_file = Path("data/processed/customers_clean.csv")

        processed_file.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(processed_file, index=False)

        logger.info(f"Processed data saved to: {processed_file}")

        # -------------------------
        # Load
        # -------------------------
        conn = get_connection()

        create_table(conn)

        load_data(conn, df)

        logger.info("ETL Pipeline executed successfully.")

        return True

    except Exception as e:

        logger.exception("ETL Pipeline Failed!")

        logger.error(str(e))

        logger.debug(traceback.format_exc())

        return False

    finally:

        if conn is not None:
            conn.close()
            logger.info("Database connection closed.")

        execution_time = time.perf_counter() - start_time

        logger.info(f"Execution Time: {execution_time:.2f} seconds")

        logger.info("=" * 60)


if __name__ == "__main__":
    run_pipeline()