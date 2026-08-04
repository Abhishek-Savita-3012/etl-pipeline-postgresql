import pandas as pd
import pytest

from etl_pipeline.validation import validate_dataframe


def test_validation_passes():

    df = pd.DataFrame(
        {
            "CustomerID": [1],
            "Name": ["Abhishek"],
            "Age": [22],
            "City": ["Kanpur"],
        }
    )

    assert validate_dataframe(df)


def test_missing_column():

    df = pd.DataFrame(
        {
            "CustomerID": [1],
            "Name": ["Abhishek"],
            "Age": [22],
        }
    )

    with pytest.raises(ValueError):

        validate_dataframe(df)