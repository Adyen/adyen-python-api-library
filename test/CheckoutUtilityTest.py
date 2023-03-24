import unittest

import Adyen
from Adyen import settings
try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestCheckoutUtility(unittest.TestCase):
    ady = Adyen.Adyen()

    client = ady.client
    test = BaseTest(ady)
    client.xapikey = "YourXapikey"
    client.platform = "test"
    checkout_version = settings.API_CHECKOUT_VERSION

    def test_origin_keys_success_mocked(self):
        request = {
            "originDomains": {
                "https://www.your-domain1.com",
                "https://www.your-domain2.com",
                "https://www.your-domain3.com"
            }
        }

        self.ady.client = self.test.create_client_from_file(200, request,
                                                            "test/mocks/"
                                                            "checkoututility/"
                                                            "originkeys"
                                                            "-success.json")
        result = self.ady.checkout.utility_api.origin_keys(request)

        self.assertEqual("pub.v2.7814286629520534.aHR0cHM6Ly93d3cu"
                         "eW91ci1kb21haW4xLmNvbQ.UEwIBmW9-c_uXo5wS"
                         "Er2w8Hz8hVIpujXPHjpcEse3xI",
                         result.message['originKeys']
                         ['https://www.your-domain1.com'])

        self.assertEqual("pub.v2.7814286629520534.aHR0cHM6Ly93d3cu"
                         "eW91ci1kb21haW4zLmNvbQ.fUvflu-YIdZSsLEH8"
                         "Qqmr7ksE4ag_NYiiMXK0s6aq_4",
                         result.message['originKeys']
                         ['https://www.your-domain3.com'])

        self.assertEqual("pub.v2.7814286629520534.aHR0cHM6Ly93d3cue"
                         "W91ci1kb21haW4yLmNvbQ.EP6eXBJKk0t7-QIUl6e_"
                         "b1qMuMHGepxG_SlUqxAYrfY",
                         result.message['originKeys']
                         ['https://www.your-domain2.com'])

    def test_checkout_utility_api_url_custom(self):
        url = self.ady.client._determine_api_url("test", "checkout", "/originKeys")

        self.assertEqual(url, "https://checkout-test.adyen.com/{}/originKeys".format(self.checkout_version))

    def test_applePay_session(self):
        request = {
          "displayName": "YOUR_MERCHANT_NAME",
          "domainName": "YOUR_DOMAIN_NAME",
          "merchantIdentifier": "YOUR_MERCHANT_ID"
        }
        self.ady.client = self.test.create_client_from_file(200, request, "test/mocks/"
                                                                            "checkoututility/"
                                                                            "applepay-sessions"
                                                                            "-success.json")
        result = self.ady.checkout.utility_api.get_apple_pay_session(request)
        self.assertEqual("BASE_64_ENCODED_DATA", result.message['data'])
