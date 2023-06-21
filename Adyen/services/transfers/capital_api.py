from ..base import AdyenServiceBase


class CapitalApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(CapitalApi, self).__init__(client=client)
        self.service = "transfers"

    def get_capital_account(self, idempotency_key=None, **kwargs):
        """
        Get a capital account
        """
        endpoint = f"/grants"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_grant_reference_details(self, id, idempotency_key=None, **kwargs):
        """
        Get grant reference details
        """
        endpoint = f"/grants/{id}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def request_grant_payout(self, request, idempotency_key=None, **kwargs):
        """
        Request a grant payout
        """
        endpoint = f"/grants"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

