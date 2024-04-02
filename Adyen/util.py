from __future__ import absolute_import, division, unicode_literals

import base64
import hmac
import hashlib
import binascii
import copy


# generates HMAC signature for the NotificationRequest object
def generate_notification_sig(dict_object, hmac_key):

    if not isinstance(dict_object, dict):
        raise ValueError("Must Provide dictionary object")

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

    signing_string = ':'.join(map(str, (request_dict.get(element, '') for element in element_orders)))

    hm = hmac.new(hmac_key, signing_string.encode('utf-8'), hashlib.sha256)
    return base64.b64encode(hm.digest())


# generates HMAC signature for the payload (bytes)
def generate_payload_sig(payload, hmac_key):

    if not isinstance(payload, bytes):
        raise ValueError("Must Provide payload as bytes")

    hmac_key = binascii.a2b_hex(hmac_key)

    hm = hmac.new(hmac_key, payload, hashlib.sha256)
    return base64.b64encode(hm.digest())


def is_valid_hmac_notification(dict_object, hmac_key):
    """
    validates the HMAC signature of the NotificationRequestItem object. Use for webhooks that provide the
    hmacSignature as part of the payload `AdditionalData` (i.e. Payments)
    Args:
        dict_object: object with a list of notificationItems
        hmac_key: HMAC key to generate the signature

    Returns:
        boolean: true when HMAC signature is valid
    """

    dict_object = copy.deepcopy(dict_object) 

    if 'notificationItems' in dict_object:
        dict_object = dict_object['notificationItems'][0]['NotificationRequestItem']

    if 'additionalData' in dict_object:
        if dict_object['additionalData']['hmacSignature'] == "":
            raise ValueError("Must Provide hmacSignature in additionalData")
        else:
            expected_sign = dict_object['additionalData']['hmacSignature']
            del dict_object['additionalData']
            merchant_sign = generate_notification_sig(dict_object, hmac_key)
            merchant_sign_str = merchant_sign.decode("utf-8")
            return hmac.compare_digest(merchant_sign_str, expected_sign)


def is_valid_hmac_payload(hmac_signature, hmac_key, payload):
    """
    validates the HMAC signature of a payload against an expected signature. Use for webhooks that provide the
    hmacSignature in the HTTP header (i.e. Banking, Management API)
    Args:
        hmac_signature: HMAC signature to validate
        hmac_key: HMAC key to generate the signature
        payload: webhook payload

    Returns:
        boolean: true when HMAC signature is valid
    """

    merchant_sign = generate_payload_sig(payload, hmac_key)
    merchant_sign_str = merchant_sign.decode("utf-8")

    return hmac.compare_digest(merchant_sign_str, hmac_signature)


def get_query(query_parameters):
    return '?' + '&'.join(["{}={}".format(k, v) for k, v in query_parameters.items()])
