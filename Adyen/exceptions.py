class AdyenError(Exception):
    def __init__(
        self,
        message,
        raw_request="",
        raw_response="",
        url="",
        psp="",
        headers="",
        status_code="",
        error_code="",
    ):
        self.message = message
        self.raw_request = raw_request
        self.raw_response = raw_response
        self.url = url
        self.psp = psp
        self.headers = headers
        self.status_code = status_code
        self.error_code = error_code

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"

    def debug(self):
        return (
            f"class: {self.__class__.__name__}\nmessage: {self.message}\nHTTP status_code:{self.status_code}\nerror_code:{self.error_code}\nurl: {self.url}\n"
            f"request: {self.raw_request}\nresponse: {self.raw_response}\nheaders: {self.headers}"
        )


class AdyenInvalidRequestError(AdyenError):
    pass


class AdyenAPIResponseError(AdyenError):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class AdyenAPIAuthenticationError(AdyenAPIResponseError):
    pass


class AdyenAPIInvalidPermission(AdyenAPIResponseError):
    pass


class AdyenAPICommunicationError(AdyenAPIResponseError):
    pass


class AdyenAPIValidationError(AdyenAPIResponseError):
    pass


class AdyenAPIUnprocessableEntity(AdyenAPIResponseError):
    pass


class AdyenAPIInvalidFormat(AdyenAPIResponseError):
    pass


class AdyenEndpointInvalidFormat(AdyenError):
    pass
