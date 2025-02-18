from ..base import AdyenServiceBase


class GrantAccountsApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(GrantAccountsApi, self).__init__(client=client)
        self.service = "balancePlatform"
        self.baseUrl = "https://balanceplatform-api-test.adyen.com/bcl/v2"

    def get_grant_account(self, id, idempotency_key=None, **kwargs):
        """
        Get a grant account

        Deprecated since Configuration API v2
        Use the `/grantAccounts/{id}` endpoint from the [Capital API](https://docs.adyen.com/api-explorer/capital/latest/get/grantAccounts/(id)) instead.
        """
        endpoint = self.baseUrl + f"/grantAccounts/{id}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

