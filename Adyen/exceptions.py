from __future__ import absolute_import, division, unicode_literals


class AdyenError(Exception):
    def __init__(self,
                 message,
                 raw_request="",
                 raw_response="",
                 url="",
                 psp="",
                 headers="",
                 status_code="",
                 error_code=""):
        self.message = message
        self.raw_request = raw_request
        self.raw_response = raw_response
        self.url = url
        self.psp = psp
        self.headers = headers
        self.status_code = status_code
        self.error_code = error_code

    def __str__(self):
        return repr("{}:{}".format(self.__class__.__name__, self.message))

    def debug(self):
        return ("class: {}\nmessage: {}\nHTTP status_code:{}\nurl: {}"
                "request: {}\nresponse: {}\nheaders: {}"
                .format(self.__class__.__name__, self.message,
                        self.status_code, self.url, self.raw_request,
                        self.raw_response, self.headers))


class AdyenInvalidRequestError(AdyenError):
    pass


class AdyenAPIResponseError(AdyenError):
    def __init__(self,
                 message,
                 *args,
                 **kwargs):
        super(AdyenAPIResponseError, self).__init__(message, *args, **kwargs)


class AdyenAPIAuthenticationError(AdyenAPIResponseError):
    pass


class AdyenAPIInvalidPermission(AdyenAPIResponseError):
    pass


class AdyenAPICommunicationError(AdyenAPIResponseError):
    pass


class AdyenAPIValidationError(AdyenAPIResponseError):
    pass


class AdyenAPIInvalidAmount(AdyenAPIResponseError):
    pass


class AdyenAPIInvalidFormat(AdyenAPIResponseError):
    pass


class AdyenEndpointInvalidFormat(AdyenError):
    pass
