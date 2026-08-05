import pandas as pd

from etl_pipeline.logger import logger
from etl_pipeline.settings import CUSTOMERS_TABLE


def filter_new_records(conn, df: pd.DataFrame):
    """
    Filter out records that already exist
    in the PostgreSQL database.
    """

    logger.info("Starting Incremental Load Check...")

    cursor = conn.cursor()

    cursor.execute(
        f"""
        SELECT customer_id
        FROM {CUSTOMERS_TABLE};
        """
    )

    existing_ids = {
        row[0]
        for row in cursor.fetchall()
    }

    cursor.close()

    existing_records = len(existing_ids)

    # -------------------------
    # Database Empty
    # -------------------------
    if existing_records == 0:

        logger.info(
            "Database is empty. Loading all records."
        )

        return (
            df,
            0,
            len(df),
        )

    # -------------------------
    # Filter New Records
    # -------------------------
    new_df = df[
        ~df["customerid"].isin(existing_ids)
    ]

    new_records = len(new_df)

    logger.info(
        f"Existing Records : {existing_records}"
    )

    logger.info(
        f"New Records : {new_records}"
    )

    return (
        new_df,
        existing_records,
        new_records,
    )