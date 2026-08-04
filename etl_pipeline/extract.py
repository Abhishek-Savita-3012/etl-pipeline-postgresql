from pathlib import Path

import pandas as pd

from etl_pipeline.logger import logger
from etl_pipeline.settings import RAW_CUSTOMERS_FILE


def extract_csv(file_path):
    """
    Reads a CSV file and returns a Pandas DataFrame.
    """

    logger.info("Starting Extract Phase...")

    file = Path(file_path)

    # Check if file exists
    if not file.exists():
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"{file_path} does not exist.")

    # Check if file is empty
    if file.stat().st_size == 0:
        logger.error(f"CSV file is empty: {file_path}")
        raise ValueError("CSV file is empty.")

    # Read CSV
    df = pd.read_csv(file)

    logger.info(f"Successfully extracted {len(df)} records from {file_path}")

    return df


if __name__ == "__main__":

    data = extract_csv(RAW_CUSTOMERS_FILE)

    logger.info("Extraction completed successfully.")
    logger.info(f"\n{data.head()}")