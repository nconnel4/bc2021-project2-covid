import pytest
import logging

from covidvaccinationproject.util.logger import logconfig
logconfig.setup_logging()
logging.getLogger('covidvaccinationproject.util.dataprocessor').setLevel(logging.DEBUG)