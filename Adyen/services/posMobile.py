from .base import AdyenServiceBase


class AdyenPosMobileApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(AdyenPosMobileApi, self).__init__(client=client)
        self.service = "posMobile"
        self.baseUrl = "https://checkout-test.adyen.com/checkout/possdk/v68"

    def create_communication_session(self, request, idempotency_key=None, **kwargs):
        """
        Create a communication session
        """
        endpoint = self.baseUrl + f"/sessions"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

