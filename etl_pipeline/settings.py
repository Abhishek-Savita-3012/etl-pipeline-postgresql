from pathlib import Path

# --------------------------------------------------
# Project Root
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# Data Directories
# --------------------------------------------------

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

ARCHIVE_DIR = DATA_DIR / "archive"

# --------------------------------------------------
# Files
# --------------------------------------------------

RAW_CUSTOMERS_FILE = RAW_DATA_DIR / "customers.csv"

PROCESSED_CUSTOMERS_FILE = (
    PROCESSED_DATA_DIR / "customers_clean.csv"
)

# --------------------------------------------------
# SQL
# --------------------------------------------------

SQL_DIR = PROJECT_ROOT / "sql"

CREATE_CUSTOMERS_TABLE_SQL = (
    SQL_DIR / "create_customers_table.sql"
)

# --------------------------------------------------
# Logs
# --------------------------------------------------

LOG_DIR = PROJECT_ROOT / "logs"

LOG_FILE = LOG_DIR / "etl.log"

# --------------------------------------------------
# Database
# --------------------------------------------------

CUSTOMERS_TABLE = "customers"