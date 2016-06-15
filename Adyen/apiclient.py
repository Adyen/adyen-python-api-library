#!/bin/python
import json as json_lib
import re

from . import util
from .httpclient import HTTPClient
from .exceptions import (
    AdyenAPICommunicationError, 
    AdyenAPIAuthenticationError, 
    AdyenAPIInvalidPermission,
    AdyenAPIValidationError, 
    AdyenInvalidRequestError)

BASE_PAL_url = "https://pal-{}.adyen.com/pal/servlet"
BASE_HPP_url = "https://{}.adyen.com/hpp"
API_VERSION = "v12"
API_CLIENT_ATTR = ["username","password","review_payout_user",
    "review_payout_password","confirm_payout_user","confirm_payout_password",
    "platform","merchant_account","merchant_specific_url","hmac"]

class AdyenResult(object):
    """Conatiner of the information returned by an API request. if message is
    a dict, it is converted into a dotdict which allows all values within it 
    to be accessed via dot notation. This allows this object to be referenced
    like "result.recurringDetails.detail.recurringDetailReference". 

    __setattr__ and __getattr__ have been overridden to allow the assigning and
    retrieving of values via dotnotation and snake case or camcel case. All 
    snake_case is convereted to camelCase. All "message" values are stored
    camelCase as is received from Adyen.

    Args:
        message (dict, optional): Parsed message returned from API client.
        status_code (int, optional): Default 200. HTTP response code, ie 200, 
            404, 500, etc.
        psp (str, optional): Psp reference returned by Adyen for a payment.
        raw_request (str, optionl): Raw request placed to Adyen.
        raw_response (str, optional): Raw response returned by Adyen.
  
    """

    def __init__(self, 
            message=None,
            status_code=200, 
            psp="",
            raw_request="",
            raw_response=""):
        if isinstance(message,dict):
            #Converting dict to the dotdict
            message = util.dotdict(message)
        self.message = message
        self.status_code = status_code
        self.psp = psp
        self.raw_request=raw_request
        self.raw_response=raw_response

    def __setattr__(self, attr, value):
        super(AdyenResult, self).__setattr__(attr, value)

    def __getattr__(self, attr):
        #This is to ensure that underscore get attrrequests are converted to 
        #camelcase so result.psp_reference will return the same value as 
        #result.pspReference.
        attr = util.underscore_to_camelcase(attr)
        if attr in self.message:
            return self.message[attr]
        else:
            raise AttributeError

    def __str__(self):
        return repr(self.message)


class AdyenAPIClient(object):
    """A requesting client that interacts with Adyen. This class holds the adyen
    logic of Adyen HTTP API communication. This is the object that can maintain
    it's own username, password, merchant_account, hmac, and skin_code. When 
    these values aren't within this object, the root adyen module variables will 
    be used.

    The public methods, call_api and call_hpp, only return AdyenResult objects. 
    Otherwise raising verias validation and communication errors.

    Args:
        username (str, optional): Username of webservice user
        password (str, optional): Password of webservice user
        merchant_account (str, optional): Merchant account for requests to be
            placed through
        platform (str, optional): Defaults "test". The Adyen platform to make 
            requests against.
        skin_code (str, optional): skin_code to place directory_lookup requests 
            and generate hpp signatures with.
        hmac (str, optional): Hmac key that is used for signature calculation.
    """
    def __init__(self, username=None, password=None, review_payout_username=None,
        review_payout_password=None, store_payout_username=None,
        store_payout_password=None, platform=None, 
        merchant_account=None, merchant_specific_url=None, skin_code=None, hmac=None):
        self.username=username
        self.password=password
        self.review_payout_username = review_payout_username
        self.review_payout_password = review_payout_password
        self.store_payout_username = store_payout_username
        self.store_payout_password = store_payout_password
        self.platform=platform
        self.merchant_specific_url=merchant_specific_url
        self.hmac=hmac
        self.merchant_account=merchant_account
        self.skin_code=skin_code
        self.http_client = HTTPClient()

    def _determine_api_url(self, platform, service, action):
        """This returns the Adyen API endpoint based on the provided platform,
        service and action.

        Args:
            platform (str): Adyen platform, ie 'live' or 'test'.
            service (str): API service to place request through.
            action (str): the API action to perform.
        """
        base_uri = BASE_PAL_url.format(platform)
        return  '/'.join([base_uri, service, API_VERSION, action]) 

    def _determine_hpp_url(self, platform, action):
        """This returns the Adyen HPP endpoint based on the provided platform,
        and action.

        Args:
            platform (str): Adyen platform, ie 'live' or 'test'.
            action (str):   the HPP action to perform.
        """
        base_uri = BASE_HPP_url.format(platform)
        service = action + '.shtml'
        return  '/'.join([base_uri, service]) 

    def _review_payout_username(self,**kwargs):
        from Adyen import review_payout_username
        if 'username' in kwargs:
            review_payout_username = kwargs['username']
        elif self.review_payout_username:
            review_payout_username = self.review_payout_username
        if not review_payout_username:
            raise AdyenInvalidRequestError("Please set your review payout "
                "webservice username. You can do this by running "
                "'Adyen.review_payout_username = 'Your payout username'")

        return review_payout_username

    def _review_payout_pass(self,**kwargs):
        from Adyen import review_payout_password
        if 'password' in kwargs:
            review_payout_password = kwargs["password"]
        elif self.review_payout_password:
            review_payout_password = self.review_payout_password
        if not review_payout_password:
            raise AdyenInvalidRequestError("Please set your review payout "
                "webservice password. You can do this by running "
                "'Adyen.review_payout_password = 'Your payout password'")

        return review_payout_password

    def _store_payout_username(self,**kwargs):
        from Adyen import store_payout_username
        if 'username' in kwargs:
            store_payout_username = kwargs['username']
        elif self.store_payout_username:
            store_payout_username = self.store_payout_username
        if not store_payout_username:
            raise AdyenInvalidRequestError("Please set your store payout "
                "webservice username. You can do this by running "
                "'Adyen.store_payout_username = 'Your payout username'")

        return store_payout_username

    def _store_payout_pass(self,**kwargs):
        from Adyen import store_payout_password
        if 'password' in kwargs:
            store_payout_password = kwargs["password"]
        elif self.store_payout_password:
            store_payout_password = self.store_payout_password
        if not store_payout_password:
            raise AdyenInvalidRequestError("Please set your store payout "
                "webservice password. You can do this by running "
                "'Adyen.store_payout_password = 'Your payout password'")
            
        return store_payout_password

    def call_api(self, request_data, service, action, idempotency=False, 
        **kwargs):
        """This will call the adyen api. username, password, merchant_account,
        and platform are pulled from root module level and or self object. 
        snake_case keynames of request_date is converted in camelCase.
        AdyenResult will be returned on 200 response. Otherwise, an exception
        is raised.

        Args:
            request_data (dict): The dictionary of the request to place. This 
                should be in the structure of the Adyen API.
                https://docs.adyen.com/manuals/api-manual
            service (str): This is the API service to be called.
            action (str): The specific action of the API service to be called 
            idempotency (bool, optional): Whether the transaction should be 
                processed idempotently. 
                https://docs.adyen.com/manuals/api-manual#apiidempotency
        Returns:
            AdyenResult: The AdyenResult is returned when a request was 
                succesful.
        """
        from Adyen import username, password, merchant_account, platform

        #username at self object has highest priority. fallback to root module
        #and ensure that it is set.
        if 'username' in kwargs:
            username = kwargs["username"]
        elif service == "Payout":
            if any(substring in action for substring in ["store","submit"]):
                username = self._store_payout_username(**kwargs)
            else:
                username = self._review_payout_username(**kwargs)
        elif self.username:
            username=self.username
        if not username:
            raise AdyenInvalidRequestError("Please set your webservice username."
                " You can do this by running 'Adyen.username = 'Your username'")
        #Ensure that username has been removed so as not to be passed to adyen.
        if 'username' in kwargs:
            del kwargs['username']

        #password at self object has highest priority. fallback to root module
        #and ensure that it is set.
        if 'password' in kwargs:
            password = kwargs["password"]
        elif service == "Payout":
            if any(substring in action for substring in ["store","submit"]):
                password = self._store_payout_pass(**kwargs)
            else:
                password = self._review_payout_pass(**kwargs)
        elif self.password:
            password= self.password
        if not password:
            raise AdyenInvalidRequestError("Please set your webservice password."
                " You can do this by running 'Adyen.password = 'Your password'")
        #Ensure that password has been removed so as not to be passed to adyen.
        if 'password' in kwargs:
            del kwargs["password"]

        #platform at self object has highest priority. fallback to root module
        #and ensure that it is set to either 'live' or 'test'.
        if 'platform' in kwargs:
            platform = kwargs['platform']
            del kwargs['platform']
        elif self.platform:
            platform = self.platform
        
        if platform.lower() not in ['live','test']:
            raise ValueError("'platform' must be the value of 'live' or 'test'")
        elif not isinstance(platform, str):
            raise TypeError("'platform' must be type string")

        #convert any keys that have snake_case to camelCase as to match the 
        #Adyen API.
        message = util.under_to_camel_dict(request_data)

        #All API call should have merchantAccount as part of the request.
        #If the merchant account is not in the request, check other locations
        if "merchantAccount" not in message:
            if 'merchant_account' in kwargs:
                message["merchantAccount"] = kwargs["merchant_account"]
                del kwargs["merchant_account"]
            elif self.merchant_account:
                #Try self object
                message["merchantCccount"] = self.merchant_account
            elif merchant_account:
                #Then try root module
                message["merchantAccount"] = merchant_account
            else:
                #merchantAccount has not ben set.
                raise AdyenInvalidRequestError("Please provide a merchant_account"
                    " either in the request or set at Module level Adyen."
                    "merchant_account=\"MerchantAccountName\". Please reach out"
                    " to support@adyen.com if the issue persists.")

        #Adyen requires this header to be set and uses the combination of
        #merchant account and merchant reference to determine uniqueness.
        headers={}
        if idempotency == True:
            headers['Pragma'] = 'process-retry'


        url = self._determine_api_url(platform, service, action)

        raw_response, raw_request, status_code, headers = self.http_client.request(
            url, json = message, username=username, password=password, 
            headers=headers, **kwargs)

        #Creates AdyenResponse if request was successful, raises error if not.
        adyen_result = self._handle_response(url, raw_response, raw_request,
            status_code, headers, message)
        return adyen_result

    def call_hpp(self, request_data, action, hmac_key="", **kwargs):
        """This will call the adyen hpp. hmac_key and platform are pulled from
        root module level and or self object. snake_case keynames of request_date 
        is converted in camelCase. AdyenResult will be returned on 200 response. 
        Otherwise, an exception is raised.

        Args:
            request_data (dict): The dictionary of the request to place. This 
                should be in the structure of the Adyen API.
                https://docs.adyen.com/manuals/api-manual
            service (str): This is the API service to be called.
            action (str): The specific action of the API service to be called 
            idempotency (bool, optional): Whether the transaction should be 
                processed idempotently. 
                https://docs.adyen.com/manuals/api-manual#apiidempotency
        Returns:
            AdyenResult: The AdyenResult is returned when a request was 
                succesful.
        """
        from Adyen import hmac, platform

        #hmac provided in function has highest priority. fallback to self then
        #root module and ensure that it is set.
        if hmac_key:
            hmac = hmac_key
        elif self.hmac:
            hmac = self.hmac
        elif not hmac:
            raise AdyenInvalidRequestError("Please set an hmac either at the "
                "module level 'Adyen.hmac = \"!WR#F@...\"' or as an additional"
                " parameter in the function call ie. "
                "'Adyen.hpp.directory_lookup(hmac=\"!WR#F@...\"'. Please reach "
                "out to support@Adyen.com if the issue persists.")

        #platform provided in self has highest priority, fallback to root module
        #and ensure that it is set.
        if self.platform:
            platform = self.platform
        if platform.lower() not in ['live','test']:
            raise ValueError("'platform' must be the value of 'live' or 'test'")
        elif not isinstance(platform, str):
            raise TypeError("'platform' must be type string")

        #convert any keys that have snake_case to camelCase as to match the 
        #Adyen API.
        message = util.under_to_camel_dict(request_data)

        message["merchantSig"] = util.generate_hpp_sig(message, hmac)

        url = self._determine_hpp_url(platform, action)

        raw_response, raw_request, status_code, headers = self.http_client.request(
            url, data =message, username="", password="", **kwargs)

        #Creates AdyenResponse if request was successful, raises error if not.
        adyen_result = self._handle_response(url, raw_response, raw_request, 
            status_code, headers, message)
        return adyen_result

    def _handle_response(self, url, raw_response, raw_request, status_code,
            headers, request_dict):
        """This parses the content from raw communication, raising an error if
        anything other than 200 was returned.

        Args:
            url (str): URL where request was made
            raw_response (str): The raw communication sent to Adyen
            raw_request (str): The raw response returned by Adyen
            status_code (int): The HTTP status code
            headers (dict): Key/Value of the headers.
            request_dict (dict): The original request dictionary that was given
                to the HTTPClient.

        Returns:
            AdyenResult: Result object if successful.
        """
        if status_code != 200:
            response = {}
            #If the result can't be parsed into json, most likely is raw html.
            try:
                response = json_lib.loads(raw_result)
            except:
                pass

            self._handle_http_error(url, response, status_code, 
                headers.get('pspReference'), raw_request, raw_response, headers)
        else:
            try:
                response = json_lib.loads(raw_response) 
                psp = headers.get('pspReference', response.get('pspReference'))
                return AdyenResult(message = response, status_code = status_code,
                    psp = psp, raw_request = raw_request, 
                    raw_response = raw_response)
            except ValueError:
                #Couldn't parse json so try to pull error from html.
                error = self._error_from_hpp(raw_response)

                reference = message.get("reference", 
                    message.get("merchantReference"))
                raise AdyenInvalidRequestError("Unable to retrieve payment "
                    "list. Received the error: {}. Please verify your request "
                    "and try again. If the issue persists, please reach out to "
                    "support@adyen.com including the "
                    "merchantReference: {}".format(error,reference),
                    raw_request=message,
                    raw_response=raw_response,
                    url=url)

    def _handle_http_error(self, url, response_obj, status_code, psp_ref,
            raw_request, raw_response, headers):
        """This function handles the non 200 responses from Adyen, raising an
        error that should provide more information.

        Args:
            url (str): url of the request
            response_obj (dict): Dict containing the parsed JSON response from
                Adyen
            status_code (int): HTTP status code of the request
            psp_ref (str): Psp reference of the request attempt
            raw_request (str): The raw request placed to Adyen
            raw_response (str): The raw response(body) returned by Adyen
            headers(dict): headers of the response

        Returns: 
            None
        """

        if status_code == 404:
            from Adyen import merchant_specific_url
            if url == merchant_specific_url:
                raise AdyenAPICommunicationError(
                    "Received a 404 for url:'{}'. Please ensure that"
                    " the custom merchant specific url is correct".format(url))
            else:
                raise AdyenAPICommunicationError(
                    "Unexpected error while communicating with Adyen. Please"
                    " reach out to support@adyen.com if the problem persists", 
                    raw_request=raw_request,
                    raw_response=raw_response,
                    url=url,
                    psp=psp_ref,
                    headers=headers)
        elif status_code in [400, 422]:
            raise AdyenAPIValidationError(
                "Received validation error with errorCode:{}, message:'{}', "
                "HTTP Code:'{}'. Please verify the values provided. Please reach"
                " out to support@adyen.com if the problem persists, providing "
                "the PSP reference:{}".format( response_obj.get("errorCode"), 
                    response_obj.get("message"), status_code, psp_ref), 
                result=response_obj, 
                error_code=response_obj.get("errorCode"),
                raw_request=raw_request, 
                raw_response=raw_response, 
                url=url,
                psp=psp_ref, 
                headers=headers, 
                status_code=status_code)
        elif status_code == 401:
            raise AdyenAPIAuthenticationError(
                "Unable to authenticate with Adyen's Servers. Please verify "
                "the username and password of your webservice user. Please "
                "reach out to your Adyen Admin if the problem persists",
                raw_request=raw_request, 
                raw_response=raw_response,
                url=url, 
                psp=psp_ref, 
                headers=headers)
        elif status_code == 403:
            from Adyen import username
            if response_obj.get("message")=="Invalid Merchant Account":
                raise AdyenAPIInvalidPermission(
                    "You provided the merchant account:'{}' that doesn't exist "
                    "or you don't have access to it. Please verify the merchant"
                    " account provided. Reach out to support@adyen.com if the "
                    "issue persists".format(
                        json_lib.loads(raw_request)["merchantAccount"]),
                    raw_request=raw_request, 
                    raw_response=raw_response,
                    url=url, 
                    psp=psp_ref, 
                    headers=headers)
            raise AdyenAPIInvalidPermission(
                "Unable to perform the requested action. message:'{}'. If you "
                "think your webservice user:'{}' might not have the necessary "
                "permissions to perform this request. Please reach out to "
                "support@adyen.com, providing the PSP reference:{}".format(
                    response_obj.get("message"),username, psp_ref),
                raw_request=raw_request, 
                raw_response=raw_response,
                url=url, 
                psp=psp_ref, 
                headers=headers)
        else:
            raise AdyenAPICommunicationError(
                "Unexpected error while communicating with Adyen. Received the "
                "response data:'{}', HTTP Code:'{}'. Please reach out to "
                "support@adyen.com if the problem persists with the psp:{}"
                    .format(raw_response,status_code,psp_ref), 
                status_code=status_code, 
                raw_request=raw_request,
                raw_response=raw_response, 
                url=url, 
                psp=psp_ref, 
                headers=headers)

    def _error_from_hpp(self, html):
        match_obj = re.search('>Error:\s*(.*?)<br', html)
        if match_obj:
            return match_obj.group(1)



