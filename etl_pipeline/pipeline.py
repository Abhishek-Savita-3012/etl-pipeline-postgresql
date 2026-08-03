from pathlib import Path

import pandas as pd

from etl_pipeline.config import get_connection
from etl_pipeline.extract import extract_csv
from etl_pipeline.load import create_table
from etl_pipeline.load import load_data
from etl_pipeline.logger import logger
from etl_pipeline.transform import transform_data


def run_pipeline():

    logger.info("Pipeline Started")

    raw_file = Path("data/raw/customers.csv")

    df = extract_csv(raw_file)

    df = transform_data(df)

    df.to_csv(
        "data/processed/customers_clean.csv",
        index=False
    )

    conn = get_connection()

    create_table(conn)

    load_data(conn, df)

    conn.close()

    logger.info("Pipeline Completed Successfully")


if __name__ == "__main__":

    run_pipeline()