import json
import requests

from terralego.conf import settings

GEOCODING_URL = settings.TERRALEGO_URL.format(api='geocoding')
GEOCODING_SEARCH = '{geodirectory_url}search'.format(geodirectory_url=GEOCODING_URL)
GEOCODING_REVERSE = '{geodirectory_url}reverse'.format(geodirectory_url=GEOCODING_URL)
GEOCODING_AUTOCOMPLETE = '{geodirectory_url}autocomplete'.format(geodirectory_url=GEOCODING_URL)


def search(text, params=None):
    """
    Search locations from a string.

    :param text: The string which will be used to do the search.
    :param params: A dict including other get parameters.
    :return: A geojson including the results.
    """
    if params is None:
        params = {}
    params['text'] = text
    response = requests.get(GEOCODING_SEARCH, params=params, auth=(settings.USER, settings.PASSWORD))
    response.raise_for_status()
    return response.json()


def reverse(lat, long, params=None):
    """
    Search addresses from a location.

    :param lat: The latitude of the location.
    :param long: The longitude of the location.
    :param params: A dict including other get parameters.
    :return: A geojson including the results.
    """
    if params is None:
        params = {}
    params['lat'] = lat
    params['long'] = long
    response = requests.get(GEOCODING_REVERSE, params=params, auth=(settings.USER, settings.PASSWORD))
    response.raise_for_status()
    return response.json()


def autocomplete(text, params=None):
    """
    Autocomplete locations from a string.

    :param text: The string which will be used to do the autocomplete.
    :param params: A dict including other get parameters.
    :return: A geojson including the results.
    """
    if params is None:
        params = {}
    params['text'] = text
    response = requests.get(GEOCODING_AUTOCOMPLETE, params=params, auth=(settings.USER, settings.PASSWORD))
    response.raise_for_status()
    return response.json()
