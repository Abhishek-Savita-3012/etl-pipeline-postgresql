import pandas as pd

from etl_pipeline.extract import extract_csv
from etl_pipeline.settings import RAW_CUSTOMERS_FILE


def test_extract_csv_returns_dataframe():

    df = extract_csv(RAW_CUSTOMERS_FILE)

    assert isinstance(df, pd.DataFrame)


def test_extract_csv_not_empty():

    df = extract_csv(RAW_CUSTOMERS_FILE)

    assert not df.empty


def test_extract_has_expected_columns():

    df = extract_csv(RAW_CUSTOMERS_FILE)

    expected = [
        "CustomerID",
        "Name",
        "Age",
        "City",
    ]

    assert list(df.columns) == expected