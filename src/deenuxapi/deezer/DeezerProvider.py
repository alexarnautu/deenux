import http.client
import json
import os

from src.deenuxapi.Provider import Provider
from src.deenuxapi.deezer.ResourceManager import ResourceManager
from src.deenuxapi.model.Artist import Artist
from src.deenuxapi.model.Track import Track
from src.deenuxapi.model.User import User
from src.deenuxapi.deezer.Jukebox import Jukebox
from urllib.parse import quote
import time


# TODO 1. remove the hardcoded encoding and use the one in the Content-Type header
# TODO 2. check http exceptions and status code
class DeezerProvider(Provider):
    """
    Provides media streaming and information services
    """

    _api_conn = http.client.HTTPSConnection(ResourceManager.API)

    def __init__(self, token: str):
        """
        Needs an access token, so the sdk can check user's permissions and features
        :param token:
        """
        super().__init__("deezer")

        self._jukebox = Jukebox(token)
        self._me = self.get_user_from_token(token)
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
        DeezerProvider._api_conn.request(method, url)
        return json.loads(DeezerProvider._api_conn.getresponse().read().decode('utf8')) # TODO 1

    @staticmethod
    def get_user_from_token(token: str) -> User:
        """
        Gets the User of the authentication token
        :param token: The access token
        :return: A User record
        """
        data = DeezerProvider._request('GET', ResourceManager.get_endpoint('user', 'me', {
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
        data = DeezerProvider._request('GET', ResourceManager.get_endpoint('user_favs', 'me', {
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

    @staticmethod
    def authorize() -> str:
        """
        Authorises the user using OAuth and retrieves the authentication token
        :return: The access token
        """
        import webbrowser
        from src.deenuxapi.deezer.oauth.OAuthHttpServer import OAuthHttpServer, OAuthRequestHandler

        server_address = ('', 0) # Binding to port 0, so the OS can allocate a free random port for us
        httpd = OAuthHttpServer(server_address, OAuthRequestHandler)

        oauth_url = ResourceManager.get_app_setting("oauth_url").format(
            ResourceManager.get_app_setting('id'),  # The application Id
            quote("http://localhost:{0}".format(httpd.server_port), safe=''), # Redirection URL (to our dear local server, of course)
            ','.join(ResourceManager.get_app_setting('perms'))  # Permissions
        )
        webbrowser.open(oauth_url)
        code = httpd.serve_until_authorized()

        data = DeezerProvider._request("GET", ResourceManager.get_app_setting('token_url').format(
            ResourceManager.get_app_setting('id'),
            ResourceManager.get_app_setting('secret_key'), # !!! HIGHLY MALICIOUS
            code
        ))

        return data['access_token']

    def get_playlists(self):
        pass

    def get_favourite_artists(self):
        pass

