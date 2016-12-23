from .exceptions import (
    AdyenAPICommunicationError,
    AdyenAPIAuthenticationError,
    AdyenAPIInvalidPermission,
    AdyenAPIValidationError,
    AdyenInvalidRequestError
)
from .client import AdyenClient
from .validation import (
    require_request_value,
    request_required,
    AMOUNT,
    MODAMOUNT,
    ORIGREF,
    SHOPPERREF,
    SHOPPEREMAIL,
    REFERENCE
)
import logging
from adyen_log import logname,getlogger
logger = logging.getLogger(logname())

class AdyenBase(object):
    def __setattr__(self, attr, value):
        client_attr = ["username","password","platform",
            "review_payout_username","review_payout_password",
            "store_payout_username","store_payout_password"]
        if attr in client_attr:
            if value:
                self.client[attr] = value
        else:
            super(AdyenBase, self).__setattr__(attr, value)

    def __getattr__(self,attr):
        client_attr = ["username","password","platform",
            "review_payout_username","review_payout_password",
            "store_payout_username","store_payout_password"]
        if attr in client_attr:
            return self.client[attr]

class AdyenServiceBase(AdyenBase):
    def __init__(self, client=""):
        if client:
            self.client = client
        else:
            self.client = AdyenAPIClient()

class AdyenRecurring(AdyenServiceBase):
    """This represents the Adyen API Recurring Service.

    API calls currently implemented: listRecurringDetails and disable. Please
    refer to the Recurring Manual for specifics around the API.
    https://docs.adyen.com/developers/recurring-manual

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """
    def __init__(self, client=""):
        super(AdyenRecurring,self).__init__(client=client)
        self.service = "Recurring"

    #@request_required
    #@require_request_value(SHOPPERREF)
    def list_recurring_details(self, request="", **kwargs):

        print request
        action = "listRecurringDetails"

        if "shopperReference" not in request:
            raise ValueError("Include property 'shopperReference' in request to get recurring details.")

        result = self.client.call_api(request, self.service, action, **kwargs)

        recurringDetails = []

        print result
        """
        #This adds the details to be accessed via "RecurringDetail"
        for detail in result.details:
            recurringDetails.append(detail["RecurringDetail"])

        result.message['recurringDetails'] = recurringDetails
        """

        return result

    #@request_required
    def disable(self, request="",**kwargs):
        print request
        action = "disable"
        return self.client.call_api(request, self.service, action, **kwargs)

class AdyenHPP(AdyenServiceBase):
    """This represents the Adyen HPP  Service.

    This currently only implements the directory_lookup request which will
    return the list of payment methods available for given shopper. Please
    refer to the HPP manual and the directory lookup section for the specifics.
    https://docs.adyen.com/developers/hpp-manual#directorylookup

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """
    def __init__(self, client=""):
        super(AdyenHPP,self).__init__(client=client)

    @request_required
    def directory_lookup(self,request="",**kwargs):
        action = "directory"

        return self.client.call_hpp(request,action)

    @request_required
    def hpp_payment(self,request="",**kwargs):

        if 'brandCode' in request:
            if request['brandCode'] != "":
                action = "pay"
        else:
            action = "select"

        logger.info('Adyen Services - Hpp payment')

        # Encode to UTF 8:
        for xf in request:
            request[xf] = request[xf].encode("utf-8")

        if 'issuerId' not in request:
            request['issuerId'] = ""
        if 'merchantReturnData' not in request:
            request['merchantReturnData'] = ""
        if type(request['sessionValidity']) is not str:
            errorstring = 'HPP: sessionValidity must be type of str, use datetime.strftime to convert and format.'
            logger.error(type(request[sessionValidity]))
            raise TypeError(errorstring)
        if 'paymentAmount' not in request:
            errorstring = 'HPP: Include paymentAmount key/value in hpp_payment dict'
            raise ValueError(errorstring)
        if 'countryCode' not in request:
            errorstring = 'HPP: Advised to include countryCode with request to make sure local payment methods are found.'
            print(errorstring)
        if all (k in request for k in ("shopperEmail","shopperReference","recurringContract")):
            recc = request['recurringContract']
            if recc != 'ONECLICK' and recc != 'RECURRING' and recc != 'ONECLICK,RECURRING':
                raise ValueError("HPP: recurringContract must be on of the following values: 'ONECLICK', 'RECURRING', 'ONECLICK,RECURRING'")

        result = self.client.hpp_payment(request,action)
        return result

class AdyenPayment(AdyenServiceBase):
    """This represents the Adyen API Payment Service.

    API calls currently implemented:
        authorise
        authorise3d
        cancel
        capture
        refund
        cancelOrRefund
    Please refer to the Recurring Manual for specifics around the API.
    https://docs.adyen.com/developers/recurring-manual

    The AdyenPayment class, is accessible as adyen.payment.method(args)

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """
    def __init__(self,client=""):
        super(AdyenPayment,self).__init__(client=client)
        self.service = "Payment"

    @request_required
    @require_request_value(AMOUNT,REFERENCE)
    def authorise(self, request="", **kwargs):
        action = "authorise"
        #TODO: do some pre-auth validation on authorise

        if 'shopperEmail' in request:
            if request['shopperEmail'] == '':
                raise ValueError('shopperEmail must not be empty when authorising recurring contracts.')
        if 'shopperReference' in request:
            if request['shopperReference'] == '':
                raise ValueError('shopperReference must not be empty when authorising recurring contracts.')

        if 'amount' not in request:
            raise ValueError("Provide an amount object: {'currency':'USD','value':100} under key 'amount' in the request dict, to perform a payment authorisation.")

        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    def authorise3d(self, request="", **kwargs):
        action = "authorise3d"

        #TODO: perform pre-auth validation
        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    @require_request_value(ORIGREF)
    def cancel(self, request="", **kwargs):
        action = "cancel"

        #TODO: set up prevalidation
        logger.info('Adyen - CANCEL')

        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    def capture(self, request="", **kwargs):
        action = "capture"
        if 'modificationAmount' not in request:
            raise KeyError("Include 'modificationAmount':{'currency':'USD','value':100} object in request. \n( example values used, replace with original payment currency and amount to be captured. )")
        if 'originalReference' not in request:
            raise KeyError("Include 'originalReference' str in request. It is the psp reference of the payment to be modified.")
        #TODO: set up prevalidation
        logger.info('Adyen - CAPTURE')
        response = self.client.call_api(request,self.service,action,**kwargs)
        return response

    @request_required
    @require_request_value(MODAMOUNT, ORIGREF)
    def refund(self, request="", **kwargs):
        action = "refund"
        #TODO: set up prevalidation
        logger.info('Adyen - REFUND')
        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    @require_request_value(ORIGREF)
    def cancel_or_refund(self, request="", **kwargs):
        action = "cancelOrRefund"
        #TODO: set up prevalidation
        logger.info('Adyen - CANCEL or REFUND')
        return self.client.call_api(request, self.service, action, **kwargs)
