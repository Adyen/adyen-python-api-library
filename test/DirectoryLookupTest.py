import unittest

import Adyen

try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest

import time


class TestDirectoryLookup(unittest.TestCase):
    ady = Adyen.Adyen()

    client = ady.client
    test = BaseTest(ady)
    client.username = "YourWSUser"
    client.password = "YourWSPassword"
    client.platform = "test"
    client.hmac = "DFB1EB5485895CFA84146406857104A" \
                  "BB4CBCABDC8AAF103A624C8F6A3EAAB00"

    def test_get_post_parameters(self):
        request = {
            'merchantAccount': "testmerchantaccount",
            'paymentAmount': "1000",
            'currencyCode': "EUR",
            'merchantReference': "Get Payment methods",
            'skinCode': "testskincode",
            'countryCode': "NL",
            'shopperLocale': "nl_NL",
            'sessionValidity': time.strftime('%Y-%m-%dT%H:%M:%SZ')
        }
        self.test.create_client_from_file(200, request, None)
        result = self.ady.hpp.hpp_payment(request)
        self.assertEqual("EUR", result["message"]["currencyCode"])
        self.assertEqual(44, len(result["message"]["merchantSig"]))

    def test_get_payment_methods(self):
        request = {
            'merchantAccount': "testmerchantaccount",
            'paymentAmount': "1000",
            'currencyCode': "EUR",
            'merchantReference': "Get Payment methods",
            'skinCode': "testskincode",
            'countryCode': "NL",
            'shopperLocale': "nl_NL",
            'sessionValidity': time.strftime('%Y-%m-%dT%H:%M:%SZ')
        }
        self.test.create_client_from_file(200, request,
                                          'test/mocks/hpp/'
                                          'directoryLookup-success.json')
        result = self.ady.hpp.directory_lookup(request)
        self.assertEqual(8, len(result.message['paymentMethods']))
        ideal = result.message['paymentMethods'][0]
        self.assertEqual("ideal", ideal['brandCode'])
        self.assertEqual("iDEAL", ideal['name'])
        self.assertEqual(3, len(ideal['issuers']))
        issuer1 = ideal['issuers'][0]
        self.assertEqual("1121", issuer1['issuerId'])
        self.assertEqual("Test Issuer", issuer1['name'])
        visa = result.message['paymentMethods'][1]
        self.assertEqual("visa", visa['brandCode'])


TestDirectoryLookup.client.http_force = "requests"
suite = unittest.TestLoader().loadTestsFromTestCase(TestDirectoryLookup)
unittest.TextTestRunner(verbosity=2).run(suite)
TestDirectoryLookup.client.http_force = "pycurl"
TestDirectoryLookup.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestDirectoryLookup)
unittest.TextTestRunner(verbosity=2).run(suite)
TestDirectoryLookup.client.http_force = "other"
TestDirectoryLookup.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestDirectoryLookup)
unittest.TextTestRunner(verbosity=2).run(suite)
