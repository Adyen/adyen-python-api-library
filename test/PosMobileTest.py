import Adyen
import unittest
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
            200,
            request,
            "test/mocks/posMobile/create-communication-session-success.json"
        )
        result = self.adyen.posMobile.pos_mobile_api.create_communication_session(request)
        self.assertEqual("CS00000000000000000000001", result.message['id'])
        self.assertEqual("session_data_example", result.message['sessionData'])
