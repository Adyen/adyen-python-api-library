import Adyen
import unittest

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestCheckout(unittest.TestCase):
    adyen = Adyen.Adyen()

    client = adyen.client
    test = BaseTest(adyen)
    client.xapikey = "YourXapikey"
    client.platform = "test"

    def test_payment_methods_success_mocked(self):
        request = {'merchantAccount': "YourMerchantAccount"}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentmethods"
                                                              "-success.json")
        result = self.adyen.checkout.payment_methods(request)
        self.assertEqual("AliPay", result.message['paymentMethods'][0]['name'])
        self.assertEqual("Credit Card",
                         result.message['paymentMethods'][2]['name'])
        self.assertEqual("Credit Card via AsiaPay",
                         result.message['paymentMethods'][3]['name'])

    def test_payment_methods_error_mocked(self):
        request = {'merchantAccount': "YourMerchantAccount"}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentmethods-"
                                                              "error-forbidden"
                                                              "-403.json")
        result = self.adyen.checkout.payment_methods(request)
        self.assertEqual(403, result.message['status'])
        self.assertEqual("901", result.message['errorCode'])
        self.assertEqual("Invalid Merchant Account", result.message['message'])
        self.assertEqual("security", result.message['errorType'])

    def test_payments_success_mocked(self):
        request = {'amount': {"value": "100000", "currency": "EUR"},
                   'reference': "123456", 'paymentMethod': {
                "type": "scheme",
                "number": "4111111111111111",
                "expiryMonth": "08",
                "expiryYear": "2018",
                "holderName": "John Smith",
                "cvc": "737"
            }, 'merchantAccount': "YourMerchantAccount",
                   'returnUrl': "https://your-company.com/..."}

        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "payments"
                                                              "-success"
                                                              ".json")
        result = self.adyen.checkout.payments(request)
        self.assertEqual("8535296650153317", result.message['pspReference'])
        self.assertEqual("Authorised", result.message['resultCode'])
        self.assertEqual("8/2018",
                         result.message["additionalData"]['expiryDate'])
        self.assertEqual("GREEN",
                         result.message["additionalData"]['fraudResultType'])

    def test_payments_error_mocked(self):
        request = {'amount': {"value": "100000", "currency": "EUR"},
                   'reference': "54431", 'paymentMethod': {
                "type": "scheme",
                "number": "4111111111111111",
                "expiryMonth": "08",
                "expiryYear": "2018",
                "holderName": "John Smith",
                "cvc": "737"
            }, 'merchantAccount': "YourMerchantAccount",
                   'returnUrl': "https://your-company.com/..."}

        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "payments-error"
                                                              "-invalid"
                                                              "-data-422"
                                                              ".json")
        result = self.adyen.checkout.payments(request)

        self.adyen.client.http_client.request.assert_called_once_with(
            'https://checkout-test.adyen.com/v64/payments',
            headers={},
            json={
                'returnUrl': 'https://your-company.com/...',
                u'applicationInfo': {
                    u'adyenLibrary': {
                        u'version': '4.0.0',
                        u'name': 'adyen-python-api-library'
                    }
                },
                'reference': '54431',
                'merchantAccount': 'YourMerchantAccount',
                'amount': {'currency': 'EUR', 'value': '100000'},
                'paymentMethod': {
                    'expiryYear': '2018',
                    'holderName': 'John Smith',
                    'number': '4111111111111111',
                    'expiryMonth': '08',
                    'type': 'scheme',
                    'cvc': '737'
                }
            },
            xapikey='YourXapikey'
        )
        self.assertEqual(422, result.message['status'])
        self.assertEqual("130", result.message['errorCode'])
        self.assertEqual("Reference Missing", result.message['message'])
        self.assertEqual("validation", result.message['errorType'])

    def test_payments_details_success_mocked(self):
        request = {'paymentData': "Hee57361f99....", 'details': {
            "MD": "sdfsdfsdf...",
            "PaRes": "sdkfhskdjfsdf..."
        }}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentsdetails"
                                                              "-success.json")

        result = self.adyen.checkout.payments_details(request)

        self.adyen.client.http_client.request.assert_called_once_with(
            u'https://checkout-test.adyen.com/v64/payments/details',
            headers={},
            json={
                'paymentData': 'Hee57361f99....',
                u'merchantAccount': None,
                'details': {'MD': 'sdfsdfsdf...', 'PaRes': 'sdkfhskdjfsdf...'}
            },
            xapikey='YourXapikey'
        )
        self.assertEqual("8515232733321252", result.message['pspReference'])
        self.assertEqual("Authorised", result.message['resultCode'])
        self.assertEqual("true",
                         result.message['additionalData']['liabilityShift'])
        self.assertEqual("AUTHORISED",
                         result.message['additionalData']['refusalReasonRaw'])

    def test_payments_details_error_mocked(self):
        request = {'paymentData': "Hee57361f99....", 'details': {
            "MD": "sdfsdfsdf...",
            "PaRes": "sdkfhskdjfsdf..."
        }}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentsdetails"
                                                              "-error-invalid-"
                                                              "data-422.json")
        result = self.adyen.checkout.payments_details(request)
        self.assertEqual(422, result.message['status'])
        self.assertEqual("101", result.message['errorCode'])
        self.assertEqual("Invalid card number", result.message['message'])
        self.assertEqual("validation", result.message['errorType'])

    def test_payments_session_success_mocked(self):
        request = {"reference": "Your order number",
                   "shopperReference": "yourShopperId_IOfW3k9G2PvXFu2j",
                   "channel": "iOS",
                   "token": "TOKEN_YOU_GET_FROM_CHECKOUT_SDK",
                   "returnUrl": "app://", "countryCode": "NL",
                   "shopperLocale": "nl_NL",
                   "sessionValidity": "2017-04-06T13:09:13Z",
                   "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
                   'amount': {"value": "17408", "currency": "EUR"}}

        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentsession"
                                                              "-success.json")
        result = self.adyen.checkout.payment_session(request)
        self.assertIsNotNone(result.message['paymentSession'])

    def test_payments_session_error_mocked(self):
        request = {"reference": "Your wro order number",
                   "shopperReference": "yourShopperId_IOfW3k9G2PvXFu2j",
                   "channel": "iOS",
                   "token": "WRONG_TOKEN",
                   "returnUrl": "app://", "countryCode": "NL",
                   "shopperLocale": "nl_NL",
                   "sessionValidity": "2017-04-06T13:09:13Z",
                   "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
                   'amount': {"value": "17408", "currency": "EUR"}}

        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentsession"
                                                              "-error-invalid-"
                                                              "data-422.json")
        result = self.adyen.checkout.payment_session(request)
        self.assertEqual(422, result.message['status'])
        self.assertEqual("14_012", result.message['errorCode'])
        self.assertEqual("The provided SDK token could not be parsed.",
                         result.message['message'])
        self.assertEqual("validation", result.message['errorType'])

    def test_payments_result_success_mocked(self):
        request = {"payload": "VALUE_YOU_GET_FROM_CHECKOUT_SDK"}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentsresult"
                                                              "-success.json")
        result = self.adyen.checkout.payment_result(request)
        self.assertEqual("8535253563623704", result.message['pspReference'])
        self.assertEqual("Authorised", result.message['resultCode'])

    def test_payments_result_error_mocked(self):
        request = {"payload": "VALUE_YOU_GET_FROM_CHECKOUT_SDK"}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentsresult"
                                                              "-error-invalid-"
                                                              "data-payload-"
                                                              "422.json")
        result = self.adyen.checkout.payment_result(request)
        self.assertEqual(422, result.message['status'])
        self.assertEqual("14_018", result.message['errorCode'])
        self.assertEqual("Invalid payload provided", result.message['message'])
        self.assertEqual("validation", result.message['errorType'])
