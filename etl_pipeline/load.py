from pathlib import Path

import pandas as pd
import psycopg2

from etl_pipeline.config import get_connection

def create_table(conn):
    """
    Create customers table.
    """

    sql_file = Path("sql/create_customers_table.sql")

    with open(sql_file, "r") as file:
        query = file.read()

    cur = conn.cursor()

    cur.execute(query)

    conn.commit()

    cur.close()


def load_data(conn, df):
    """
    Load DataFrame into PostgreSQL.
    """

    cur = conn.cursor()

    inserted = 0

    for _, row in df.iterrows():

        cur.execute(
            """
            INSERT INTO customers
            (customer_id, name, age, city)

            VALUES (%s, %s, %s, %s)

            ON CONFLICT (customer_id)
            DO NOTHING;
            """,
            (
                int(row["customerid"]),
                row["name"],
                int(row["age"]),
                row["city"]
            )
        )

        inserted += 1

    conn.commit()

    cur.close()

    print(f"\nRows Processed : {inserted}")


if __name__ == "__main__":

    conn = get_connection()

    create_table(conn)

    df = pd.read_csv("data/processed/customers_clean.csv")

    load_data(conn, df)

    conn.close()

    print("\nData Loaded Successfully!")