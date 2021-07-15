import logging

from covidvaccinationproject.util import dataconnector

URL = 'https://covid.ourworldindata.org/data/owid-covid-data.json'
JSON_DATA = dataconnector.get_json_from_web(URL)


def extract_country_list():
    """ Produces a country list and metadata obtained from OWID """
    # instantiate logging
    logger = logging.getLogger(__name__)

    # instantiate country list
    country_list = []
    logger.info('Extracting country metadata')

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


def extract_covid_data():
    """ Produces a list of dictionaries with the covid data from each date recorded by OWID """
    # instantiate logging
    logger = logging.getLogger(__name__)

    covid_data_list = []
    logger.info('Extracting covid data')

    for key, value in JSON_DATA.items():
        covid_data = {
            'country_id': key
        }

        for data_point in value['data']:
            for key, value in data_point.items():
                covid_data[key] = value

            covid_data_list.append(covid_data.copy())

    logger.debug(covid_data_list[0])

    return covid_data_list

