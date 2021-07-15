import pytest
import logging

from covidvaccinationproject.util import dataprocessor as dp

from covidvaccinationproject.util.logger import logconfig
logconfig.setup_logging()
logging.getLogger('covidvaccinationproject.util.dataprocessor').setLevel(logging.DEBUG)

def test_country_list():
    country_list = dp.extract_country_list()

    assert country_list[0]['country_id'] == 'AFG'
    assert country_list[2]['location'] == 'Albania'
    assert len(country_list) == 218