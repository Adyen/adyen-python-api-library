import Adyen
import unittest
try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestModifications(unittest.TestCase):
    ady = Adyen.Adyen()

    client = ady.client
    test = BaseTest(ady)
    client.username = "YourWSUser"
    client.password = "YourWSPassword"
    client.platform = "test"

    def test_capture_success(self):
        request = {}
        request['merchantAccount'] = "YourMerchantAccount"
        request['reference'] = "YourReference"
        request['modificationAmount'] = {"value": "1234", "currency": "EUR"}
        request['originalReference'] = "YourOriginalReference"
        self.ady.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'capture-success'
                                                            '.json')
        result = self.ady.payment.modifications_api.capture(request)
        self.assertEqual("[capture-received]", result.message['response'])

    def test_capture_error_167(self):
        request = {}
        request['merchantAccount'] = "YourMerchantAccount"
        request['reference'] = "YourReference"
        request['modificationAmount'] = {"value": "1234", "currency": "EUR"}
        request['originalReference'] = "YourOriginalReference"
        self.ady.client = self.test.create_client_from_file(422, request,
                                                            'test/mocks/'
                                                            'capture-error-167'
                                                            '.json')
        self.assertRaisesRegex(
            Adyen.AdyenAPIUnprocessableEntity,
            "AdyenAPIUnprocessableEntity:{'status': 422, 'errorCode': '167', 'message': 'Original pspReference required for this operation', 'errorType': 'validation'}",
            self.ady.payment.modifications_api.capture,
            request
        )

    def test_cancel_or_refund_received(self):
        request = {}
        request['merchantAccount'] = "YourMerchantAccount"
        request['reference'] = "YourReference"
        request['originalReference'] = "YourOriginalReference"
        self.ady.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'cancelOrRefund'
                                                            '-received.json')
        result = self.ady.payment.modifications_api.cancel_or_refund(request)
        self.assertEqual("[cancelOrRefund-received]",
                         result.message['response'])

    def test_refund_received(self):
        request = {}
        request['merchantAccount'] = "YourMerchantAccount"
        request['reference'] = "YourReference"
        request['originalReference'] = "YourOriginalReference"
        request['modificationAmount'] = {"value": "1234", "currency": "EUR"}
        self.ady.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'refund-received'
                                                            '.json')
        result = self.ady.payment.modifications_api.refund(request)
        self.assertEqual("[refund-received]", result.message['response'])

    def test_cancel_received(self):
        request = {}
        request['merchantAccount'] = "YourMerchantAccount"
        request['reference'] = "YourReference"
        request['originalReference'] = "YourOriginalReference"
        self.ady.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'cancel-received'
                                                            '.json')
        result = self.ady.payment.modifications_api.cancel(request)
        self.assertEqual("[cancel-received]", result.message['response'])

    def test_adjust_authorisation_received(self):
        request = {}
        request['merchantAccount'] = "YourMerchantAccount"
        request['reference'] = "YourReference"
        request['modificationAmount'] = {"value": "1234", "currency": "EUR"}
        request['originalReference'] = "YourOriginalReference"
        self.ady.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'adjust-'
                                                            'authorisation-'
                                                            'received.json')
        result = self.ady.payment.modifications_api.adjust_authorisation(request)
        self.assertEqual("[adjustAuthorisation-received]",
                         result.message['response'])


TestModifications.client.http_force = "requests"
suite = unittest.TestLoader().loadTestsFromTestCase(TestModifications)
unittest.TextTestRunner(verbosity=2).run(suite)
TestModifications.client.http_force = "pycurl"
TestModifications.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestModifications)
unittest.TextTestRunner(verbosity=2).run(suite)
TestModifications.client.http_force = "other"
TestModifications.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestModifications)
unittest.TextTestRunner(verbosity=2).run(suite)
