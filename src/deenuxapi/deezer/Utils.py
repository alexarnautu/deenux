import http.client
import json
from src.deenuxapi.deezer.ResourceManager import ResourceManager

class Utils:


    @staticmethod
    def request(method: str, url: str) -> dict:
        """
        Performs a synchronously HTTP request to the Web Api
        :param method: HTTP request method
        :param url: The tip of the url
        :return: Returns json parsed response data as a dictionary
        """
        api_conn = http.client.HTTPSConnection(ResourceManager.API)
        api_conn.request(method, url)
        return json.loads(api_conn.getresponse().read().decode('utf8')) # TODO 1