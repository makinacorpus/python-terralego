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


def closest(entry_id, tags=None):
    """
    Get the closest entry.

    :param entry_id: The id of the entry on which to get the closest one.
    :param tags: Optional, a list of tags to filter the entry which can be the closests.
    :return: A geojson describing the entry as a python dictionnary. Raise 404 if no entry are found.
    """
    url = GEODIRECTORY_ENTRY_DETAIL_URL.format(entry_id=entry_id) + 'closest/'
    params = {}
    if tags is not None:
        params['tags'] = tags
    response = requests.get(url, auth=(settings.USER, settings.PASSWORD), params=params)
    response.raise_for_status()
    return response.json()


def closest_from(lat, long, tags=None, dist=None):
    """
    Get the closest entry from the point.

    :param lat: The latitude of the point.
    :param long: The longitude of the point.
    :param tags: Optional, a list of tags to filter the entry which can be the closests.
    :param dist: Optional, a distance in meters.
    :return: A geojson describing the entry as a python dictionnary. Raise 404 if no entry are found.
    """
    url = GEODIRECTORY_ENTRY_LIST_URL + 'closest_from/'
    params = {
        'point': '{lon},{lat}'.format(lat=float(lat), lon=float(long))
    }
    if tags is not None:
        params['tags'] = tags
    if dist is not None:
        params['dist'] = dist
    response = requests.get(url, auth=(settings.USER, settings.PASSWORD), params=params)
    response.raise_for_status()
    return response.json()

# TODO get_entries_list (with filters for tag/distance/contains)
