import re
from functools import wraps
from collections import OrderedDict
import base64
import hmac
import hashlib
import binascii
import logging
from adyen_log import logname,getlogger
logger = logging.getLogger(logname())

def _generate_signing_string(dict_object,hmac_key):

    if not isinstance(dict_object, dict):
        raise ValueError("Must Provide dictionary object")
    def escapeVal(val):
        if isinstance(val,int):
            return val
        return val.replace('\\','\\\\').replace(':','\\:')

    hmac_key = binascii.a2b_hex(hmac_key)

    ordered_request = OrderedDict(sorted(dict_object.items(), key=lambda t: t[0]))

    #for k,v in ordered_request.items():
    #    signing_string.append(':'.join(k,escapeVal(v)))

    signing_string = ':'.join(map(escapeVal, map(str,ordered_request.keys()) + map(str,ordered_request.values())))

    return signing_string


def generate_hpp_sig(dict_object, hmac_key):

    if 'issuerId' in dict_object:
        if dict_object['issuerId'] == "":
            del dict_object['issuerId']

    if not isinstance(dict_object, dict):
        raise ValueError("Must Provide dictionary object")
    def escapeVal(val):
        if isinstance(val,int):
            return val
        return val.replace('\\','\\\\').replace(':','\\:')

    hmac_key = binascii.a2b_hex(hmac_key)

    ordered_request = OrderedDict(sorted(dict_object.items(), key=lambda t: t[0]))

    signing_string = ':'.join(map(escapeVal, map(str,ordered_request.keys()) + map(str,ordered_request.values())))


    hm = hmac.new(hmac_key, signing_string, hashlib.sha256)
    return base64.b64encode(hm.digest())
