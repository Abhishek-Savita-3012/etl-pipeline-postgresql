import os

import psycopg2
from dotenv import load_dotenv

from etl_pipeline.retry import retry_on_failure

load_dotenv()


@retry_on_failure
def get_connection():
    """
    Returns a PostgreSQL database connection.
    Retries automatically if the connection fails.
    """

    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
