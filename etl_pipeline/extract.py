from pathlib import Path

import pandas as pd

from etl_pipeline.logger import logger


def extract_csv(path):
    """
    Reads one or more CSV files and returns a combined DataFrame.

    Supports:
    - Single CSV file
    - Directory containing multiple CSV files
    """

    logger.info("Starting Extract Phase...")

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(
            f"{path} does not exist."
        )

    # -------------------------
    # Single CSV File
    # -------------------------
    if path.is_file():

        if path.suffix.lower() != ".csv":
            raise ValueError("File must be a CSV.")

        if path.stat().st_size == 0:
            raise ValueError("CSV file is empty.")

        logger.info(f"Reading {path.name}")

        df = pd.read_csv(path)

        logger.info(
            f"Successfully extracted {len(df)} records."
        )

        return df

    # -------------------------
    # Directory of CSV Files
    # -------------------------
    csv_files = sorted(path.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            "No CSV files found."
        )

    dataframes = []

    for file in csv_files:

        if file.stat().st_size == 0:

            logger.warning(
                f"Skipping empty file: {file.name}"
            )

            continue

        logger.info(f"Reading {file.name}")

        df = pd.read_csv(file)

        logger.info(
            f"{len(df)} records loaded."
        )

        dataframes.append(df)

    if not dataframes:
        raise ValueError(
            "All CSV files are empty."
        )

    combined_df = pd.concat(
        dataframes,
        ignore_index=True
    )

    logger.info(
        f"Total records extracted: {len(combined_df)}"
    )

    return combined_df


if __name__ == "__main__":

    from etl_pipeline.settings import RAW_DATA_DIRECTORY

    df = extract_csv(RAW_DATA_DIRECTORY)

    print(df.head())