import datetime
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from sqlite_utils.db import Database, Table

from . import client


def open_database(db_file_path: str) -> Database:
    """
    Open the RescueTime SQLite database.
    """
    return Database(db_file_path)


def get_table(table_name: str, *, db: Database) -> Table:
    """
    Returns a Table from a given db Database object.
    """
    return Table(db=db, name=table_name)


def build_database(db: Database):
    """
    Build the RescueTime SQLite database structure.
    """
    analytics_table = get_table("analytics", db=db)
    daily_summary_table = get_table("daily_summary", db=db)

    if analytics_table.exists() is False:
        analytics_table.create(
            columns={
                "id": int,
                "date": str,
                "seconds_spent": int,
                "number_of_people": int,
                "activity": str,
                "category": str,
                "productivity": int,
            },
            pk="id",
        )
        analytics_table.enable_fts(
            ["activity", "category"], create_triggers=True
        )

    if daily_summary_table.exists() is False:
        daily_summary_table.create(
            columns={
                "id": int,
                "date": str,
                "productivity_pulse": float,
                "total_hours": float,
                "very_productive_hours": float,
                "productive_hours": float,
                "neutral_hours": float,
                "distracting_hours": float,
                "very_distracting_hours": float,
                "all_productive_hours": float,
                "all_distracting_hours": float,
                "uncategorized_hours": float,
                "business_hours": float,
                "communication_and_scheduling_hours": float,
                "social_networking_hours": float,
                "design_and_composition_hours": float,
                "entertainment_hours": float,
                "news_hours": float,
                "software_development_hours": float,
                "reference_and_learning_hours": float,
                "shopping_hours": float,
                "utilities_hours": float,
            }
        )


def get_client(auth_file_path: str) -> client.RescueTimeClient:
    """
    Returns a fully authenticated RescueTimeClient.
    """
    with Path(auth_file_path).absolute().open() as file_obj:
        raw_auth = file_obj.read()

    auth = json.loads(raw_auth)

    return client.RescueTimeClient(key=auth["rescuetime_api_key"])


def get_analytic_data(
    rt_client: client.RescueTimeClient,
    source_type: Optional[client.RestrictSourceType] = None,
) -> client.AnalyticData:
    """
    Get authenticated user's analytic data.
    """
    _request, response = rt_client.get_analytic_data(
        perspective=client.Perspective.INTERVAL,
        resolution_time=client.ResolutionTime.DAY,
        restrict_source_type=source_type,
    )
    response.raise_for_status()
    return response.json()


def transform_analytic_data_row(
    row: Dict[str, Union[str, int]],
):
    """
    Transformer a RescueTime Analytic Data row, so it can be safely saved to
    the SQLite database.
    """
    row["date"] = row.pop("Date")
    row["seconds_spent"] = row.pop("Time Spent (seconds)")
    row["number_of_people"] = row.pop("Number of People")
    row["activity"] = row.pop("Activity")
    row["category"] = row.pop("Category")
    row["productivity"] = row.pop("Productivity")

    to_remove = [
        k
        for k in row.keys()
        if k
        not in (
            "date",
            "seconds_spent",
            "number_of_people",
            "activity",
            "category",
            "productivity",
        )
    ]
    for key in to_remove:
        del row[key]


def convert_analytic_data_to_rows(
    analytic_data: client.AnalyticData,
) -> List[Dict[str, Union[str, int]]]:
    """
    Transformer a RescueTime Analytic Data response, so it can be easily
    transformed and saved to the SQLite database.
    """
    row_headers = analytic_data["row_headers"]
    rows = analytic_data["rows"]
    return [dict(zip(row_headers, row)) for row in rows]


def save_analytic_data(
    db: Database,
    analytic_data: client.AnalyticData,
):
    """
    Save RescueTime analytic data to the SQLite database.
    """
    build_database(db)
    analytics_table = get_table("analytics", db=db)

    analytic_data_rows = convert_analytic_data_to_rows(analytic_data)

    for row in analytic_data_rows:
        transform_analytic_data_row(row)

    analytics_table.insert_all(
        analytic_data_rows, pk="id", alter=True, replace=True
    )


def get_daily_summary_feed(
    rt_client: client.RescueTimeClient,
) -> List[Dict[str, Union[str, float, int]]]:
    """
    Get authenticated user's daily summary feed.
    """
    _request, response = rt_client.get_daily_summary_feed()
    response.raise_for_status()
    return response.json()


def transform_daily_summary_item(
    item: Dict[str, Union[str, float, int]],
):
    """
    Transformer a RescueTime Daily Summary Feed item, so it can be safely saved
    to the SQLite database.
    """
    to_remove = [
        k
        for k in item.keys()
        if k
        not in (
            "id",
            "date",
            "productivity_pulse",
            "total_hours",
            "very_productive_hours",
            "productive_hours",
            "neutral_hours",
            "distracting_hours",
            "very_distracting_hours",
            "all_productive_hours",
            "all_distracting_hours",
            "uncategorized_hours",
            "business_hours",
            "communication_and_scheduling_hours",
            "social_networking_hours",
            "design_and_composition_hours",
            "entertainment_hours",
            "news_hours",
            "software_development_hours",
            "reference_and_learning_hours",
            "shopping_hours",
            "utilities_hours",
        )
    ]
    for key in to_remove:
        del item[key]


def save_daily_summary_feed(
    db: Database,
    daily_summary: List[Dict[str, Union[str, float, int]]],
):
    """
    Save RescueTime daily summary feed to the SQLite database.
    """
    build_database(db)
    daily_summary_table = get_table("daily_summary", db=db)

    for item in daily_summary:
        transform_daily_summary_item(item)

    daily_summary_table.insert_all(
        daily_summary, pk="id", alter=True, replace=True
    )
