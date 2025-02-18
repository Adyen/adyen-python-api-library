from ..base import AdyenServiceBase


class PlatformApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(PlatformApi, self).__init__(client=client)
        self.service = "balancePlatform"
        self.baseUrl = "https://balanceplatform-api-test.adyen.com/bcl/v2"

    def get_all_account_holders_under_balance_platform(self, id, idempotency_key=None, **kwargs):
        """
        Get all account holders under a balance platform
        """
        endpoint = self.baseUrl + f"/balancePlatforms/{id}/accountHolders"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_all_transaction_rules_for_balance_platform(self, id, idempotency_key=None, **kwargs):
        """
        Get all transaction rules for a balance platform
        """
        endpoint = self.baseUrl + f"/balancePlatforms/{id}/transactionRules"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_balance_platform(self, id, idempotency_key=None, **kwargs):
        """
        Get a balance platform
        """
        endpoint = self.baseUrl + f"/balancePlatforms/{id}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

