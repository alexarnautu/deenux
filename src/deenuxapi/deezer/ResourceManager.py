import json
import os
from urllib.parse import urlencode

class ResourceManager:
    """
    Url operation collection, and API endpoint url generator
    """

    @staticmethod
    def load ():
        """
        Loads and parses the settings from the json file
        :param settings_path: Path of the json settings file
        """
        ResourceManager.__settings = json.loads(
            open(os.path.realpath(os.path.dirname(__file__)) + '/resources/DeezerApi.json').read()
        )
        ResourceManager.__endpoint_tpl = ResourceManager.__settings['endpoints']

        url_prefix = ResourceManager.__settings['hostname'] + ':' + ResourceManager.__settings['port']
        ResourceManager.API = url_prefix

    @staticmethod
    def get_app_setting(setting):
        """
        Get the app settings
        :param setting: setting key
        :return: setting value
        """
        return ResourceManager.__settings['app'][setting];

    @staticmethod
    def get_endpoint(name: str, ids: any, params: dict = None):
        """
        Gets endpoint url tip.
        :param name: Name of the endpoint, specified in the resource
        :param ids: An id or an array representing the required ids for the string formatting
        :param params: Additional query params, as a dictionary
        :return: The built url tip
        """
        if type(ids) is list:
            url = ResourceManager.__endpoint_tpl[name].format(*ids)
        else:
            url = ResourceManager.__endpoint_tpl[name].format(ids)
        if params:
            url += ('&' if '?' in url else '?') + urlencode(params)
        return '/' + url

ResourceManager.load()
