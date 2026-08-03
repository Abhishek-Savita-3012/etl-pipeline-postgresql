from pathlib import Path
import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform customer data.
    """

    print("\nStarting Data Transformation...\n")

    # ----------------------------
    # Standardize column names
    # ----------------------------
    df.columns = df.columns.str.strip().str.lower()

    # ----------------------------
    # Remove duplicate rows
    # ----------------------------
    duplicates_removed = df.duplicated().sum()
    df = df.drop_duplicates()

    # ----------------------------
    # Handle missing values
    # ----------------------------

    # Drop rows where Name is missing
    missing_names = df["name"].isnull().sum()
    df = df.dropna(subset=["name"])

    # Fill missing Age with median
    df["age"] = df["age"].fillna(df["age"].median())

    # Fill missing City with "Unknown"
    df["city"] = df["city"].fillna("Unknown")

    # ----------------------------
    # Standardize names
    # ----------------------------
    df["name"] = df["name"].str.title()

    # ----------------------------
    # Remove invalid ages
    # ----------------------------
    invalid_age = (df["age"] > 100).sum()

    df = df[df["age"] <= 100]

    # ----------------------------
    # Convert Age to integer
    # ----------------------------
    df["age"] = df["age"].astype(int)

    print(f"Duplicates Removed : {duplicates_removed}")
    print(f"Missing Names      : {missing_names}")
    print(f"Invalid Ages       : {invalid_age}")

    print("\nTransformation Completed Successfully!\n")

    return df


if __name__ == "__main__":

    input_file = Path("data/raw/customers.csv")

    df = pd.read_csv(input_file)

    cleaned_df = transform_data(df)

    output_file = Path("data/processed/customers_clean.csv")

    cleaned_df.to_csv(output_file, index=False)

    print(cleaned_df)

    print(f"\nCleaned data saved to:\n{output_file}")