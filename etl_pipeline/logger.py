import logging
from logging.handlers import RotatingFileHandler

from etl_pipeline.settings import (
    LOG_DIR,
    LOG_FILE,
    LOG_LEVEL,
    LOG_MAX_SIZE_MB,
    LOG_BACKUP_COUNT,
)

# --------------------------------------------------
# Create Logs Directory
# --------------------------------------------------

LOG_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

# --------------------------------------------------
# Logger
# --------------------------------------------------

logger = logging.getLogger("etl_pipeline")

logger.setLevel(LOG_LEVEL)

# Prevent duplicate handlers
if logger.hasHandlers():
    logger.handlers.clear()

# --------------------------------------------------
# Formatter
# --------------------------------------------------

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

# --------------------------------------------------
# Rotating File Handler
# --------------------------------------------------

file_handler = RotatingFileHandler(
    filename=LOG_FILE,
    maxBytes=LOG_MAX_SIZE_MB * 1024 * 1024,
    backupCount=LOG_BACKUP_COUNT,
    encoding="utf-8",
)

file_handler.setFormatter(formatter)

# --------------------------------------------------
# Console Handler
# --------------------------------------------------

console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)

# --------------------------------------------------
# Add Handlers
# --------------------------------------------------

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Prevent log messages from propagating
# to the root logger.
logger.propagate = False