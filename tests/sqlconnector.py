import pytest
import logging
from sqlalchemy import Column, String, Integer, inspect

from covidvaccinationproject.util.sqlconnector import SqlConnector

from covidvaccinationproject.util.logger import logconfig

logconfig.setup_logging()
logging.getLogger('covidvaccinationproject.util.sqlconnector').setLevel(logging.DEBUG)


@pytest.fixture
def connector():
    return SqlConnector()


def test_connect_db():
    connector = SqlConnector()

    try:
        conn = connector._connect_engine()
        conn.connect()
        connection_success = True
    except Exception:
        connection_success = False

    assert connection_success


def test_create_table(connector):
    table_schema = {'__tablename__': 'test_table',
                    'test_col_1': Column(Integer, primary_key=True),
                    'test_col_2': Column(String)}

    connector.create_table(table_schema)

    assert inspect(connector.engine).has_table('test_table')


