from .base import AdyenServiceBase


class AdyenTerminal(AdyenServiceBase):
    """This represents the Adyen API Terminal service.

    API call currently implemented:
        - assignTerminals
        - findTerminal
        - getStoreUnderAccount
        - getTerminalDetails
        - getTerminalsUnderAccount
    Please refer to the Terminal Manual for specifics around the API.
    https://docs.adyen.com/api-explorer/#/postfmapi/

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """

    def __init__(self, client=None):
        super(AdyenTerminal, self).__init__(client=client)
        self.service = "terminal"

    def assign_terminals(self, request="", **kwargs):
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, "assignTerminals", **kwargs)

    def find_terminal(self, request="", **kwargs):
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, "findTerminal", **kwargs)

    def get_stores_under_account(self, request="", **kwargs):
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, "getStoresUnderAccount", **kwargs)

    def get_terminal_details(self, request="", **kwargs):
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, "getTerminalDetails", **kwargs)

    def get_terminals_under_account(self, request="", **kwargs):
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, "getTerminalsUnderAccount", **kwargs)