import datetime
import util
from .client import AdyenClient
import validation
import logging
from adyen_log import logname,getlogger
logger = logging.getLogger(logname())

class AdyenBase(object):
    def __setattr__(self, attr, value):
        client_attr = ["username","password","platform"]
        if attr in client_attr:
            if value:
                self.client[attr] = value
        else:
            super(AdyenBase, self).__setattr__(attr, value)

    def __getattr__(self,attr):
        client_attr = ["username","password","platform"]
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

    def list_recurring_details(self, request="", **kwargs):

        action = "listRecurringDetails"

        if validation.check_in(request,action):
            return self.client.call_api(request, self.service, action, **kwargs)

    def disable(self, request="",**kwargs):

        action = "disable"

        if validation.check_in(request,action):
            if 'recurringDetailReference' not in request:
                raise ValueError("Include a 'recurringDetailReference' to disable a specific recurring contract.")
            else:
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

    def directory_lookup(self,request="",**kwargs):

        action = "directory"

        if validation.check_in(request,action):
            try:
                datetime.datetime.strptime(request['sessionValidity'],'%Y-%m-%dT%H:%M:%SZ')
            except ValueError:
                raise ValueError("Incorrect date format, should be Y-m-dH:M:SZ, use datetime.strftime('%Y-%m-%dT%H:%M:%SZ') to format a datetime object.")

            return self.client.call_hpp(request,action)

    def hpp_payment(self,request="",skipDetails=None,**kwargs):

        if skipDetails == True:
            action = "skipDetails"
        else:
            action = "select"

        if validation.check_in(request,action):

            if action == "skipDetails":
                if "issuerId" not in request:
                    request['issuerId'] = ""
            if type(request['sessionValidity']) is not str:
                raise TypeError('HPP: sessionValidity must be type of str, use datetime.strftime to convert and format.')
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

    def authorise(self, request="", **kwargs):

        action = "authorise"

        if validation.check_in(request,action):
            if 'shopperEmail' in request:
                if request['shopperEmail'] == '':
                    raise ValueError('shopperEmail must contain the shopper email when authorising recurring contracts.')
            if 'shopperReference' in request:
                if request['shopperReference'] == '':
                    raise ValueError('shopperReference must contain the shopper name when authorising recurring contracts.')

            return self.client.call_api(request, self.service, action, **kwargs)

    def authorise3d(self, request="", **kwargs):
        action = "authorise3d"

        if validation.check_in(request,action):
            return self.client.call_api(request, self.service, action, **kwargs)

    def cancel(self, request="", **kwargs):
        action = "cancel"

        if validation.check_in(request,action):
            return self.client.call_api(request, self.service, action, **kwargs)

    def capture(self, request="", **kwargs):

        action = "capture"

        if validation.check_in(request,action):
            if request['modificationAmount']["value"] == "" or request['modificationAmount']['value'] == "0":
                raise ValueError("Set the 'modificationAmount' to the original transaction amount, or less for a partial capture. modificationAmount should be an object with the following keys: {'currency':,'value':}")
            if request['originalReference'] == "":
                raise ValueError("Set the 'originalReference' to the psp reference of the transaction to be modified")

            response = self.client.call_api(request,self.service,action,**kwargs)
            return response

    def refund(self, request="", **kwargs):

        action = "refund"

        print "REFUND:"
        print request

        if validation.check_in(request,action):
            if request['modificationAmount']['value'] == "" or request['modificationAmount']['value'] == "0":
                raise ValueError("To refund this payment, provide the original value. Set the value to less than the original amount, to partially refund this payment.")
            else:
                return self.client.call_api(request, self.service, action, **kwargs)

    def cancel_or_refund(self, request="", **kwargs):
        action = "cancelOrRefund"

        if validation.check_in(request,action):
            return self.client.call_api(request, self.service, action, **kwargs)
