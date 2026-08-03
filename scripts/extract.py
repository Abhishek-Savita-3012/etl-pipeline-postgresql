from pathlib import Path
import pandas as pd


def extract_csv(file_path):
    """
    Reads a CSV file and returns a Pandas DataFrame.
    """

    file = Path(file_path)

    # Check if file exists
    if not file.exists():
        raise FileNotFoundError(f"{file_path} does not exist.")

    # Check if file is empty
    if file.stat().st_size == 0:
        raise ValueError("CSV file is empty.")

    # Read CSV
    df = pd.read_csv(file)

    return df


if __name__ == "__main__":

    data = extract_csv("data/raw/customers.csv")

    print("\nData Extracted Successfully!\n")

    print(data.head())