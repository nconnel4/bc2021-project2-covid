import requests
import json


def get_json_from_web(url):
    r = requests.get(url)

    return r.json()