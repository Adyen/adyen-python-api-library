from __future__ import absolute_import, division, unicode_literals

from itertools import chain
from collections import OrderedDict
import base64
import hmac
import hashlib
import binascii


def generate_hpp_sig(dict_object, hmac_key):
    if 'issuerId' in dict_object:
        if dict_object['issuerId'] == "":
            del dict_object['issuerId']

    if not isinstance(dict_object, dict):
        raise ValueError("Must Provide dictionary object")

    def escape_val(val):
        if isinstance(val, int):
            return val
        return val.replace('\\', '\\\\').replace(':', '\\:')

    hmac_key = binascii.a2b_hex(hmac_key)

    ordered_request = OrderedDict(sorted(dict_object.items(),
                                         key=lambda t: t[0]))

    signing_string = ':'.join(
        map(escape_val, chain(map(str, ordered_request.keys()),
                              map(str, ordered_request.values()))))

    hm = hmac.new(hmac_key, signing_string.encode('utf-8'), hashlib.sha256)
    return base64.b64encode(hm.digest())


def is_valid_hmac(dict_object, hmac_key):
    if 'additionalData' in dict_object:
        if dict_object['additionalData']['hmacSignature'] == "":
            raise ValueError("Must Provide hmacSignature in additionalData")
        else:
            expected_sign = dict_object['additionalData']['hmacSignature']
            del dict_object['additionalData']
            merchant_sign = generate_hpp_sig(dict_object, hmac_key)
            merchant_sign_str = merchant_sign.decode("utf-8")
            return merchant_sign_str == expected_sign


def generate_notification_sig(dict_object, hmac_key):
    if 'issuerId' in dict_object:
        if dict_object['issuerId'] == "":
            del dict_object['issuerId']

    if not isinstance(dict_object, dict):
        raise ValueError("Must Provide dictionary object")

    def escape_val(val):
        if isinstance(val, int):
            return val
        return val.replace('\\', '\\\\').replace(':', '\\:')

    hmac_key = binascii.a2b_hex(hmac_key)

    request_dict = dict(dict_object)
    request_dict['value'] = request_dict['amount']['value']
    request_dict['currency'] = request_dict['amount']['currency']

    element_orders = [
        'pspReference',
        'originalReference',
        'merchantAccountCode',
        'merchantReference',
        'value',
        'currency',
        'eventCode',
        'success',
    ]

    signing_string = ':'.join(
        map(escape_val, map(str, (
            request_dict.get(element, '') for element in element_orders))))

    hm = hmac.new(hmac_key, signing_string.encode('utf-8'), hashlib.sha256)
    return base64.b64encode(hm.digest())


def is_valid_hmac_notification(dict_object, hmac_key):
    if 'additionalData' in dict_object:
        if dict_object['additionalData']['hmacSignature'] == "":
            raise ValueError("Must Provide hmacSignature in additionalData")
        else:
            expected_sign = dict_object['additionalData']['hmacSignature']
            del dict_object['additionalData']
            merchant_sign = generate_notification_sig(dict_object, hmac_key)
            merchant_sign_str = merchant_sign.decode("utf-8")
            return merchant_sign_str == expected_sign
