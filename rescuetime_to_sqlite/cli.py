import json
from pathlib import Path

import click

from . import service
from .client import RestrictSourceType


@click.group()
@click.version_option()
def cli():
    """
    Save data from RescueTime to a SQLite database.
    """


@cli.command()
@click.option(
    "-a",
    "--auth",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    default="auth.json",
    help="Path to save tokens to, defaults to auth.json",
)
def auth(auth):
    """
    Save RescueTime authentication credentials to a JSON file.
    """
    auth_file_path = Path(auth).absolute()

    click.echo(
        f"Create a new API key here: https://www.rescuetime.com/anapi/manage"
    )
    click.echo("Paste the API key in the following:")
    click.echo("")

    api_key = click.prompt("Key")

    auth_file_content = json.dumps(
        {"rescuetime_api_key": api_key},
        indent=4,
    )

    with auth_file_path.open("w") as file_obj:
        file_obj.write(auth_file_content + "\n")


@cli.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.option(
    "-a",
    "--auth",
    type=click.Path(
        file_okay=True, dir_okay=False, allow_dash=True, exists=True
    ),
    default="auth.json",
    help="Path to auth.json token file",
)
@click.option("--source-type", type=click.Choice(list(RestrictSourceType)))
def analytic_data(db_path, auth, source_type):
    """
    Save RescueTime analytic data.
    """
    db = service.open_database(db_path)
    client = service.get_client(auth)

    service.save_analytic_data(
        db=db,
        analytic_data=service.get_analytic_data(
            client, source_type=source_type
        ),
    )



@cli.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.option(
    "-a",
    "--auth",
    type=click.Path(
        file_okay=True, dir_okay=False, allow_dash=True, exists=True
    ),
    default="auth.json",
    help="Path to auth.json token file",
)
def daily_summary_feed(db_path, auth):
    """
    Save RescueTime Daily Summary Feed.
    """
    db = service.open_database(db_path)
    client = service.get_client(auth)

    service.save_daily_summary_feed(
        db=db,
        analytic_data=service.get_daily_summary_feed(client),
    )
