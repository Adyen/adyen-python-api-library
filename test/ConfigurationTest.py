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
    balance_platform_version = settings.API_BALANCE_PLATFORM_VERSION

    def test_creating_balance_account(self):
        request = {
            "accountHolderId": "AH32272223222B59K6ZKBBFNQ",
            "description": "S.Hopper - Main balance account"
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/configuration/"
                                                              "balance-account-created.json")
        result = self.adyen.balancePlatform.balance_accounts_api.create_balance_account(request)
        self.assertEqual('AH32272223222B59K6ZKBBFNQ', result.message['accountHolderId'])
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://balanceplatform-api-test.adyen.com/bcl/{self.balance_platform_version}/balanceAccounts',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_creating_account_holder(self):
        request = {
            "description": "Liable account holder used for international payments and payouts",
            "reference": "S.Eller-001",
            "legalEntityId": "LE322JV223222D5GG42KN6869"
        }
        self.adyen.client = self.test.create_client_from_file(200, request, "test/mocks/configuration/"
                                                                            "account-holder-created.json")
        result = self.adyen.balancePlatform.account_holders_api.create_account_holder(request)
        self.assertEqual("LE322JV223222D5GG42KN6869", result.message['legalEntityId'])
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://balanceplatform-api-test.adyen.com/bcl/{self.balance_platform_version}/accountHolders',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_get_balance_platform(self):
        platform_id = "YOUR_BALANCE_PLATFORM"
        self.adyen.client = self.test.create_client_from_file(200, None, "test/mocks/configuration/"
                                                                         "balance-platform-retrieved.json")
        result = self.adyen.balancePlatform.platform_api.get_balance_platform(platform_id)
        self.assertEqual(platform_id, result.message['id'])
        self.adyen.client.http_client.request.assert_called_once_with(
            'GET',
            f'https://balanceplatform-api-test.adyen.com/bcl/{self.balance_platform_version}/balancePlatforms/{platform_id}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=None,
            xapikey="YourXapikey"
        )

    def test_creating_payment_instrument(self):
        request = {
            "type": "bankAccount",
            "description": "YOUR_DESCRIPTION",
            "balanceAccountId": "BA3227C223222B5CTBLR8BWJB",
            "issuingCountryCode": "NL"
        }
        self.adyen.client = self.test.create_client_from_file(200, request, "test/mocks/configuration/"
                                                                            "business-account-created.json")
        result = self.adyen.balancePlatform.payment_instruments_api.create_payment_instrument(request)
        self.assertEqual("BA3227C223222B5CTBLR8BWJB", result.message["balanceAccountId"])
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://balanceplatform-api-test.adyen.com/bcl/{self.balance_platform_version}/paymentInstruments',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_creating_payment_instrument_group(self):
        request = {
            "balancePlatform": "YOUR_BALANCE_PLATFORM",
            "txVariant": "mc"
        }
        self.adyen.client = self.test.create_client_from_file(200, request, "test/mocks/configuration/"
                                                                            "payment-instrument-group-created.json")
        result = self.adyen.balancePlatform.payment_instrument_groups_api.create_payment_instrument_group(request)
        self.assertEqual("YOUR_BALANCE_PLATFORM", result.message['balancePlatform'])
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://balanceplatform-api-test.adyen.com/bcl/{self.balance_platform_version}/paymentInstrumentGroups',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_get_transaction_rule(self):
        transactionRuleId = "TR32272223222B5CMD3V73HXG"
        self.adyen.client = self.test.create_client_from_file(200, {}, "test/mocks/configuration/"
                                                                       "transaction-rule-retrieved.json")
        result = self.adyen.balancePlatform.transaction_rules_api.get_transaction_rule(transactionRuleId)
        self.assertEqual(transactionRuleId, result.message['transactionRule']['id'])
        self.adyen.client.http_client.request.assert_called_once_with(
            'GET',
            f'https://balanceplatform-api-test.adyen.com/bcl/{self.balance_platform_version}/'
            f'transactionRules/{transactionRuleId}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=None,
            xapikey="YourXapikey"
        )
