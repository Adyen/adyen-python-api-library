#!/bin/python

from __future__ import absolute_import, division, unicode_literals
import sys

try:
    import requests
except ImportError:
    requests = None

try:
    import pycurl
except ImportError:
    pycurl = None

try:
    # Python 3
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
except ImportError:
    # Python 2
    from urllib import urlencode
    from urllib2 import Request, urlopen, HTTPError

try:
    # Python 2
    from StringIO import StringIO
except ImportError:
    # Python 3
    from io import BytesIO

import json as json_lib
import base64


class HTTPClient(object):
    def __init__(
        self,
        user_agent_suffix,
        lib_version,
        force_request=None,
        timeout=None,
    ):
        # Check if requests already available, default to urllib
        self.user_agent = user_agent_suffix + lib_version
        if not force_request:
            if requests:
                self.request = self._requests_post
            elif pycurl:
                self.request = self._pycurl_post
            else:
                self.request = self._urllib_post
        else:
            if force_request == 'requests':
                self.request = self._requests_post
            elif force_request == 'pycurl':
                self.request = self._pycurl_post
            else:
                self.request = self._urllib_post

        self.timeout = timeout

    def _pycurl_post(
        self,
        url,
        json=None,
        data=None,
        username="",
        password="",
        xapikey="",
        headers=None
     ):
        """This function will POST to the url endpoint using pycurl. returning
        an AdyenResult object on 200 HTTP response. Either json or data has to
        be provided. If username and password are provided, basic auth will be
        used.


        Args:
            url (str): url to send the POST
            json (dict, optional): Dict of the JSON to POST
            data (dict, optional): Dict, presumed flat structure
                of key/value of request to place
            username (str, optional): Username for basic auth. Must be included
                as part of password.
            password (str, optional): Password for basic auth. Must be included
                as part of username.
            xapikey (str, optional):    Adyen API key.  Will be used for auth
                                        if username and password are absent.
            headers (dict, optional): Key/Value pairs of headers to include
            timeout (int, optional): Default 30. Timeout for the request.

        Returns:
            str:    Raw response received
            str:    Raw request placed
            int:    HTTP status code, eg 200,404,401
            dict:   Key/Value pairs of the headers received.
        """
        if headers is None:
            headers = {}

        response_headers = {}

        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        if sys.version_info[0] >= 3:
            stringbuffer = BytesIO()
        else:
            stringbuffer = StringIO()

        curl.setopt(curl.WRITEDATA, stringbuffer)

        # Add User-Agent header to request so that the
        # request can be identified as coming from the Adyen Python library.
        headers['User-Agent'] = self.user_agent

        if username and password:
            curl.setopt(curl.USERPWD, '%s:%s' % (username, password))
        elif xapikey:
            headers["X-API-KEY"] = xapikey

        # Convert the header dict to formatted array as pycurl needs.
        if sys.version_info[0] >= 3:
            header_list = ["%s:%s" % (k, v) for k, v in headers.items()]
        else:
            header_list = ["%s:%s" % (k, v) for k, v in headers.iteritems()]
        # Ensure proper content-type when adding headers
        if json:
            header_list.append("Content-Type:application/json")

        curl.setopt(pycurl.HTTPHEADER, header_list)

        # Return regular dict instead of JSON encoded dict for request:
        raw_store = json

        # Set the request body.
        raw_request = json_lib.dumps(json) if json else urlencode(data)
        curl.setopt(curl.POSTFIELDS, raw_request)

        curl.setopt(curl.TIMEOUT, self.timeout)
        curl.perform()

        # Grab the response content
        result = stringbuffer.getvalue()
        status_code = curl.getinfo(curl.RESPONSE_CODE)

        curl.close()

        # Return regular dict instead of JSON encoded dict for request:
        raw_request = raw_store

        return result, raw_request, status_code, response_headers

    def _requests_post(
        self,
        url,
        json=None,
        data=None,
        username="",
        password="",
        xapikey="",
        headers=None
    ):
        """This function will POST to the url endpoint using requests.
        Returning an AdyenResult object on 200 HTTP response.
        Either json or data has to be provided.
        If username and password are provided, basic auth will be used.


        Args:
            url (str): url to send the POST
            json (dict, optional): Dict of the JSON to POST
            data (dict, optional): Dict, presumed flat structure of key/value
                of request to place
            username (str, optionl): Username for basic auth. Must be included
                as part of password.
            password (str, optional): Password for basic auth. Must be included
                as part of username.
            xapikey (str, optional):    Adyen API key.  Will be used for auth
                                        if username and password are absent.
            headers (dict, optional): Key/Value pairs of headers to include
            timeout (int, optional): Default 30. Timeout for the request.

        Returns:
            str:    Raw response received
            str:    Raw request placed
            int:    HTTP status code, eg 200,404,401
            dict:   Key/Value pairs of the headers received.
        """
        if headers is None:
            headers = {}

        # Adding basic auth if username and password provided.
        auth = None
        if username and password:
            auth = requests.auth.HTTPBasicAuth(username, password)
        elif xapikey:
            headers['x-api-key'] = xapikey

        # Add User-Agent header to request so that the request
        # can be identified as coming from the Adyen Python library.
        headers['User-Agent'] = self.user_agent

        request = requests.post(
            url=url,
            auth=auth,
            data=data,
            json=json,
            headers=headers,
            timeout=self.timeout
        )

        # Ensure either json or data is returned for raw request
        # Updated: Only return regular dict,
        # don't switch out formats if this is not important.
        message = json

        return request.text, message, request.status_code, request.headers

    def _urllib_post(
        self,
        url,
        json=None,
        data=None,
        username="",
        password="",
        xapikey="",
        headers=None,
    ):

        """This function will POST to the url endpoint using urllib2. returning
        an AdyenResult object on 200 HTTP responce. Either json or data has to
        be provided. If username and password are provided, basic auth will be
        used.

        Args:
            url (str):                  url to send the POST
            json (dict, optional):      Dict of the JSON to POST
            data (dict, optional):      Dict, presumed flat structure of
                                        key/value of request to place as
                                        www-form
            username (str, optional):    Username for basic auth. Must be
                                        uncluded as part of password.
            password (str, optional):   Password for basic auth. Must be
                                        included as part of username.
            xapikey (str, optional):    Adyen API key.  Will be used for auth
                                        if username and password are absent.
            headers (dict, optional):   Key/Value pairs of headers to include

        Returns:
            str:    Raw response received
            str:    Raw request placed
            int:    HTTP status code, eg 200,404,401
            dict:   Key/Value pairs of the headers received.
        """

        if headers is None:
            headers = {}

        # Store regular dict to return later:
        raw_store = json

        raw_request = json_lib.dumps(json) if json else urlencode(data)
        url_request = Request(url, data=raw_request.encode('utf8'))
        if json:
            url_request.add_header('Content-Type', 'application/json')
        elif not data:
            raise ValueError("Please provide either a json or a data field.")

        # Add User-Agent header to request so that the
        # request can be identified as coming from the Adyen Python library.
        headers['User-Agent'] = self.user_agent

        # Set regular dict to return as raw_request:
        raw_request = raw_store

        # Adding basic auth is username and password provided.
        if username and password:
            if sys.version_info[0] >= 3:
                basic_authstring = base64.encodebytes(('%s:%s' %
                                                       (username, password))
                                                      .encode()).decode(). \
                    replace('\n', '')
            else:
                basic_authstring = base64.encodestring('%s:%s' % (username,
                                                                  password)). \
                    replace('\n', '')
            url_request.add_header("Authorization",
                                   "Basic %s" % basic_authstring)
        elif xapikey:
            headers["X-API-KEY"] = xapikey

        # Adding the headers to the request.
        for key, value in headers.items():
            url_request.add_header(key, str(value))

        # URLlib raises all non 200 responses as en error.
        try:
            response = urlopen(url_request, timeout=self.timeout)
        except HTTPError as e:
            raw_response = e.read()

            return raw_response, raw_request, e.getcode(), e.headers
        else:
            raw_response = response.read()
            response.close()

            # The dict(response.info()) is the headers of the response
            # Raw response, raw request, status code and headers returned
            return (raw_response, raw_request,
                    response.getcode(), dict(response.info()))

    def request(
        self,
        url,
        json="",
        data="",
        username="",
        password="",
        headers=None,
    ):
        """This is overridden on module initialization. This function will make
        an HTTP POST to a given url. Either json/data will be what is posted to
        the end point. he HTTP request needs to be basicAuth when username and
        password are provided. a headers dict maybe provided,
        whatever the values are should be applied.

        Args:
            url (str):                  url to send the POST
            json (dict, optional):      Dict of the JSON to POST
            data (dict, optional):      Dict, presumed flat structure of
                                        key/value of request to place as
                                        www-form
            username (str, optional):    Username for basic auth. Must be
                                        included as part of password.
            password (str, optional):   Password for basic auth. Must be
                                        included as part of username.
            xapikey (str, optional):    Adyen API key.  Will be used for auth
                                        if username and password are absent.
            headers (dict, optional):   Key/Value pairs of headers to include
        Returns:
            str:    Raw request placed
            str:    Raw response received
            int:    HTTP status code, eg 200,404,401
            dict:   Key/Value pairs of the headers received.
        """
        raise NotImplementedError('request of HTTPClient should have been '
                                  'overridden on initialization. '
                                  'Otherwise, can be overridden to '
                                  'supply your own post method')
