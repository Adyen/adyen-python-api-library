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
    checkout_version = settings.API_CHECKOUT_VERSION
    payment_version = settings.API_PAYMENT_VERSION
    binLookup_version = settings.API_BIN_LOOKUP_VERSION
    management_version = settings.API_MANAGEMENT_VERSION

    def test_checkout_api_url_custom(self):
        self.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
        url = self.adyen.client._determine_api_url("live", "checkout", "/payments")
        self.assertEqual("https://1797a841fbb37ca7-AdyenDemo-checkout-"
                         f"live.adyenpayments.com/checkout/{self.checkout_version}/payments", url)

    def test_checkout_api_url(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url("test", "checkout",
                                                   "/payments/details")
        self.assertEqual(url, "https://checkout-test.adyen.com"
                              f"/{self.checkout_version}/payments/details")

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
            "live", "payments", "/payments"
        )
        self.assertEqual(
            url,
            ("https://1797a841fbb37ca7-AdyenDemo-pal-"
             f"live.adyenpayments.com/pal/servlet/Payment/{self.payment_version}/payments")
        )

    def test_pal_url_live_endpoint_prefix_test_platform(self):
        self.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
        url = self.adyen.client._determine_api_url(
            "test", "payments", "/payments"
        )
        self.assertEqual(
            url,
            f"https://pal-test.adyen.com/pal/servlet/Payment/{self.payment_version}/payments")

    def test_pal_url_no_live_endpoint_prefix_test_platform(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url(
            "test", "payments", "/payments"
        )
        self.assertEqual(
            url,
            f"https://pal-test.adyen.com/pal/servlet/Payment/{self.payment_version}/payments")

    def test_binlookup_url_no_live_endpoint_prefix_test_platform(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url(
            "test", "binlookup", "/get3dsAvailability"
        )
        self.assertEqual(
            url,
            ("https://pal-test.adyen.com/pal/servlet/"
             f"BinLookup/{self.binLookup_version}/get3dsAvailability")
        )

    def test_checkout_api_url_orders(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url("test", "checkout",
                                                   "/orders")
        self.assertEqual(url, "https://checkout-test.adyen.com"
                              f"/{self.checkout_version}/orders")

    def test_checkout_api_url_order_cancel(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url("test", "checkout",
                                                   "/orders/cancel")
        self.assertEqual(url, "https://checkout-test.adyen.com"
                              f"/{self.checkout_version}/orders/cancel")

    def test_checkout_api_url_order_payment_methods_balance(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url("test", "checkout",
                                                   "/paymentMethods/"
                                                   "balance")
        self.assertEqual(url, f"https://checkout-test.adyen.com/{self.checkout_version}/"
                              "paymentMethods/balance")

    def test_checkout_api_url_sessions(self):
        self.client.live_endpoint_prefix = None
        url = self.adyen.client._determine_api_url("test", "checkout",
                                                   "/sessions")
        self.assertEqual(url, f"https://checkout-test.adyen.com/{self.checkout_version}/"
                              "sessions")

    def test_management_api_url_companies(self):
        companyId = "YOUR_COMPANY_ID"
        url = self.adyen.client._determine_api_url("test", "management", f'/companies/{companyId}/users')
        self.assertEqual(url, f"https://management-test.adyen.com/{self.management_version}/"
                              "companies/YOUR_COMPANY_ID/users")
