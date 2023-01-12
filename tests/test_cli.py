import json

import responses

from rescuetime_to_sqlite import cli

from . import fixtures


def test_auth(cli_runner, tmp_path):
    auth_json_path = tmp_path / "auth.json"
    rescuetime_api_key = "IAmARescueTimeAPIKey"

    cli_runner.invoke(cli.auth, f"--auth={auth_json_path}", rescuetime_api_key)

    with auth_json_path.open() as file_obj:
        auth = json.loads(file_obj.read())

    assert auth["rescuetime_api_key"] == rescuetime_api_key


@responses.activate
def test_analytic_data(mocker, mock_db, cli_runner):
    mocker.patch(
        "rescuetime_to_sqlite.cli.service.open_database",
        return_value=mock_db,
    )

    responses.add(
        responses.Response(
            method="GET",
            url="https://www.rescuetime.com/anapi/data",
            json=fixtures.ANALYTIC_DATA,
        )
    )

    cli_runner.invoke(
        cli.analytic_data,
        [
            "rescuetime.db",
            "--auth=tests/fixture-auth.json",
        ],
    )

    assert mock_db["analytics"].count == 1


@responses.activate
def test_daily_summary_feed(mocker, mock_db, cli_runner):
    mocker.patch(
        "rescuetime_to_sqlite.cli.service.open_database",
        return_value=mock_db,
    )

    responses.add(
        responses.Response(
            method="GET",
            url="https://www.rescuetime.com/anapi/daily_summary_feed",
            json=[fixtures.DAILY_SUMMARY],
        )
    )

    cli_runner.invoke(
        cli.daily_summary_feed,
        [
            "rescuetime.db",
            "--auth=tests/fixture-auth.json",
        ],
    )

    assert mock_db["daily_summary"].count == 1
