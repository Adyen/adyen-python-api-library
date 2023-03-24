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
    transfers_version = settings.API_TRANSFERS_VERSION

    def test_transfer_fund(self):
        request = {
            "amount": {
                "value": 110000,
                "currency": "EUR"
            },
            "balanceAccountId": "BAB8B2C3D4E5F6G7H8D9J6GD4",
            "category": "bank",
            "counterparty": {
                "bankAccount": {
                    "accountHolder": {
                        "fullName": "A. Klaassen",
                        "address": {
                            "city": "San Francisco",
                            "country": "US",
                            "postalCode": "94678",
                            "stateOrProvince": "CA",
                            "street": "Brannan Street",
                            "street2": "274"
                        }
                    }
                },
                "accountIdentification": {
                    "type": "numberAndBic",
                    "accountNumber": "123456789",
                    "bic": "BOFAUS3NXXX"
                }
            },
            "priority": "wire",
            "referenceForBeneficiary": "Your reference sent to the beneficiary",
            "reference": "Your internal reference for the transfer",
            "description": "Your description for the transfer"
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/transfers/"
                                                              "make-transfer-response.json")
        result = self.adyen.transfers.transfers_api.transfer_funds(request)

        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://balanceplatform-api-test.adyen.com/btl/{self.transfers_version}/transfers',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_get_all_transactions(self):
        self.adyen.client = self.test.create_client_from_file(200, None, "test/mocks/transfers/"
                                                                         "get-all-transactions.json")

        result = self.adyen.transfers.transactions_api.get_all_transactions()
        self.adyen.client.http_client.request.assert_called_once_with(
            'GET',
            f'https://balanceplatform-api-test.adyen.com/btl/{self.transfers_version}/transactions',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=None,
            xapikey="YourXapikey"
        )

    def test_get_transaction(self):
        transacion_id="123"
        self.adyen.client = self.test.create_client_from_file(200, None, "test/mocks/transfers/"
                                                                         "get-transaction.json")
        result = self.adyen.transfers.transactions_api.get_transaction(transacion_id)
        self.adyen.client.http_client.request.assert_called_once_with(
            'GET',
            f'https://balanceplatform-api-test.adyen.com/btl/{self.transfers_version}/transactions/{transacion_id}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=None,
            xapikey="YourXapikey"
        )

