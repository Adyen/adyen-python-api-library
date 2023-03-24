import Adyen
import unittest
from Adyen import settings

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
    checkout_version = settings.API_CHECKOUT_VERSION
    lib_version = settings.LIB_VERSION

    def test_payment_methods_success_mocked(self):
        request = {'merchantAccount': "YourMerchantAccount"}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentmethods"
                                                              "-success.json")
        result = self.adyen.checkout.payments_api.payment_methods(request)
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
        result = self.adyen.checkout.payments_api.payment_methods(request)
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
        result = self.adyen.checkout.payments_api.payments(request)
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
        result = self.adyen.checkout.payments_api.payments(request)

        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            'https://checkout-test.adyen.com/{}/payments'.format(self.checkout_version),
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json={
                'returnUrl': 'https://your-company.com/...',
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

        result = self.adyen.checkout.payments_api.payments_details(request)

        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            u'https://checkout-test.adyen.com/{}/payments/details'.format(self.checkout_version),
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json={
                'paymentData': 'Hee57361f99....',
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
        result = self.adyen.checkout.payments_api.payments_details(request)
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
        result = self.adyen.checkout.classic_checkout_sdk_api.payment_session(request)
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
        result = self.adyen.checkout.classic_checkout_sdk_api.payment_session(request)
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
        result = self.adyen.checkout.classic_checkout_sdk_api.verify_payment_result(request)
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
        result = self.adyen.checkout.classic_checkout_sdk_api.verify_payment_result(request)
        self.assertEqual(422, result.message['status'])
        self.assertEqual("14_018", result.message['errorCode'])
        self.assertEqual("Invalid payload provided", result.message['message'])
        self.assertEqual("validation", result.message['errorType'])

    def test_payments_cancels_without_reference(self):
        requests = {
            "paymentReference": "Payment123",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "reference": "YourCancelReference",
        }
        self.adyen.client = self.test.create_client_from_file(200, requests,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentscancel-"
                                                              "withoutreference-succes.json")
        results = self.adyen.checkout.modifications_api.cancel_authorised_payment(requests)
        self.assertIsNotNone(results.message['paymentReference'])
        self.assertEqual("8412534564722331", results.message['pspReference'])
        self.assertEqual("received", results.message['status'])

    def test_payments_cancels_without_reference_error_mocked(self):
        requests = {
            "paymentReference": "Payment123",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "reference": "YourCancelReference",
        }
        self.adyen.client = self.test.create_client_from_file(200, requests,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentsresult"
                                                              "-error-invalid-"
                                                              "data-payload-"
                                                              "422.json")

        result = self.adyen.checkout.modifications_api.cancel_authorised_payment(requests)
        self.assertEqual(422, result.message['status'])
        self.assertEqual("14_018", result.message['errorCode'])
        self.assertEqual("Invalid payload provided", result.message['message'])
        self.assertEqual("validation", result.message['errorType'])

    def test_payments_cancels_success_mocked(self):
        requests = {"reference": "Your wro order number", "merchantAccount": "YOUR_MERCHANT_ACCOUNT"}

        reference_id = "8836183819713023"
        self.adyen.client = self.test.create_client_from_file(200, requests,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentscancels"
                                                              "-success.json")
        result = self.adyen.checkout.modifications_api.refund_or_cancel_payment(requests, reference_id)
        self.assertEqual(reference_id, result.message["paymentPspReference"])
        self.assertEqual("received", result.message['status'])

    def test_payments_cancels_error_mocked(self):
        request = {"reference": "Your wro order number"}
        psp_reference = "8836183819713023"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentsresult-error-invalid-"
                                                              "data-payload-422.json")
        result = self.adyen.checkout.modifications_api.refund_or_cancel_payment(request, psp_reference)
        self.assertEqual(422, result.message['status'])
        self.assertEqual("14_018", result.message['errorCode'])
        self.assertEqual("Invalid payload provided", result.message['message'])
        self.assertEqual("validation", result.message['errorType'])

    def test_payments_refunds_success_mocked(self):
        requests = {
            "paymentReference": "Payment123",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "reference": "YourCancelReference",
        }
        psp_reference = "Payment123"
        self.adyen.client = self.test.create_client_from_file(200, requests,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentscancel-"
                                                              "withoutreference-succes.json")

        result = self.adyen.checkout.modifications_api.refund_captured_payment(requests,psp_reference)
        self.assertEqual(psp_reference, result.message["paymentReference"])
        self.assertIsNotNone(result.message["pspReference"])
        self.assertEqual("received", result.message['status'])

    def test_payments_refunds_error_mocked(self):
        requests = {
            "paymentReference": "Payment123",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "reference": "YourCancelReference",
        }
        reference_id = "Payment123"
        self.adyen.client = self.test.create_client_from_file(200, requests,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentsresult-error-invalid-"
                                                              "data-payload-422.json")

        result = self.adyen.checkout.modifications_api.refund_captured_payment(requests, reference_id)
        self.assertEqual(422, result.message['status'])
        self.assertEqual("14_018", result.message['errorCode'])
        self.assertEqual("Invalid payload provided", result.message['message'])
        self.assertEqual("validation", result.message['errorType'])

    def test_reversals_success_mocked(self):
        requests = {
            "reference": "YourReversalReference",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
        }
        psp_reference = "8836183819713023"
        self.adyen.client = self.test.create_client_from_file(200, requests,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentsreversals-"
                                                              "success.json")

        result = self.adyen.checkout.modifications_api.refund_or_cancel_payment(requests, psp_reference)
        self.assertEqual(psp_reference, result.message["paymentPspReference"])
        self.assertIsNotNone(result.message["pspReference"])
        self.assertEqual("received", result.message['status'])

    def test_payments_reversals_failure_mocked(self):
        requests = {
            "reference": "YourReversalReference",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
        }
        psp_reference = "8836183819713023"

        self.adyen.client = self.test.create_client_from_file(200, requests,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentsresult-error-invalid-"
                                                              "data-payload-422.json")

        result = self.adyen.checkout.modifications_api.refund_or_cancel_payment(requests,psp_reference)
        self.assertEqual(422, result.message['status'])
        self.assertEqual("14_018", result.message['errorCode'])
        self.assertEqual("Invalid payload provided", result.message['message'])
        self.assertEqual("validation", result.message['errorType'])

    def test_payments_capture_success_mocked(self):
        request = {
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "amount": {
                "value": 2500,
                "currency": "EUR"
            },
            "reference": "YOUR_UNIQUE_REFERENCE"
        }
        psp_reference = "8536214160615591"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentcapture-"
                                                              "success.json")

        result = self.adyen.checkout.modifications_api.capture_authorised_payment(request, psp_reference)
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://checkout-test.adyen.com/{self.checkout_version}/payments/{psp_reference}/captures',
            json=request,
            xapikey='YourXapikey',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
        )
        self.assertEqual(psp_reference, result.message["paymentPspReference"])
        self.assertIsNotNone(result.message["pspReference"])
        self.assertEqual("received", result.message['status'])
        self.assertEqual(2500, result.message['amount']['value'])

    def test_payments_capture_error_mocked(self):
        request = {
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "amount": {
                "value": 2500,
                "currency": "EUR"
            },
            "reference": "YOUR_UNIQUE_REFERENCE"
        }
        psp_reference = "8536214160615591"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentsresult-error-invalid-"
                                                              "data-payload-422.json")

        result = self.adyen.checkout.modifications_api.capture_authorised_payment(request, psp_reference)
        self.assertEqual(422, result.message['status'])
        self.assertEqual("14_018", result.message['errorCode'])
        self.assertEqual("Invalid payload provided", result.message['message'])
        self.assertEqual("validation", result.message['errorType'])

    def test_orders_success(self):
        request = {'merchantAccount': "YourMerchantAccount"}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "orders"
                                                              "-success.json")
        result = self.adyen.checkout.orders_api.orders(request)
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://checkout-test.adyen.com/{self.checkout_version}/orders',
            json=request,
            xapikey='YourXapikey',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},

        )
        self.assertEqual("8515930288670953", result.message['pspReference'])
        self.assertEqual("Success", result.message['resultCode'])
        self.assertEqual("order reference", result.message['reference'])
        self.assertEqual("EUR", result.message['remainingAmount']["currency"])
        self.assertEqual(2500, result.message['remainingAmount']['value'])

    def test_orders_cancel_success(self):
        request = {'merchantAccount': "YourMerchantAccount"}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "orders-cancel"
                                                              "-success.json")
        result = self.adyen.checkout.orders_api.cancel_order(request)
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://checkout-test.adyen.com/{self.checkout_version}/orders/cancel',
            json=request,
            xapikey='YourXapikey',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
        )
        self.assertEqual("8515931182066678", result.message['pspReference'])
        self.assertEqual("Received", result.message['resultCode'])

    def test_paymentmethods_balance_success(self):
        request = {'merchantAccount': "YourMerchantAccount"}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentmethods"
                                                              "-balance"
                                                              "-success.json")
        result = self.adyen.checkout.orders_api.get_balance_of_gift_card(request)
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://checkout-test.adyen.com/{self.checkout_version}/paymentMethods/balance',
            json=request,
            xapikey='YourXapikey',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
        )
        self.assertEqual("851611111111713K", result.message['pspReference'])
        self.assertEqual("Success", result.message['resultCode'])
        self.assertEqual(100, result.message['balance']['value'])
        self.assertEqual("EUR", result.message['balance']['currency'])

    def test_sessions_success(self):
        request = {'merchantAccount': "YourMerchantAccount"}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "sessions"
                                                              "-success.json")
        result = self.adyen.checkout.payments_api.sessions(request)

        self.assertEqual("session-test-id", result.message['id'])
        self.assertEqual("TestReference", result.message['reference'])
        self.assertEqual("http://test-url.com", result.message['returnUrl'])

    def test_sessions_error(self):
        request = {'merchantAccount': "YourMerchantAccount"}
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "sessions"
                                                              "-error"
                                                              "-invalid"
                                                              "-data-422"
                                                              ".json")
        result = self.adyen.checkout.payments_api.sessions(request)
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://checkout-test.adyen.com/{self.checkout_version}/sessions',
            json={'merchantAccount': 'YourMerchantAccount'},
            xapikey='YourXapikey',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
        )
        self.assertEqual(422, result.message['status'])
        self.assertEqual("130", result.message['errorCode'])
        self.assertEqual("validation", result.message['errorType'])

    def test_payment_link(self):
        request = {
            "reference": "YOUR_ORDER_NUMBER",
            "amount": {
                "value": 1250,
                "currency": "BRL"
            },
            "countryCode": "BR",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "shopperReference": "YOUR_UNIQUE_SHOPPER_ID",
            "shopperEmail": "test@email.com",
            "shopperLocale": "pt-BR",
            "billingAddress": {
                "street": "Roque Petroni Jr",
                "postalCode": "59000060",
                "city": "São Paulo",
                "houseNumberOrName": "999",
                "country": "BR",
                "stateOrProvince": "SP"
            },
            "deliveryAddress": {
                "street": "Roque Petroni Jr",
                "postalCode": "59000060",
                "city": "São Paulo",
                "houseNumberOrName": "999",
                "country": "BR",
                "stateOrProvince": "SP"
            }
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentlinks"
                                                              "-success"
                                                              ".json")
        result = self.adyen.checkout.payment_links_api.payment_links(request)
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://checkout-test.adyen.com/{self.checkout_version}/paymentLinks',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            xapikey='YourXapikey',
            json=request
        )
        self.assertEqual("YOUR_ORDER_NUMBER", result.message["reference"])

    def test_get_payment_link(self):
        id = "PL61C53A8B97E6915A"
        self.adyen.client = self.test.create_client_from_file(200, None,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "getpaymenlinks"
                                                              "-succes.json")
        result = self.adyen.checkout.payment_links_api.get_payment_link(id)
        self.adyen.client.http_client.request.assert_called_once_with(
            'GET',
            f'https://checkout-test.adyen.com/{self.checkout_version}/paymentLinks/{id}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            xapikey="YourXapikey",
            json=None
        )
        self.assertEqual("TestMerchantCheckout", result.message["merchantAccount"])

    def test_update_payment_link(self):
        id = "PL61C53A8B97E6915A"
        request = {
            "status": "expired"
        }
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/checkout"
                                                              "/updatepaymentlinks"
                                                              "-success.json")
        result = self.adyen.checkout.payment_links_api.update_payment_link(request, id)
        self.adyen.client.http_client.request.assert_called_once_with(
            'PATCH',
            f'https://checkout-test.adyen.com/{self.checkout_version}/paymentLinks/{id}',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            xapikey="YourXapikey",
            json=request
        )
        self.assertEqual("expired",result.message["status"])
