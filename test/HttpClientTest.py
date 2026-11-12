import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

import Adyen
from Adyen import httpclient, settings

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestHttpClient(unittest.TestCase):
    def setUp(self):
        self.adyen = Adyen.Adyen()
        self.client = self.adyen.client
        self.client.xapikey = "TEST_XAPI_KEY"
        self.test = BaseTest(self.adyen)

    def test_user_agent_without_application_name(self):
        # Mock the http_client.request method
        self.test.create_client_from_file(
            200, {}, "test/mocks/checkout/paymentmethods-success.json"
        )

        # Call a dummy API method
        _ = self.adyen.checkout.payments_api.payment_methods({})

        # Assert that http_client.request was called with the correct headers
        self.client.http_client.request.assert_called_once_with(
            "POST",
            f"{self.adyen.checkout.payments_api.baseUrl}/paymentMethods",
            headers={
                "adyen-library-name": settings.LIB_NAME,
                "adyen-library-version": settings.LIB_VERSION,
                "User-Agent": settings.LIB_NAME + "/" + settings.LIB_VERSION,
            },
            json={},
            xapikey="TEST_XAPI_KEY",
        )

    def test_user_agent_with_application_name(self):
        self.client.application_name = "MyTestApp"

        # Mock the http_client.request method
        self.test.create_client_from_file(
            200, {}, "test/mocks/checkout/paymentmethods-success.json"
        )

        # Call a dummy API method
        _ = self.adyen.checkout.payments_api.payment_methods({})

        # Assert that http_client.request was called with the correct headers
        self.client.http_client.request.assert_called_once_with(
            "POST",
            f"{self.adyen.checkout.payments_api.baseUrl}/paymentMethods",
            headers={
                "adyen-library-name": settings.LIB_NAME,
                "adyen-library-version": settings.LIB_VERSION,
                "User-Agent": "MyTestApp " + settings.LIB_NAME + "/" + settings.LIB_VERSION,
            },
            json={},
            xapikey="TEST_XAPI_KEY",
        )


class TestEmptyJsonPayload(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.received = []

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
                cls.received.append((self.command, self.headers.get("Content-Type"), body))
                self.send_response(200)
                self.send_header("Content-Length", "2")
                self.end_headers()
                self.wfile.write(b"{}")

            do_PATCH = do_POST

            def log_message(self, *args):
                pass

        cls.server = HTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f"http://127.0.0.1:{cls.server.server_port}/test"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def check_empty_json(self, transport):
        client = httpclient.HTTPClient("test/", "1", force_request=transport, timeout=5)
        for method in ("POST", "PATCH"):
            with self.subTest(method=method):
                result = client.request(method, self.url, json={})
                self.assertEqual(result[1], {})
                self.assertEqual(result[2], 200)
                self.assertEqual(self.received[-1], (method, "application/json", b"{}"))

    def test_urllib_empty_json(self):
        self.check_empty_json("urllib")

    @unittest.skipIf(httpclient.pycurl is None, "pycurl is not installed")
    def test_pycurl_empty_json(self):
        self.check_empty_json("pycurl")

    def test_requests_empty_json(self):
        self.check_empty_json("requests")

    def check_missing_body(self, transport):
        client = httpclient.HTTPClient("test/", "1", force_request=transport, timeout=5)
        for method in ("POST", "PATCH"):
            with self.subTest(method=method):
                with self.assertRaisesRegex(ValueError, "either a json or a data field"):
                    client.request(method, self.url)

    def test_urllib_missing_body(self):
        self.check_missing_body("urllib")

    @unittest.skipIf(httpclient.pycurl is None, "pycurl is not installed")
    def test_pycurl_missing_body(self):
        self.check_missing_body("pycurl")


if __name__ == "__main__":
    unittest.main()
