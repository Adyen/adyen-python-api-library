#!/bin/python

from __future__ import absolute_import, division, unicode_literals

import json as json_lib

from . import util
from .httpclient import HTTPClient
from .exceptions import (
    AdyenAPICommunicationError,
    AdyenAPIAuthenticationError,
    AdyenAPIInvalidPermission,
    AdyenAPIValidationError,
    AdyenInvalidRequestError,
    AdyenAPIResponseError,
    AdyenAPIUnprocessableEntity,
    AdyenEndpointInvalidFormat)
from . import settings
from re import match


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
    IDEMPOTENCY_HEADER_NAME = 'Idempotency-Key'
    APPLICATION_INFO_HEADER_NAME = 'adyen-library-name'
    APPLICATION_VERSION_HEADER_NAME = 'adyen-library-version'
    """A requesting client that interacts with Adyen. This class holds the
    adyen logic of Adyen HTTP API communication. This is the object that can
    maintain its own username, password, merchant_account, hmac and skin_code.
    When these values aren't within this object, the root adyen module
    variables will be used.

    The public methods and call_api only return AdyenResult objects.
    Otherwise raising various validation and communication errors.

    Args:
        username (str, optional): Username of webservice user
        password (str, optional): Password of webservice user
        merchant_account (str, optional): Merchant account for requests to be
            placed through
        platform (str, optional): Defaults "test". The Adyen platform to make
            requests against.
        hmac (str, optional): Hmac key that is used for signature calculation.
        http_timeout (int, optional): The timeout in seconds for HTTP calls,
            default 30.
    """

    def __init__(
            self,
            username=None,
            password=None,
            xapikey=None,
            review_payout_username=None,
            review_payout_password=None,
            store_payout_username=None, store_payout_password=None,
            platform="test", merchant_account=None,
            merchant_specific_url=None,
            hmac=None,
            http_force=None,
            live_endpoint_prefix=None,
            http_timeout=30,
            api_bin_lookup_version=None,
            api_checkout_utility_version=None,
            api_checkout_version=None,
            api_management_version=None,
            api_payment_version=None,
            api_payout_version=None,
            api_recurring_version=None,
            api_terminal_version=None,
            api_legal_entity_management_version=None,
            api_data_protection_version=None,
            api_transfers_version=None,
            api_stored_value_version=None,
            api_balance_platform_version=None
    ):
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
        self.psp_list = []
        self.LIB_VERSION = settings.LIB_VERSION
        self.USER_AGENT_SUFFIX = settings.LIB_NAME + "/"
        self.http_init = False
        self.http_force = http_force
        self.live_endpoint_prefix = live_endpoint_prefix
        self.http_timeout = http_timeout
        self.api_bin_lookup_version = api_bin_lookup_version or settings.API_BIN_LOOKUP_VERSION
        self.api_checkout_utility_version = api_checkout_utility_version or settings.API_CHECKOUT_UTILITY_VERSION
        self.api_checkout_version = api_checkout_version or settings.API_CHECKOUT_VERSION
        self.api_management_version = api_management_version or settings.API_MANAGEMENT_VERSION
        self.api_payment_version = api_payment_version or settings.API_PAYMENT_VERSION
        self.api_payout_version = api_payout_version or settings.API_PAYOUT_VERSION
        self.api_recurring_version = api_recurring_version or settings.API_RECURRING_VERSION
        self.api_terminal_version = api_terminal_version or settings.API_TERMINAL_VERSION
        self.api_legal_entity_management_version = api_legal_entity_management_version or settings.API_LEGAL_ENTITY_MANAGEMENT_VERSION
        self.api_data_protection_version = api_data_protection_version or settings.API_DATA_PROTECION_VERSION
        self.api_transfers_version = api_transfers_version or settings.API_TRANSFERS_VERSION
        self.api_stored_value_version = api_stored_value_version or settings.API_STORED_VALUE_VERSION
        self.api_balance_platform_version = api_balance_platform_version or settings.API_BALANCE_PLATFORM_VERSION

    def _determine_base_url_and_version(self, platform, service):

        live_pal_url = settings.PAL_LIVE_ENDPOINT_URL_TEMPLATE
        live_checkout_url = settings.ENDPOINT_CHECKOUT_LIVE_SUFFIX

        if platform == 'live' and self.live_endpoint_prefix:
            live_pal_url = live_pal_url.format(live_prefix=self.live_endpoint_prefix)
            live_checkout_url = live_checkout_url.format(live_prefix=self.live_endpoint_prefix)

        versions_and_urls = {
            'recurring': {
                'version': self.api_recurring_version,
                'base_url': {
                    'live': live_pal_url + '/Recurring',
                    'test': settings.PAL_TEST_URL + '/Recurring',
                }
            },
            'payouts': {
                'version': self.api_payout_version,
                'base_url': {
                    'live': live_pal_url + '/Payout',
                    'test': settings.PAL_TEST_URL + '/Payout'
                }
            },
            'binlookup': {
                'version': self.api_bin_lookup_version,
                'base_url': {
                    'live': live_pal_url + '/BinLookup',
                    'test': settings.PAL_TEST_URL + '/BinLookup'
                }
            },
            'terminal': {
                'version': self.api_terminal_version,
                'base_url': {
                    'live': settings.BASE_TERMINAL_URL.format(platform),
                    'test': settings.BASE_TERMINAL_URL.format(platform)
                }
            },
            'payments': {
                'version': self.api_payment_version,
                'base_url': {
                    'live': live_pal_url + '/Payment',
                    'test': settings.PAL_TEST_URL + '/Payment'
                }
            },
            'checkout': {
                'version': self.api_checkout_version,
                'base_url': {
                    'live': live_checkout_url,
                    'test': settings.ENDPOINT_CHECKOUT_TEST
                }
            },
            'management': {
                'version': self.api_management_version,
                'base_url': {
                    'live': settings.BASE_MANAGEMENT_URL.format(platform),
                    'test': settings.BASE_MANAGEMENT_URL.format(platform)
                }
            },
            'legalEntityManagement': {
                'version': self.api_legal_entity_management_version,
                'base_url': {
                    'live': settings.BASE_LEGAL_ENTITY_MANAGEMENT_URL.format(platform),
                    'test': settings.BASE_LEGAL_ENTITY_MANAGEMENT_URL.format(platform)
                },
            },
            'balancePlatform': {
                'version': self.api_balance_platform_version,
                'base_url': {
                    'live': settings.BASE_CONFIGURATION_URL.format(platform),
                    'test': settings.BASE_CONFIGURATION_URL.format(platform)
                }
            },
            'dataProtection': {
                'version': self.api_data_protection_version,
                'base_url': {
                    'live': settings.BASE_DATA_PROTECION_URL.format(platform),
                    'test': settings.BASE_DATA_PROTECION_URL.format(platform)
                }
            },
            'transfers': {
                'version': self.api_transfers_version,
                'base_url': {
                    'live': settings.BASE_TRANSFERS_URL.format(platform),
                    'test': settings.BASE_TRANSFERS_URL.format(platform)
                }
            },
            'storedValue': {
                'version': self.api_stored_value_version,
                'base_url': {
                    'live': settings.BASE_STORED_VALUE_URL.format(platform),
                    'test': settings.BASE_STORED_VALUE_URL.format(platform)
                }
            }
        }

        version = versions_and_urls[service]['version']
        base_url = versions_and_urls[service]['base_url'][platform]
        # Match urls that require a live prefix and do not have one

        if platform == 'live' and '{live_prefix}' in base_url:
            errorstring = "Please set your live suffix. You can set it by running " \
                          "adyen.client.live_endpoint_prefix = 'Your live suffix'"
            raise AdyenEndpointInvalidFormat(errorstring)

        return version, base_url

    def _determine_api_url(self, platform, service, endpoint):
        api_version, base_url = self._determine_base_url_and_version(platform, service)
        return base_url + '/' + api_version + endpoint

    def _review_payout_username(self, **kwargs):
        if 'username' in kwargs:
            return kwargs['username']
        elif self.review_payout_username:
            return self.review_payout_username
        errorstring = "Please set your review payout " \
                      "webservice username. You can do this by running " \
                      "Adyen.review_payout_username = 'Your payout username'"
        raise AdyenInvalidRequestError(errorstring)

    def _review_payout_pass(self, **kwargs):
        if 'password' in kwargs:
            return kwargs["password"]
        elif self.review_payout_password:
            return self.review_payout_password
        errorstring = "Please set your review payout " \
                      "webservice password. You can do this by running " \
                      "Adyen.review_payout_password = 'Your payout password"
        raise AdyenInvalidRequestError(errorstring)

    def _store_payout_username(self, **kwargs):
        if 'username' in kwargs:
            return kwargs['username']
        elif self.store_payout_username:
            return self.store_payout_username
        errorstring = "Please set your review payout " \
                      "webservice username. You can do this by running " \
                      "Adyen.review_payout_username = 'Your payout username'"
        raise AdyenInvalidRequestError(errorstring)

    def _store_payout_pass(self, **kwargs):
        if 'password' in kwargs:
            return kwargs["password"]
        elif self.store_payout_password:
            return self.store_payout_password
        errorstring = "Please set your review payout " \
                      "webservice password. You can do this by running " \
                      "Adyen.review_payout_password = 'Your payout password"
        raise AdyenInvalidRequestError(errorstring)

    def _set_credentials(self, service, endpoint, **kwargs):
        xapikey = None
        username = None
        password = None

        # username at self object has highest priority. fallback to root module
        # and ensure that it is set.

        if self.xapikey:
            xapikey = self.xapikey
        elif 'xapikey' in kwargs:
            xapikey = kwargs.pop("xapikey")

        if self.username:
            username = self.username
        elif 'username' in kwargs:
            username = kwargs.pop("username")
        if service == "Payout":
            if any(substring in endpoint for substring in
                   ["store", "submit"]):
                username = self._store_payout_username(**kwargs)
            else:
                username = self._review_payout_username(**kwargs)

        if not username and not xapikey:
            errorstring = "Please set your webservice username.You can do this by running " \
                          "Adyen.username = 'Your username'"
            raise AdyenInvalidRequestError(errorstring)
            # password at self object has highest priority.
            # fallback to root module
            # and ensure that it is set.

        if self.password and not xapikey:
            password = self.password
        elif 'password' in kwargs:
            password = kwargs.pop("password")
        if service == "Payout":
            if any(substring in endpoint for substring in
                   ["store", "submit"]):
                password = self._store_payout_pass(**kwargs)
            else:
                password = self._review_payout_pass(**kwargs)

        if not password and not xapikey:
            errorstring = "Please set your webservice password.You can do this by running " \
                          "Adyen.password = 'Your password'"
            raise AdyenInvalidRequestError(errorstring)
            # xapikey at self object has highest priority.
            # fallback to root module
            # and ensure that it is set.

        return xapikey, username, password

    def _set_platform(self, **kwargs):
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

        return platform

    def call_adyen_api(
            self,
            request_data,
            service,
            method,
            endpoint,
            idempotency_key=None,
            **kwargs
    ):
        """This will call the adyen api. username, password, merchant_account,
        and platform are pulled from root module level and or self object.
        AdyenResult will be returned on 200 response. Otherwise, an exception
        is raised.

        Args:
            idempotency_key: https://docs.adyen.com/development-resources
            /api-idempotency
            request_data (dict): The dictionary of the request to place. This
                should be in the structure of the Adyen API.
                https://docs.adyen.com/api-explorer
            service (str): This is the API service to be called.
            method (str): This is the method used to send the request to an endpoint.
            endpoint (str): The specific endpoint of the API service to be called
        Returns:
            AdyenResult: The AdyenResult is returned when a request was
                successful.
        """
        # Initialize http client
        if not self.http_init:
            self._init_http_client()

        # Set credentials
        xapikey, username, password = self._set_credentials(service, endpoint, **kwargs)
        # Set platform
        platform = self._set_platform(**kwargs)
        message = request_data

        headers = {
            self.APPLICATION_INFO_HEADER_NAME: settings.LIB_NAME,
            self.APPLICATION_VERSION_HEADER_NAME: settings.LIB_VERSION
        }

        # Adyen requires this header to be set and uses the combination of
        # merchant account and merchant reference to determine uniqueness.
        if idempotency_key:
            headers[self.IDEMPOTENCY_HEADER_NAME] = idempotency_key

        url = self._determine_api_url(platform, service, endpoint)

        if 'query_parameters' in kwargs:
            url = url + util.get_query(kwargs['query_parameters'])
            kwargs.pop('query_parameters')

        if xapikey:
            raw_response, raw_request, status_code, headers = \
                self.http_client.request(method, url, json=request_data,
                                         xapikey=xapikey, headers=headers,
                                         **kwargs)
        else:
            raw_response, raw_request, status_code, headers = \
                self.http_client.request(method, url, json=message, username=username,
                                         password=password,
                                         headers=headers,
                                         **kwargs)

        # Creates AdyenResponse if request was successful, raises error if not.
        adyen_result = self._handle_response(url, raw_response, raw_request,
                                             status_code, headers)

        return adyen_result

    def _init_http_client(self):
        self.http_client = HTTPClient(
            user_agent_suffix=self.USER_AGENT_SUFFIX,
            lib_version=self.LIB_VERSION,
            force_request=self.http_force,
            timeout=self.http_timeout,
        )
        self.http_init = True

    def _handle_response(self, url, raw_response, raw_request,
                         status_code, headers):
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

        if status_code not in [200, 201, 204]:
            response = {}
            # If the result can't be parsed into json, most likely is raw html.
            # Some response are neither json or raw html, handle them here:
            if raw_response:
                response = json_lib.loads(raw_response)
            # Pass raised error to error handler.
            self._handle_http_error(url, response, status_code,
                                    headers.get('pspReference'),
                                    raw_request, raw_response,
                                    headers)

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
            if status_code != 204:
                response = json_lib.loads(raw_response)
            else:
                response = {}
            psp = self._get_psp(response, headers)
            return AdyenResult(message=response, status_code=status_code,
                               psp=psp, raw_request=raw_request,
                               raw_response=raw_response)

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

        if response_obj == {}:
            message = raw_response
        else:
            message = response_obj

        error_code = response_obj.get("errorCode")

        if status_code == 404:
            raise AdyenAPICommunicationError(message, raw_request, raw_response, url, psp_ref, headers, status_code,
                                             error_code)
        elif status_code == 400:
            raise AdyenAPIValidationError(message, raw_request, raw_response, url, psp_ref, headers, status_code,
                                          error_code)
        elif status_code == 401:
            raise AdyenAPIAuthenticationError(message, raw_request, raw_response, url, psp_ref, headers, status_code,
                                              error_code)
        elif status_code == 403:
            raise AdyenAPIInvalidPermission(message, raw_request, raw_response, url, psp_ref, headers, status_code,
                                            error_code)
        elif status_code == 422:
            raise AdyenAPIUnprocessableEntity(message, raw_request, raw_response, url, psp_ref, headers, status_code,
                                              error_code)
        elif status_code == 500:
            raise AdyenAPICommunicationError(message, raw_request, raw_response, url, psp_ref, headers, status_code,
                                             error_code)
        else:
            raise AdyenAPIResponseError(message, raw_request, raw_response, url, psp_ref, headers, status_code,
                                        error_code)

    @staticmethod
    def _get_psp(response, headers):
        psp_ref = response.get('pspReference')
        if psp_ref is None:
            psp_ref = headers.get('pspReference')
        return psp_ref
