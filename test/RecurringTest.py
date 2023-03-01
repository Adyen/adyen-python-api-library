import Adyen
import unittest
from Adyen import settings
try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class TestRecurring(unittest.TestCase):
    adyen = Adyen.Adyen()
    client = adyen.client
    test = BaseTest(adyen)
    client.username = "YourWSUser"
    client.password = "YourWSPassword"
    client.platform = "test"
    recurring_version = settings.API_RECURRING_VERSION

    def test_list_recurring_details(self):
        request = {}
        request['merchantAccount'] = "YourMerchantAccount"
        request['reference'] = "YourReference"
        request["shopperEmail"] = "ref@email.com"
        request["shopperReference"] = "ref"
        request['recurring'] = {}
        request["recurring"]['contract'] = "RECURRING"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'recurring/'
                                                            'listRecurring'
                                                            'Details-'
                                                            'success.json')
        result = self.adyen.recurring.list_recurring_details(request)
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://pal-test.adyen.com/pal/servlet/Recurring/{self.recurring_version}/listRecurringDetails',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            username='YourWSUser',
            password='YourWSPassword'
        )
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
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                            'test/mocks/'
                                                            'recurring/'
                                                            'disable-success'
                                                            '.json')
        result = self.adyen.recurring.disable(request)
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://pal-test.adyen.com/pal/servlet/Recurring/{self.recurring_version}/disable',
            headers={'adyen-library-name': 'adyen-python-api-library', 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            username='YourWSUser',
            password='YourWSPassword',
        )
        self.assertEqual(1, len(result.message['details']))
        self.assertEqual("[detail-successfully-disabled]",
                         result.message['response'])

    def test_disable_803(self):
        request = {}
        request["shopperEmail"] = "ref@email.com"
        request["shopperReference"] = "ref"
        request["recurringDetailReference"] = "12345678889"
        self.adyen.client = self.test.create_client_from_file(422, request,
                                                            'test/mocks/'
                                                            'recurring/'
                                                            'disable-error-803'
                                                            '.json')
        self.assertRaisesRegex(
            Adyen.AdyenAPIUnprocessableEntity,
            "AdyenAPIUnprocessableEntity:{'status': 422, 'errorCode': '803', 'message': 'PaymentDetail not found', 'errorType': 'validation'}",
            self.adyen.recurring.disable,
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
