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

"""
def underscore_to_camelcase(value):
    first, rest = value.split('_')[0], value.split('_')[1:]
    return first + "".join(word.capitalize() for word in rest)

def camelcase_to_underscore(value):
    s1 = re.sub('(.)([0-9]+[A-Z][a-z]+)', r'\1_\2', value)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def under_to_camel_dict(dict_object):
    def next_level(obj):
        temp_obj = {}
        if isinstance(obj, dict):
            for key, value in obj.iteritems():
                key = underscore_to_camelcase(key)
                if not isinstance(value, str):
                    value = next_level(value)
                temp_obj[key] = value
        elif isinstance(obj, str):
            obj = underscore_to_camelcase(obj)
            return obj
        elif isinstance(obj, list):
            for item in obj:
                item = next_level(item)
                temp_obj.append(item)
        #Non iterable or not string
        else:
            temp_obj = obj
        return temp_obj

    return next_level(dict_object)

def camel_to_underscore(dict_object):
    def next_level(obj):
            temp_obj = {}
            if isinstance(obj, dict):
                for key, value in obj.iteritems():
                    key = camelcase_to_underscore(key)
                    value = next_level(value)
                    temp_obj[key] = value
            elif isinstance(obj, str):
                obj = camelcase_to_underscore(obj)
                return obj
            elif isinstance(obj, list):
                for item in obj:
                    item = next_level(item)
                    temp_obj.append(item)
            #Non iterable or not string
            else:
                temp_obj = obj
            return temp_obj

    return next_level(dict_object)
"""

def generate_hpp_sig(dict_object, hmac_key):

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

    print signing_string

    hm = hmac.new(hmac_key, signing_string, hashlib.sha256)
    return base64.b64encode(hm.digest())

"""
class dotdict(dict):
    def __init__(self, d="",**kwargs):
        #super(dotdict, self).__init__(self,dictionary)
        if kwargs:
            #print(kwargs)
            for k, v in kwargs.iteritems():
                setattr(self, k, v)
        if d:
            for k,v in d.iteritems():
                #print'k:\n',k,'\nv:\n',v
                setattr(self,k,v)

    def __setattr__(self, attr, value):
        def recur(list_obj):
            #print 'ddr:'
            #print(list_obj)
            list_sub_obj = []
            for elem in list_obj:
                #print 'ddr.e:\n',elem
                if isinstance(elem,dict):
                    list_sub_obj.append(dotdict(elem))
                elif isinstance(elem,(list,tuple)):
                    list_sub_obj.append(recur(elem))
                else:
                    list_sub_obj.append(elem)
            #print 'ddr.end:\n',list_sub_obj
            return list_sub_obj

        if isinstance(value, dict):
            value = dotdict(value)
        elif isinstance(value, (list,tuple)):
            value = recur(value)
        #print'set a:\n',attr,'\nv:\n',value
        super(dotdict, self).__setattr__(attr, value)
        super(dotdict, self).__setitem__(attr, value)

    def __getattr__(self, attr):
        attr = underscore_to_camelcase(attr)
        return self[attr]


    __setitem__ = __setattr__
    #__getattr__ = dict.__getitem__

"""
