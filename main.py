import os

from src.config import (
    OUTPUT_PATH,
    ANALYSIS_PATH,
    REPORT_PATH,
    GRAPH_PATH
)

from src.data_loader import load_data

from src.data_cleaning import (
    clean_data,
    save_cleaned_data
)

from src.data_transformation import (
    transform_data
)

from src.analysis import (
    generate_analysis,
    save_student_insights
)

from src.visualization import (
    create_visualization
)

from src.report import (
    create_report
)


def main():

    print("Loading student data...")

    df = load_data()


    print("Cleaning data...")

    df = clean_data(df)

    save_cleaned_data(
        df,
        os.path.join(
            OUTPUT_PATH,
            "cleaned_student_data.csv"
        )
    )


    print("Transforming data...")

    df = transform_data(df)


    print("Generating analysis...")

    analysis = generate_analysis(df)


    print("Saving student insights...")

    os.makedirs(
        os.path.dirname(
            ANALYSIS_PATH
        ),
        exist_ok=True
    )

    save_student_insights(
        analysis,
        ANALYSIS_PATH
    )


    print("Creating visualizations...")

    create_visualization(
        df,
        GRAPH_PATH
    )


    print("Creating report...")

    os.makedirs(
        os.path.dirname(
            REPORT_PATH
        ),
        exist_ok=True
    )

    create_report(
        analysis,
        REPORT_PATH
    )


    print(
        "\nProject completed successfully!"
    )

    print(
        "Total Students:",
        analysis["Total Students"]
    )

    print(
        "Average Score:",
        analysis["Average Score"]
    )

    print(
        "Pass Percentage:",
        analysis["Pass Percentage"]
    )

    print(
        "Best Subject:",
        analysis["Best Subject"]
    )

    print(
        "Top City:",
        analysis["Top City"]
    )


if __name__ == "__main__":
    main()