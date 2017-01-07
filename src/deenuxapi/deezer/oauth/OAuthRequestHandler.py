from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import os


class OAuthRequestHandler(BaseHTTPRequestHandler):

    success_msg = {
        'title': 'Success',
        'h1': 'Auth success'
    }

    failure_msg = {
        'title': 'Failure',
        'h1': 'Auth failed'
    }

    def do_GET(self):
        """
        Handles GET requests, and sets on server object a code, if in the current GET request
        there is a query param with `code` key. Otherwise, it rejects the request
        (Good URL example /?code=whatever)
        :return:
        """
        self.server._serve = False
        try:
            # This gets the code query parameter (or thows KeyError if it isn't present)
            code = parse_qs(urlparse(self.path).query)['code'][0]

            self.send_response(200)
            msg = self.success_msg
            self.server.authorized = True
            self.server.code = code
        except KeyError:
            # There isn't a `code` query param in the url
            # Reject
            self.send_response(400)
            msg = self.failure_msg

        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(
            open(os.path.realpath(os.path.dirname(__file__)) + '/StatusMessage.html')
                .read()
                .format(**msg)
                .encode('ascii')
        )
