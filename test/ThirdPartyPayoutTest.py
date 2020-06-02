import Adyen
import unittest

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestThirdPartyPayout(unittest.TestCase):
    ady = Adyen.Adyen()

    client = ady.client
    test = BaseTest(ady)
    client.username = "YourWSUser"
    client.password = "YourWSPassword"
    client.platform = "test"
    client.review_payout_username = "YourReviewPayoutUser"
    client.review_payout_password = "YourReviewPayoutPassword"
    client.store_payout_username = "YourStorePayoutUser"
    client.store_payout_password = "YourStorePayoutPassword"

    def test_confirm_success(self):
        request = {
            "merchantAccount": "YourMerchantAccount",
            "originalReference": "YourReference"
        }
        resp = 'test/mocks/payout/confirm-success.json'
        self.ady.client = self.test.create_client_from_file(200, request, resp)
        result = self.ady.payout.confirm(request)
        self.assertIsNotNone(result.message['pspReference'])
        expected = "[payout-confirm-received]"
        self.assertEqual(expected, result.message['resultCode'])

    def test_confirm_missing_reference(self):
        request = {
            "merchantAccount": "YourMerchantAccount",
            "originalReference": ""
        }
        resp = 'test/mocks/payout/confirm-missing-reference.json'
        self.ady.client = self.test.create_client_from_file(500, request, resp)
        self.assertRaisesRegexp(
            Adyen.AdyenAPIValidationError,
            "Received validation error with errorCode: 702,"
            " message: Required field 'merchantAccount' is null,"
            " HTTP Code: 500. Please verify the values provided.",
            self.ady.payout.confirm,
            request
        )

    def test_decline_success(self):
        request = {
            "merchantAccount": "YourMerchantAccount",
            "originalReference": "YourReference"
        }
        resp = 'test/mocks/payout/decline-success.json'
        self.ady.client = self.test.create_client_from_file(200, request, resp)
        result = self.ady.payout.confirm(request)
        self.assertIsNotNone(result.message['pspReference'])
        expected = "[payout-decline-received]"
        self.assertEqual(expected, result.message['resultCode'])

    def test_decline_missing_reference(self):
        request = {
            "merchantAccount": "YourMerchantAccount",
            "originalReference": ""
        }
        resp = 'test/mocks/payout/decline-missing-reference.json'
        self.ady.client = self.test.create_client_from_file(500, request, resp)
        self.assertRaisesRegexp(
            Adyen.AdyenAPIValidationError,
            "Received validation error with errorCode: 702,"
            " message: Required field 'merchantAccount' is null,"
            " HTTP Code: 500. Please verify the values provided.",
            self.ady.payout.confirm,
            request
        )

    def test_store_detail_bank_success(self):
        request = {
            "bank": {
                "bankName": "AbnAmro",
                "bic": "ABNANL2A",
                "countryCode": "NL",
                "iban": "NL32ABNA0515071439",
                "ownerName": "Adyen",
                "bankCity": "Amsterdam",
                "taxId": "bankTaxId"
            },
            "merchantAccount": "YourMerchantAccount",
            "recurring": {
                "contract": "PAYOUT"
            },
            "shopperEmail": "ref@email.com",
            "shopperReference": "ref"
        }
        resp = 'test/mocks/payout/storeDetail-success.json'
        self.ady.client = self.test.create_client_from_file(200, request, resp)
        result = self.ady.payout.store_detail(request)
        self.assertIsNotNone(result.message['pspReference'])
        self.assertIsNotNone(result.message['recurringDetailReference'])
        expected = "Success"
        self.assertEqual(expected, result.message['resultCode'])

    def test_submit_success(self):
        request = {
            "amount": {
                "value": "100000",
                "currency": "EUR"
            },
            "reference": "payout-test", "recurring": {
                "contract": "PAYOUT"
            },
            "merchantAccount": "YourMerchantAccount",
            "shopperEmail": "ref@email.com",
            "shopperReference": "ref",
            "selectedRecurringDetailReference": "LATEST"
        }
        resp = 'test/mocks/payout/submit-success.json'
        self.ady.client = self.test.create_client_from_file(200, request, resp)
        result = self.ady.payout.submit(request)
        self.assertIsNotNone(result.message['pspReference'])
        expected = "[payout-submit-received]"
        self.assertEqual(expected, result.message['resultCode'])

    def test_submit_invalid_recurring_reference(self):
        request = {
            "amount": {
                "value": "100000",
                "currency": "EUR"
            },
            "reference": "payout-test", "recurring": {
                "contract": "PAYOUT"
            },
            "merchantAccount": "YourMerchantAccount",
            "shopperEmail": "ref@email.com",
            "shopperReference": "ref",
            "selectedRecurringDetailReference": "1234"
        }
        resp = 'test/mocks/payout/submit-invalid-reference.json'
        self.ady.client = self.test.create_client_from_file(422, request, resp)
        self.assertRaisesRegexp(
            Adyen.AdyenAPICommunicationError,
            "Unexpected error",
            self.ady.payout.submit,
            request
        )

    def test_store_detail_and_submit_missing_reference(self):
        request = {
            "amount": {
                "value": "100000",
                "currency": "EUR"
            },
            "merchantAccount": "YourMerchantAccount",
            "recurring": {
                "contract": "PAYOUT"
            },
            "shopperEmail": "ref@email.com",
            "shopperReference": "ref",
            "bank": {
                "iban": "NL32ABNA0515071439",
                "ownerName": "Adyen",
                "countryCode": "NL",
            }
        }

        resp = 'test/mocks/payout/submit-missing-reference.json'
        self.ady.client = self.test.create_client_from_file(422, request, resp)

        self.assertRaisesRegexp(
            Adyen.AdyenAPICommunicationError,
            "Unexpected error",
            self.ady.payout.store_detail_and_submit,
            request
        )

    def test_store_detail_and_submit_missing_payment(self):
        request = {
            "amount": {
                "value": "100000",
                "currency": "EUR"
            },
            "merchantAccount": "YourMerchantAccount",
            "reference": "payout-test",
            "recurring": {
                "contract": "PAYOUT"
            },
            "shopperEmail": "ref@email.com",
            "shopperReference": "ref"
        }
        resp = 'test/mocks/payout/storeDetailAndSubmit-missing-payment.json'
        self.ady.client = self.test.create_client_from_file(422, request, resp)
        self.assertRaisesRegexp(
            Adyen.AdyenAPICommunicationError,
            "Unexpected error",
            self.ady.payout.store_detail_and_submit,
            request
        )

    def test_store_detail_and_submit_invalid_iban(self):
        request = {
            "amount": {
                "value": "100000",
                "currency": "EUR"
            },
            "merchantAccount": "YourMerchantAccount",
            "reference": "payout-test",
            "recurring": {
                "contract": "PAYOUT"
            },
            "shopperEmail": "ref@email.com",
            "shopperReference": "ref",
            "bank": {
                "countryCode": "NL",
                "iban": "4111111111111111",
                "ownerName": "Adyen",
            }
        }
        resp = 'test/mocks/payout/storeDetailAndSubmit-invalid-iban.json'
        self.ady.client = self.test.create_client_from_file(422, request, resp)
        self.assertRaisesRegexp(
            Adyen.AdyenAPICommunicationError,
            "Unexpected error",
            self.ady.payout.store_detail_and_submit,
            request
        )

    def test_store_detail_and_submit_card_success(self):
        request = {
            "amount": {
                "value": "100000",
                "currency": "EUR"
            },
            "merchantAccount": "YourMerchantAccount",
            "reference": "payout-test",
            "recurring": {
                "contract": "PAYOUT"
            },
            "shopperEmail": "ref@email.com",
            "shopperReference": "ref",
            "card": {
                "number": "4111111111111111",
                "expiryMonth": "08",
                "expiryYear": "2018",
                "cvc": "737",
                "holderName": "John Smith"
            }
        }
        resp = 'test/mocks/payout/storeDetailAndSubmit-card-success.json'
        self.ady.client = self.test.create_client_from_file(200, request, resp)
        result = self.ady.payout.store_detail_and_submit(request)
        self.assertIsNotNone(result.message['pspReference'])
        expected = "[payout-submit-received]"
        self.assertEqual(expected, result.message['resultCode'])

    def test_store_detail_and_submit_bank_success(self):
        request = {
            "amount": {
                "value": "100000",
                "currency": "EUR"
            },
            "bank": {
                "countryCode": "NL",
                "iban": "NL32ABNA0515071439",
                "ownerName": "Adyen",
            },
            "merchantAccount": "YourMerchantAccount",
            "recurring": {
                "contract": "PAYOUT"
            },
            "reference": "YourReference",
            "shopperEmail": "ref@email.com",
            "shopperReference": "ref"
        }
        resp = 'test/mocks/payout/storeDetailAndSubmit-bank-success.json'
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
