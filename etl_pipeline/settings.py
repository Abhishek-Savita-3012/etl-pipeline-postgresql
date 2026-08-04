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

# --------------------------------------------------
# Files & Directories
# --------------------------------------------------

# Directory containing all raw CSV files
RAW_DATA_DIRECTORY = RAW_DATA_DIR

# (Optional) Default raw customer file
RAW_CUSTOMERS_FILE = RAW_DATA_DIR / "customers.csv"

# Processed output file
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

# --------------------------------------------------
# Reports
# --------------------------------------------------

REPORTS_DIR = PROJECT_ROOT / "reports"

DATA_QUALITY_REPORT = (
    REPORTS_DIR / "data_quality_report.csv"
)

# --------------------------------------------------
# Audit
# --------------------------------------------------

CREATE_ETL_RUN_HISTORY_SQL = (
    SQL_DIR / "create_etl_run_history.sql"
)

ETL_RUN_HISTORY_TABLE = "etl_run_history"

# --------------------------------------------------
# Archive
# --------------------------------------------------

ARCHIVE_DIRECTORY = DATA_DIR / "archive"