from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import logging
from pathlib import Path


class SqlConnector:

    def __init__(self):
        self._logger = logging.getLogger(__name__)

        self.engine = self._connect_engine()

    def _connect_engine(self):
        # get flask root level folder
        root_path = Path(__file__).parent.parent
        db_path = root_path / 'data/covid.db'

        self._logger.info('Connecting to database')
        try:
            engine = create_engine(f'sqlite:///{db_path}')
        except Exception as ex:
            self._logger.error(ex)

        return engine

    def create_table(self, table_schema):
        Base = declarative_base()

        table = type('Table', (Base, ), table_schema)
        table.__table__.create(bind=self.engine)