import pandas as pd

from etl_pipeline.extract import extract_csv
from etl_pipeline.settings import RAW_CUSTOMERS_FILE
from etl_pipeline.transform import transform_data


def test_transform_returns_dataframe():

    df = extract_csv(RAW_CUSTOMERS_FILE)

    cleaned = transform_data(df)

    assert isinstance(cleaned, pd.DataFrame)


def test_no_missing_names():

    df = extract_csv(RAW_CUSTOMERS_FILE)

    cleaned = transform_data(df)

    assert cleaned["name"].isnull().sum() == 0


def test_no_duplicate_rows():

    df = extract_csv(RAW_CUSTOMERS_FILE)

    cleaned = transform_data(df)

    assert cleaned.duplicated().sum() == 0


def test_invalid_age_removed():

    df = extract_csv(RAW_CUSTOMERS_FILE)

    cleaned = transform_data(df)

    assert (cleaned["age"] > 100).sum() == 0