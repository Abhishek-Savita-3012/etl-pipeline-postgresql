from etl_pipeline.pipeline import run_pipeline

if __name__ == "__main__":

    success = run_pipeline()

    if success:
        print("\nPipeline Finished Successfully.")
    else:
        print("\nPipeline Failed.")