import responses

from rescuetime_to_sqlite import cli

from . import fixtures


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
