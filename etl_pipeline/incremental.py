import pandas as pd

from etl_pipeline.logger import logger


def filter_new_records(conn, df: pd.DataFrame):

    logger.info("Starting Incremental Load Check...")

    query = """
        SELECT customer_id
        FROM customers;
    """

    existing = pd.read_sql(query, conn)

    if existing.empty:

        logger.info(
            "Database is empty. Loading all records."
        )

        return df

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

    return new_df