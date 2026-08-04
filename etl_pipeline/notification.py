from etl_pipeline.logger import logger


def notify_success(metrics):
    """
    Handle successful pipeline execution notification.
    """

    logger.info("=" * 50)
    logger.info("PIPELINE STATUS : SUCCESS")
    logger.info(
        f"Records Loaded : {metrics['New Records']}"
    )
    logger.info("=" * 50)


def notify_failure(error):
    """
    Handle failed pipeline execution notification.
    """

    logger.error("=" * 50)
    logger.error("PIPELINE STATUS : FAILED")
    logger.error(str(error))
    logger.error("=" * 50)