ANALYTIC_DATA_ROW_ONE = ["2020-01-12T00:00:00", 629, 1, "Slack", "Communications", 0]

CONVERTED_ANALYTIC_DATA_ROW_ONE = {
    "Date": ANALYTIC_DATA_ROW_ONE[0],
    "Time Spent (seconds)": ANALYTIC_DATA_ROW_ONE[1],
    "Number of People": ANALYTIC_DATA_ROW_ONE[2],
    "Activity": ANALYTIC_DATA_ROW_ONE[3],
    "Category": ANALYTIC_DATA_ROW_ONE[4],
    "Productivity": ANALYTIC_DATA_ROW_ONE[5],
}

TRANSFORMED_ANALYTIC_DATA_ROW_ONE = {
    "date": CONVERTED_ANALYTIC_DATA_ROW_ONE["Date"],
    "seconds_spent": CONVERTED_ANALYTIC_DATA_ROW_ONE["Time Spent (seconds)"],
    "number_of_people": CONVERTED_ANALYTIC_DATA_ROW_ONE["Number of People"],
    "activity": CONVERTED_ANALYTIC_DATA_ROW_ONE["Activity"],
    "category": CONVERTED_ANALYTIC_DATA_ROW_ONE["Category"],
    "productivity": CONVERTED_ANALYTIC_DATA_ROW_ONE["Productivity"]
}

ANALYTIC_DATA = {
    "notes": "data is an array of arrays (rows), column names for rows in row_headers",
    "row_headers": [
        "Date",
        "Time Spent (seconds)",
        "Number of People",
        "Activity",
        "Category",
        "Productivity",
    ],
    "rows": [
        ANALYTIC_DATA_ROW_ONE,
    ],
}

CONVERTED_ANALYTIC_DATA_ROWS = [
    CONVERTED_ANALYTIC_DATA_ROW_ONE,
]

TRANSFORMED_ANALYTIC_DATA_ROWS = [
    TRANSFORMED_ANALYTIC_DATA_ROW_ONE,
]
