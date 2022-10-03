from unittest import result
from requests import request
import Adyen
import unittest

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestManagement(unittest.TestCase):
    adyen = Adyen.Adyen()

    client = adyen.client
    test = BaseTest(adyen)
    client.platform = "test"
    client.xapikey = "YourXApiKey"

    def test_list_of_company_accounts(self):
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "management/"
                                                              "list_of_company"
                                                              "_accounts.json")
        result = self.adyen.management.get_list_of_company_accounts()
        self.assertEqual("YOUR_COMPANY_ACCOUNT", result.message['data'][0]['id'])

    def test_no_api_key(self):
        request = {''}
        self.adyen.client = self.test.create_client_from_file(401, request,
                                                              "test/mocks/"
                                                              "management/"
                                                              "unauthorized"
                                                              "401.json")

        self.assertRaisesRegexp(Adyen.AdyenAPIAuthenticationError,
                                "Unable to authenticate with Adyen's Servers."
                                " Please verify the credentials set with the"
                                " Adyen base class. Please reach out to your"
                                " Adyen Admin if the problem persists",
            self.adyen.management.get_list_of_company_accounts,
            request)
    
    def test_list_of_merchants_under_account(self):
        request = {}
        path_param="YOUR_COMPANY_ACCOUNT"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "management/"
                                                              "list_of_merchants"
                                                              "_under_company.json")
        result = self.adyen.management.get_list_of_merchant_accounts_under_company(path_param=path_param)
        self.assertEqual("YOUR_MERCHANT_ACCOUNT_1", result.message['data'][0]['id'])
                                                    
    def test_create_merchant_account(self):
        request = {
        "companyId": "YOUR_COMPANY_ACCOUNT",
        "legalEntityId": "YOUR_LEGAL_ENTITY_ID",
        "businessLineId": "YOUR_BUSINESS_LINE_ID",
        "description": "YOUR_DESCRIPTION",
        "reference": "YOUR_OWN_REFERENCE"
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                            "test/mocks/"
                                                            "management/"
                                                             "create_merchant"
                                                             "_account.json")
        result = self.adyen.management.create_merchant_account(request)
        self.assertEqual("YOUR_COMPANY_ACCOUNT",result.message['companyId'])

    def test_get_merchant_account(self):
        path_param = "YOUR_MERCHANT_ACCOUNT"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                            "test/mocks/"
                                                            "management/"
                                                            "get_merchant_"
                                                            "account.json")
        result = self.adyen.management.get_merchant_account(path_param=path_param)
        self.assertEqual("YOUR_MERCHANT_ACCOUNT", result.message['id'])

    def test_get_list_of_merchant_accounts(self):
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                            "test/mocks/"
                                                            "management/"
                                                            "list_of_"
                                                            "merchant_"
                                                            "accounts.json")
        result = self.adyen.management.get_list_of_merchant_accounts()
        self.assertEqual("YOUR_MERCHANT_ACCOUNT_1", result.message['data'][0]['id'])

    def test_get_list_of_stores_under_merchant_account(self):
        path_param = "YOUR_MERCHANT_ACCOUNT_ID"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                            "test/mocks/"
                                                            "management/"
                                                            "list_of_stores_"
                                                            "under_merchant_"
                                                            "account.json")
        result = self.adyen.management.get_list_of_stores_under_merchant_account(path_param=path_param)
        self.assertEqual("YOUR_MERCHANT_ACCOUNT_ID", result.message['data'][0]['merchantId'])
        self.assertEqual("ST322LJ223223K5F4SQNR9XL5", result.message['data'][0]['storeId'])
    

    def test_get_store_under_merchant_account(self):
        path_param = "YOUR_MERCHANT_ACCOUNT,YOUR_STORE"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                            "test/mocks/"
                                                            "management/"
                                                            "get_store_under_"
                                                            "merchant_account.json")
        result = self.adyen.management.get_store_under_merchant_account(path_param=path_param)
        self.assertEqual("ST322LJ223223K5F4SQNR9XL5", result.message["storeId"])

    def test_update_store_under_merchant_account(self):
        request = {
            "address": {
                "line1": "1776 West Pinewood Avenue",
                "line2": "Heartland Building",
                "line3": "",
                "postalCode": "20251"
            }
            }
        path_param = "YOUR_MERCHANT_ACCOUNT_ID,YOUR_STORE_ID"
        
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                            "test/mocks/"
                                                            "management/"
                                                            "update_store_under_"
                                                            "merchant_account.json")
        result = self.adyen.management.update_store_under_merchant_account(request, path_param=path_param)
        self.assertEqual("1776 West Pinewood Avenue", result.message["address"]["line1"])

    def test_get_list_of_stores(self):
        request = {}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                            "test/mocks/"
                                                            "management/"
                                                            "list_of_"
                                                            "stores.json")
        result = self.adyen.management.get_list_of_stores()
        self.assertEqual(2, result.message["itemsTotal"])
        self.assertEqual("ST322LJ223223K5F4SQNR9XL5", result.message["data"][0]["storeId"])

    def test_create_store(self):
        request = {
        "merchantId": "YOUR_MERCHANT_ACCOUNT_ID",
        "description": "City centre store",
        "shopperStatement": "Springfield Shop",
        "phoneNumber": "+1813702551707653",
        "reference": "Spring_store_2",
        "address": {
            "country": "US",
            "line1": "200 Main Street",
            "line2": "Building 5A",
            "line3": "Suite 3",
            "city": "Springfield",
            "stateOrProvince": "NY",
            "postalCode": "20250"}
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                            "test/mocks/"
                                                            "management/"
                                                            "create_store.json")
        result = self.adyen.management.create_store(request)
        self.assertEqual("YOUR_STORE_ID", result.message["id"])
                                    

    def test_get_store(self):
        path_param = "ST322LJ223223K5F4SQNR9XL5"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                            "test/mocks/"
                                                            "management/"
                                                            "get_store.json")
        result = self.adyen.management.get_store(path_param=path_param)
        self.assertEqual("ST322LJ223223K5F4SQNR9XL5", result.message["storeId"])

    def test_udpate_store(self):
        request = {
        "address": {
            "line1": "1776 West Pinewood Avenue",
            "line2": "Heartland Building",
            "line3": "",
            "postalCode": "20251"}
        }
        path_param = "YOUR_STORE_ID"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                            "test/mocks/"
                                                            "management/"
                                                            "update_store.json")
        result = self.adyen.management.update_store(request, path_param=path_param)
        self.assertEqual("YOUR_STORE_ID", result.message['id'])
        self.assertEqual("1776 West Pinewood Avenue", result.message['address']['line1'])
