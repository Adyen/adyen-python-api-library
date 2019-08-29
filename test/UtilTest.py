import unittest

import Adyen
from Adyen import generate_hpp_sig
from Adyen.util import is_valid_hmac


class UtilTest(unittest.TestCase):
    ady = Adyen.Adyen()
    client = ady.client

    def test_notification_request_item_hmac(self):
        request = {
            "pspReference": "pspReference",
            "originalReference": "originalReference",
            "merchantAccount": "merchantAccount",
            "amount": {
                "value": 100000,
                "currency": "EUR"
            },
            "eventCode": "EVENT",
            "Success": "true"
        }
        key = "DFB1EB5485895CFA84146406857104AB" \
              "B4CBCABDC8AAF103A624C8F6A3EAAB00"
        hmac_calculation = generate_hpp_sig(request, key)
        hmac_calculation_str = hmac_calculation.decode("utf-8")
        expected_hmac = "cRBVEz3qxJPPDRCUppYhxor5K4Qylr77mlYwii7RL5Q="
        self.assertTrue(hmac_calculation != "")
        self.assertEqual(hmac_calculation, expected_hmac)
        request['additionalData'] = {'hmacSignature': hmac_calculation_str}
        hmac_validate = is_valid_hmac(request, key)
        self.assertTrue(hmac_validate)
