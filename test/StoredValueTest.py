import Adyen
import unittest
from Adyen import settings

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestManagement(unittest.TestCase):
    adyen = Adyen.Adyen()

    client = adyen.client
    test = BaseTest(adyen)
    client.xapikey = "YourXapikey"
    client.platform = "test"
    stored_value_version = settings.API_STORED_VALUE_VERSION

    def issue(self):
        request = {
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "store": "YOUR_STORE_ID",
            "paymentMethod": {
                "type": "valuelink"
            },
            "giftCardPromoCode": "1324",
            "reference": "YOUR_REFERENCE"
        }

        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/storedValue/issue-giftcard.json")
        result = self.adyen.storedValue.issue(request)
        self.assertEqual(result.message['paymentMethod']['type'], 'givex')
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://pal-test.adyen.com/pal/servlet/StoredValue/{self.stored_value_version}/issue',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_activate_giftcard(self):
        request = {
            "status": "active",
            "amount": {
                "currency": "USD",
                "value": 1000
            },
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "store": "YOUR_STORE_ID",
            "paymentMethod": {
                "type": "svs",
                "number": "6006491286999921374",
                "securityCode": "1111"
            },
            "reference": "YOUR_REFERENCE"
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/storedValue/activate-giftcards.json")
        result = self.adyen.storedValue.change_status(request)
        self.assertEqual(result.message['currentBalance']['value'], 1000)
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://pal-test.adyen.com/pal/servlet/StoredValue/{self.stored_value_version}/changeStatus',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_load_funds(self):
        request = {
            "amount": {
                "currency": "USD",
                "value": 2000
            },
            "loadType": "merchandiseReturn",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "store": "YOUR_STORE_ID",
            "paymentMethod": {
                "type": "svs",
                "number": "6006491286999921374",
                "securityCode": "1111"
            },
            "reference": "YOUR_REFERENCE"
        }
        self.adyen.client = self.test.create_client_from_file(200, request, "test/mocks/storedValue/load-funds.json")
        result = self.adyen.storedValue.load(request)
        self.assertEqual(result.message['resultCode'], 'Success')
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://pal-test.adyen.com/pal/servlet/StoredValue/{self.stored_value_version}/load',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_check_balance(self):
        request = {
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "store": "YOUR_STORE_ID",
            "paymentMethod": {
                "type": "svs",
                "number": "603628672882001915092",
                "securityCode": "5754"
            },
            "reference": "YOUR_REFERENCE"
        }
        self.adyen.client = self.test.create_client_from_file(200, request, "test/mocks/storedValue/check-balance.json")
        result = self.adyen.storedValue.check_balance(request)
        self.assertEqual(result.message['currentBalance']['value'], 5600)
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://pal-test.adyen.com/pal/servlet/StoredValue/{self.stored_value_version}/checkBalance',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_merge_balance(self):
        request = {
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "store": "YOUR_STORE_ID",
            "sourcePaymentMethod": {
                "number": "7777182708544835",
                "securityCode": "2329"
            },
            "paymentMethod": {
                "type": "valuelink",
                "number": "8888182708544836",
                "securityCode": "2330"
            },
            "reference": "YOUR_REFERENCE"
        }
        self.adyen.client = self.test.create_client_from_file(200, request, "test/mocks/storedValue/merge-balance.json")
        result = self.adyen.storedValue.merge_balance(request)
        self.assertEqual(result.message['pspReference'], "881564657480267D")
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://pal-test.adyen.com/pal/servlet/StoredValue/{self.stored_value_version}/mergeBalance',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_void_transaction(self):
        request = {
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "originalReference": "851564654294247B",
            "reference": "YOUR_REFERENCE"
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/storedValue/undo-transaction.json")
        result = self.adyen.storedValue.void_transaction(request)
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://pal-test.adyen.com/pal/servlet/StoredValue/{self.stored_value_version}/voidTransaction',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )
