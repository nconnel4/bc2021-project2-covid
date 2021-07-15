import sys

sys.path.append("..")

from covidvaccinationproject.util import dataprocessor
from covidvaccinationproject.util.sqlconnector import Table, SqlConnector


from sqlalchemy import Integer, DateTime, String, Float, Column, PrimaryKeyConstraint


def _create_database():
    sql_connector = SqlConnector('covid.db')

    return sql_connector


def _create_tables(engine):
    country_schema = {
        '__tablename__': 'country',
        '__table_args__': {'extend_existing': True},
        'country_id': Column(String, primary_key=True),
        'continent': Column(String, nullable=True),
        'location': Column(String, nullable=True),
        'population': Column(Integer, nullable=True),
        'population_density': Column(Float),
        'median_age': Column(Float),
        'aged_65_older': Column(Float),
        'aged_70_older': Column(Float),
        'gdp_per_capita': Column(Float),
        'cardivasc_death_rate': Column(Float),
        'diabetes_prvalence': Column(Float),
        'handwashing_facilities': Column(Float),
        'hospital_beds_per_thousand': Column(Float),
        'life_expectancy':Column(Float),
        'human_development_index': Column(Float)
    }

    country = Table('country', engine, country_schema)

    country.drop_table()
    country.create_table()

    covid_data_schema = {
        '__tablename__': 'covid_data',
        '__table_args__': (PrimaryKeyConstraint('country_id', 'date'),
                           {'extend_existing': True}),
        'country_id': Column(String),
        'date': Column(DateTime),
        'total_cases': Column(Integer),
        'new_cases': Column(Integer),
        'total_cases_per_million': Column(Float),
        'new_cases_per_million': Column(Float),
        'stringency_index': Column(Float)
    }

    covid_data = Table('covid_data', engine, covid_data_schema)

    covid_data.drop_table()
    covid_data.create_table()


def _load_database(engine):

    country = Table('country', engine)

    country_data = dataprocessor.extract_country_list()
    country.insert_data(country_data)

    covid = Table('covid_data', engine)
    covid_data = dataprocessor.extract_covid_data()
    covid.insert_data(covid_data)


def build_database():
    conn = _create_database()
    _create_tables(conn.engine)
    _load_database(conn.engine)


build_database()