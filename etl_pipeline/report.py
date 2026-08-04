from datetime import datetime

import pandas as pd

from etl_pipeline.logger import logger
from etl_pipeline.settings import (
    REPORTS_DIR,
    DATA_QUALITY_REPORT,
)


def generate_report(metrics: dict):
    """
    Generate Data Quality Report.
    """

    REPORTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    report = pd.DataFrame([metrics])

    report.to_csv(
        DATA_QUALITY_REPORT,
        index=False
    )

    logger.info(
        f"Data Quality Report saved to: {DATA_QUALITY_REPORT}"
    )


def create_metrics(
    total_records,
    duplicates_removed,
    missing_names,
    invalid_ages,
    cleaned_records,
    existing_records,
    new_records,
    execution_time,
    pipeline_status,
):
    """
    Create report metrics.
    """

    return {
        "Timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "Total Records": total_records,
        "Duplicates Removed": duplicates_removed,
        "Missing Names": missing_names,
        "Invalid Ages": invalid_ages,
        "Cleaned Records": cleaned_records,
        "Existing Records": existing_records,
        "New Records": new_records,
        "Execution Time (sec)": round(
            execution_time,
            2,
        ),
        "Pipeline Status": pipeline_status,
    }