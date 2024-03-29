from ..base import AdyenServiceBase


class ClassicCheckoutSDKApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(ClassicCheckoutSDKApi, self).__init__(client=client)
        self.service = "checkout"
        self.baseUrl = "https://checkout-test.adyen.com/v71"

    def payment_session(self, request, idempotency_key=None, **kwargs):
        """
        Create a payment session
        """
        endpoint = self.baseUrl + f"/paymentSession"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def verify_payment_result(self, request, idempotency_key=None, **kwargs):
        """
        Verify a payment result
        """
        endpoint = self.baseUrl + f"/payments/result"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

