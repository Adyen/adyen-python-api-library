from ..base import AdyenServiceBase


class PaymentLinksApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(PaymentLinksApi, self).__init__(client=client)
        self.service = "checkout"
        self.baseUrl = "https://checkout-test.adyen.com/v70"

    def get_payment_link(self, linkId, idempotency_key=None, **kwargs):
        """
        Get a payment link
        """
        endpoint = self.baseUrl + f"/paymentLinks/{linkId}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_payment_link(self, request, linkId, idempotency_key=None, **kwargs):
        """
        Update the status of a payment link
        """
        endpoint = self.baseUrl + f"/paymentLinks/{linkId}"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def payment_links(self, request, idempotency_key=None, **kwargs):
        """
        Create a payment link
        """
        endpoint = self.baseUrl + f"/paymentLinks"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

