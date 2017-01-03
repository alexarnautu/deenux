import http.client
import json
import os

from src.deenuxapi.Provider import Provider
from src.deenuxapi.deezer.UrlManager import UrlManager
from src.deenuxapi.model.Artist import Artist
from src.deenuxapi.model.Track import Track
from src.deenuxapi.model.User import User
from src.deenuxapi.deezer.Jukebox import Jukebox
import time

# TODO 1. remove the hardcoded encoding and use the one in the Content-Type header
# TODO 2. check http exceptions and status code
class DeezerProvider(Provider):
    """
    Provides media streaming and information services
    """

    def __init__(self, token: str):
        """
        Needs an access token, so the sdk can check user's permissions and features
        :param token:
        """
        super().__init__("deezer")
        UrlManager.load(os.path.realpath(os.path.dirname(__file__)) + '/resources/DeezerApi.json')
        self._me = self.get_user_from_token(token)
        self._jukebox = Jukebox(token)
        self._token = token

    @property
    def jukebox(self):
        return self._jukebox

    @staticmethod
    def _request(method: str, url: str) -> dict:
        """
        Performs a synchronously HTTP request to the Web Api
        :param method: HTTP request method
        :param url: The tip of the url
        :return: Returns json parsed response data as a dictionary
        """
        http_conn = http.client.HTTPSConnection(UrlManager.API)
        http_conn.request(method, url)
        return json.loads(http_conn.getresponse().read().decode('utf8')) # TODO 1

    @staticmethod
    def get_user_from_token(token: str) -> User:
        """
        Gets the User of the authentication token
        :param token: The access token
        :return: A User record
        """
        data = DeezerProvider._request('GET', UrlManager.Endpoint.user('me', {
            'access_token': token
        })) # TODO 2

        return User (
            id=data['id'],
            username=data['name'],
            firstname=data['firstname'],
            lastname=data['lastname'],
            email=data['email']
        )

    def get_favourite_tracks(self, skip: int = 0, take: int = 25) -> list:
        """
        Gets a list of user's favourite tracks
        Supports pagination parameters
        :param skip: Pagination param (.NET's LINQ-like, also self-explainatory)
        :param take: Like above
        :return: List of trakcs
        """
        data = self._request('GET', UrlManager.add_query_params(UrlManager.Endpoint.user_favs('me'), {
            'index': skip,
            'limit': take,
            'access_token': self._token
        })) # TODO 2

        return list(map(lambda t: Track (
            id=t['id'],
            title=t['title'],
            artist=Artist (
                id=t['artist']['id'],
                name=t['artist']['name']
            )
        ), data['data']))

    def get_playlists(self):
        pass

    def get_favourite_artists(self):
        pass

