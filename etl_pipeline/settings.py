from pathlib import Path

from etl_pipeline.config_loader import config

# --------------------------------------------------
# Project Root
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# Data Directories
# --------------------------------------------------

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = PROJECT_ROOT / config["files"]["raw_directory"]

PROCESSED_DATA_DIR = (
    PROJECT_ROOT / config["files"]["processed_directory"]
)

ARCHIVE_DIRECTORY = (
    PROJECT_ROOT / config["files"]["archive_directory"]
)

# --------------------------------------------------
# Files & Directories
# --------------------------------------------------

# Directory containing all raw CSV files
RAW_DATA_DIRECTORY = RAW_DATA_DIR

# Default raw customer file
RAW_CUSTOMERS_FILE = (
    RAW_DATA_DIR / "customers.csv"
)

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

CREATE_ETL_RUN_HISTORY_SQL = (
    SQL_DIR / "create_etl_run_history.sql"
)

# --------------------------------------------------
# Logs
# --------------------------------------------------

LOG_DIR = PROJECT_ROOT / "logs"

LOG_FILE = LOG_DIR / "etl.log"

LOG_LEVEL = config["logging"]["level"]

LOG_MAX_SIZE_MB = config["logging"]["max_size_mb"]

LOG_BACKUP_COUNT = config["logging"]["backup_count"]

# --------------------------------------------------
# Database
# --------------------------------------------------

CUSTOMERS_TABLE = (
    config["database"]["customers_table"]
)

ETL_RUN_HISTORY_TABLE = (
    config["database"]["audit_table"]
)

# --------------------------------------------------
# Reports
# --------------------------------------------------

REPORTS_DIR = PROJECT_ROOT / "reports"

DATA_QUALITY_REPORT = (
    REPORTS_DIR / "data_quality_report.csv"
)

# --------------------------------------------------
# Pipeline Options
# --------------------------------------------------

ARCHIVE_ENABLED = (
    config["pipeline"]["archive_enabled"]
)

NOTIFICATIONS_ENABLED = (
    config["pipeline"]["notifications_enabled"]
)

# --------------------------------------------------
# Retry
# --------------------------------------------------

RETRY_ATTEMPTS = config["retry"]["attempts"]

RETRY_DELAY = config["retry"]["delay_seconds"]