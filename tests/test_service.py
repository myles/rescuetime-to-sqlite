from rescuetime_to_sqlite import service

from . import fixtures


def test_transform_analytic_data_row():
    row = fixtures.CONVERTED_ANALYTIC_DATA_ROW_ONE.copy()
    transformed_row = fixtures.TRANSFORMED_ANALYTIC_DATA_ROW_ONE.copy()

    service.transform_analytic_data_row(row)
    assert row == transformed_row


def test_convert_analytic_data_to_rows():
    analytic_data = fixtures.ANALYTIC_DATA.copy()
    expected_rows = fixtures.CONVERTED_ANALYTIC_DATA_ROWS.copy()

    rows = service.convert_analytic_data_to_rows(analytic_data)
    assert rows == expected_rows


def test_transform_daily_summary_item():
    daily_summary = fixtures.DAILY_SUMMARY.copy()
    expected_result = fixtures.TRANSFORMED_DAILY_SUMMARY.copy()

    service.transform_daily_summary_item(daily_summary)
    assert daily_summary == expected_result
