def create_report(
    analysis,
    path
):

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "STUDENT PERFORMANCE ANALYSIS REPORT\n"
        )

        file.write(
            "=" * 45
        )

        file.write("\n\n")

        for key, value in analysis.items():

            file.write(
                f"{key}: {value}\n"
            )