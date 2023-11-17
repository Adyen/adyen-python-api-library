import unittest

import Adyen
from Adyen import settings

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestBalancePlatform(unittest.TestCase):
    adyen = Adyen.Adyen()

    client = adyen.client
    test = BaseTest(adyen)
    client.xapikey = "YourXapikey"
    client.platform = "test"
    balance_platform_url = adyen.balancePlatform.platform_api.baseUrl

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
            f'{self.balance_platform_url}/balanceAccounts',
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
            f'{self.balance_platform_url}/accountHolders',
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
            f'{self.balance_platform_url}/balancePlatforms/{platform_id}',
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
            f'{self.balance_platform_url}/paymentInstruments',
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
            f'{self.balance_platform_url}/paymentInstrumentGroups',
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
            f'{self.balance_platform_url}/'
            f'transactionRules/{transactionRuleId}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=None,
            xapikey="YourXapikey"
        )

    def test_update_network_token(self):
        request = {
            "status": "closed"
        }
        self.adyen.client = self.test.create_client_from_file(202, request)

        result = self.adyen.balancePlatform.network_tokens_api.update_network_token(request, 'TK123ABC')

        self.assertEqual(202, result.status_code)
        self.assertEqual({}, result.message)
        self.assertEqual("", result.raw_response)
        self.adyen.client.http_client.request.assert_called_once_with(
            'PATCH',
            f'{self.balance_platform_url}/networkTokens/TK123ABC',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )
