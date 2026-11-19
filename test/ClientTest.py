import unittest

import Adyen
from Adyen import settings

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestClient(unittest.TestCase):
    adyen = Adyen.Adyen()

    client = adyen.client
    test = BaseTest(adyen)
    client.xapikey = "YOUR_API_KEY"
    client.platform = "test"
    lib_version = settings.LIB_VERSION

    def test_unknown_properties_raise_attribute_error(self):
        with self.assertRaises(AttributeError):
            _ = self.adyen.foobar
        # Resolve parent attributes outside of assertRaises to avoid false positives
        payments_api = self.adyen.payment.payments_api
        with self.assertRaises(AttributeError):
            _ = payments_api.foobar
