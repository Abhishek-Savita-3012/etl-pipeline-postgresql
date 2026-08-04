from pathlib import Path

import pandas as pd

from etl_pipeline.logger import logger


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform customer data.
    """

    logger.info("Starting Transform Phase...")

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    # Remove duplicates
    duplicates_removed = df.duplicated().sum()
    df = df.drop_duplicates()

    # Remove rows with missing names
    missing_names = df["name"].isnull().sum()
    df = df.dropna(subset=["name"])

    # Fill missing age
    df["age"] = df["age"].fillna(df["age"].median())

    # Fill missing city
    df["city"] = df["city"].fillna("Unknown")

    # Standardize names
    df["name"] = df["name"].str.title()

    # Remove invalid ages
    invalid_age = (df["age"] > 100).sum()
    df = df[df["age"] <= 100]

    # Convert datatype
    df["age"] = df["age"].astype(int)

    logger.info(f"Duplicates Removed : {duplicates_removed}")
    logger.info(f"Missing Names      : {missing_names}")
    logger.info(f"Invalid Ages       : {invalid_age}")

    logger.info("Transformation completed successfully.")

    return df


if __name__ == "__main__":

    input_file = Path("data/raw/customers.csv")

    df = pd.read_csv(input_file)

    cleaned_df = transform_data(df)

    output_file = Path("data/processed/customers_clean.csv")

    output_file.parent.mkdir(parents=True, exist_ok=True)

    cleaned_df.to_csv(output_file, index=False)

    logger.info(f"Cleaned data saved to {output_file}")