CREATE TABLE IF NOT EXISTS etl_run_history (

    run_id SERIAL PRIMARY KEY,

    run_timestamp TIMESTAMP NOT NULL,

    pipeline_status VARCHAR(20),

    total_records INTEGER,

    cleaned_records INTEGER,

    existing_records INTEGER,

    new_records INTEGER,

    execution_time_seconds NUMERIC(10,2)

);