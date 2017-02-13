from urllib.parse import quote
import re

from src.deenuxapi.deezer.Request import Request
from src.deenuxapi.deezer.model.User import User

from src.deenuxapi.deezer.model.Track import Track
from src.deenuxapi.deezer.model.Artist import Artist

from src.deenuxapi.deezer.Jukebox import Jukebox
from src.deenuxapi.deezer.Provider import Provider
from src.deenuxapi.deezer.ResourceManager import ResourceManager


# TODO 1. remove the hardcoded encoding and use the one in the Content-Type header
# TODO 2. check http exceptions and status code
class DeezerProvider(Provider):
    """
    Provides media streaming and information services
    """

    def __init__(self, token: str = None):
        """
        Needs an access token, so the sdk can check user's permissions and features
        :param token:
        """
        super().__init__("deezer")

        self.token = token

    @property
    def token(self):
        return self._token

    @property
    def jukebox(self):
        return self._jukebox

    @property
    def me(self):
        return self._me

    @token.setter
    def token(self, token):
        if token is not None:
            self._jukebox = Jukebox(token)
            self._me = User.get_from_token(token)
            self._token = token
        else:
            self._token = None

    @staticmethod
    def authorize() -> str:
        """
        Authorises the user using OAuth and retrieves the authentication token
        :return: The access token
        """
        import webbrowser
        from src.deenuxapi.deezer.oauth.OAuthHttpServer import OAuthHttpServer
        from src.deenuxapi.deezer.oauth.OAuthRequestHandler import OAuthRequestHandler

        server_address = ('', 0)  # Binding to port 0, so the OS can allocate a free random port for us
        httpd = OAuthHttpServer(server_address, OAuthRequestHandler)

        oauth_url = ResourceManager.get_app_setting("oauth_url").format(
            ResourceManager.get_app_setting('id'),  # The application Id
            quote("http://localhost:{0}".format(httpd.server_port), safe=''), # Redirection URL (to our dear local server, of course)
            ','.join(ResourceManager.get_app_setting('perms'))  # Permissions
        )
        webbrowser.open(oauth_url)
        code = httpd.serve_until_authorized()

        data = Request.get(ResourceManager.get_app_setting('token_url').format(code))

        Request.session_token = data['access_token']

        return data['access_token']

    @staticmethod
    def get_info_from_dz_url(url: str):
        splitted = re.split(r"[-/]", url)
        id = int(splitted[-1])
        model_name = splitted[-2].capitalize()
        return id, globals()[model_name]

    @staticmethod
    def get_entity_from_dz_url(url: str):
        """
        """
        info = DeezerProvider.get_info_from_dz_url(url)
        return info[1].get(info[0])
