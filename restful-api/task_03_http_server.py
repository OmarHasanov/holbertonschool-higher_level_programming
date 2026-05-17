#!/usr/bin/python3
"""
A simple HTTP server built using the http.server module.
This API handles different endpoints and returns text or JSON data.
"""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP request handler for our simple API.
    """

    def do_GET(self):
        """
        Handles GET requests for various endpoints.
        """
        if self.path == '/':
            # Əsas səhifə üçün sadə mətn cavabı
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            # /data endpointi üçün JSON cavabı
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(sample_data).encode("utf-8"))

        elif self.path == '/status':
            # /status endpointi API-nin işləkliyini yoxlayır
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            # /info endpointi üçün əlavə JSON məlumatı
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info_data).encode("utf-8"))

        else:
            # Tapılmayan endpointlər üçün 404 xətası
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server(port=8000):
    """
    Starts the HTTP server on the specified port.
    """
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print(f"Serving on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
