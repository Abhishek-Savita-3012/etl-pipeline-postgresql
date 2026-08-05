import time
from functools import wraps

from etl_pipeline.logger import logger
from etl_pipeline.settings import (
    RETRY_ATTEMPTS,
    RETRY_DELAY,
)


def retry_on_failure(func):
    """
    Retry a function if it raises an exception.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        last_exception = None

        for attempt in range(
            1,
            RETRY_ATTEMPTS + 1,
        ):

            try:

                return func(
                    *args,
                    **kwargs,
                )

            except Exception as e:

                last_exception = e

                logger.warning(
                    f"Attempt {attempt}/{RETRY_ATTEMPTS} failed: {e}"
                )

                if attempt < RETRY_ATTEMPTS:

                    logger.info(
                        f"Retrying in {RETRY_DELAY} seconds..."
                    )

                    time.sleep(RETRY_DELAY)

        logger.error(
            "Maximum retry attempts reached."
        )

        raise last_exception

    return wrapper