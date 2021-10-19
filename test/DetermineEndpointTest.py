import Adyen
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

    def test_checkout_api_url_custom(self):
        self.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
        url = self.adyen.client._determine_checkout_url("live", "payments")
        self.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
        self.assertEqual(url, "https://1797a841fbb37ca7-AdyenDemo-checkout-"
                              "live.adyenpayments.com/checkout/v68/payments")

    def test_checkout_api_url(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_checkout_url("test",
                                                        "paymentsDetails")
        self.assertEqual(url, "https://checkout-test.adyen.com"
                              "/v68/payments/details")

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
            self.adyen.checkout.payments(request)
        except AdyenEndpointInvalidFormat as error:
            self.assertIsNotNone(error)

    def test_pal_url_live_endpoint_prefix_live_platform(self):
        self.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
        url = self.adyen.client._determine_api_url(
            "live", "Payment", "payments"
        )
        self.assertEqual(
            url,
            ("https://1797a841fbb37ca7-AdyenDemo-pal-"
             "live.adyenpayments.com/pal/servlet/Payment/v64/payments")
        )

    def test_pal_url_live_endpoint_prefix_test_platform(self):
        self.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
        url = self.adyen.client._determine_api_url(
            "test", "Payment", "payments"
        )
        self.assertEqual(
            url,
            "https://pal-test.adyen.com/pal/servlet/Payment/v64/payments"
        )

    def test_pal_url_no_live_endpoint_prefix_live_platform(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url(
            "live", "Payment", "payments"
        )
        self.assertEqual(
            url,
            "https://pal-live.adyen.com/pal/servlet/Payment/v64/payments"
        )

    def test_pal_url_no_live_endpoint_prefix_test_platform(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url(
            "test", "Payment", "payments"
        )
        self.assertEqual(
            url,
            "https://pal-test.adyen.com/pal/servlet/Payment/v64/payments"
        )

    def test_binlookup_url_no_live_endpoint_prefix_test_platform(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url(
            "test", "BinLookup", "get3dsAvailability"
        )
        self.assertEqual(
            url,
            ("https://pal-test.adyen.com/pal/servlet/"
             "BinLookup/v50/get3dsAvailability")
        )

    def test_checkout_api_url_orders(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_checkout_url("test",
                                                        "orders")
        self.assertEqual(url, "https://checkout-test.adyen.com"
                              "/v68/orders")

    def test_checkout_api_url_order_cancel(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_checkout_url("test",
                                                        "ordersCancel")
        self.assertEqual(url, "https://checkout-test.adyen.com"
                              "/v68/orders/cancel")

    def test_checkout_api_url_order_payment_methods_balance(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_checkout_url("test",
                                                        "paymentMethods"
                                                        "Balance")
        self.assertEqual(url, "https://checkout-test.adyen.com""/v68/"
                              "paymentMethods/balance")

    def test_checkout_api_url_sessions(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_checkout_url("test",
                                                        "sessions")
        self.assertEqual(url, "https://checkout-test.adyen.com""/v68/"
                              "sessions")
