import json
import requests

from terralego.conf import settings

GEODIRECTORY_URL = settings.TERRALEGO_URL.format(api='geodirectory')
GEODIRECTORY_ENTRY_LIST_URL = '{geodirectory_url}entries/'.format(geodirectory_url=GEODIRECTORY_URL)
GEODIRECTORY_ENTRY_DETAIL_URL = '{geodirectory_url}entries/{{entry_id}}/'.format(geodirectory_url=GEODIRECTORY_URL)


def create_entry(geometry, tags=None):
    """
    Create a new entry.

    :param geometry: A WKT string representing the geometry of the entry or a dict representing the geojson.
    :param tags: A list of string describing the entry. Can be used for filtering later on.
    :return: A geojson describing the entry as a python dictionnary.
    """
    if tags is None:
        tags = []
    if isinstance(geometry, dict):
        geometry = json.dumps(geometry)
    data = {
        'geometry': geometry,
        'tags': json.dumps(tags),
    }
    response = requests.post(GEODIRECTORY_ENTRY_LIST_URL, data=data, auth=(settings.USER, settings.PASSWORD))
    response.raise_for_status()
    return response.json()


def get_entry(entry_id):
    """
    Get an entry.

    :param entry_id: The id of the entry.
    :return: A geojson describing the entry as a python dictionnary.
    """
    url = GEODIRECTORY_ENTRY_DETAIL_URL.format(entry_id=entry_id)
    response = requests.get(url, auth=(settings.USER, settings.PASSWORD))
    response.raise_for_status()
    return response.json()


def update_entry(entry_id, geometry, tags=None):
    """
    Update an entry.

    :param entry_id: The id of the entry.
    :param geometry: A WKT string representing the geometry of the entry or a dict representing the geojson.
    :param tags: A list of string describing the entry. Can be used for filtering later on.
    :return: A geojson describing the updated entry as a python dictionnary.
    """
    if tags is None:
        tags = []
    if isinstance(geometry, dict):
        geometry = json.dumps(geometry)
    data = {
        'geometry': geometry,
        'tags': json.dumps(tags),
    }
    url = GEODIRECTORY_ENTRY_DETAIL_URL.format(entry_id=entry_id)
    response = requests.put(url, data=data, auth=(settings.USER, settings.PASSWORD))
    response.raise_for_status()
    return response.json()


def delete_entry(entry_id):
    """
    Delete an entry.

    :param entry_id: The id of the entry.
    """
    url = GEODIRECTORY_ENTRY_DETAIL_URL.format(entry_id=entry_id)
    response = requests.delete(url, auth=(settings.USER, settings.PASSWORD))
    response.raise_for_status()


# TODO get_entries_list (with filters for tag/distance/contains)
