import pandas as pd


def clean_data(df):

    df = df.copy()

    # Remove spaces from column names
    df.columns = [
        column.strip()
        for column in df.columns
    ]

    numeric_columns = [
        "Age",
        "Study_Hours",
        "Attendance",
        "Previous_Score",
        "Math_Score",
        "Science_Score",
        "English_Score"
    ]

    # Convert columns into numeric
    for column in numeric_columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove missing values
    df = df.dropna(
        subset=numeric_columns +
        ["Student_ID", "Gender", "City"]
    )

    return df


def save_cleaned_data(df, path):

    df.to_csv(
        path,
        index=False
    )