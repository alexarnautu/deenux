import http.client
import requests
import json
from src.deenuxapi.deezer.ResourceManager import ResourceManager
from collections import defaultdict

class Request:
    session_token = None

    @staticmethod
    def get(url: str, params: dict = {}) -> dict:
        """
        Perform a POST request to Web API
        :param url: The url
        :param params: Query strings
        :return: JSON response data as a dictionary
        """
        if Request.session_token is not None:
            params['access_token'] = Request.session_token

        response = requests.get(url, params=params)
        decoded_content = response.content.decode()

        return defaultdict(lambda: None, json.loads(decoded_content))

    @staticmethod
    def post(url: str, params: dict = {}, payload: dict = {}) -> dict:
        """
        Performs a POST request to Web API
        :param url: The URL
        :param params: Request query string
        :param payload: Request payload
        :return: JSON response data as a dictionary
        """
        params['access_token'] = Request.session_token

        response = requests.post(url, params=params, data=payload)
        decoded_content = response.content.decode()

        return json.loads(decoded_content)


    @staticmethod
    def request(method: int, url: str, params: str,) -> dict:
        """
        Performs a synchronously HTTP request to the Web Api
        :param method: HTTP request method
        :param url: The tip of the url
        :param host: The host URL
        :return: Returns json parsed response data as a dictionary
        """
        if method == HTTP_METHOD.GET:
            response = requests.get(url)

            return json.loads(response.decode())
        response = requests
        return json.loads(api_conn.getresponse().read().decode('utf8')) # TODO 1
