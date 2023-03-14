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
    lem_version = settings.API_LEGAL_ENTITY_MANAGEMENT_VERSION

    def test_creating_legal_entity(self):
        request = {
            "type": "individual",
            "individual": {
                "residentialAddress": {
                    "city": "Amsterdam",
                    "country": "NL",
                    "postalCode": "1011DJ",
                    "street": "Simon Carmiggeltstraat 6 - 50"
                },
                "name": {
                    "firstName": "Shelly",
                    "lastName": "Eller"
                },
                "birthData": {
                    "dateOfBirth": "1990-06-21"
                },
                "email": "s.eller@example.com"
            }
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/legalEntityManagement/"
                                                              "individual_legal_entity_created.json")
        result = self.adyen.legalEntityManagement.legal_entities_api.create_legal_entity(request)
        self.assertEqual('Shelly', result.message['individual']['name']['firstName'])
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://kyc-test.adyen.com/lem/{self.lem_version}/legalEntities',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_get_transfer_instrument(self):
        instrumentId = "SE322JV223222F5GNXSR89TMW"
        self.adyen.client = self.test.create_client_from_file(200, None, "test/mocks/legalEntityManagement/"
                                                                         "details_of_trainsfer_instrument.json")
        result = self.adyen.legalEntityManagement.transfer_instruments_api.get_transfer_instrument(instrumentId)
        self.assertEqual(instrumentId, result.message['id'])
        self.adyen.client.http_client.request.assert_called_once_with(
            'GET',
            f'https://kyc-test.adyen.com/lem/{self.lem_version}/transferInstruments/{instrumentId}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=None,
            xapikey="YourXapikey"
        )

    def test_update_business_line(self):
        businessLineId = "SE322JV223222F5GVGMLNB83F"
        request = {
            "industryCode": "55",
            "webData": [
                {
                    "webAddress": "https://www.example.com"
                }
            ]
        }
        self.adyen.client = self.test.create_client_from_file(200, request, "test/mocks/legalEntityManagement/"
                                                                            "business_line_updated.json")
        result = self.adyen.legalEntityManagement.business_lines_api.update_business_line(request, businessLineId)
        self.assertEqual(businessLineId, result.message['id'])
        self.adyen.client.http_client.request.assert_called_once_with(
            'PATCH',
            f'https://kyc-test.adyen.com/lem/{self.lem_version}/businessLines/{businessLineId}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_accept_terms_of_service(self):
        legalEntityId = "legalId"
        documentId = "documentId"
        request = {
            'acceptedBy': "UserId",
            'ipAddress': "UserIpAddress"
        }
        self.adyen.client = self.test.create_client_from_file(204, request)
        self.adyen.legalEntityManagement.terms_of_service_api.accept_terms_of_service(request, legalEntityId,
                                                                                      documentId)
        self.adyen.client.http_client.request.assert_called_once_with(
            'PATCH',
            f'https://kyc-test.adyen.com/lem/{self.lem_version}/legalEntities/{legalEntityId}/termsOfService/{documentId}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )
