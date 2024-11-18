from ..base import AdyenServiceBase


class PaymentsApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(PaymentsApi, self).__init__(client=client)
        self.service = "checkout"
        self.baseUrl = "https://checkout-test.adyen.com/v71"

    def card_details(self, request, idempotency_key=None, **kwargs):
        """
        Get the brands and other details of a card
        """
        endpoint = self.baseUrl + f"/cardDetails"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_result_of_payment_session(self, sessionId, idempotency_key=None, **kwargs):
        """
        Get the result of a payment session
        """
        endpoint = self.baseUrl + f"/sessions/{sessionId}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def payment_methods(self, request, idempotency_key=None, **kwargs):
        """
        Get a list of available payment methods
        """
        endpoint = self.baseUrl + f"/paymentMethods"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def payments(self, request, idempotency_key=None, **kwargs):
        """
        Start a transaction
        """
        endpoint = self.baseUrl + f"/payments"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def payments_details(self, request, idempotency_key=None, **kwargs):
        """
        Submit details for a payment
        """
        endpoint = self.baseUrl + f"/payments/details"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def sessions(self, request, idempotency_key=None, **kwargs):
        """
        Create a payment session
        """
        endpoint = self.baseUrl + f"/sessions"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

