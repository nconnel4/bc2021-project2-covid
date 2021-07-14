import pytest
import logging
import sqlite3

from covidvaccinationproject.util import sqlconnector as sc

from covidvaccinationproject.util.logger import logconfig
from covidvaccinationproject.util.logger import logconfig

logconfig.setup_logging()
logging.getLogger('covidvacinationproject.util.sqlconnector').setLevel(logging.DEBUG)


def test_connect_db():
    conn = sc.connect_db()

    try:
        conn.cursor()
        connection_success = True
    except Exception:
        connection_success = False

    assert connection_success

