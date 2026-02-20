import pytest
import json
import Adyen
from unittest import mock
import http.server
import threading
import socket

import os

class MockHandler(http.server.BaseHTTPRequestHandler):
    def _respond_from_file(self, filename):
        if not filename:
            return None
            
        # Try to find the file
        if not os.path.exists(filename):
            self.send_response(404)
            self.end_headers()
            self.wfile.write(f"Mock file not found: {filename}".encode())
            return True

        with open(filename, 'rb') as f:
            content = f.read()
            
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(content)
        return True

    def handle_request(self):
        # Allow tests to specify a mock file via header
        mock_file = self.headers.get('X-Mock-File')
        if mock_file and self._respond_from_file(mock_file):
            return

        if self.path == "/slow-endpoint":
            import time
            threading.Event().wait(0.5)
            
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        response = {
            "status": "success",
            "method": self.command,
            "path": self.path,
            "received_headers": dict(self.headers)
        }
        
        # Read body if present
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            post_data = self.rfile.read(content_length)
            try:
                response["received_body"] = json.loads(post_data.decode('utf-8'))
            except:
                response["received_body"] = post_data.decode('utf-8')

        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_POST(self):
        self.handle_request()

    def do_PATCH(self):
        self.handle_request()

    def do_GET(self):
        self.handle_request()

    def do_DELETE(self):
        self.handle_request()

    def log_message(self, format, *args):
        return

@pytest.fixture(scope="session")
def mock_server():
    """Starts a local HTTP server for integration testing backends."""
    server = http.server.HTTPServer(('localhost', 0), MockHandler)
    port = server.server_port
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    yield f"http://localhost:{port}"
    server.shutdown()
    server.server_close()

@pytest.fixture
def mock_server_client(mock_server):
    """Provides an Adyen instance configured to use the real HTTP stack against the mock server."""
    def _create_integration_client(mock_file=None, backend="requests"):
        ady = Adyen.Adyen()
        ady.client.xapikey = "TEST_XAPI_KEY"
        ady.client.platform = "test"
        ady.client.http_force = backend
        
        # Override the base URLs to point to our mock server
        # We need to catch calls and redirect them
        # A simple way is to use a prefix or just point everything to mock_server
        
        # We can pass the mock file via a header parameter in the actual call
        header_params = {}
        if mock_file:
            header_params['X-Mock-File'] = mock_file
            
        return ady, header_params

    return _create_integration_client

@pytest.fixture
def adyen_instance():
    """Returns a fresh Adyen instance for each test."""
    ady = Adyen.Adyen()
    # xapikey and platform can be set by individual tests if needed
    ady.client.platform = "test"
    return ady

@pytest.fixture
def mock_client(adyen_instance):
    """Fixture that provides a function to mock the Adyen client from a file."""
    def _create_client_from_file(status, request, filename=None):
        if filename:
            with open(filename) as data_file:
                data = json.load(data_file)
            with open(filename) as st:
                strjson = st.read()
        else:
            data = {}
            strjson = ""

        # Ensure the actual http_client instance is initialized
        if not adyen_instance.client.http_init:
            adyen_instance.client._init_http_client()

        adyen_instance.client.http_init = True
        adyen_instance.client.http_client.request = mock.MagicMock(
            return_value=[strjson, request, status, data])

        return adyen_instance.client

    return _create_client_from_file
