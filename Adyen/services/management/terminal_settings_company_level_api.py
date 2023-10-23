from ..base import AdyenServiceBase


class TerminalSettingsCompanyLevelApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(TerminalSettingsCompanyLevelApi, self).__init__(client=client)
        self.service = "management"
        self.baseUrl = "https://management-test.adyen.com/v3"

    def get_terminal_logo(self, companyId, idempotency_key=None, **kwargs):
        """
        Get the terminal logo
        """
        endpoint = self.baseUrl + f"/companies/{companyId}/terminalLogos"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_terminal_settings(self, companyId, idempotency_key=None, **kwargs):
        """
        Get terminal settings
        """
        endpoint = self.baseUrl + f"/companies/{companyId}/terminalSettings"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_terminal_logo(self, request, companyId, idempotency_key=None, **kwargs):
        """
        Update the terminal logo
        """
        endpoint = self.baseUrl + f"/companies/{companyId}/terminalLogos"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_terminal_settings(self, request, companyId, idempotency_key=None, **kwargs):
        """
        Update terminal settings
        """
        endpoint = self.baseUrl + f"/companies/{companyId}/terminalSettings"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

