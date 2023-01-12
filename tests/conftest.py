import pytest
from click.testing import CliRunner
from sqlite_utils.db import Database


@pytest.fixture
def mock_db() -> Database:
    db = Database(memory=True)
    return db


@pytest.fixture
def cli_runner() -> CliRunner:
    runner = CliRunner()
    return runner
