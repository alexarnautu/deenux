import json
import os
from typing import Union

class ResourceManager:
    """
    Url operation collection, and API endpoint url generator
    """

    @staticmethod
    def load (settings_path: str):
        """
        Loads and parses the settings from the json file
        :param settings_path: Path of the json settings file
        """
        ResourceManager.__settings = json.loads(open(settings_path).read())
        ResourceManager.__endpoint_tpl = ResourceManager.__settings['endpoints']

        url_prefix = ResourceManager.__settings['hostname'] + ':' + ResourceManager.__settings['port']
        ResourceManager.API = url_prefix

    @staticmethod
    def add_query_params(url: str, params: dict) -> str:
        """
        Adds query params to a url
        This will not handle duplicate keys
        :param url: Base url
        :param params: Params to add. If this is an empty dict or None, the function will return the url
        :return: Modified url, with added params
        """
        if not params:
            return url
        return url + ('&' if '?' in url else '?') + \
            '&'.join(map(
                lambda x: str(x) + '=' + str(params[x]),
                params.keys()
            ))

    @staticmethod
    def get_app_setting(setting):
        """
        Get the app settings
        :param setting: setting key
        :return: setting value
        """
        return ResourceManager.__settings['app'][setting];

    @staticmethod
    def get_endpoint(name: str, ids: any, params: dict):
        if type(ids) is list:
            url = ResourceManager.__endpoint_tpl[name].format(*ids)
        else:
            url = ResourceManager.__endpoint_tpl[name].format(ids)
        return '/' + ResourceManager.add_query_params(url, params)

