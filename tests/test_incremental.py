import pandas as pd

from etl_pipeline.incremental import filter_new_records


def test_incremental_dataframe():

    df = pd.DataFrame(
        {
            "customerid": [1, 2],
            "name": ["A", "B"],
            "age": [20, 25],
            "city": ["X", "Y"],
        }
    )

    assert isinstance(df, pd.DataFrame)