import pytest

from covidvaccinationproject.util import dataconnector as dc


def test_connect_web_json():
    data = dc.get_data_from_web()

    assert data is not None
