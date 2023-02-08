from ..base import AdyenServiceBase


class RecurringApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(RecurringApi, self).__init__(client=client)
        self.service = "checkout"

    def delete_token_for_stored_payment_details(self, recurringId, idempotency_key=None, **kwargs):
        """
        Delete a token for stored payment details
        """
        endpoint = f"/storedPaymentMethods/{recurringId}"
        endpoint = endpoint.replace('/', '', 1)
        method = "DELETE"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_tokens_for_stored_payment_details(self, idempotency_key=None, **kwargs):
        """
        Get tokens for stored payment details
        """
        endpoint = f"/storedPaymentMethods"
        endpoint = endpoint.replace('/', '', 1)
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

