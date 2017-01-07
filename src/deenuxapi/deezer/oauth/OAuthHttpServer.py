from http.server import HTTPServer


class OAuthHttpServer(HTTPServer):

    def __init__ (self, *args):
        super().__init__(*args)
        self._serve = True
        self._code = None

    @property
    def code(self) -> str:
        return self._code
    @code.setter
    def code(self, value: str) -> None:
        self._code = value

    def serve_until_authorized(self) -> str:
        """
        The server accepts HTTP requests, until there is a code
        When there is a code, it means that the user is authorized
        :return: The authorization code
        """
        while self._serve is True:
            self.handle_request()
        return self.code



