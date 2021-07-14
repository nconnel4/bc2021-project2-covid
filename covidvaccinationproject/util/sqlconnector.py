from sqlalchemy import create_engine
import logging
from pathlib import Path


def connect_db():
    # instantiate logger
    logger = logging.getLogger(__name__)

    # get flask root level folder
    root_path = Path(__file__).parent.parent
    db_path = root_path / 'data/covid.db'

    logger.info('Connecting to database')
    try:
        engine = create_engine(f'sqlite:///{db_path}')
    except Exception as ex:
        logger.error(ex)

    return engine
