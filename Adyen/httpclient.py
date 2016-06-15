#!/bin/python
try:
    import requests
except ImportError:
    requests = None

import urllib2

from urllib import urlencode
import json as json_lib
import re
import base64


#Could be used instead of the large tuple response from request function
#from collections import namedtuple
#RequestResult = namedtuple('RequestResult',
#    ['raw_response','raw_request','status_code','headers'])

class HTTPClient(object):
    def __init__(self):
        #Check if requests already available, default to urllib
        if requests:
            self.request = self._requests_post
        else:
            self.request = self._urllib_post

    def _requests_post(self, url, 
        json=None, 
        data=None,
        username="",
        password="",
        headers={}, 
        timeout=30):
        """This function will POST to the url endpoint using requests. returning
        an AdyenResult object on 200 HTTP responce. Either json or data has to
        be provided. If username and password are provided, basic auth will be 
        used.


        Args:
            url (str): url to send the POST
            json (dict, optional): Dict of the JSON to POST
            data (dict, optional): Dict, presumed flat structure of key/value of 
                request to place
            username (str, optionl): Username for basic auth. Must be included 
                as part of password.
            password (str, optional): Password for basic auth. Must be included 
                as part of username.
            headers (dict, optional): Key/Value pairs of headers to include
            timeout (int, optional): Default 30. Timeout for the request.

        Returns: 
            str:    Raw request placed
            str:    Raw response received
            int:    HTTP status code, eg 200,404,401
            dict:   Key/Value pairs of the headers received.                    
        """

        #Adding basic auth is username and password provided.
        auth = ""
        if username and password:
            auth = requests.auth.HTTPBasicAuth(username, password)
        else:
            auth = None

        request = requests.post(url, auth=auth, data=data, json = json, 
            headers=headers, timeout=timeout)


        #Ensure either json or data is returned for raw request
        message = str(json if json else data)

        #Raw response, raw request, status code returned, and headers returned
        return request.text, message, request.status_code, request.headers

    def _urllib_post(self, url, 
        json="",
        data="", 
        username="",
        password="",
        headers={},
        timout=30):
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
            headers (dict, optional):   Key/Value pairs of headers to include
        Returns: 
            str:    Raw request placed
            str:    Raw response received
            int:    HTTP status code, eg 200,404,401
            dict:   Key/Value pairs of the headers received.  
        """

        raw_request = json_lib.dumps(json) if json else urlencode(data)
        url_request = urllib2.Request(url,data=raw_request)
        if json: 
            url_request.add_header('Content-Type','application/json')  
        elif not data:
            raise ValueError("Please provide either a json or a data field.")
        
        #Adding basic auth is username and password provided.
        if username and password:
            basicAuthstring = base64.encodestring('%s:%s' % (username, 
                password)).replace('\n', '')
            url_request.add_header("Authorization", "Basic %s" % basicAuthstring) 

        #Adding the headers to the request.
        for key, value in headers.items():
            url_request.add_header(k, str(v))

        #URLlib raises all non 200 responses as en error.
        try:
            response = urllib2.urlopen(url_request, timeout=20)
        except urllib2.HTTPError as e:
            raw_response = e.read()

            return raw_response, raw_request, e.getcode, e.headers
        else:  
            raw_response = response.read()
            response.close()
            
            #The dict(response.info()) is the headers of the response
            #Raw response, raw request, status code returned, and headers returned
            return (raw_response, raw_request, response.getcode(), 
                dict(response.info()))

    def request(self, url, 
        json="",
        data="", 
        username="",
        password="",
        headers={},
        timout=30):
        """This is overridden on module initialization. This function will make
        an HTTP POST to a given url. Either json/data will be what is posted to
        the end point. he HTTP request needs to be basicAuth when username and 
        password are provided. a headers dict maybe provided, whatever the values
        are should be applied. 

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
            headers (dict, optional):   Key/Value pairs of headers to include
        Returns: 
            str:    Raw request placed
            str:    Raw response received
            int:    HTTP status code, eg 200,404,401
            dict:   Key/Value pairs of the headers received.  
        """
        raise NotImplementedError('request of HTTPClient should have been '
            'overridden on initialization. Otherwise, can be overridden to '
            'supply your own post method')