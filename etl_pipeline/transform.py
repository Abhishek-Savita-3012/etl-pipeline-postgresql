import pandas as pd

from etl_pipeline.logger import logger
from etl_pipeline.settings import (
    RAW_CUSTOMERS_FILE,
    PROCESSED_CUSTOMERS_FILE,
)


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform customer data.
    """

    logger.info("Starting Transform Phase...")

    # ----------------------------
    # Standardize column names
    # ----------------------------
    df.columns = df.columns.str.strip().str.lower()

    # ----------------------------
    # Remove duplicate rows
    # ----------------------------
    duplicates_removed = df.duplicated().sum()
    df = df.drop_duplicates()

    # ----------------------------
    # Handle missing values
    # ----------------------------

    # Drop rows where Name is missing
    missing_names = df["name"].isnull().sum()
    df = df.dropna(subset=["name"])

    # Fill missing Age with median
    df["age"] = df["age"].fillna(df["age"].median())

    # Fill missing City with "Unknown"
    df["city"] = df["city"].fillna("Unknown")

    # ----------------------------
    # Standardize names
    # ----------------------------
    df["name"] = df["name"].str.title()

    # ----------------------------
    # Remove invalid ages
    # ----------------------------
    invalid_age = (df["age"] > 100).sum()
    df = df[df["age"] <= 100]

    # ----------------------------
    # Convert Age to integer
    # ----------------------------
    df["age"] = df["age"].astype(int)

    logger.info(f"Duplicates Removed : {duplicates_removed}")
    logger.info(f"Missing Names      : {missing_names}")
    logger.info(f"Invalid Ages       : {invalid_age}")

    logger.info("Transformation completed successfully.")

    metrics = {
        "duplicates_removed": duplicates_removed,
        "missing_names": missing_names,
        "invalid_ages": invalid_age,
    }

    return df, metrics


if __name__ == "__main__":

    df = pd.read_csv(RAW_CUSTOMERS_FILE)

    cleaned_df = transform_data(df)

    PROCESSED_CUSTOMERS_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    cleaned_df.to_csv(
        PROCESSED_CUSTOMERS_FILE,
        index=False
    )

    logger.info(
        f"Cleaned data saved to {PROCESSED_CUSTOMERS_FILE}"
    )