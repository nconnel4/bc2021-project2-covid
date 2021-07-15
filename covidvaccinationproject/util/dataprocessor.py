import logging
import datetime as dt

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
            'country_id': key,
            'continent': value.get('continent'),
            'location': value.get('location'),
            'population': value.get('population'),
            'population_density': value.get('population_density'),
            'median_age': value.get('median_age'),
            'aged_65_older': value.get('aged_65_older'),
            'aged_70_older': value.get('aged_70_older'),
            'gdp_per_capita': value.get('gdp_per_capita'),
            'cardiovasc_death_rate': value.get('cardiovasc_death_rate'),
            'diabetes_prevalence': value.get('diabetes_prevalence'),
            'handwashing_facilities': value.get('handwashing_facilities'),
            'hospital_beds_per_thousand': value.get('hospital_beds_per_thousand'),
            'life_expectancy': value.get('life_expectancy'),
            'human_development_index': value.get('human_development_index')
        }
        country_list.append(country_info.copy())

    return country_list


def extract_covid_data():
    """ Produces a list of dictionaries with the covid data from each date recorded by OWID """
    # instantiate logging
    logger = logging.getLogger(__name__)

    covid_data_list = []
    logger.info('Extracting covid data')

    for key, value in JSON_DATA.items():

        for data_point in value['data']:
            covid_data = {
                'country_id': key,
                'date': dt.datetime.strptime(data_point.get('date'), '%Y-%m-%d'),
                'total_cases': data_point.get('total_cases'),
                'new_cases': data_point.get('new_cases'),
                'total_cases_per_million': data_point.get('total_cases_per_million'),
                'new_cases_per_million': data_point.get('new_cases_per_million'),
                'stringency_index': data_point.get('stringency_index')
            }

            covid_data_list.append(covid_data.copy())

    logger.debug(covid_data_list[0])

    return covid_data_list

