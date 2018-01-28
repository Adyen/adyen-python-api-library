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
