from .exceptions import AdyenInvalidRequestError
from functools import wraps
# from .util import under_to_camel_dict
import logging
from adyen_log import logname,getlogger
logger = logging.getLogger(logname())

actions = {}
actions['listRecurringDetails'] = ["shopperReference"]
actions['disable'] = ["shopperReference"]
actions['directory'] = ["currencyCode","paymentAmount","merchantReference","sessionValidity","shipBeforeDate"]
actions['skipDetails'] = ["sessionValidity","currencyCode","paymentAmount","merchantReference","brandCode","issuerId"]
actions['select'] = ["sessionValidity","currencyCode","paymentAmount","merchantReference"]
actions['authorise'] = ["amount","reference"]
actions['authorise3d'] = ["md","paResponse","browserInfo"]
actions['cancel'] = ["originalReference"]
actions['capture'] = ["modificationAmount","originalReference"]
actions['refund'] = ["modificationAmount","originalReference"]
actions['cancelOrRefund'] = ["originalReference"]

def check_in(request,action):

    # This function checks for missing properties in the request dict
    # for the corresponding action.

    if request:
        action = actions[action]
        missing = []
        for x in action:
            if x not in request:
                missing.append(x)
        if len(missing) > 0:
            missing_string = ""
            for idx,val in enumerate(missing):
                missing_string += "\n" + val
            erstr = "Provide the required request parameters to complete this request: %s" % missing_string
            raise ValueError(erstr)
        else:
            return True
    else:
        req_str = ""
        for idx,val in enumerate(actions[action]):
            req_str += "\n" + val
        erstr = "Provide a request dict with the following properties: %s" % req_str
        raise ValueError(erstr)
