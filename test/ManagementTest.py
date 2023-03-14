import Adyen
from Adyen import settings
import unittest

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
    management_version = settings.API_MANAGEMENT_VERSION

    def test_get_company_account(self):
        request = None
        id = "YOUR_COMPANY_ACCOUNT"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "management/"
                                                              "get_company_account"
                                                              ".json")

        result = self.adyen.management.account_company_level_api.get_company_account(companyId=id)
        self.assertEqual(id, result.message['id'])
        self.adyen.client.http_client.request.assert_called_once_with(
            'GET',
            f'https://management-test.adyen.com/{self.management_version}/companies/{id}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=None,
            xapikey="YourXapikey"
        )

    def test_my_api_credential_api(self):
        request = {"domain": "YOUR_DOMAIN"}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "management/"
                                                              "post_me_allowed"
                                                              "_origins.json")
        result = self.adyen.management.my_api_credential_api.add_allowed_origin(request)
        originId = result.message['id']
        self.assertEqual("YOUR_DOMAIN", result.message['domain'])
        self.adyen.client = self.test.create_client_from_file(204, {},
                                                              "test/mocks/"
                                                              "management/"
                                                              "no_content.json")
        result = self.adyen.management.my_api_credential_api.remove_allowed_origin(originId)
        self.adyen.client.http_client.request.assert_called_once_with(
            'DELETE',
            f'https://management-test.adyen.com/{self.management_version}/me/allowedOrigins/{originId}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=None,
            xapikey="YourXapikey"
        )

    def test_update_a_store(self):
        request = {
            "address": {
                "line1": "1776 West Pinewood Avenue",
                "line2": "Heartland Building",
                "line3": "",
                "postalCode": "20251"
            }
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "management/"
                                                              "update_a_store"
                                                              ".json")
        storeId = "YOUR_STORE_ID"
        merchantId = "YOUR_MERCHANT_ACCOUNT_ID"
        result = self.adyen.management.account_store_level_api.update_store(request, merchantId, storeId)
        self.adyen.client.http_client.request.assert_called_once_with(
            'PATCH',
            f'https://management-test.adyen.com/{self.management_version}/merchants/{merchantId}/stores/{storeId}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )
        self.assertEqual(storeId, result.message['id'])
        self.assertEqual("1776 West Pinewood Avenue", result.message['address']['line1'])

    def test_create_a_user(self):
        request = {
            "name": {
                "firstName": "John",
                "lastName": "Smith"
            },
            "username": "johnsmith",
            "email": "john.smith@example.com",
            "timeZoneCode": "Europe/Amsterdam",
            "roles": [
                "Merchant standard role",
                "Merchant admin"
            ],
            "associatedMerchantAccounts": [
                "YOUR_MERCHANT_ACCOUNT"
            ]
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "management/"
                                                              "create_a_user"
                                                              ".json")
        companyId = "YOUR_COMPANY_ACCOUNT"
        result = self.adyen.management.users_company_level_api.create_new_user(request, companyId)
        self.assertEqual(request['name']['firstName'], result.message['name']['firstName'])
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://management-test.adyen.com/{self.management_version}/companies/{companyId}/users',
            json=request,
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            xapikey="YourXapikey"
        )

    def test_get_list_of_android_apps(self):
        request = {}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "management/"
                                                              "get_list_of"
                                                              "_android_apps"
                                                              ".json")
        companyId = "YOUR_COMPANY_ACCOUNT"
        result = self.adyen.management.terminal_actions_company_level_api.list_android_apps(companyId)
        self.assertEqual("ANDA422LZ223223K5F694GCCF732K8", result.message['androidApps'][0]['id'])

    def test_query_paramaters(self):
        request = {}
        companyId = "YOUR_COMPANY_ACCOUNT"
        query_parameters = {
            'pageNumber': 1,
            'pageSize': 10

        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "management/"
                                                              "get_list_of_merchant_accounts.json")
        result = self.adyen.management.account_company_level_api. \
            list_merchant_accounts(companyId, query_parameters=query_parameters)
        self.adyen.client.http_client.request.assert_called_once_with(
            'GET',
            f'https://management-test.adyen.com/{self.management_version}/companies/{companyId}/merchants?pageNumber=1&pageSize=10',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=None,
            xapikey="YourXapikey"
        )
