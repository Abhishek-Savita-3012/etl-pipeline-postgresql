from etl_pipeline.cli import parse_arguments
from etl_pipeline.pipeline import run_pipeline


def main():

    args = parse_arguments()

    success = run_pipeline(
        skip_load=args.skip_load,
        report_only=args.report_only,
        no_notify=args.no_notify,
        verbose=args.verbose,
    )

    if success:

        print(
            "\nPipeline Finished Successfully."
        )

    else:

        print(
            "\nPipeline Failed."
        )


if __name__ == "__main__":

    main()