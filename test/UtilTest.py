import unittest
from json import load
import Adyen
from Adyen import settings
from Adyen.util import (
    generate_notification_sig,
    is_valid_hmac_notification,
    get_query
)
try:
    from BaseTest import BaseTest
except ImportError:
    from .BaseTest import BaseTest


class UtilTest(unittest.TestCase):
    adyen = Adyen.Adyen()
    client = adyen.client

    def test_notification_request_item_hmac(self):
        request = {
            "pspReference": "7914073381342284",
            "merchantReference": "TestPayment-1407325143704",
            "merchantAccountCode": "TestMerchant",
            "amount": {
                "currency": "EUR",
                "value": 1130
            },
            "eventCode": "AUTHORISATION",
            "success": "true",
            "eventDate": "2019-05-06T17:15:34.121+02:00",
            "operations": [
                "CANCEL",
                "CAPTURE",
                "REFUND"
            ],
            "paymentMethod": "visa",
        }
        key = "44782DEF547AAA06C910C43932B1EB0C" \
              "71FC68D9D0C057550C48EC2ACF6BA056"
        hmac_calculation = generate_notification_sig(request, key)
        hmac_calculation_str = hmac_calculation.decode("utf-8")
        expected_hmac = "coqCmt/IZ4E3CzPvMY8zTjQVL5hYJUiBRg8UU+iCWo0="
        self.assertTrue(hmac_calculation_str != "")
        self.assertEqual(hmac_calculation_str, expected_hmac)
        request['additionalData'] = {'hmacSignature': hmac_calculation_str}
        hmac_validate = is_valid_hmac_notification(request, key)
        self.assertIn('additionalData', request)
        self.assertDictEqual(request['additionalData'],
                             {'hmacSignature': hmac_calculation_str})
        self.assertTrue(hmac_validate)

    def test_webhooks_with_slashes(self):
        hmac_key = "74F490DD33F7327BAECC88B2947C011FC02D014A473AAA33A8EC93E4DC069174"
        with open('test/mocks/util/backslash_notification.json') as file:
            backslash_notification = load(file)
            self.assertTrue(is_valid_hmac_notification(backslash_notification, hmac_key))
        with open('test/mocks/util/colon_notification.json') as file:
            colon_notification = load(file)
            self.assertTrue(is_valid_hmac_notification(colon_notification, hmac_key))
        with open('test/mocks/util/forwardslash_notification.json') as file:
            forwardslash_notification = load(file)
            self.assertTrue(is_valid_hmac_notification(forwardslash_notification, hmac_key))
        with open('test/mocks/util/mixed_notification.json') as file:
            mixed_notification = load(file)
            self.assertTrue(is_valid_hmac_notification(mixed_notification, hmac_key))


    def test_query_string_creation(self):
        query_parameters = {
            "pageSize":7,
            "pageNumber":3
        }
        query_string = get_query(query_parameters)
        self.assertEqual(query_string,'?pageSize=7&pageNumber=3')

    def test_passing_xapikey_in_method(self):
        request = {'merchantAccount': "YourMerchantAccount"}
        self.test = BaseTest(self.adyen)
        self.client.platform = "test"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                              "test/mocks/"
                                                              "checkout/"
                                                              "paymentmethods"
                                                              "-success.json")
        result = self.adyen.checkout.payments_api.payment_methods(request, xapikey="YourXapikey")
        self.assertEqual("AliPay", result.message['paymentMethods'][0]['name'])
        self.assertEqual("Credit Card",
                         result.message['paymentMethods'][2]['name'])
        self.assertEqual("Credit Card via AsiaPay",
                         result.message['paymentMethods'][3]['name'])

    def test_custom_version(self):
        self.client.api_checkout_version = 60
        request = {'merchantAccount': "YourMerchantAccount"}
        self.test = BaseTest(self.adyen)
        self.client.platform = "test"
        self.adyen.client = self.test.create_client_from_file(200, request,
                                                            "test/mocks/"
                                                            "checkout/"
                                                            "paymentmethods"
                                                            "-success.json")
        result = self.adyen.checkout.payments_api.payment_methods(request, xapikey="YourXapikey")
        self.adyen.client.http_client.request.assert_called_once_with(
            'POST',
            f'https://checkout-test.adyen.com/v{self.client.api_checkout_version}/paymentMethods',
            headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION},
            json=request,
            xapikey="YourXapikey"
        )

    def test_is_valid_hmac_notification_removes_additional_data(self):
        notification = {
                            "live":"false",
                            "notificationItems":[
                                {
                                    "NotificationRequestItem":{
                                        "additionalData":{
                                        "hmacSignature":"11aa",
                                        "fraudResultType":"GREEN",
                                        "fraudManualReview": "false",
                                        "totalFraudScore":"75"
                                        },
                                        "amount":{
                                        "currency":"USD",
                                        "value":10000
                                        },
                                        "success":"true"
                                        
                                    }
                                }
                            ]}
        is_valid_hmac_notification(notification, "11aa")
        self.assertIsNotNone(notification['notificationItems'][0]['NotificationRequestItem']['additionalData'])
    