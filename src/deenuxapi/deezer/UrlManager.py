import json
import os

class UrlManager:

    @staticmethod
    def load (settings_path):
        UrlManager.__settings = json.loads(open(settings_path).read())
        endpoints = UrlManager.__settings['endpoints']

        url_prefix = UrlManager.__settings['hostname'] + ':' + UrlManager.__settings['port']
        UrlManager.API = url_prefix

        for endpoint in endpoints:
            setattr(UrlManager, endpoint.upper(), '/' + endpoints[endpoint])

    @staticmethod
    def _params_to_url(params: dict) -> str:
        return \
            '&'.join(map(
            lambda x, y: str(x) + '=' + str(y),
            params.keys(), params.values()
            ))

    @staticmethod
    def add_query_params(url: str, params: dict):
        if not params:
            return url
        return url + ('&' if '?' in url else '?') + UrlManager._params_to_url(params)

    @staticmethod
    def get_app_setting(setting):
        return UrlManager.__settings['app'][setting];

    class Endpoint:
        @staticmethod
        def user(user_id: str, query_params: dict = {}) -> str:
            return UrlManager.add_query_params(UrlManager.USER.format(user_id), query_params)
        @staticmethod
        def user_favs(user_id: str, query_params: dict = {}) -> str:
            return UrlManager.add_query_params(UrlManager.USER_FAVS.format(user_id), query_params)
        @staticmethod
        def track(track_id: str, query_params: dict = {}) -> str:
            return UrlManager.add_query_params(UrlManager.TRACK.format(track_id), query_params)

