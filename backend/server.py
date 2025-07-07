from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class Server(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        # Handle the incoming request here
        message = f"Served by {socket.gethostname()}"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode())


HTTPServer(('0.0.0.0', 8080), Server).serve_forever()
