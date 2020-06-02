#!/bin/python

from __future__ import absolute_import, division, unicode_literals

import json as json_lib
import re

from . import util
from .httpclient import HTTPClient
from .exceptions import (
    AdyenAPICommunicationError,
    AdyenAPIAuthenticationError,
    AdyenAPIInvalidPermission,
    AdyenAPIValidationError,
    AdyenInvalidRequestError,
    AdyenAPIInvalidFormat,
    AdyenAPIInvalidAmount,
    AdyenEndpointInvalidFormat)
from . import settings


class AdyenResult(object):
    """
    Args:
        message (dict, optional): Parsed message returned from API client.
        status_code (int, optional): Default 200. HTTP response code, ie 200,
            404, 500, etc.
        psp (str, optional): Psp reference returned by Adyen for a payment.
        raw_request (str, optional): Raw request placed to Adyen.
        raw_response (str, optional): Raw response returned by Adyen.

    """

    def __init__(self, message=None, status_code=200,
                 psp="", raw_request="", raw_response=""):
        self.message = message
        self.status_code = status_code
        self.psp = psp
        self.raw_request = raw_request
        self.raw_response = raw_response
        self.details = {}

    def __str__(self):
        return repr(self.message)


class AdyenClient(object):
    """A requesting client that interacts with Adyen. This class holds the
    adyen logic of Adyen HTTP API communication. This is the object that can
    maintain its own username, password, merchant_account, hmac and skin_code.
    When these values aren't within this object, the root adyen module
    variables will be used.

    The public methods, call_api and call_hpp, only return AdyenResult objects.
    Otherwise raising various validation and communication errors.

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

    def __init__(self, username=None, password=None, xapikey=None,
                 review_payout_username=None, review_payout_password=None,
                 store_payout_username=None, store_payout_password=None,
                 platform="test", merchant_account=None,
                 merchant_specific_url=None, skin_code=None,
                 hmac=None,
                 http_force=None, live_endpoint_prefix=None):
        self.username = username
        self.password = password
        self.xapikey = xapikey
        self.review_payout_username = review_payout_username
        self.review_payout_password = review_payout_password
        self.store_payout_username = store_payout_username
        self.store_payout_password = store_payout_password
        self.platform = platform
        self.merchant_specific_url = merchant_specific_url
        self.hmac = hmac
        self.merchant_account = merchant_account
        self.skin_code = skin_code
        self.psp_list = []
        self.LIB_VERSION = settings.LIB_VERSION
        self.USER_AGENT_SUFFIX = settings.LIB_NAME + "/"
        self.http_init = False
        self.http_force = http_force
        self.live_endpoint_prefix = live_endpoint_prefix

    @staticmethod
    def _determine_api_url(platform, service, action):
        """This returns the Adyen API endpoint based on the provided platform,
        service and action.

        Args:
            platform (str): Adyen platform, ie 'live' or 'test'.
            service (str): API service to place request through.
            action (str): the API action to perform.
        """
        base_uri = settings.BASE_PAL_URL.format(platform)
        if service == "Recurring":
            api_version = settings.API_RECURRING_VERSION
        elif service == "Payout":
            api_version = settings.API_PAYOUT_VERSION
        elif service == "BinLookup":
            api_version = settings.API_BIN_LOOKUP_VERSION
        else:
            api_version = settings.API_PAYMENT_VERSION
        return '/'.join([base_uri, service, api_version, action])

    @staticmethod
    def _determine_hpp_url(platform, action):
        """This returns the Adyen HPP endpoint based on the provided platform,
        and action.

        Args:
            platform (str): Adyen platform, ie 'live' or 'test'.
            action (str):   the HPP action to perform.
            possible actions: select, pay, skipDetails, directory
        """
        base_uri = settings.BASE_HPP_URL.format(platform)
        service = action + '.shtml'
        result = '/'.join([base_uri, service])
        return result

    def _determine_checkout_url(self, platform, action):
        """This returns the Adyen API endpoint based on the provided platform,
        service and action.

        Args:
            platform (str): Adyen platform, ie 'live' or 'test'.
            action (str): the API action to perform.
        """
        api_version = settings.API_CHECKOUT_VERSION
        if platform == "test":
            base_uri = settings.ENDPOINT_CHECKOUT_TEST
        elif self.live_endpoint_prefix is not None and platform == "live":
            base_uri = settings.ENDPOINT_CHECKOUT_LIVE_SUFFIX.format(
                self.live_endpoint_prefix)
        elif self.live_endpoint_prefix is None and platform == "live":
            errorstring = """Please set your live suffix. You can set it
                   by running 'settings.
                   ENDPOINT_CHECKOUT_LIVE_SUFFIX = 'Your live suffix'"""
            raise AdyenEndpointInvalidFormat(errorstring)
        else:
            raise AdyenEndpointInvalidFormat("invalid config")

        if action == "paymentsDetails":
            action = "payments/details"
        if action == "paymentsResult":
            action = "payments/result"
        if action == "originKeys":
            api_version = settings.API_CHECKOUT_UTILITY_VERSION

        return '/'.join([base_uri, api_version, action])

    def _review_payout_username(self, **kwargs):
        if 'username' in kwargs:
            return kwargs['username']
        elif self.review_payout_username:
            return self.review_payout_username
        errorstring = """Please set your review payout
        webservice username. You can do this by running
        'Adyen.review_payout_username = 'Your payout username' """
        raise AdyenInvalidRequestError(errorstring)

    def _review_payout_pass(self, **kwargs):
        if 'password' in kwargs:
            return kwargs["password"]
        elif self.review_payout_password:
            return self.review_payout_password
        errorstring = """Please set your review payout
        webservice password. You can do this by running
        'Adyen.review_payout_password = 'Your payout password'"""
        raise AdyenInvalidRequestError(errorstring)

    def _store_payout_username(self, **kwargs):
        if 'username' in kwargs:
            return kwargs['username']
        elif self.store_payout_username:
            return self.store_payout_username
        errorstring = """Please set your store payout
        webservice username. You can do this by running
        'Adyen.store_payout_username = 'Your payout username'"""
        raise AdyenInvalidRequestError(errorstring)

    def _store_payout_pass(self, **kwargs):
        if 'password' in kwargs:
            return kwargs["password"]
        elif self.store_payout_password:
            return self.store_payout_password
        errorstring = """Please set your store payout
        webservice password. You can do this by running
        'Adyen.store_payout_password = 'Your payout password'"""
        raise AdyenInvalidRequestError(errorstring)

    def call_api(self, request_data, service, action, idempotency=False,
                 **kwargs):
        """This will call the adyen api. username, password, merchant_account,
        and platform are pulled from root module level and or self object.
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
        if not self.http_init:
            self.http_client = HTTPClient(self.USER_AGENT_SUFFIX,
                                          self.LIB_VERSION,
                                          self.http_force)
            self.http_init = True

        # username at self object has highest priority. fallback to root module
        # and ensure that it is set.
        xapikey = None
        if self.xapikey:
            xapikey = self.xapikey
        elif 'xapikey' in kwargs:
            xapikey = kwargs.pop("xapikey")

        username = None
        if self.username:
            username = self.username
        elif 'username' in kwargs:
            username = kwargs.pop("username")
        if service == "Payout":
            if any(substring in action for substring in
                   ["store", "submit"]):
                username = self._store_payout_username(**kwargs)
            else:
                username = self._review_payout_username(**kwargs)

        if not username and not xapikey:
            errorstring = """Please set your webservice username.
              You can do this by running
              'Adyen.username = 'Your username'"""
            raise AdyenInvalidRequestError(errorstring)
            # password at self object has highest priority.
            # fallback to root module
            # and ensure that it is set.

        password = None
        if self.password and not xapikey:
            password = self.password
        elif 'password' in kwargs:
            password = kwargs.pop("password")
        if service == "Payout":
            if any(substring in action for substring in
                   ["store", "submit"]):
                password = self._store_payout_pass(**kwargs)
            else:
                password = self._review_payout_pass(**kwargs)

        if not password and not xapikey:
            errorstring = """Please set your webservice password.
              You can do this by running
              'Adyen.password = 'Your password'"""
            raise AdyenInvalidRequestError(errorstring)
            # xapikey at self object has highest priority.
            # fallback to root module
            # and ensure that it is set.

        # platform at self object has highest priority. fallback to root module
        # and ensure that it is set to either 'live' or 'test'.
        platform = None
        if self.platform:
            platform = self.platform
        elif 'platform' in kwargs:
            platform = kwargs.pop('platform')

        if not isinstance(platform, str):
            errorstring = "'platform' value must be type of string"
            raise TypeError(errorstring)
        elif platform.lower() not in ['live', 'test']:
            errorstring = "'platform' must be the value of 'live' or 'test'"
            raise ValueError(errorstring)

        message = request_data

        if not message.get('merchantAccount'):
            message['merchantAccount'] = self.merchant_account

        # Add application info
        if 'applicationInfo' in request_data:
            request_data['applicationInfo'].update({
                "adyenLibrary": {
                    "name": settings.LIB_NAME,
                    "version": settings.LIB_VERSION
                }
            })
        else:
            request_data['applicationInfo'] = {
                "adyenLibrary": {
                    "name": settings.LIB_NAME,
                    "version": settings.LIB_VERSION
                }
            }
        # Adyen requires this header to be set and uses the combination of
        # merchant account and merchant reference to determine uniqueness.
        headers = {}
        if idempotency:
            headers['Pragma'] = 'process-retry'

        url = self._determine_api_url(platform, service, action)

        if xapikey:
            raw_response, raw_request, status_code, headers = \
                self.http_client.request(url, json=request_data,
                                         xapikey=xapikey, headers=headers,
                                         **kwargs)
        else:
            raw_response, raw_request, status_code, headers = \
                self.http_client.request(url, json=message, username=username,
                                         password=password,
                                         headers=headers,
                                         **kwargs)

        # Creates AdyenResponse if request was successful, raises error if not.
        adyen_result = self._handle_response(url, raw_response, raw_request,
                                             status_code, headers, message)

        return adyen_result

    def call_hpp(self, message, action, hmac_key="", **kwargs):
        """This will call the adyen hpp. hmac_key and platform are pulled from
        root module level and or self object.
        AdyenResult will be returned on 200 response.
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
                :param message:
                :param hmac_key:
        """
        if not self.http_init:
            self.http_client = HTTPClient(self.USER_AGENT_SUFFIX,
                                          self.LIB_VERSION,
                                          self.http_force)
            self.http_init = True

        # hmac provided in function has highest priority. fallback to self then
        # root module and ensure that it is set.
        hmac = hmac_key
        if self.hmac:
            hmac = self.hmac
        elif not hmac:
            errorstring = """Please set an hmac with your Adyen.Adyen
            class instance.
            'Adyen.hmac = \"!WR#F@...\"' or as an additional
             parameter in the function call ie.
            'Adyen.hpp.directory_lookup(hmac=\"!WR#F@...\"'. Please reach
            out to support@Adyen.com if the issue persists."""
            raise AdyenInvalidRequestError(errorstring)

        # platform provided in self has highest priority,
        # fallback to root module and ensure that it is set.
        platform = self.platform
        if not isinstance(platform, str):
            errorstring = "'platform' must be type string"
            raise TypeError(errorstring)
        elif platform.lower() not in ['live', 'test']:
            errorstring = " 'platform' must be the value of 'live' or 'test' "
            raise ValueError(errorstring)

        if 'skinCode' not in message:
            message['skinCode'] = self.skin_code

        if 'merchantAccount' not in message:
            message['merchantAccount'] = self.merchant_account
        if message['merchantAccount'] == "":
            message['merchantAccount'] = self.merchant_account

        message["merchantSig"] = util.generate_hpp_sig(message, hmac)

        url = self._determine_hpp_url(platform, action)

        raw_response, raw_request, status_code, headers = \
            self.http_client.request(url, data=message,
                                     username="", password="", **kwargs)

        # Creates AdyenResponse if request was successful, raises error if not.
        adyen_result = self._handle_response(url, raw_response, raw_request,
                                             status_code, headers, message)
        return adyen_result

    def call_checkout_api(self, request_data, action, **kwargs):
        """This will call the checkout adyen api. xapi key merchant_account,
        and platform are pulled from root module level and or self object.
        AdyenResult will be returned on 200 response. Otherwise, an exception
        is raised.

        Args:
            request_data (dict): The dictionary of the request to place. This
                should be in the structure of the Adyen API.
                https://docs.adyen.com/developers/checkout/api-integration
            service (str): This is the API service to be called.
            action (str): The specific action of the API service to be called
        """
        if not self.http_init:
            self.http_client = HTTPClient(self.USER_AGENT_SUFFIX,
                                          self.LIB_VERSION,
                                          self.http_force)
            self.http_init = True

        # xapi at self object has highest priority. fallback to root module
        # and ensure that it is set.
        xapikey = False
        if self.xapikey:
            xapikey = self.xapikey
        elif 'xapikey' in kwargs:
            xapikey = kwargs.pop("xapikey")

        if not xapikey:
            errorstring = """Please set your webservice xapikey.
             You can do this by running 'Adyen.xapikey = 'Your xapikey'"""
            raise AdyenInvalidRequestError(errorstring)

        # platform at self object has highest priority. fallback to root module
        # and ensure that it is set to either 'live' or 'test'.
        platform = None
        if self.platform:
            platform = self.platform
        elif 'platform' in kwargs:
            platform = kwargs.pop('platform')

        if not isinstance(platform, str):
            errorstring = "'platform' value must be type of string"
            raise TypeError(errorstring)
        elif platform.lower() not in ['live', 'test']:
            errorstring = "'platform' must be the value of 'live' or 'test'"
            raise ValueError(errorstring)

        if not request_data.get('merchantAccount'):
            request_data['merchantAccount'] = self.merchant_account

        if 'applicationInfo' in request_data:
            request_data['applicationInfo'].update({
                "adyenLibrary": {
                    "name": settings.LIB_NAME,
                    "version": settings.LIB_VERSION
                }
            })
        else:
            request_data['applicationInfo'] = {
                "adyenLibrary": {
                    "name": settings.LIB_NAME,
                    "version": settings.LIB_VERSION
                }
            }
        # Adyen requires this header to be set and uses the combination of
        # merchant account and merchant reference to determine uniqueness.
        headers = {}

        url = self._determine_checkout_url(platform, action)

        raw_response, raw_request, status_code, headers = \
            self.http_client.request(url, json=request_data,
                                     xapikey=xapikey, headers=headers,
                                     **kwargs)

        # Creates AdyenResponse if request was successful, raises error if not.
        adyen_result = self._handle_response(url, raw_response, raw_request,
                                             status_code, headers,
                                             request_data)

        return adyen_result

    def hpp_payment(self, request_data, action, hmac_key="", **kwargs):

        if not self.http_init:
            self.http_client = HTTPClient(self.USER_AGENT_SUFFIX,
                                          self.LIB_VERSION,
                                          self.http_force)
            self.http_init = True

        platform = self.platform
        if not isinstance(platform, str):
            errorstring = "'platform' must be type string"
            raise TypeError(errorstring)
        elif platform.lower() not in ['live', 'test']:
            errorstring = " 'platform' must be the value of 'live' or 'test' "
            raise ValueError(errorstring)

        if 'skinCode' not in request_data:
            request_data['skinCode'] = self.skin_code

        hmac = self.hmac

        if 'merchantAccount' not in request_data:
            request_data['merchantAccount'] = self.merchant_account
        if request_data['merchantAccount'] == "":
            request_data['merchantAccount'] = self.merchant_account

        request_data["merchantSig"] = util.generate_hpp_sig(request_data, hmac)

        url = self._determine_hpp_url(platform, action)

        adyen_result = {
            'url': url,
            'message': request_data
        }

        return adyen_result

    def _handle_response(self, url, raw_response, raw_request,
                         status_code, headers, request_dict):
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
            # If the result can't be parsed into json, most likely is raw html.
            # Some response are neither json or raw html, handle them here:
            if raw_response:
                response = json_lib.loads(raw_response)
            # Pass raised error to error handler.
            self._handle_http_error(url, response, status_code,
                                    headers.get('pspReference'),
                                    raw_request, raw_response,
                                    headers, request_dict)

            try:
                if response['errorCode']:
                    raise AdyenAPICommunicationError(
                        "Unexpected error while communicating with Adyen."
                        " Received the response data:'{}', HTTP Code:'{}'. "
                        "Please reach out to support@adyen.com if the "
                        "problem persists with the psp:{}".format(
                            raw_response,
                            status_code,
                            headers.get('pspReference')),
                        status_code=status_code,
                        raw_request=raw_request,
                        raw_response=raw_response,
                        url=url,
                        psp=headers.get('pspReference'),
                        headers=headers,
                        error_code=response['errorCode'])
            except KeyError:
                erstr = 'KeyError: errorCode'
                raise AdyenAPICommunicationError(erstr)
        else:
            try:
                response = json_lib.loads(raw_response)
                psp = headers.get('pspReference', response.get('pspReference'))
                return AdyenResult(message=response, status_code=status_code,
                                   psp=psp, raw_request=raw_request,
                                   raw_response=raw_response)
            except ValueError:
                # Couldn't parse json so try to pull error from html.

                error = self._error_from_hpp(raw_response)

                message = request_dict

                reference = message.get("reference",
                                        message.get("merchantReference"))

                errorstring = """Unable to retrieve payment "
                list. Received the error: {}. Please verify your request "
                and try again. If the issue persists, please reach out to "
                support@adyen.com including the "
                merchantReference: {}""".format(error, reference),

                raise AdyenInvalidRequestError(errorstring)

    def _handle_http_error(self, url, response_obj, status_code, psp_ref,
                           raw_request, raw_response, headers, message):
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
            if url == self.merchant_specific_url:
                erstr = "Received a 404 for url:'{}'. Please ensure that" \
                        " the custom merchant specific url is correct" \
                    .format(url)
                raise AdyenAPICommunicationError(erstr,
                                                 error_code=response_obj.get(
                                                     "errorCode"))
            else:
                erstr = "Unexpected error while communicating with Adyen." \
                        " Please reach out to support@adyen.com" \
                        " if the problem persists"
                raise AdyenAPICommunicationError(erstr,
                                                 raw_request=raw_request,
                                                 raw_response=raw_response,
                                                 url=url,
                                                 psp=psp_ref,
                                                 headers=headers,
                                                 error_code=response_obj.get(
                                                     "errorCode"))
        elif status_code == 400:
            erstr = "Received validation error with errorCode: %s," \
                    " message: %s, HTTP Code: %s. Please verify" \
                    " the values provided. Please reach out" \
                    " to support@adyen.com if the problem persists," \
                    " providing the PSP reference: %s" % (
                        response_obj["errorCode"], response_obj["message"],
                        status_code, psp_ref)

            raise AdyenAPIValidationError(erstr, error_code=response_obj.get(
                "errorCode"))
        elif status_code == 401:
            erstr = "Unable to authenticate with Adyen's Servers." \
                    " Please verify the credentials set with the Adyen base" \
                    " class. Please reach out to your Adyen Admin" \
                    " if the problem persists"
            raise AdyenAPIAuthenticationError(erstr,
                                              error_code=response_obj.get(
                                                  "errorCode"))
        elif status_code == 403:

            if response_obj.get("message") == "Invalid Merchant Account":
                erstr = ("You provided the merchant account:'%s' that"
                         " doesn't exist or you don't have access to it.\n"
                         "Please verify the merchant account provided. \n"
                         "Reach out to support@adyen.com"
                         " if the issue persists") \
                        % raw_request['merchantAccount']
                raise AdyenAPIInvalidPermission(erstr,
                                                error_code=response_obj.get(
                                                    "errorCode"))

            erstr = "Unable to perform the requested action. message: %s." \
                    " If you think your webservice user: %s might not have" \
                    " the necessary permissions to perform this request." \
                    " Please reach out to support@adyen.com, providing" \
                    " the PSP reference: %s" % (
                        response_obj["message"], self.username, psp_ref)
            raise AdyenAPIInvalidPermission(erstr, error_code=response_obj.get(
                "errorCode"))
        elif status_code == 422:
            if response_obj.get("message") == "Invalid amount specified":
                raise AdyenAPIInvalidAmount(
                    "Invalid amount specified"
                    "Amount may be improperly formatted, too small or too big."
                    "If the issue persists, contact support@adyen.com",
                    error_code=response_obj.get("errorCode"))

        elif status_code == 500:
            if response_obj.get("errorType") == "validation":
                err_args = (response_obj.get("errorCode"),
                            response_obj.get("message"),
                            status_code)
                erstr = "Received validation error with errorCode: %s," \
                        " message: %s, HTTP Code: %s. Please verify" \
                        " the values provided." % err_args
                raise AdyenAPIValidationError(erstr,
                                              error_code=response_obj.get(
                                                  "errorCode"))

            if response_obj.get("message") == "Failed to serialize node " \
                                              "Failed to parse [123.34]" \
                                              " as a Long":
                raise AdyenAPIInvalidFormat(
                    "The payment amount must be set in cents,"
                    " and can not contain commas or points.",
                    error_code=response_obj.get("errorCode")
                )
        else:
            raise AdyenAPICommunicationError(
                "Unexpected error while communicating with Adyen. Received the"
                " response data:'{}', HTTP Code:'{}'. Please reach out to "
                "support@adyen.com if the problem persists"
                " with the psp:{}".format(raw_response, status_code, psp_ref),
                status_code=status_code,
                raw_request=raw_request,
                raw_response=raw_response,
                url=url,
                psp=psp_ref,
                headers=headers, error_code=response_obj.get("errorCode"))

    @staticmethod
    def _error_from_hpp(html):
        # Must be updated when Adyen response is changed:
        match_obj = re.search(r'>Error:\s*(.*?)<br', html)
        if match_obj:
            return match_obj.group(1)
