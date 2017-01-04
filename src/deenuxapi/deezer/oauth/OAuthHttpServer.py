
from http.server import HTTPServer, BaseHTTPRequestHandler


class OAuthHttpServer(HTTPServer):

    def __init__ (self, *args):
        super().__init__(*args)
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
        while self.code is None:
            self.handle_request()
        return self.code


class OAuthRequestHandler(BaseHTTPRequestHandler):

    close_window = "<html><head><script>" \
                       "close();" \
                       "</script></head></html>".encode('ascii')

    @staticmethod
    def _parse_params(url: str) -> dict:
        """
        Parses the params from an url to a dictionary
        :param url:
        :return:
        """
        ans = dict()
        for param in url.split('?')[1].split('&'):
            (key, val) = param.split('=')
            ans[key] = val

        return ans

    def do_GET(self):
        """
        Handles GET requests, and sets on server object a code, if in the current GET request
        there is a query param with `code` key. Otherwise, it rejects the request
        (Good URL example /?code=whatever)
        :return:
        """
        try:
            code = self._parse_params(self.path)['code']

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.close_window)

            self.server.authorized = True
            self.server.code = code
        except:
            # Invalid request / url
            # Reject
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("No code query param".encode('ascii'))

