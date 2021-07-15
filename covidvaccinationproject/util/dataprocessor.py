import logging

from covidvaccinationproject.util import dataconnector

URL = 'https://covid.ourworldindata.org/data/owid-covid-data.json'
JSON_DATA = dataconnector.get_json_from_web(URL)


def extract_country_list():
    # instantiate logging
    logger = logging.getLogger(__name__)

    # instantiate country list
    country_list = []

    for key, value in JSON_DATA.items():
        country_info = {
            'country_id': key
        }

        # append inner dictionary to id
        for key, value in value.items():
            if not key == 'data':
                country_info[key] = value

        country_list.append(country_info)

    return country_list
