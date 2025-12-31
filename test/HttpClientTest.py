import unittest
import Adyen
from Adyen import settings

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestHttpClient(unittest.TestCase):

    def test_user_agent_without_application_name(self):
        adyen = Adyen.Adyen()
        client = adyen.client
        client.xapikey = "TEST_XAPI_KEY"

        test = BaseTest(adyen)
        
        # Mock the http_client.request method
        client = test.create_client_from_file(200, {}, "test/mocks/checkout/paymentmethods-success.json")

        # Call a dummy API method
        _ = adyen.checkout.payments_api.payment_methods({})

        # Assert that http_client.request was called with the correct headers
        client.http_client.request.assert_called_once_with(
            'POST',
            f'{adyen.checkout.payments_api.baseUrl}/paymentMethods',
            headers={
                'adyen-library-name': settings.LIB_NAME,
                'adyen-library-version': settings.LIB_VERSION,
                'User-Agent': settings.LIB_NAME + "/" + settings.LIB_VERSION
            },
            json={},
            xapikey='TEST_XAPI_KEY'
        )

    def test_user_agent_with_application_name(self):
        adyen = Adyen.Adyen()
        client = adyen.client
        client.xapikey = "TEST_XAPI_KEY"
        client.application_name = "MyTestApp"

        test = BaseTest(adyen)

        # Mock the http_client.request method
        client = test.create_client_from_file(200, {}, "test/mocks/checkout/paymentmethods-success.json")

        # Call a dummy API method
        _ = adyen.checkout.payments_api.payment_methods({})

        # Assert that http_client.request was called with the correct headers
        client.http_client.request.assert_called_once_with(
            'POST',
            f'{adyen.checkout.payments_api.baseUrl}/paymentMethods',
            headers={
                'adyen-library-name': settings.LIB_NAME,
                'adyen-library-version': settings.LIB_VERSION,
                'User-Agent': "MyTestApp " + settings.LIB_NAME + "/" + settings.LIB_VERSION
            },
            json={},
            xapikey='TEST_XAPI_KEY'
        )

if __name__ == '__main__':
    unittest.main()
