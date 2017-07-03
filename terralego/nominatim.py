import requests

from terralego.conf import settings

NOMINATIM_URL = settings.TERRALEGO_URL.format(api='nominatim')


def search(**kwargs):
    """
    Search nominatim. Either pass q for generic search or country/postalcode/...

    :return: A list of dict containing the responses.
    """
    response = requests.get(NOMINATIM_URL, params=kwargs, auth=(settings.USER, settings.PASSWORD))
    response.raise_for_status()
    return response.json()
