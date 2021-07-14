import pytest
import logging
import sqlite3

from covidvaccinationproject.util import sqlconnector as sc

from covidvaccinationproject.util.logger import logconfig

logconfig.setup_logging()
logging.getLogger('covidvaccinationproject.util.sqlconnector').setLevel(logging.DEBUG)


def test_connect_db():
    try:
        conn = sc.connect_db()
        conn.connect()
        connection_success = True
    except Exception:
        connection_success = False

    assert connection_success

