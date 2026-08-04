from etl_pipeline.logger import logger
from etl_pipeline.settings import (
    CREATE_ETL_RUN_HISTORY_SQL,
    ETL_RUN_HISTORY_TABLE,
)


def create_audit_table(conn):
    """
    Create ETL audit table if it doesn't exist.
    """

    with open(CREATE_ETL_RUN_HISTORY_SQL, "r") as file:
        query = file.read()

    cur = conn.cursor()

    cur.execute(query)

    conn.commit()

    cur.close()

    logger.info("ETL audit table verified successfully.")


def insert_audit_record(conn, metrics):
    """
    Insert one ETL execution record.
    """

    cur = conn.cursor()

    cur.execute(
        f"""
        INSERT INTO {ETL_RUN_HISTORY_TABLE}
        (
            run_timestamp,
            pipeline_status,
            total_records,
            cleaned_records,
            existing_records,
            new_records,
            execution_time_seconds
        )

        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """,
        (
            metrics["Timestamp"],
            metrics["Pipeline Status"],
            metrics["Total Records"],
            metrics["Cleaned Records"],
            metrics["Existing Records"],
            metrics["New Records"],
            metrics["Execution Time (sec)"],
        ),
    )

    conn.commit()

    cur.close()

    logger.info("Audit record inserted successfully.")