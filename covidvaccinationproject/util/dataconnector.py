import requests
import json
import logging


class InvalidSiteError(Exception):
    """Exception raised if status code returned is 404"""
    pass


def get_json_from_web(url):
    # instantiate logger
    logger = logging.getLogger(__name__)

    r = requests.get(url)

    if r.status_code == 404:
        raise InvalidSiteError

    return r.json()