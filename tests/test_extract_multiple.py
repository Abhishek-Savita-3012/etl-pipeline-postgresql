from pathlib import Path

import pandas as pd

from etl_pipeline.extract import extract_csv


def test_extract_folder():

    folder = Path("data/raw")

    df = extract_csv(folder)

    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0