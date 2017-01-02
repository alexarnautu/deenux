import json
import os

class UrlManager:
    """
    Url operation collection, and API endpoint url generator
    """

    @staticmethod
    def load (settings_path: str):
        """
        Loads and parses the settings from the json file
        :param settings_path: Path of the json settings file
        """
        UrlManager.__settings = json.loads(open(settings_path).read())
        endpoints = UrlManager.__settings['endpoints']

        url_prefix = UrlManager.__settings['hostname'] + ':' + UrlManager.__settings['port']
        UrlManager.API = url_prefix

        for endpoint in endpoints:
            setattr(UrlManager, endpoint.upper(), '/' + endpoints[endpoint])

    @staticmethod
    def _params_to_url(params: dict) -> str:
        """
        Converts a dictionary into key1=value1&key2=value2 url format
        :param params: The dictionary with the {key1:value1,key2:value2} query params
        :return: The url format
        """
        return \
            '&'.join(map(
            lambda x, y: str(x) + '=' + str(y),
            params.keys(), params.values()
            ))

    @staticmethod
    def add_query_params(url: str, params: dict) -> str:
        """
        Adds query params to a string
        This will not handle duplicate keys
        :param url: Base url
        :param params: Params to add
        :return: Modified url, with added params
        """
        if not params:
            return url
        return url + ('&' if '?' in url else '?') + UrlManager._params_to_url(params)

    @staticmethod
    def get_app_setting(setting):
        """
        Get the app settings
        :param setting: setting key
        :return: setting value
        """
        return UrlManager.__settings['app'][setting];

    class Endpoint:
        """
        Endpoint url builder collection
        Each of the following methods return a url (without hostname), with an appended id
        """

        @staticmethod
        def user(user_id: str, query_params: dict = {}) -> str:
            return UrlManager.add_query_params(UrlManager.USER.format(user_id), query_params)
        @staticmethod
        def user_favs(user_id: str, query_params: dict = {}) -> str:
            return UrlManager.add_query_params(UrlManager.USER_FAVS.format(user_id), query_params)
        @staticmethod
        def track(track_id: str, query_params: dict = {}) -> str:
            return UrlManager.add_query_params(UrlManager.TRACK.format(track_id), query_params)

