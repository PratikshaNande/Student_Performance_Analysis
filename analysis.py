import pandas as pd


def generate_analysis(df):

    analysis = {}

    # Total students
    analysis["Total Students"] = (
        df["Student_ID"].nunique()
    )

    # Average score
    analysis["Average Score"] = round(
        df["Average_Score"].mean(),
        2
    )

    # Highest score
    analysis["Highest Score"] = round(
        df["Average_Score"].max(),
        2
    )

    # Lowest score
    analysis["Lowest Score"] = round(
        df["Average_Score"].min(),
        2
    )

    # Pass students
    analysis["Pass Students"] = int(
        (df["Result"] == "Pass").sum()
    )

    # Fail students
    analysis["Fail Students"] = int(
        (df["Result"] == "Fail").sum()
    )

    # Pass percentage
    analysis["Pass Percentage"] = round(
        df["Result"].eq("Pass").mean() * 100,
        2
    )

    # Subject average
    subject_columns = [
        "Math_Score",
        "Science_Score",
        "English_Score"
    ]

    subject_average = df[
        subject_columns
    ].mean()

    # Best subject
    analysis["Best Subject"] = (
        subject_average.idxmax()
        .replace("_Score", "")
    )

    # Weakest subject
    analysis["Weakest Subject"] = (
        subject_average.idxmin()
        .replace("_Score", "")
    )

    # City performance
    city_average = (
        df.groupby("City")[
            "Average_Score"
        ]
        .mean()
        .sort_values(
            ascending=False
        )
    )

    analysis["Top City"] = (
        city_average.index[0]
    )

    return analysis


def save_student_insights(
    analysis,
    path
):

    result = pd.DataFrame(
        [analysis]
    )

    result.to_csv(
        path,
        index=False
    )