from .exceptions import AdyenInvalidRequestError
from functools import wraps
# from .util import under_to_camel_dict
import logging
from adyen_log import logname,getlogger
logger = logging.getLogger(logname())

AMOUNT = "amount"
REFERENCE = "reference"
MODAMOUNT = "modificationAmount"
ORIGREF = "originalReference"
SHOPPEREMAIL = "shopperEmail"
SHOPPERREF = "shopperReference"

ERR_MSGS = {'amount' : "Please provide an amount in your request. ex: "+
                "'amount':{'currency':'USD','value':100}",
            'reference' : "Please provide a reference in your request. ex: "+
                "'reference':'yourUniqureReference123'",
            'modificationAmount': "Please provide a modificationAmount in your "+
                "request. ex: 'amount':{'currency':'USD','value':100}",
            'originalReference' : "Please provide the pspReference of the "+
                "original payment via the value 'originalReference'",
            'shopperEmail' : "Please provide a shopperEmail in your request."+
                " ex: 'shopperEmail':'shopper@adyen.com'",
            'shopperReference' : "Please provide a shopperReference in your "+
                "request. ex. 'shopperReference':'reference12345'"
}

#Ensure value is in request object
def require_request_value(*required_values):
    def wrapper(func):
        def decorated(*args,**kwargs):
            for value in required_values:
                # compare_request = under_to_camel_dict(kwargs["request"])
                if value not in kwargs["request"]:
                    raise AdyenInvalidRequestError(ERR_MSGS[value])
            return func(*args,**kwargs)
        return wraps(func)(decorated)
    return wrapper

#Ensure that "request" was a parameter.
def request_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        if 'request' in kwargs:
            if not kwargs['request']:
                raise TypeError("You need to provide a valid dictionary request"
                            " object. This could contain information in the "
                            "currency, amount, card details and so on. Please "
                            "reach out to support@adyen.com if you have more "
                            "questions.")
        return f(*args, **kwargs)
    return decorated

#Ensure store payout user exists and not null
def store_payout_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        if 'request' in kwargs:
            if not kwargs['request']:
                raise TypeError("You need to provide a valid dictionary request"
                            " object. This could contain information in the "
                            "currency, amount, card details and so on. Please "
                            "reach out to support@adyen.com if you have more "
                            "questions.")
        return f(*args, **kwargs)
    return decorated
