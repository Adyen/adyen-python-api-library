import Adyen
import unittest
from BaseTest import BaseTest


class TestPayments(unittest.TestCase):
    ady = Adyen.Adyen()

    client = ady.client
    test = BaseTest(ady)
    client.username = "YourWSUser"
    client.password = "YourWSPassword"
    client.platform = "test"
    client.app_name = "appname"

    def test_authorise_success_mocked(self):
        request = {}
        request['merchantAccount'] = "YourMerchantAccount"
        request['amount'] = {"value": "100000", "currency": "EUR"}
        request['reference'] = "123456"
        request['card'] = {
            "number": "5136333333333335",
            "expiryMonth": "08",
            "expiryYear": "2018",
            "cvc": "737",
            "holderName": "John Doe"
        }
        self.ady.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'authorise-success'
                                                            '.json')
        result = self.ady.payment.authorise(request)
        self.assertEqual("Authorised", result.message['resultCode'])
        self.assertEqual("8/2018",
                         result.message['additionalData']['expiryDate'])
        self.assertEqual("411111",
                         result.message['additionalData']['cardBin'])
        self.assertEqual("1111",
                         result.message['additionalData']['cardSummary'])
        self.assertEqual("Holder",
                         result.message['additionalData']['cardHolderName'])
        self.assertEqual("true",
                         result.message['additionalData']['threeDOffered'])
        self.assertEqual("false",
                         result.message['additionalData']
                         ['threeDAuthenticated'])
        self.assertEqual("69746", result.message['authCode'])
        self.assertEqual(11, len(result.message['fraudResult']['results']))
        fraud_checks = result.message['fraudResult']['results']
        fraud_check_result = fraud_checks[0]['FraudCheckResult']
        self.assertEqual("CardChunkUsage", fraud_check_result['name'])
        self.assertEqual(8, fraud_check_result['accountScore'])
        self.assertEqual(2, fraud_check_result['checkId'])

    def test_authorise_error010_mocked(self):
        request = {}
        request['merchantAccount'] = "testaccount"
        request['amount'] = {"value": "100000", "currency": "EUR"}
        request['reference'] = "123456"
        request['card'] = {
            "number": "5136333333333335",
            "expiryMonth": "08",
            "expiryYear": "2018",
            "cvc": "737",
            "holderName": "John Doe"
        }
        self.ady.client = self.test.create_client_from_file(403, request,
                                                            'test/mocks/'
                                                            'authorise-error'
                                                            '-010'
                                                            '.json')
        self.assertRaises(Adyen.AdyenAPIInvalidPermission,
                          self.ady.payment.authorise, request)

    def test_authorise_error_cvc_declined_mocked(self):
        request = {}
        request['amount'] = {"value": "100000", "currency": "EUR"}
        request['reference'] = "123456"
        request['card'] = {
            "number": "5136333333333335",
            "expiryMonth": "08",
            "expiryYear": "2018",
            "cvc": "787",
            "holderName": "John Doe"
        }
        self.ady.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'authorise-error-'
                                                            'cvc-declined'
                                                            '.json')
        result = self.ady.payment.authorise(request)
        self.assertEqual("Refused", result.message['resultCode'])

    def test_authorise_success_3d_mocked(self):
        request = {}
        request['merchantAccount'] = "YourMerchantAccount"
        request['amount'] = {"value": "100000", "currency": "EUR"}
        request['reference'] = "123456"
        request['card'] = {
            "number": "5136333333333335",
            "expiryMonth": "08",
            "expiryYear": "2018",
            "cvc": "787",
            "holderName": "John Doe"
        }
        request['browserInfo'] = {
            "userAgent": "YourUserAgent",
            "acceptHeader": "YourAcceptHeader"
        }
        self.ady.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'authorise-success'
                                                            '-3d.json')
        result = self.ady.payment.authorise(request)
        self.assertEqual("RedirectShopper", result.message['resultCode'])
        self.assertIsNotNone(result.message['md'])
        self.assertIsNotNone(result.message['issuerUrl'])
        self.assertIsNotNone(result.message['paRequest'])

    def test_authorise_3d_success_mocked(self):
        request = {}
        request['merchantAccount'] = "YourMerchantAccount"
        request['md'] = "testMD"
        request['paResponse'] = "paresponsetest"
        request['browserInfo'] = {
            "userAgent": "YourUserAgent",
            "acceptHeader": "YourAcceptHeader"
        }
        self.ady.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'authorise3d-'
                                                            'success.json')
        result = self.ady.payment.authorise3d(request)
        self.assertEqual("Authorised", result.message['resultCode'])
        self.assertIsNotNone(result.message['pspReference'])

    def test_authorise_cse_success_mocked(self):
        request = {}
        request['amount'] = {"value": "1234", "currency": "EUR"}
        request['merchantAccount'] = "YourMerchantAccount"
        request['reference'] = "YourReference"
        request['additionalData'] = {
            "card.encrypted.json": "YourCSEToken"
        }
        self.ady.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'authorise-success'
                                                            '-cse.json')
        result = self.ady.payment.authorise(request)
        self.assertEqual("Authorised", result.message['resultCode'])

    def test_authorise_cse_error_expired_mocked(self):
        request = {}
        request['amount'] = {"value": "1234", "currency": "EUR"}
        request['merchantAccount'] = "YourMerchantAccount"
        request['reference'] = "YourReference"
        request['additionalData'] = {
            "card.encrypted.json": "YourCSEToken"
        }

        self.ady.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'authorise-error-'
                                                            'expired.json')
        result = self.ady.payment.authorise(request)
        self.assertEqual("Refused", result.message['resultCode'])
        self.assertEqual("DECLINED Expiry Incorrect",
                         result.message['additionalData']['refusalReasonRaw'])

    def test_error_401_mocked(self):
        request = {}
        request['merchantAccount'] = "YourMerchantAccount"
        request['amount'] = {"value": "100000", "currency": "EUR"}
        request['reference'] = "123456"
        request['card'] = {
            "number": "5136333333333335",
            "expiryMonth": "08",
            "expiryYear": "2018",
            "cvc": "787",
            "holderName": "John Doe"
        }
        self.ady.client = self.test.create_client_from_file(401, request,
                                                            'test/mocks/'
                                                            'authorise-error-'
                                                            '010.json')
        self.assertRaisesRegexp(Adyen.AdyenAPIAuthenticationError,
                                "Unable to authenticate with Adyen's Servers."
                                " Please verify the credentials set with the"
                                " Adyen base class. Please reach out to your"
                                " Adyen Admin if the problem persists",
                                self.ady.payment.authorise, request)


TestPayments.client.http_force = "requests"
suite = unittest.TestLoader().loadTestsFromTestCase(TestPayments)
unittest.TextTestRunner(verbosity=2).run(suite)
TestPayments.client.http_force = "pycurl"
TestPayments.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestPayments)
unittest.TextTestRunner(verbosity=2).run(suite)
TestPayments.client.http_force = "other"
TestPayments.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestPayments)
unittest.TextTestRunner(verbosity=2).run(suite)
