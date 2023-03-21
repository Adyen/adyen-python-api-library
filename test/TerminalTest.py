import unittest
import Adyen
from Adyen import settings

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestTerminal(unittest.TestCase):
    adyen = Adyen.Adyen(username="YourWSUser",
                        password="YourWSPassword",
                        platform="test",
                        xapikey="YourXapikey")
    test = BaseTest(adyen)
    client = adyen.client
    terminal_version = settings.API_TERMINAL_VERSION

    def test_assign_terminals(self):
        request = {
            "companyAccount": "YOUR_COMPANY_ACCOUNT",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "store": "YOUR_STORE",
            "terminals": [
                "P400Plus-275479597"
            ]
        }
        self.test.create_client_from_file(
            200, request, "test/mocks/terminal/assignTerminals.json"
        )
        result = self.adyen.terminal.assign_terminals(request=request)
        self.assertIn("P400Plus-275479597", result.message["results"])

        self.client.http_client.request.assert_called_once_with(
            "POST",
            f"https://postfmapi-test.adyen.com/postfmapi/terminal/{self.terminal_version}/assignTerminals",
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json={
                "companyAccount": "YOUR_COMPANY_ACCOUNT",
                "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
                "store": "YOUR_STORE",
                "terminals": [
                    "P400Plus-275479597"
                ]
            },
            xapikey="YourXapikey"
        )

    def test_assign_terminals_422(self):
        request = {
            "companyAccount": "YOUR_COMPANY_ACCOUNT",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "store": "YOUR_STORE",
            "terminals": [
                "P400Plus-123456789"
            ]
        }
        self.test.create_client_from_file(
            200, request, "test/mocks/terminal/assignTerminals-422.json"
        )
        result = self.adyen.terminal.assign_terminals(request=request)
        self.assertEqual(422, result.message["status"])
        self.assertEqual("000", result.message["errorCode"])
        self.assertEqual("Terminals not found: P400Plus-123456789", result.message["message"])
        self.assertEqual("validation", result.message["errorType"])

    def test_find_terminal(self):
        request = {
            "terminal": "P400Plus-275479597",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
        }
        self.test.create_client_from_file(
            200, request, "test/mocks/terminal/findTerminal.json"
        )
        result = self.adyen.terminal.find_terminal(request=request)
        self.assertIn("P400Plus-275479597", result.message["terminal"])

        self.client.http_client.request.assert_called_once_with(
            "POST",
            f"https://postfmapi-test.adyen.com/postfmapi/terminal/{self.terminal_version}/findTerminal",
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json={
                "terminal": "P400Plus-275479597",
                "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            },
            xapikey="YourXapikey"
        )

    def test_find_terminal_422(self):
        request = {
            "terminal": "P400Plus-123456789"
        }
        self.test.create_client_from_file(
            200, request, "test/mocks/terminal/findTerminal-422.json"
        )
        result = self.adyen.terminal.find_terminal(request=request)
        self.assertEqual(422, result.message["status"])
        self.assertEqual("000", result.message["errorCode"])
        self.assertEqual("Terminal not found", result.message["message"])
        self.assertEqual("validation", result.message["errorType"])

    def test_get_stores_under_account(self):
        request = {
            "companyAccount": "YOUR_COMPANY_ACCOUNT",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
        }
        self.test.create_client_from_file(
            200, request, "test/mocks/terminal/getStoresUnderAccount.json"
        )
        result = self.adyen.terminal.get_stores_under_account(request=request)
        self.assertEqual(result.message["stores"], [
            {
                "store": "YOUR_STORE",
                "description": "YOUR_STORE",
                "address": {
                    "city": "The City",
                    "countryCode": "NL",
                    "postalCode": "1234",
                    "streetAddress": "The Street"
                },
                "status": "Active",
                "merchantAccountCode": "YOUR_MERCHANT_ACCOUNT"
            }
        ])

        self.client.http_client.request.assert_called_once_with(
            "POST",
            f"https://postfmapi-test.adyen.com/postfmapi/terminal/{self.terminal_version}/getStoresUnderAccount",
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json={
               "companyAccount": "YOUR_COMPANY_ACCOUNT",
                "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            },
            xapikey="YourXapikey"
        )

    def test_get_terminal_details(self):
        request = {
            "terminal": "P400Plus-275479597",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        }

        self.test.create_client_from_file(
            200, request, "test/mocks/terminal/getTerminalDetails.json"
        )
        result = self.adyen.terminal.get_terminal_details(request=request)

        self.assertEqual(result.message["deviceModel"], "P400Plus")
        self.assertEqual(result.message["terminal"], "P400Plus-275479597")

        self.client.http_client.request.assert_called_once_with(
            "POST",
            f"https://postfmapi-test.adyen.com/postfmapi/terminal/{self.terminal_version}/getTerminalDetails",
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json={
                "terminal": "P400Plus-275479597",
                "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            },
            xapikey="YourXapikey"
        )

    def test_get_terminal_details_422(self):
        request = {
            "terminal": "P400Plus-123456789"
        }
        self.test.create_client_from_file(
            200, request, "test/mocks/terminal/getTerminalDetails-422.json"
        )
        result = self.adyen.terminal.get_terminal_details(request=request)
        self.assertEqual(422, result.message["status"])
        self.assertEqual("000", result.message["errorCode"])
        self.assertEqual("Terminal not found", result.message["message"])
        self.assertEqual("validation", result.message["errorType"])

    def test_get_terminals_under_account(self):
        request = {
            "companyAccount": "YOUR_COMPANY_ACCOUNT",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
        }

        self.test.create_client_from_file(
            200, request, "test/mocks/terminal/getTerminalsUnderAccount.json"
        )
        result = self.adyen.terminal.get_terminals_under_account(request=request)

        self.assertEqual(result.message["merchantAccounts"], [
            {
                "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
                "inStoreTerminals": [
                    "P400Plus-275479597"
                ],
                "stores": [
                    {
                        "store": "YOUR_STORE",
                        "inStoreTerminals": [
                            "M400-401972715"
                        ]
                    }
                ]
            }
        ])

        self.client.http_client.request.assert_called_once_with(
            "POST",
            f"https://postfmapi-test.adyen.com/postfmapi/terminal/{self.terminal_version}/getTerminalsUnderAccount",
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json={
                "companyAccount": "YOUR_COMPANY_ACCOUNT",
                "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            },
            xapikey="YourXapikey"
        )

    def test_get_terminals_under_account_store(self):
        request = {
            "companyAccount": "YOUR_COMPANY_ACCOUNT",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "store": "YOUR_STORE"
        }

        self.test.create_client_from_file(
            200, request, "test/mocks/terminal/getTerminalsUnderAccount-store.json"
        )
        result = self.adyen.terminal.get_terminals_under_account(request=request)

        self.assertEqual(result.message["merchantAccounts"], [
            {
                "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
                "stores": [
                    {
                        "store": "YOUR_STORE",
                        "inStoreTerminals": [
                            "M400-401972715"
                        ]
                    }
                ]
            }
        ])

        self.client.http_client.request.assert_called_once_with(
            "POST",
            f"https://postfmapi-test.adyen.com/postfmapi/terminal/{self.terminal_version}/getTerminalsUnderAccount",
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json={
                "companyAccount": "YOUR_COMPANY_ACCOUNT",
                "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
                "store": "YOUR_STORE",
            },
            xapikey="YourXapikey"
        )


TestTerminal.client.http_force = "requests"
suite = unittest.TestLoader().loadTestsFromTestCase(TestTerminal)
unittest.TextTestRunner(verbosity=2).run(suite)

TestTerminal.client.http_force = "pycurl"
TestTerminal.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestTerminal)
unittest.TextTestRunner(verbosity=2).run(suite)

TestTerminal.client.http_force = "other"
TestTerminal.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestTerminal)
unittest.TextTestRunner(verbosity=2).run(suite)
