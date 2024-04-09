from __future__ import absolute_import, division, unicode_literals

import base64
import binascii
import copy
import hashlib
import hmac


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

    notification_items = dict_object.get("notificationItems")
    if notification_items is None:
        raise ValueError("Must provide notificationItems in the dictionary object")

    for notification_item in notification_items:
        notification_request_item = notification_item.get("NotificationRequestItem")
        if notification_request_item is None:
            raise ValueError("Must provide NotificationRequestItem in the NotificationRequestItems")

        additionalData = notification_request_item.get("additionalData")
        if additionalData is None:
            raise ValueError("Must provide additionalData in the NotificationRequestItem")

        hmac_signature = additionalData.get("hmacSignature")
        if not hmac_signature:
            raise ValueError("Must provide hmacSignature in additionalData")

        del notification_request_item["additionalData"]
        merchant_sign = generate_notification_sig(notification_request_item, hmac_key)
        merchant_sign_str = merchant_sign.decode("utf-8")
        if not hmac.compare_digest(merchant_sign_str, hmac_signature):
            return False

    return True


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
