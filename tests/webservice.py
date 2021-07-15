import pytest
import logging
from sqlalchemy import Column, String, Integer, inspect, select

from covidvaccinationproject.util import webservice

from covidvaccinationproject.util.logger import logconfig

logconfig.setup_logging()
logging.getLogger('covidvaccinationproject.util.sqlconnector').setLevel(logging.DEBUG)

def test_country_list():
    country_list = webservice.get_country_list()

    assert country_list[0] == {'country_id': 'AFG', 'country': 'Afghanistan'}

def test_country_metric():
    country_metric_list = webservice.get_country_demographics()

    assert len(country_metric_list) > 1

    country_metric_list_filtered = webservice.get_country_demographics('AFG')

    assert len(country_metric_list_filtered) == 1
    assert country_metric_list[0]['country_id'] == 'AFG'