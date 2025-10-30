import Adyen
import unittest
from Adyen import settings

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestSessionAuthentication(unittest.TestCase):
    adyen = Adyen.Adyen()

    client = adyen.client
    test = BaseTest(adyen)
    client.xapikey = "YourXapikey"
    client.platform = "test"
    session_url = adyen.sessionAuthentication.session_authentication_api.baseUrl

    def test_create_session_token(self):
        request = {
            "allowOrigin": 'https://www.your-website.com',
            "product": "platform",
            "policy": {
                "resources": [
                    {
                        "type": "accountHolder",
                        "accountHolderId": "AH00000000000000000000001"
                    }
                ],
                "roles": [
                    "Transactions Overview Component: View",
                    "Payouts Overview Component: View"
                ]
            }
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/sessionAuthentication/"
                                                              "authentication-session-created.json")

        result = self.adyen.sessionAuthentication.session_authentication_api.create_authentication_session(request)
        self.assertEqual("long_session_token_string", result.message["sessionToken"])
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'{self.session_url}/sessions',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )
