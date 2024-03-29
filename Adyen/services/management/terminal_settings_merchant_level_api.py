from ..base import AdyenServiceBase


class TerminalSettingsMerchantLevelApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(TerminalSettingsMerchantLevelApi, self).__init__(client=client)
        self.service = "management"
        self.baseUrl = "https://management-test.adyen.com/v3"

    def get_terminal_logo(self, merchantId, idempotency_key=None, **kwargs):
        """
        Get the terminal logo
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/terminalLogos"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_terminal_settings(self, merchantId, idempotency_key=None, **kwargs):
        """
        Get terminal settings
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/terminalSettings"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_terminal_logo(self, request, merchantId, idempotency_key=None, **kwargs):
        """
        Update the terminal logo
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/terminalLogos"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_terminal_settings(self, request, merchantId, idempotency_key=None, **kwargs):
        """
        Update terminal settings
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/terminalSettings"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

