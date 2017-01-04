
from http.server import HTTPServer, BaseHTTPRequestHandler

class OAuthHttpServer(HTTPServer):

    def __init__ (self, *args):
        super().__init__(*args)
        self._authorized = False

    @property
    def authorized(self) -> bool:
        return self._authorized
    @authorized.setter
    def authorized(self, value: bool) -> None:
        self._authorized = value
    @property
    def code(self) -> bool:
        return self._code
    @code.setter
    def code(self, value: bool) -> None:
        self._code = value

    def serve_until_authorization(self) -> str:
        while not self.authorized:
            self.handle_request()
        return self.code


class OAuthRequestHandler(BaseHTTPRequestHandler):

    close_window = "<html><head><script>" \
                       "close();" \
                       "</script></head></html>".encode('ascii')

    @staticmethod
    def _parse_params(url):
        ans = dict()
        for param in url.split('?')[1].split('&'):
            (key, val) = param.split('=')
            ans[key] = val

        return ans

    def reject_request(self):
        self.send_response(400)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("No code query param".encode('ascii'))

    def do_GET(self):

        try:
            params = self._parse_params(self.path)
            code = params['code']
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.close_window)

            self.server.authorized = True
            self.server.code = code
        except:
            # Invalid request / url
            self.reject_request()

