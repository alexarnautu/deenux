import json
import os


class Config:

    @staticmethod
    def load (settings_path):
        Config.__settings = json.loads(open(settings_path).read())
        endpoints = Config.__settings['endpoints']

        url_prefix = Config.__settings['hostname'] + ':' + Config.__settings['port']
        Config.API = url_prefix

        for endpoint in endpoints:
            setattr(Config, endpoint.upper(), '/' + endpoints[endpoint])

    @staticmethod
    def params_to_url(params: dict) -> str:
        return \
            '&'.join(map(
            lambda x, y: str(x) + '=' + str(y),
            params.keys(), params.values()
            ))

    @staticmethod
    def add_query_params(url: str, params: dict):
        if not params:
            return url
        if '?' in url:
            return url + '&' + Config.params_to_url(params)
        else:
            return url + '?' + Config.params_to_url(params)

    @staticmethod
    def user(user_id: str, query_params: dict = {}) -> str:
        return Config.add_query_params(Config.USER.format(user_id), query_params)
    @staticmethod
    def user_favs(user_id: str, query_params: dict = {}) -> str:
        return Config.add_query_params(Config.USER_FAVS.format(user_id), query_params)
    @staticmethod
    def track(track_id: str, query_params: dict = {}) -> str:
        return Config.add_query_params(Config.TRACK.format(track_id), query_params)

    @staticmethod
    def get_app_setting(setting):
        return Config.__settings['app'][setting];


