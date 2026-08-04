from pathlib import Path

from etl_pipeline.config import get_connection
from etl_pipeline.extract import extract_csv
from etl_pipeline.load import create_table, load_data
from etl_pipeline.logger import logger
from etl_pipeline.transform import transform_data


def run_pipeline():

    logger.info("=" * 60)
    logger.info("ETL PIPELINE STARTED")
    logger.info("=" * 60)

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

    try:
        create_table(conn)
        load_data(conn, df)

    finally:
        conn.close()
        logger.info("Database connection closed.")

    logger.info("=" * 60)
    logger.info("ETL PIPELINE COMPLETED SUCCESSFULLY")
    logger.info("=" * 60)


if __name__ == "__main__":
    run_pipeline()