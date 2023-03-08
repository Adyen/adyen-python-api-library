import unittest
from Adyen import checkout


class TestClassicCheckoutSDKApi(unittest.TestCase):
    client = checkout.classic_checkout_sdk_api

    def test_payment_session(self):
        self.assertIsNotNone(self.client.payment_session)

    def test_verify_payment_result(self):
        self.assertIsNotNone(self.client.verify_payment_result)


class TestModificationsApi(unittest.TestCase):
    client = checkout.modifications_api

    def test_cancel_authorised_payment(self):
        self.assertIsNotNone(self.client.cancel_authorised_payment)

    def test_update_authorised_amount(self):
        self.assertIsNotNone(self.client.update_authorised_amount)

    def test_cancel_authorised_payment_by_psp_reference(self):
        self.assertIsNotNone(self.client.cancel_authorised_payment_by_psp_reference)

    def test_capture_authorised_payment(self):
        self.assertIsNotNone(self.client.capture_authorised_payment)

    def test_refund_captured_payment(self):
        self.assertIsNotNone(self.client.refund_captured_payment)

    def test_refund_or_cancel_payment(self):
        self.assertIsNotNone(self.client.refund_or_cancel_payment)


class TestOrdersApi(unittest.TestCase):
    client = checkout.orders_api

    def test_orders(self):
        self.assertIsNotNone(self.client.orders)

    def test_cancel_order(self):
        self.assertIsNotNone(self.client.cancel_order)

    def test_get_balance_of_gift_card(self):
        self.assertIsNotNone(self.client.get_balance_of_gift_card)


class TestPaymentLinksApi(unittest.TestCase):
    client = checkout.payment_links_api

    def test_get_payment_link(self):
        self.assertIsNotNone(self.client.get_payment_link)

    def test_update_payment_link(self):
        self.assertIsNotNone(self.client.update_payment_link)

    def test_payment_links(self):
        self.assertIsNotNone(self.client.payment_links)


class TestPaymentsApi(unittest.TestCase):
    client = checkout.payments_api

    def test_card_details(self):
        self.assertIsNotNone(self.client.card_details)

    def test_donations(self):
        self.assertIsNotNone(self.client.donations)

    def test_payment_methods(self):
        self.assertIsNotNone(self.client.payment_methods)

    def test_payments(self):
        self.assertIsNotNone(self.client.payments)

    def test_payments_details(self):
        self.assertIsNotNone(self.client.payments_details)

    def test_sessions(self):
        self.assertIsNotNone(self.client.sessions)


class TestRecurringApi(unittest.TestCase):
    client = checkout.recurring_api

    def test_delete_token_for_stored_payment_details(self):
        self.assertIsNotNone(self.client.delete_token_for_stored_payment_details)

    def test_get_tokens_for_stored_payment_details(self):
        self.assertIsNotNone(self.client.get_tokens_for_stored_payment_details)


class TestUtilityApi(unittest.TestCase):
    client = checkout.utility_api

    def test_get_apple_pay_session(self):
        self.assertIsNotNone(self.client.get_apple_pay_session)

    def test_origin_keys(self):
        self.assertIsNotNone(self.client.origin_keys)


