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
    management_url = adyen.management.my_api_credential_api.baseUrl

    def test_get_company_account(self):
        request = None
        company_id = "YOUR_COMPANY_ACCOUNT"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "management/"
                                                              "get_company_account"
                                                              ".json")

        result = self.adyen.management.account_company_level_api.get_company_account(companyId=company_id)

        self.assertEqual(company_id, result.message['id'])
        self.adyen.client.http_client.request.assert_called_once_with(
            'GET',
            f'{self.management_url}/companies/{company_id}',
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

        self.assertEqual("YOUR_DOMAIN", result.message['domain'])

    def test_no_content(self):
        self.adyen.client = self.test.create_client_from_file(204, {},
                                                              "test/mocks/"
                                                              "management/"
                                                              "no_content.json")
        origin_id = 'YOUR_DOMAIN_ID'

        self.adyen.management.my_api_credential_api.remove_allowed_origin(origin_id)

        self.adyen.client.http_client.request.assert_called_once_with(
            'DELETE',
            f'{self.management_url}/me/allowedOrigins/{origin_id}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=None,
            xapikey="YourXapikey"
        )

    def test_update_store(self):
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
        store_id = "YOUR_STORE_ID"
        merchant_id = "YOUR_MERCHANT_ACCOUNT_ID"

        result = self.adyen.management.account_store_level_api.update_store(request, merchant_id, store_id)

        self.adyen.client.http_client.request.assert_called_once_with(
            'PATCH',
            f'{self.management_url}/merchants/{merchant_id}/stores/{store_id}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )
        self.assertEqual(store_id, result.message['id'])
        self.assertEqual("1776 West Pinewood Avenue", result.message['address']['line1'])

    def test_reassign_terminal(self):
        request = {
            'storeId': 'ST123ABC',
            'inventory': False,
        }
        self.adyen.client = self.test.create_client_from_file(200, request)

        result = self.adyen.management.terminals_terminal_level_api.reassign_terminal(request, 'AMS1-2345')

        self.assertEqual(200, result.status_code)
        self.assertEqual({}, result.message)
        self.assertEqual("", result.raw_response)

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
        company_id = "YOUR_COMPANY_ACCOUNT"

        result = self.adyen.management.users_company_level_api.create_new_user(request, company_id)

        self.assertEqual(request['name']['firstName'], result.message['name']['firstName'])
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'{self.management_url}/companies/{company_id}/users',
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
        company_id = "YOUR_COMPANY_ACCOUNT"

        result = self.adyen.management.android_files_company_level_api.list_android_apps(company_id)

        self.assertEqual("ANDA422LZ223223K5F694GCCF732K8", result.message['androidApps'][0]['id'])

    def test_query_parameters(self):
        request = {}
        company_id = "YOUR_COMPANY_ACCOUNT"
        query_parameters = {
            'pageNumber': 1,
            'pageSize': 10

        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "management/"
                                                              "get_list_of_merchant_accounts.json")

        self.adyen.management.account_company_level_api. \
            list_merchant_accounts(company_id, query_parameters=query_parameters)

        self.adyen.client.http_client.request.assert_called_once_with(
            'GET',
            f'{self.management_url}/companies/{company_id}/merchants?pageNumber=1&pageSize=10',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=None,
            xapikey="YourXapikey"
        )
