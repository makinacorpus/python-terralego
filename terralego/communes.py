import requests

from terralego.conf import settings

COMMUNES_URL = settings.TERRALEGO_URL.format(api='communes')

COMMUNES_INSEE_URL = '{communes_url}insee/{{insee_code}}/'.format(communes_url=COMMUNES_URL)
COMMUNES_POSTALCODE_URL = '{communes_url}postalcode/{{postal_code}}/'.format(communes_url=COMMUNES_URL)


def get_by_insee_code(insee_code):
    """
    Create a new entry.

    :param insee_code: The INSEE code of the town.
    :return: A dictionnary containing: 'insee_code', 'postal_code', 'name', 'latitude', 'longitude'
    """
    url = COMMUNES_INSEE_URL.format(insee_code=insee_code)
    response = requests.get(url, auth=(settings.USER, settings.PASSWORD))
    response.raise_for_status()
    return response.json()


def get_by_postal_code(postal_code):
    """
    Create a new entry.

    :param postal_code: The postal code of the town.
    :return: A list of dictionnaries containing: 'insee_code', 'postal_code', 'name', 'latitude', 'longitude'
    """
    url = COMMUNES_POSTALCODE_URL.format(postal_code=postal_code)
    response = requests.get(url, auth=(settings.USER, settings.PASSWORD))
    response.raise_for_status()
    return response.json()
