from .base import AdyenServiceBase


class AdyenPayment(AdyenServiceBase):
    """This represents the Adyen API Payment Service.

    API calls currently implemented:
        authorise
        authorise3d
        adjustAuthorisation
        cancel
        capture
        refund
        cancelOrRefund
    Please refer to our API Explorer for specifics around these APIs.
    https://docs.adyen.com/api-explorer/

    The AdyenPayment class, is accessible as adyen.payment.method(args)

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """

    def __init__(self, client=None):
        super(AdyenPayment, self).__init__(client=client)
        self.service = "Payment"

    def authorise(self, request, idempotency_key=None, **kwargs):

        endpoint = "authorise"

        if 'shopperEmail' in request:
            if request['shopperEmail'] == '':
                raise ValueError(
                    'shopperEmail must contain the shopper email'
                    ' when authorising recurring contracts.')
        if 'shopperReference' in request:
            if request['shopperReference'] == '':
                raise ValueError(
                    'shopperReference must contain the shopper'
                    ' name when authorising recurring contracts.')
        method = "POST"

        return self.client.call_adyen_api(request, self.service, method,
                                          endpoint, idempotency_key, **kwargs)

    def authorise3d(self, request, idempotency_key=None, **kwargs):
        endpoint = "authorise3d"
        method = "POST"

        return self.client.call_adyen_api(request, self.service, method,
                                          endpoint, idempotency_key, **kwargs)

    def adjustAuthorisation(self, request, **kwargs):
        endpoint = "adjustAuthorisation"
        method = "POST"

        return self.client.call_adyen_api(request, self.service, method,
                                          endpoint, **kwargs)

    def cancel(self, request, idempotency_key=None, **kwargs):
        endpoint = "cancel"
        method = "POST"

        return self.client.call_adyen_api(request, self.service, method,
                                          endpoint, idempotency_key, **kwargs)

    def capture(self, request, idempotency_key=None, **kwargs):

        endpoint = "capture"

        if request['modificationAmount']["value"] == "" or \
                request['modificationAmount']['value'] == "0":
            raise ValueError(
                "Set the 'modificationAmount' to the original transaction"
                " amount, or less for a partial capture. "
                "modificationAmount should be an object with the following"
                " keys: {'currency':,'value':}")
        if request['originalReference'] == "":
            raise ValueError("Set the 'originalReference' to the psp "
                             "reference of the transendpoint to be modified")
        method = "POST"

        response = self.client.call_adyen_api(request, self.service, method,
                                              endpoint, idempotency_key, **kwargs)
        return response

    def refund(self, request, idempotency_key=None, **kwargs):

        endpoint = "refund"
        method = "POST"

        if request['modificationAmount']['value'] == "" or \
                request['modificationAmount']['value'] == "0":
            raise ValueError(
                "To refund this payment, provide the original value. "
                "Set the value to less than the original amount, "
                "to partially refund this payment.")
        else:
            return self.client.call_adyen_api(request, self.service, method,
                                              endpoint, idempotency_key, **kwargs)

    def cancel_or_refund(self, request, idempotency_key=None, **kwargs):
        endpoint = "cancelOrRefund"
        method = "POST"

        return self.client.call_adyen_api(
            request, self.service, method, endpoint, idempotency_key, **kwargs
        )
