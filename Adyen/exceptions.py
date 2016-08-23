import logging
from adyen_log import logname,getlogger
logger = logging.getLogger(logname())

class AdyenError(Exception):

    def __init__(self,
            message,
            raw_request="",
            raw_response="",
            url="",
            psp="",
            headers="",
            status_code=""):
        self.message = message
        self.raw_request=raw_request
        self.raw_response=raw_response
        self.url=url
        self.psp=psp
        self.headers=headers
        self.status_code=status_code

    def __str__(self):
        return repr(self.message)

    def debug(self):
        return "message: {}\nHTTP status_code:{}\nurl: {}\nrequest: {}\nresponse: {}\nheaders: {}".format(
            self.message,
            self.status_code,
            self.url,
            self.raw_request,
            self.raw_response,
            self.headers)

class AdyenInvalidRequestError(AdyenError):
    pass

class AdyenAPIResponseError(AdyenError):

    def __init__(self,
            message,
            result="",
            error_code="",
            *args,
            **kwargs):
        super(AdyenAPIResponseError,self).__init__(message, *args,**kwargs)
        self.error_code=error_code
        self.result=result

    def __str__(self):
        return repr(self.message)

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
