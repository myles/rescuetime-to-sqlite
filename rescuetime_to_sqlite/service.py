import datetime
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from sqlite_utils.db import Database, Table

from . import client


def open_database(db_file_path) -> Database:
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
    Transformer a RescueTime Analytic Data, so it can be safely saved to the
    SQLite database.
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


def save_analytic_data(
    db: Database,
    analytic_data: client.AnalyticData,
):
    """
    Save RescueTime analytic data to the SQLite database.
    """
    build_database(db)
    analytics_table = get_table("analytics", db=db)

    row_headers = analytic_data["row_headers"]
    rows = analytic_data["rows"]
    analytic_data_rows = [
        dict(zip(row_headers, row)) for row in rows
    ]

    for row in analytic_data_rows:
        transform_analytic_data_row(row)

    analytics_table.insert_all(analytic_data_rows, pk="id", alter=True, replace=True)
