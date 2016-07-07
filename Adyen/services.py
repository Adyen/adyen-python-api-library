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




class AdyenClientAttr(object):
    def __setattr__(self, attr, value):
        client_attr = ["username", "password","review_payout_username",
            "review_payout_password","store_payout_username",
            "store_payout_password","platform","merchant_specific_url",
            "hmac","merchant_account","skin_code"]
        if attr in client_attr:
            self.client.__setattr__(attr, value)
        else:
            super(AdyenClientAttr, self).__setattr__(attr, value)

    def __getattr__(self,attr):
        client_attr = ["username", "password","review_payout_username",
            "review_payout_password","store_payout_username",
            "store_payout_password","platform","merchant_specific_url",
            "hmac","merchant_account","skin_code"]
        if attr in client_attr:
            return self.client.__getattribute__(attr)

class AdyenServiceBase(AdyenClientAttr):
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

    @request_required
    @require_request_value(SHOPPERREF)
    def list_recurring_details(self, request="", **kwargs):
        action = "listRecurringDetails"
        #TODO: prevalidation
        result = self.client.call_api(request, self.service, action, **kwargs)

        #If not valid shopper reference, list recurring details returns empty 
        #object.
        if hasattr(result, "details"):
            recurringDetails = []
            #This adds the details to be accessed via "RecurringDetail"
            for detail in result.details:
                recurringDetails.append(detail["RecurringDetail"])
            result.recurringDetails = recurringDetails
        return result


    @request_required
    def disable(self, request="",**kwargs):
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

class AdyenPayment(AdyenServiceBase):
    """This represents the Adyen API Payment Service.

    API calls currently implemented: 
        authorise 
        authorise3d
        cancel
        capture
        refund
        cancelOrRefund
        refundWithData
    Please refer to the Recurring Manual for specifics around the API.
    https://docs.adyen.com/developers/recurring-manual

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
        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    @require_request_value(MODAMOUNT, ORIGREF)
    def capture(self, request="", **kwargs):
        action = "capture"
        #TODO: set up prevalidation
        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    @require_request_value(MODAMOUNT, ORIGREF)
    def refund(self, request="", **kwargs):
        action = "refund"
        #TODO: set up prevalidation
        return self.client.call_api(request, self.service, action, **kwargs)    

    @request_required
    @require_request_value(ORIGREF)
    def cancel_or_refund(self, request="", **kwargs):
        action = "cancelOrRefund"
        #TODO: set up prevalidation
        return self.client.call_api(request, self.service, action, **kwargs)  

    @request_required
    def refund_with_data(self, request="", **kwargs):
        action = "refundWithData"
        #TODO: set up prevalidation
        return self.client.call_api(request, self.service, action, **kwargs)  


class AdyenPayout(AdyenServiceBase):
    """This represents the Adyen API Payout Service.

    API calls currently implemented: 
        
    Please refer to the Payout Manual for specifics around the API.
    https://docs.adyen.com/developers/recurring-manual

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """
    def __init__(self, client=""):
        super(AdyenPayout,self).__init__(client=client)
        self.service = "Payout"

    @request_required
    def store_detail(self, request="", **kwargs):
        action = "storeDetail"

        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    @require_request_value(AMOUNT,SHOPPERREF,SHOPPEREMAIL)
    def store_detail_and_submit(self, request="", **kwargs):
        action = "storeDetailAndSubmit"
        
        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    @require_request_value(AMOUNT,SHOPPERREF,SHOPPEREMAIL)
    def submit(self, request="", **kwargs):
        action = 'submit'

        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    @require_request_value(ORIGREF)
    def confirm(self, request="", **kwargs):
        action = "confirm"

        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    @require_request_value(ORIGREF)
    def decline(self, request="", **kwargs):
        action = "decline"

        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    @require_request_value(AMOUNT,SHOPPERREF,SHOPPEREMAIL)
    def submit_third_party(self, request="", **kwargs):
        action = "submitThirdParty"

        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    @require_request_value(AMOUNT,SHOPPERREF,SHOPPEREMAIL)
    def store_detail_and_submit_third_party(self, request="", **kwargs):
        action = "storeDetailAndSubmitThirdParty"
        
        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    @require_request_value(ORIGREF)
    def confirm_third_party(self, request="", **kwargs):
        action = "confirmThirdParty"

        return self.client.call_api(request, self.service, action, **kwargs)

    @request_required
    @require_request_value(ORIGREF)
    def decline_third_party(self, request="", **kwargs):
        action = "declineThirdParty"

        return self.client.call_api(request, self.service, action, **kwargs)


