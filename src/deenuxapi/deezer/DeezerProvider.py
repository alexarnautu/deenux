import http.client
import json
import os

from src.deenuxapi.Provider import Provider
from src.deenuxapi.deezer.Config import Config
from src.deenuxapi.model.Artist import Artist
from src.deenuxapi.model.Track import Track
from src.deenuxapi.model.User import User
from src.deenuxapi.deezer.Jukebox import Jukebox
import time

# TODO 1. remove the hardcoded encoding and use the one in the Content-Type header
# TODO 2. check http exceptions and status code
class DeezerProvider(Provider):

    def __init__(self, token: str):
        super().__init__("deezer")
        Config.load(os.path.realpath(os.path.dirname(__file__)) + '/resources/DeezerApi.json')
        self.__me = self.authenticate(token)
        self.__jukebox = Jukebox(token)
        self.__token = token

    @property
    def jukebox(self):
        return self.__jukebox

    def __tokenize(self, url: str) -> str:
        return Config.add_query_params(url, {
            'access_token': self.__token
        })

    def authenticate(self, token: str) -> User:
        http_conn = http.client.HTTPSConnection(Config.API)
        http_conn.request('GET', Config.user('me', {
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
        http_conn = http.client.HTTPSConnection(Config.API)
        http_conn.request('GET', Config.add_query_params(Config.user_favs('me'), {
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

