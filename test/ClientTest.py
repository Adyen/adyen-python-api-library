import Adyen
import unittest
from Adyen import settings

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestClient(unittest.TestCase):
    adyen = Adyen.Adyen()

    client = adyen.client
    test = BaseTest(adyen)
    client.xapikey = "YourXapikey"
    client.platform = "test"
    lib_version = settings.LIB_VERSION

    def test_url_creation_for_capitalAPI(self):
        self.adyen.client = self.test.create_client_from_file(200, {}, "test/mocks/"
                                                              "generic_response.json")
        self.adyen.transfers.capital_api.get_capital_account()
        self.adyen.client.http_client.request.assert_called_once_with(
            'GET',
            'https://balanceplatform-api-test.adyen.com/btl/{}/grants'.format(settings.API_CAPITAL_VERSION),
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=None,
            xapikey='YourXapikey'
        )
