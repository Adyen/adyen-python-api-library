import Adyen
import unittest
from Adyen import settings

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestDisputes(unittest.TestCase):
    adyen = Adyen.Adyen()

    client = adyen.client
    test = BaseTest(adyen)
    client.xapikey = "YourXapikey"
    client.platform = "test"
    disputes_url = adyen.disputes.baseUrl

    def test_accept_dispute(self):
        request = {
            "disputePspReference": "DZ4DPSHB4WD2WN82",
            "merchantAccountCode": "YOUR_MERCHANT_ACCOUNT"
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/disputes/"
                                                              "post-acceptDispute-accept-dispute-200.json")
        result = self.adyen.disputes.accept_dispute(request)

        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'{self.disputes_url}/acceptDispute',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_defend_dispute(self):
        request = {
            "defenseReasonCode": "SupplyDefenseMaterial",
            "disputePspReference": "DZ4DPSHB4WD2WN82",
            "merchantAccountCode": "YOUR_MERCHANT_ACCOUNT"
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/disputes/"
                                                              "post-defendDispute-defend-dispute-200.json")
        result = self.adyen.disputes.defend_dispute(request)

        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'{self.disputes_url}/defendDispute',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_delete_defense_dispute_document(self):
        request = {
            "defenseDocumentType": "DefenseMaterial",
            "disputePspReference": "DZ4DPSHB4WD2WN82",
            "merchantAccountCode": "YOUR_MERCHANT_ACCOUNT"
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/disputes/"
                                                              "post-deleteDisputeDefenseDocument-delete-dispute-defense-document-200.json")
        result = self.adyen.disputes.delete_dispute_defense_document(request)

        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'{self.disputes_url}/deleteDisputeDefenseDocument',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )        

    def test_download_dispute_defense_document(self):
        request = {
            "disputePspReference": "DZ4DPSHB4WD2WN82",
            "merchantAccountCode": "YOUR_MERCHANT_ACCOUNT"
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/disputes/"
                                                              "post-downloadDisputeDefenseDocument-download-dispute-defense-document-200.json")
        result = self.adyen.disputes.delete_dispute_defense_document(request)

        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'{self.disputes_url}/deleteDisputeDefenseDocument',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )        

    def test_retrieve_applicable_defense_reasons(self):
        request = {
            "disputePspReference": "DZ4DPSHB4WD2WN82",
            "merchantAccountCode": "YOUR_MERCHANT_ACCOUNT"
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/disputes/"
                                                              "post-retrieveApplicableDefenseReasons-retrieve-defense-reasons-200.json")
        result = self.adyen.disputes.retrieve_applicable_defense_reasons(request)

        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'{self.disputes_url}/retrieveApplicableDefenseReasons',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )       
         
    def test_supply_defense_document(self):
        request = {
            "defenseDocuments": [
                {
                    "content": "JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBv+f/ub0j6JPRX+E3EmC==",
                    "contentType": "application/pdf",
                    "defenseDocumentTypeCode": "DefenseMaterial"
                }
            ],
            "disputePspReference": "DZ4DPSHB4WD2WN82",
            "merchantAccountCode": "YOUR_MERCHANT_ACCOUNT"
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/disputes/"
                                                              "post-supplyDefenseDocument-supply-defense-document-200.json")
        result = self.adyen.disputes.supply_defense_document(request)

        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'{self.disputes_url}/supplyDefenseDocument',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )        