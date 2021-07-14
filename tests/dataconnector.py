import pytest

from covidvaccinationproject.util import dataconnector as dc


def test_connect_web_json():
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.json'
    data = dc.get_json_from_web(url)

    assert data is not None
