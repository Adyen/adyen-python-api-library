import unittest

import Adyen
from Adyen import settings

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestPosMobile(unittest.TestCase):
    adyen = Adyen.Adyen()

    client = adyen.client
    test = BaseTest(adyen)
    client.xapikey = "YourXapikey"
    client.platform = "test"
    lib_version = settings.LIB_VERSION

    def test_create_communication_session(self):
        request = {}
        self.adyen.client = self.test.create_client_from_file(
            200, request, "test/mocks/posMobile/create-communication-session-success.json"
        )
        result = self.adyen.posMobile.pos_mobile_api.create_communication_session(request)
        self.assertEqual("CS00000000000000000000001", result.message["id"])
        self.assertEqual("session_data_example", result.message["sessionData"])

    def test_base_url_test_environment(self):
        pos_mobile_url = self.adyen.posMobile.pos_mobile_api.baseUrl
        url = self.adyen.client._determine_api_url("test", pos_mobile_url)
        self.assertEqual(url, pos_mobile_url)
        self.assertTrue(url.startswith("https://checkout-test.adyen.com/checkout/possdk/"))

    def test_base_url_live_environment(self):
        self.adyen.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
        try:
            pos_mobile_url = self.adyen.posMobile.pos_mobile_api.baseUrl
            pos_mobile_version = pos_mobile_url.split("/")[-1]
            url = self.adyen.client._determine_api_url("live", pos_mobile_url)
            self.assertEqual(
                url,
                f"https://1797a841fbb37ca7-AdyenDemo-checkout-live.adyenpayments.com"
                f"/checkout/possdk/{pos_mobile_version}",
            )
        finally:
            self.adyen.client.live_endpoint_prefix = None

    def test_base_url_live_environment_no_prefix_raises(self):
        self.adyen.client.live_endpoint_prefix = None
        pos_mobile_url = self.adyen.posMobile.pos_mobile_api.baseUrl
        from Adyen.exceptions import AdyenEndpointInvalidFormat
        self.assertRaises(
            AdyenEndpointInvalidFormat,
            self.adyen.client._determine_api_url,
            "live",
            pos_mobile_url,
        )

