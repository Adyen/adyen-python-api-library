from unittest.mock import ANY
import unittest

from BaseTest import BaseTest
import Adyen


REQUEST_KWARGS = {
    'merchantAccount': 'YourMerchantAccount',
    'amount': '1000'
}


class TestBinLookup(unittest.TestCase):
    ady = Adyen.Adyen()

    client = ady.client
    test = BaseTest(ady)
    client.username = "YourWSUser"
    client.password = "YourWSPassword"
    client.platform = "test"
    client.app_name = "appname"

    def test_get_cost_estimate_success(self):
        self.ady.client.http_client.request.reset_mock()
        expected = {
            'cardBin': {
                'bin': '458012',
                'commercial': False,
                'fundingSource': 'CHARGE',
                'fundsAvailability': 'N',
                'issuingBank': 'Bank Of America',
                'issuingCountry': 'US', 'issuingCurrency': 'USD',
                'paymentMethod': 'Y',
                'summary': '6789'
            },
            'costEstimateAmount': {
                'currency': 'USD', 'value': 1234
            },
            'resultCode': 'Success',
            'surchargeType': 'PASSTHROUGH'
        }

        self.ady.client = self.test.create_client_from_file(
            status=200,
            request=REQUEST_KWARGS,
            filename='test/mocks/binlookup/getcostestimate-success.json'
        )

        result = self.ady.binlookup.get_cost_estimate(REQUEST_KWARGS)
        self.assertEqual(expected, result.message)
        self.ady.client.http_client.request.assert_called_once_with(
            'https://pal-test.adyen.com/pal/servlet/'
            'BinLookup/v50/getCostEstimate',
            headers={},
            json={
                'merchantAccount': 'YourMerchantAccount',
                'amount': '1000', 'applicationInfo': {
                    'adyenLibrary': {
                        'name': 'adyen-python-api-library',
                        'version': ANY
                    }
                }
            },
            password='YourWSPassword',
            username='YourWSUser'
        )

    def test_get_cost_estimate_error_mocked(self):
        self.ady.client = self.test.create_client_from_file(
            status=200,
            request=REQUEST_KWARGS,
            filename=(
                "test/mocks/binlookup/"
                "getcostestimate-error-invalid-data-422.json"
            )
        )

        result = self.ady.binlookup.get_cost_estimate(REQUEST_KWARGS)
        self.assertEqual(422, result.message['status'])
        self.assertEqual("101", result.message['errorCode'])
        self.assertEqual("Invalid card number", result.message['message'])
        self.assertEqual("validation", result.message['errorType'])


TestBinLookup.client.http_force = "requests"
suite = unittest.TestLoader().loadTestsFromTestCase(TestBinLookup)
unittest.TextTestRunner(verbosity=2).run(suite)
TestBinLookup.client.http_force = "pycurl"
TestBinLookup.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestBinLookup)
unittest.TextTestRunner(verbosity=2).run(suite)
TestBinLookup.client.http_force = "other"
TestBinLookup.client.http_init = False
suite = unittest.TestLoader().loadTestsFromTestCase(TestBinLookup)
unittest.TextTestRunner(verbosity=2).run(suite)
