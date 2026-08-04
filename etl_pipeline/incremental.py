import pandas as pd

from etl_pipeline.logger import logger
from etl_pipeline.settings import CUSTOMERS_TABLE


def filter_new_records(conn, df: pd.DataFrame):
    """
    Filter out records that already exist in the database.
    """

    logger.info("Starting Incremental Load Check...")

    query = f"""
        SELECT customer_id
        FROM {CUSTOMERS_TABLE};
    """

    existing = pd.read_sql(query, conn)

    # -------------------------
    # Database Empty
    # -------------------------
    if existing.empty:

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
        ~df["customerid"].isin(
            existing["customer_id"]
        )
    ]

    logger.info(
        f"Existing Records : {len(existing)}"
    )

    logger.info(
        f"New Records : {len(new_df)}"
    )

    return (
        new_df,
        len(existing),
        len(new_df),
    )