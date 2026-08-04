import pandas as pd

from etl_pipeline.logger import logger


REQUIRED_COLUMNS = [
    "CustomerID",
    "Name",
    "Age",
    "City",
]


def validate_dataframe(df: pd.DataFrame) -> bool:
    """
    Validate raw customer data before transformation.
    """

    logger.info("Starting Data Validation...")

    # ----------------------------
    # Check required columns
    # ----------------------------
    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        logger.error(
            f"Missing columns: {missing_columns}"
        )
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    logger.info("Required columns validated.")

    # ----------------------------
    # Duplicate Customer IDs
    # ----------------------------
    duplicate_ids = df["CustomerID"].duplicated().sum()

    logger.info(
        f"Duplicate Customer IDs: {duplicate_ids}"
    )

    # ----------------------------
    # Missing Customer IDs
    # ----------------------------
    missing_ids = df["CustomerID"].isnull().sum()

    logger.info(
        f"Missing Customer IDs: {missing_ids}"
    )

    # ----------------------------
    # Invalid Ages
    # ----------------------------
    invalid_age = (
        (df["Age"] < 0) |
        (df["Age"] > 100)
    ).sum()

    logger.info(
        f"Invalid Ages: {invalid_age}"
    )

    # ----------------------------
    # Missing Names
    # ----------------------------
    missing_names = df["Name"].isnull().sum()

    logger.info(
        f"Missing Names: {missing_names}"
    )

    logger.info("Validation completed.")

    return True