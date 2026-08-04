from datetime import datetime
import shutil

from etl_pipeline.logger import logger
from etl_pipeline.settings import (
    ARCHIVE_DIRECTORY,
    ARCHIVE_ENABLED,
    PROCESSED_CUSTOMERS_FILE,
)


def archive_processed_file():
    """
    Archive the processed CSV with a timestamp.
    """

    if not ARCHIVE_ENABLED:

        logger.info(
            "Archiving is disabled in configuration."
        )

        return

    if not PROCESSED_CUSTOMERS_FILE.exists():

        logger.warning(
            "Processed file not found. Skipping archive."
        )

        return

    ARCHIVE_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    archive_file = (
        ARCHIVE_DIRECTORY
        / f"customers_{timestamp}.csv"
    )

    shutil.copy2(
        PROCESSED_CUSTOMERS_FILE,
        archive_file
    )

    logger.info(
        f"Archived processed file to: {archive_file}"
    )


if __name__ == "__main__":

    archive_processed_file()