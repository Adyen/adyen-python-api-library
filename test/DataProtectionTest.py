import Adyen
import unittest
from Adyen import settings

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestCheckout(unittest.TestCase):
    adyen = Adyen.Adyen()

    client = adyen.client
    test = BaseTest(adyen)
    client.xapikey = "YourXapikey"
    client.platform = "test"
    data_protection_version = settings.API_DATA_PROTECION_VERSION
    lib_version = settings.LIB_VERSION

    def test_data_erasure(self):
        request = {
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "pspReference": "9915520502347613",
            "forceErasure": True
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/dataProtection/erasure-response.json")
        result = self.adyen.dataProtection.request_subject_erasure(request)
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://ca-test.adyen.com/ca/services/DataProtectionService/{self.data_protection_version}'
            '/requestSubjectErasure',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            xapikey="YourXapikey",
            json=request
        )
        self.assertEqual("SUCCESS", result.message["result"])
