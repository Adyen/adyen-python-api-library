import unittest

import Adyen
from Adyen.util import (
    generate_hpp_sig,
    is_valid_hmac,
    generate_notification_sig,
    is_valid_hmac_notification,
    get_query
)


class UtilTest(unittest.TestCase):
    ady = Adyen.Adyen()
    client = ady.client

    def test_hpp_request_item_hmac(self):
        request = {
            "pspReference": "pspReference",
            "originalReference": "originalReference",
            "merchantAccount": "merchantAccount",
            "amount": {
                "currency": "EUR",
                "value": 100000
            },
            "eventCode": "EVENT",
            "Success": "true"
        }
        key = "DFB1EB5485895CFA84146406857104AB" \
              "B4CBCABDC8AAF103A624C8F6A3EAAB00"
        hmac_calculation = generate_hpp_sig(request, key)
        hmac_calculation_str = hmac_calculation.decode("utf-8")
        expected_hmac = "+xK25vgc9XcZFwu7WNLIwqVewyumVsgp+X+C0a2e+DE="
        self.assertTrue(hmac_calculation_str != "")
        self.assertEqual(hmac_calculation_str, expected_hmac)
        request['additionalData'] = {'hmacSignature': hmac_calculation_str}
        hmac_validate = is_valid_hmac(request, key)
        self.assertIn('additionalData', request)
        self.assertDictEqual(request['additionalData'],
                             {'hmacSignature': hmac_calculation_str})
        self.assertTrue(hmac_validate)

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

    def test_query_string_creation(self):
        query_parameters = {
            "pageSize":7,
            "pageNumber":3
        }
        query_string = get_query(query_parameters)
        self.assertEqual(query_string,'?pageSize=7&pageNumber=3')