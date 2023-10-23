import Adyen
from Adyen import settings
import unittest

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest

from Adyen.exceptions import AdyenEndpointInvalidFormat


class TestDetermineUrl(unittest.TestCase):
    adyen = Adyen.Adyen()

    client = adyen.client
    test = BaseTest(adyen)
    client.xapikey = "YourXapikey"
    checkout_url = adyen.checkout.classic_checkout_sdk_api.baseUrl
    checkout_version = checkout_url.split('/')[-1]
    payment_url = adyen.payment.payments_api.baseUrl
    payment_version = payment_url.split('/')[-1]
    binlookup_url = adyen.binlookup.baseUrl
    management_url = adyen.management.account_merchant_level_api.baseUrl

    def test_checkout_api_url_custom(self):
        self.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
        url = self.adyen.client._determine_api_url("live", self.checkout_url + "/payments")
        self.assertEqual("https://1797a841fbb37ca7-AdyenDemo-checkout-"
                         f"live.adyenpayments.com/checkout/{self.checkout_version}/payments", url)

    def test_checkout_api_url(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url("test", self.checkout_url + "/payments/details")
        self.assertEqual(url, f"{self.checkout_url}/payments/details")

    def test_payments_invalid_platform(self):

        request = {
            'amount': {"value": "100000", "currency": "EUR"},
            "reference": "Your order number",
            'paymentMethod': {
                "type": "scheme",
                "number": "4111111111111111",
                "expiryMonth": "08",
                "expiryYear": "2018",
                "holderName": "John Smith",
                "cvc": "737"
            },
            'merchantAccount': "YourMerchantAccount",
            'returnUrl': "https://your-company.com/..."
        }

        self.client.platform = "live"
        self.client.live_endpoint_prefix = None

        try:
            self.adyen.checkout.payments_api.sessions(request)
        except AdyenEndpointInvalidFormat as error:
            self.assertIsNotNone(error)

    def test_pal_url_live_endpoint_prefix_live_platform(self):
        self.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
        url = self.adyen.client._determine_api_url(
            "live", self.payment_url + "/payments"
        )
        self.assertEqual(
            url,
            ("https://1797a841fbb37ca7-AdyenDemo-pal-"
             f"live.adyenpayments.com/pal/servlet/Payment/{self.payment_version}/payments")
        )

    def test_pal_url_live_endpoint_prefix_test_platform(self):
        self.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
        url = self.adyen.client._determine_api_url(
            "test", self.payment_url + "/payments"
        )
        self.assertEqual(
            url,
            f"{self.payment_url}/payments")

    def test_pal_url_no_live_endpoint_prefix_test_platform(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url(
            "test", self.payment_url + "/payments"
        )
        self.assertEqual(
            url,
            f"{self.payment_url}/payments")

    def test_binlookup_url_no_live_endpoint_prefix_test_platform(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url(
            "test", self.binlookup_url + "/get3dsAvailability"
        )
        self.assertEqual(
            url,
            f"{self.binlookup_url}/get3dsAvailability"
        )

    def test_checkout_api_url_orders(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url("test", self.checkout_url +
                                                   "/orders")
        self.assertEqual(url, f"{self.checkout_url}/orders")

    def test_checkout_api_url_order_cancel(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url("test", self.checkout_url + "/orders/cancel")
        self.assertEqual(url, f"{self.checkout_url}/orders/cancel")

    def test_checkout_api_url_order_payment_methods_balance(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url("test", self.checkout_url + "/paymentMethods/balance")
        self.assertEqual(url, f"{self.checkout_url}/paymentMethods/balance")

    def test_checkout_api_url_sessions(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url("test", self.checkout_url + "/sessions")
        self.assertEqual(url, f"{self.checkout_url}/sessions")

    def test_management_api_url_companies(self):
        companyId = "YOUR_COMPANY_ID"
        url = self.adyen.client._determine_api_url("test", self.management_url + f'/companies/{companyId}/users')
        self.assertEqual(url, f"{self.management_url}/companies/{companyId}/users")
