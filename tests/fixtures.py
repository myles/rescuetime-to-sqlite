ANALYTIC_DATA_ROW_ONE = [
    "2020-01-12T00:00:00",
    629,
    1,
    "Slack",
    "Communications",
    0,
]

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
    "productivity": CONVERTED_ANALYTIC_DATA_ROW_ONE["Productivity"],
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

DAILY_SUMMARY = {
    "id": 1672473600,
    "date": "2022-12-31",
    "productivity_pulse": 98,
    "very_productive_percentage": 95.6,
    "productive_percentage": 1.5,
    "neutral_percentage": 2.5,
    "distracting_percentage": 0.0,
    "very_distracting_percentage": 0.3,
    "all_productive_percentage": 97.1,
    "all_distracting_percentage": 0.3,
    "uncategorized_percentage": 1.2,
    "business_percentage": 9.6,
    "communication_and_scheduling_percentage": 0.4,
    "social_networking_percentage": 0.3,
    "design_and_composition_percentage": 0.0,
    "entertainment_percentage": 0.0,
    "news_percentage": 0.0,
    "software_development_percentage": 86.1,
    "reference_and_learning_percentage": 1.2,
    "shopping_percentage": 0.0,
    "utilities_percentage": 1.3,
    "total_hours": 2.54,
    "very_productive_hours": 2.43,
    "productive_hours": 0.04,
    "neutral_hours": 0.06,
    "distracting_hours": 0.0,
    "very_distracting_hours": 0.01,
    "all_productive_hours": 2.47,
    "all_distracting_hours": 0.01,
    "uncategorized_hours": 0.03,
    "business_hours": 0.24,
    "communication_and_scheduling_hours": 0.01,
    "social_networking_hours": 0.01,
    "design_and_composition_hours": 0.0,
    "entertainment_hours": 0.0,
    "news_hours": 0.0,
    "software_development_hours": 2.19,
    "reference_and_learning_hours": 0.03,
    "shopping_hours": 0.0,
    "utilities_hours": 0.03,
    "total_duration_formatted": "2h 32m",
    "very_productive_duration_formatted": "2h 25m",
    "productive_duration_formatted": "2m 20s",
    "neutral_duration_formatted": "3m 51s",
    "distracting_duration_formatted": "no time",
    "very_distracting_duration_formatted": "30s",
    "all_productive_duration_formatted": "2h 28m",
    "all_distracting_duration_formatted": "30s",
    "uncategorized_duration_formatted": "1m 46s",
    "business_duration_formatted": "14m 34s",
    "communication_and_scheduling_duration_formatted": "41s",
    "social_networking_duration_formatted": "27s",
    "design_and_composition_duration_formatted": "no time",
    "entertainment_duration_formatted": "3s",
    "news_duration_formatted": "no time",
    "software_development_duration_formatted": "2h 11m",
    "reference_and_learning_duration_formatted": "1m 46s",
    "shopping_duration_formatted": "no time",
    "utilities_duration_formatted": "1m 58s",
}

TRANSFORMED_DAILY_SUMMARY = {
    "id": DAILY_SUMMARY["id"],
    "date": DAILY_SUMMARY["date"],
    "productivity_pulse": DAILY_SUMMARY["productivity_pulse"],
    "total_hours": DAILY_SUMMARY["total_hours"],
    "very_productive_hours": DAILY_SUMMARY["very_productive_hours"],
    "productive_hours": DAILY_SUMMARY["productive_hours"],
    "neutral_hours": DAILY_SUMMARY["neutral_hours"],
    "distracting_hours": DAILY_SUMMARY["distracting_hours"],
    "very_distracting_hours": DAILY_SUMMARY["very_distracting_hours"],
    "all_productive_hours": DAILY_SUMMARY["all_productive_hours"],
    "all_distracting_hours": DAILY_SUMMARY["all_distracting_hours"],
    "uncategorized_hours": DAILY_SUMMARY["uncategorized_hours"],
    "business_hours": DAILY_SUMMARY["business_hours"],
    "communication_and_scheduling_hours": DAILY_SUMMARY[
        "communication_and_scheduling_hours"
    ],
    "social_networking_hours": DAILY_SUMMARY["social_networking_hours"],
    "design_and_composition_hours": DAILY_SUMMARY[
        "design_and_composition_hours"
    ],
    "entertainment_hours": DAILY_SUMMARY["entertainment_hours"],
    "news_hours": DAILY_SUMMARY["news_hours"],
    "software_development_hours": DAILY_SUMMARY["software_development_hours"],
    "reference_and_learning_hours": DAILY_SUMMARY[
        "reference_and_learning_hours"
    ],
    "shopping_hours": DAILY_SUMMARY["shopping_hours"],
    "utilities_hours": DAILY_SUMMARY["utilities_hours"],
}
