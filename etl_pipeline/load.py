import pandas as pd

from etl_pipeline.config import get_connection
from etl_pipeline.logger import logger
from etl_pipeline.settings import (
    CREATE_CUSTOMERS_TABLE_SQL,
    PROCESSED_CUSTOMERS_FILE,
    CUSTOMERS_TABLE,
)


def create_table(conn):
    """
    Create customers table if it doesn't already exist.
    """

    with open(CREATE_CUSTOMERS_TABLE_SQL, "r") as file:
        query = file.read()

    cur = conn.cursor()

    cur.execute(query)

    conn.commit()

    cur.close()

    logger.info(f"Table '{CUSTOMERS_TABLE}' verified successfully.")


def load_data(conn, df):
    """
    Load DataFrame into PostgreSQL.
    """

    logger.info("Starting Load Phase...")

    cur = conn.cursor()

    inserted = 0

    for _, row in df.iterrows():

        cur.execute(
            f"""
            INSERT INTO {CUSTOMERS_TABLE}
            (customer_id, name, age, city)

            VALUES (%s, %s, %s, %s)

            ON CONFLICT (customer_id)
            DO NOTHING;
            """,
            (
                int(row["customerid"]),
                row["name"],
                int(row["age"]),
                row["city"],
            ),
        )

        inserted += 1

    conn.commit()

    cur.close()

    logger.info(f"Rows Processed : {inserted}")
    logger.info("Data loaded successfully.")


if __name__ == "__main__":

    conn = get_connection()

    create_table(conn)

    df = pd.read_csv(PROCESSED_CUSTOMERS_FILE)

    load_data(conn, df)

    conn.close()

    logger.info("Database connection closed.")