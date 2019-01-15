import Adyen
import unittest
from BaseTest import BaseTest

from Adyen.exceptions import AdyenEndpointInvalidFormat


class TestDetermineUrl(unittest.TestCase):
    adyen = Adyen.Adyen()

    client = adyen.client
    test = BaseTest(adyen)
    client.xapikey = "YourXapikey"
    client.app_name = "appname"

    def test_checkout_api_url_custom(self):
        self.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
        url = self.adyen.client._determine_checkout_url("live", "",
                                                        "payments")
        self.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
        self.assertEqual(url, "https://1797a841fbb37ca7-AdyenDemo-checkout-"
                              "live.adyenpayments.com/checkout/v40/payments")

    def test_payments_invalid_platform(self):

        request = {'amount': {"value": "100000", "currency": "EUR"},
                   "reference": "Your order number",
                   'paymentMethod': {
                       "type": "scheme",
                       "number": "4111111111111111",
                       "expiryMonth": "08",
                       "expiryYear": "2018",
                       "holderName": "John Smith",
                       "cvc": "737"
                   }, 'merchantAccount': "YourMerchantAccount",
                   'returnUrl': "https://your-company.com/..."}

        self.client.platform = "test"
        try:
            result = self.adyen.checkout.payments(request)
        except AdyenEndpointInvalidFormat as error:
            print("the error" + str(error.__class__.__name__))
            self.assertIsNotNone("dfasdf")

    def test_checkout_api_url(self):

        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_checkout_url("test", "",
                                                        "paymentsDetails")
        self.assertEqual(url, "https://checkout-test.adyen.com"
                              "/v40/payments/details")
