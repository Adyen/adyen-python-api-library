import Adyen
import unittest
from BaseTest import BaseTest


class TestThirdPartyPayout(unittest.TestCase):
    ady = Adyen.Adyen()

    client = ady.client
    test = BaseTest(ady)
    client.username = "YourWSUser"
    client.password = "YourWSPassword"
    client.platform = "test"
    client.app_name = "appname"
    client.review_payout_username = "YourReviewPayoutUser"
    client.review_payout_password = "YourReviewPayoutPassword"
    client.store_payout_username = "YourStorePayoutUser"
    client.store_payout_password = "YourStorePayoutPassword"

    def test_store_detail_and_submit_success(self):
        request = {}
        request["amount"] = {
            "value": "100000",
            "currency": "EUR"
        }
        request["bank"] = {
            "bankName": "AbnAmro",
            "bic": "ABNANL2A",
            "countryCode": "NL",
            "iban": "NL32ABNA0515071439",
            "ownerName": "Adyen",
            "bankCity": "Amsterdam",
            "taxId": "bankTaxId"
        }
        request["merchantAccount"] = "YourMerchantAccount"
        request["recurring"] = {
            "contract": "PAYOUT"
        }
        request["reference"] = "YourReference"
        request["shopperEmail"] = "ref@email.com"
        request["shopperReference"] = "ref"
        request["shopperName"] = {
            "firstName": "Adyen",
            "gender": "MALE",
            "lastName": "Test"
        }
        request["dateOfBirth"] = "1990-01-01",
        request["entityType"] = "Company",
        request["nationality"] = "NL",
        request["billingAddress"] = {
            "houseNumberOrName": "17",
            "street": "Teststreet 1",
            "city": "Amsterdam",
            "stateOrProvince": "NY",
            "country": "US",
            "postalCode": "12345"
        }
        resp = 'test/mocks/payout/storeDetailAndSubmitThirdParty-success.json'
        self.ady.client = self.test.create_client_from_file(200, request, resp)
        result = self.ady.payout.store_detail_and_submit(request)
        self.assertIsNotNone(result.message['pspReference'])
        expected = "[payout-submit-received]"
        self.assertEqual(expected, result.message['resultCode'])


TestThirdPartyPayout.client.http_force = "requests"
suite = unittest.TestLoader().loadTestsFromTestCase(TestThirdPartyPayout)
unittest.TextTestRunner(verbosity=2).run(suite)
TestThirdPartyPayout.client.http_force = "pycurl"
TestThirdPartyPayout.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestThirdPartyPayout)
unittest.TextTestRunner(verbosity=2).run(suite)
TestThirdPartyPayout.client.http_force = "other"
TestThirdPartyPayout.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestThirdPartyPayout)
unittest.TextTestRunner(verbosity=2).run(suite)
