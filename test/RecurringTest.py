import Adyen
import unittest
from BaseTest import BaseTest


class TestRecurring(unittest.TestCase):
    ady = Adyen.Adyen()
    client = ady.client
    test = BaseTest(ady)
    client.username = "YourWSUser"
    client.password = "YourWSPassword"
    client.platform = "test"
    client.app_name = "appname"

    def test_list_recurring_details(self):
        request = {}
        request['merchantAccount'] = "YourMerchantAccount"
        request['reference'] = "YourReference"
        request["shopperEmail"] = "ref@email.com"
        request["shopperReference"] = "ref"
        request['recurring'] = {}
        request["recurring"]['contract'] = "RECURRING"
        self.ady.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'recurring/'
                                                            'listRecurring'
                                                            'Details-'
                                                            'success.json')
        result = self.ady.recurring.list_recurring_details(request)
        self.assertEqual(1, len(result.message['details']))
        self.assertEqual(1, len(result.message['details'][0]))
        recurringDetail = result.message['details'][0]['RecurringDetail']
        self.assertEqual("recurringReference",
                         recurringDetail['recurringDetailReference'])
        self.assertEqual("cardAlias", recurringDetail['alias'])
        self.assertEqual("1111", recurringDetail['card']['number'])

    def test_disable(self):
        request = {}
        request["shopperEmail"] = "ref@email.com"
        request["shopperReference"] = "ref"
        request["recurringDetailReference"] = "12345678889"
        self.ady.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'recurring/'
                                                            'disable-success'
                                                            '.json')
        result = self.ady.recurring.disable(request)
        self.assertEqual(1, len(result.message['details']))
        self.assertEqual("[detail-successfully-disabled]",
                         result.message['response'])

    def test_disable_803(self):
        request = {}
        request["shopperEmail"] = "ref@email.com"
        request["shopperReference"] = "ref"
        request["recurringDetailReference"] = "12345678889"
        self.ady.client = self.test.create_client_from_file(422, request,
                                                            'test/mocks/'
                                                            'recurring/'
                                                            'disable-error-803'
                                                            '.json')
        self.assertRaisesRegexp(
            Adyen.AdyenAPICommunicationError,
            "Unexpected error",
            self.ady.recurring.disable,
            request
        )


TestRecurring.client.http_force = "requests"
suite = unittest.TestLoader().loadTestsFromTestCase(TestRecurring)
unittest.TextTestRunner(verbosity=2).run(suite)
TestRecurring.client.http_force = "pycurl"
TestRecurring.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestRecurring)
unittest.TextTestRunner(verbosity=2).run(suite)
TestRecurring.client.http_force = "other"
TestRecurring.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestRecurring)
unittest.TextTestRunner(verbosity=2).run(suite)
