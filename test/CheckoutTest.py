import Adyen
import unittest
from BaseTest import BaseTest
import pprint


class TestCheckout(unittest.TestCase):
    ady = Adyen.Adyen()

    client = ady.client
    test = BaseTest(ady)
    client.xapikey = "YourXapikey"
    client.platform = "test"
    client.app_name = "appname"

    def test_payment_methods_success_mocked(self):
        request = {'merchantAccount': "YourMerchantAccount"}
        file = "test/mocks/checkout/paymentmethods-success.json"
        self.ady.client = self.test.create_client_from_file(200, request,
                                                            file)
        result = self.ady.checkout.payment_methods(request)
        self.assertEqual("AliPay", result.message['paymentMethods'][0]['name'])
        self.assertEqual("Credit Card", result.message['paymentMethods'][2]['name'])
        self.assertEqual("Credit Card via AsiaPay", result.message['paymentMethods'][3]['name'])
