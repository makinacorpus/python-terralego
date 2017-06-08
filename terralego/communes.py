import requests
from requests import RequestException

from terralego.conf import settings

COMMUNES_URL = settings.TERRALEGO_URL.format(api='communes')
COMMUNES_SEARCH_URL = '{communes_url}search/'.format(communes_url=COMMUNES_URL)


def _request_commune(params):
    response = requests.get(
        COMMUNES_SEARCH_URL,
        params=params,
        auth=(settings.USER, settings.PASSWORD)
    )
    try:
        response.raise_for_status()
    except RequestException:
        return None
    return response.json()


def get_communes(insee_code=None, postal_code=None):
    """
    Get a list of towns by insee_code, postal_code or both.

    :param insee_code: The INSEE code of the town.
    :param postal_code: The postal code of the town.
    :return: A dictionnary containing: 'insee_code', 'postal_code', 'name', 'latitude', 'longitude'
    """
    if insee_code is not None and postal_code is not None:
        towns = _request_commune({'insee_code': insee_code, 'postal_code': postal_code})
        if towns is not None:
            return towns
    if insee_code is not None:
        towns = _request_commune({'insee_code': insee_code})
        if towns is not None:
            return towns
    if postal_code is not None:
        towns = _request_commune({'postal_code': postal_code})
        if towns is not None:
            return towns
    return []
