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
        UrlManager.load(os.path.realpath(os.path.dirname(__file__)) + '/DeezerApi.json')
        self.__me = self.authenticate(token)
        self.__jukebox = Jukebox(token)
        self.__token = token

    @property
    def jukebox(self):
        return self.__jukebox

    def __tokenize(self, url: str) -> str:
        return UrlManager.add_query_params(url, {
            'access_token': self.__token
        })

    def authenticate(self, token: str) -> User:
        """
        Authenticates the user
        :param token: The access token
        :return: The authenticated User record
        """
        http_conn = http.client.HTTPSConnection(UrlManager.API)
        http_conn.request('GET', UrlManager.Endpoint.user('me', {
            'access_token': token
        })) # TODO 2

        data = json.loads(http_conn.getresponse().read().decode('utf-8')) # TODO 1
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
        http_conn = http.client.HTTPSConnection(UrlManager.API)
        http_conn.request('GET', UrlManager.add_query_params(UrlManager.Endpoint.user_favs('me'), {
            'index': skip,
            'limit': take,
            'access_token': self.__token
        })) # TODO 2

        data = json.loads(http_conn.getresponse().read().decode('utf-8')) # TODO 1

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

