import os
import re
import unittest
from unittest import mock

import Adyen
from Adyen.exceptions import AdyenInvalidRequestError
from Adyen.services.base import AdyenServiceBase


class TestPathParameterEncoding(unittest.TestCase):
    def setUp(self):
        self.adyen = Adyen.Adyen()
        self.adyen.client.xapikey = "YourXapikey"
        self.adyen.client.platform = "test"
        self.adyen.client._init_http_client()
        self.adyen.client.http_init = True
        self.http_request = mock.MagicMock(return_value=["{}", {}, 200, {}])
        self.adyen.client.http_client.request = self.http_request

    def requested_url(self):
        return self.http_request.call_args.args[1]

    def test_ordinary_ids_are_unchanged(self):
        self.adyen.checkout.payment_links_api.get_payment_link("PL61C53A8B97E6915A")
        self.assertEqual(
            "https://checkout-test.adyen.com/v72/paymentLinks/PL61C53A8B97E6915A",
            self.requested_url(),
        )

    def test_query_and_fragment_delimiters_stay_in_the_path_segment(self):
        self.adyen.checkout.recurring_api.delete_token_for_stored_payment_details(
            "RL8FW7WZM6KXWD82?shopperReference=other-shopper#",
            query_parameters={
                "merchantAccount": "TestMerchantAccount",
                "shopperReference": "test-1234",
            },
        )
        self.assertEqual(
            "https://checkout-test.adyen.com/v72/storedPaymentMethods/"
            "RL8FW7WZM6KXWD82%3FshopperReference%3Dother-shopper%23"
            "?merchantAccount=TestMerchantAccount&shopperReference=test-1234",
            self.requested_url(),
        )

    def test_slashes_stay_in_the_path_segment(self):
        self.adyen.management.users_merchant_level_api.get_user_details(
            "TestMerchantAccount", "../apiCredentials/S2-123"
        )
        self.assertEqual(
            "https://management-test.adyen.com/v3/merchants/TestMerchantAccount/users/"
            "..%2FapiCredentials%2FS2-123",
            self.requested_url(),
        )

    def test_every_path_parameter_is_encoded(self):
        self.adyen.management.users_merchant_level_api.get_user_details("Test/Merchant", "user 1")
        self.assertEqual(
            "https://management-test.adyen.com/v3/merchants/Test%2FMerchant/users/user%201",
            self.requested_url(),
        )

    def test_dot_segments_are_rejected_before_sending(self):
        for value in (".", ".."):
            with self.subTest(value=value), self.assertRaises(AdyenInvalidRequestError):
                self.adyen.checkout.payment_links_api.get_payment_link(value)
        self.http_request.assert_not_called()

    def test_reserved_and_non_ascii_characters_are_encoded(self):
        self.assertEqual(
            "/stores/a%252Fb%20c%2B%C3%A9",
            AdyenServiceBase._build_path("/stores/{storeId}", storeId="a%2Fb c+é"),
        )

    def test_non_string_values_are_converted(self):
        self.assertEqual("/items/42", AdyenServiceBase._build_path("/items/{id}", id=42))

    def test_generated_services_do_not_interpolate_path_parameters(self):
        services_dir = os.path.join(os.path.dirname(Adyen.__file__), "services")
        unencoded = []
        for root, _, files in os.walk(services_dir):
            for name in sorted(files):
                if not name.endswith(".py"):
                    continue
                with open(os.path.join(root, name), encoding="utf-8") as source:
                    for match in re.finditer(
                        r'self\.baseUrl\s*\+\s*f"[^"]*\{[^"]*"', source.read()
                    ):
                        unencoded.append(f"{name}: {' '.join(match.group(0).split())}")
        self.assertEqual([], unencoded)
