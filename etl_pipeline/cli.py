import argparse


def parse_arguments():
    """
    Parse command-line arguments.
    """

    parser = argparse.ArgumentParser(
        description="Customer ETL Pipeline"
    )

    parser.add_argument(
        "--skip-load",
        action="store_true",
        help="Skip loading data into PostgreSQL.",
    )

    parser.add_argument(
        "--report-only",
        action="store_true",
        help="Generate report without loading data.",
    )

    parser.add_argument(
        "--no-notify",
        action="store_true",
        help="Disable notifications for this run.",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Display additional information.",
    )

    return parser.parse_args()