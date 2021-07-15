from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
import logging
import datetime as dt

from covidvaccinationproject.util.sqlconnector import Table, SqlConnector


def get_country_list():
    logger = logging.getLogger(__name__)

    conn = SqlConnector('covid.db')
    country_list= []

    country_table = Table('country', conn.engine)

    Session = sessionmaker(bind=conn.engine)
    session = Session()

    query = session.query(country_table.table.c.country_id, country_table.table.c.location)

    for country in query:
        country_list.append({
            'country_id': country[0],
            'country': country[1]
        })

    logger.debug(country_list)

    session.close()

    return country_list


def get_country_demographics(country_id=None):
    logger = logging.getLogger(__name__)

    conn = SqlConnector('covid.db')
    country_demo_list = []

    country_table = Table('country', conn.engine)

    Sesssion = sessionmaker(bind=conn.engine)
    session = Sesssion()

    if country_id:
        query = session.query(country_table.table).where(country_table.table.c.country_id == country_id)
    else:
        query = session.query(country_table.table)

    for country in query:
        country_demo_list.append({
            'country_id': country[0],
            'continent': country[1],
            'location': country[2],
            'population': country[3],
            'median_age': country[4],
            'aged_65_older': country[5],
            'aged_70_older': country[6],
            'gdp_per_capita': country[7],
            'cardivasc_death_rate': country[8],
            'diabetes_prvalence': country[9],
            'handwashing_facilities': country[10],
            'hospital_beads_per_thousand': country[11],
            'life_expectancy': country[12],
            'human_development_index': country[13]
        })

    logger.debug(country_demo_list)

    session.close()

    return country_demo_list


def get_covid_data(country_id=None, start_date=None, end_date = None):
    logger = logging.getLogger(__name__)

    conn = SqlConnector('covid.db')
    covid_data_list = []

    covid_table = Table('covid_data', conn.engine)

    Sesssion = sessionmaker(bind=conn.engine)
    session = Sesssion()

    query = session.query(covid_table.table)

    if country_id:
        query = query.where(covid_table.table.c.country_id == country_id)
    if start_date:
        query = query.where(covid_table.table.c.date >= start_date)
    if end_date:
        query = query.where(covid_table.table.c.date <= end_date)

    for data_point in query:
        covid_data_list.append({
            'country_id': data_point[0],
            'date': data_point[1]
        })

    logger.debug(covid_data_list)

    session.close()

    return covid_data_list