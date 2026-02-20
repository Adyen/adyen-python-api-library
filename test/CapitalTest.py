import Adyen
import unittest
from Adyen import settings

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestCapital(unittest.TestCase):
    adyen = Adyen.Adyen()

    client = adyen.client
    test = BaseTest(adyen)
    client.xapikey = "YourXapikey"
    client.platform = "test"
    lib_version = settings.LIB_VERSION

    def test_request_grant(self):
        request = {}
        self.adyen.client = self.test.create_client_from_file(
            200,
            request,
            "test/mocks/capital/grants-success.json"
        )
        result = self.adyen.capital.grants_api.request_grant(request)
        self.assertEqual(1, len(result.message['grants']))
        self.assertEqual("GR00000000000000000000001", result.message['grants'][0]['id'])

    def test_get_all_grant_offers(self):
        request = {}
        self.adyen.client = self.test.create_client_from_file(
            200,
            request,
            "test/mocks/capital/grant-offers-success.json"
        )
        result = self.adyen.capital.grant_offers_api.get_all_grant_offers(request)
        self.assertEqual(1, len(result.message['grantOffers']))
        self.assertEqual("GO00000000000000000000001", result.message['grantOffers'][0]['id'])

    def test_get_all_grants(self):
        request = {}
        self.adyen.client = self.test.create_client_from_file(
            200,
            request,
            "test/mocks/capital/grants-success.json"
        )
        result = self.adyen.capital.grants_api.get_all_grants(counterparty_account_holder_id="AH00000000000000000000001")
        self.assertEqual(1, len(result.message['grants']))
        self.assertEqual("GR00000000000000000000001", result.message['grants'][0]['id'])

    def test_get_grant(self):
        request = {}
        self.adyen.client = self.test.create_client_from_file(
            200,
            request,
            "test/mocks/capital/get-grant-success.json"
        )
        result = self.adyen.capital.grants_api.get_grant(grantId="GR00000000000000000000001")
        self.assertEqual("GR00000000000000000000001", result.message['id'])

    def test_get_all_grant_disbursements(self):
        request = {}
        self.adyen.client = self.test.create_client_from_file(
            200,
            request,
            "test/mocks/capital/get-grant-disbursements-success.json"
        )
        result = self.adyen.capital.grants_api.get_all_grant_disbursements(grantId="GR00000000000000000000001")
        self.assertEqual(1, len(result.message['disbursements']))
        self.assertEqual("DI00000000000000000000001", result.message['disbursements'][0]['id'])

    def test_get_grant_disbursement(self):
        request = {}
        self.adyen.client = self.test.create_client_from_file(
            200,
            request,
            "test/mocks/capital/get-grant-disbursement-success.json"
        )
        result = self.adyen.capital.grants_api.get_grant_disbursement(grantId="GR00000000000000000000001",
                                                                       disbursementId="DI00000000000000000000001")
        self.assertEqual("DI00000000000000000000001", result.message['id'])

    def test_update_grant_disbursement(self):
        request = {}
        self.adyen.client = self.test.create_client_from_file(
            200,
            request,
            "test/mocks/capital/update-grant-disbursement-success.json"
        )
        result = self.adyen.capital.grants_api.update_grant_disbursement(request, grantId="GR00000000000000000000001",
                                                                          disbursementId="DI00000000000000000000001")
        self.assertEqual(1500, result.message['repayment']['basisPoints'])

    def test_get_grant_account_information(self):
        request = {}
        self.adyen.client = self.test.create_client_from_file(
            200,
            request,
            "test/mocks/capital/get-grant-account-success.json"
        )
        result = self.adyen.capital.grant_accounts_api.get_grant_account_information(id="CG00000000000000000000001")
        self.assertEqual("CG00000000000000000000001", result.message['id'])

    def test_get_grant_offer(self):
        request = {}
        self.adyen.client = self.test.create_client_from_file(
            200,
            request,
            "test/mocks/capital/get-grant-offer-success.json"
        )
        result = self.adyen.capital.grant_offers_api.get_grant_offer(id="GO00000000000000000000001")
        self.assertEqual("GO00000000000000000000001", result.message['id'])
