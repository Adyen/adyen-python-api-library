from ..base import AdyenServiceBase


class CapitalApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(CapitalApi, self).__init__(client=client)
        self.service = "transfers"
        self.baseUrl = "https://balanceplatform-api-test.adyen.com/btl/v4"

    def get_capital_account(self, idempotency_key=None, **kwargs):
        """
        Get a capital account

        Deprecated since Transfers API v4
        Use the `/grants` endpoint from the [Capital API](https://docs.adyen.com/api-explorer/capital/latest/get/grants) instead.
        """
        endpoint = self.baseUrl + f"/grants"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_grant_reference_details(self, id, idempotency_key=None, **kwargs):
        """
        Get grant reference details

        Deprecated since Transfers API v4
        Use the `/grants/{grantId}` endpoint from the [Capital API](https://docs.adyen.com/api-explorer/capital/latest/get/grants/(grantId)) instead.
        """
        endpoint = self.baseUrl + f"/grants/{id}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def request_grant_payout(self, request, idempotency_key=None, **kwargs):
        """
        Request a grant payout

        Deprecated since Transfers API v4
        Use the `/grants` endpoint from the [Capital API](https://docs.adyen.com/api-explorer/capital/latest/post/grants) instead.
        """
        endpoint = self.baseUrl + f"/grants"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

