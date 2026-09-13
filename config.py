import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "student_raw.csv"
)

OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "output"
)

ANALYSIS_PATH = os.path.join(
    OUTPUT_PATH,
    "analysis",
    "student_insights.csv"
)

REPORT_PATH = os.path.join(
    OUTPUT_PATH,
    "reports",
    "student_report.txt"
)

GRAPH_PATH = os.path.join(
    OUTPUT_PATH,
    "visualizations"
)