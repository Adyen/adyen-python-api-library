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
        return self.client.call_api(request, self.service, "assignTerminals", **kwargs)

    def find_terminal(self, request="", **kwargs):
        return self.client.call_api(request, self.service, "findTerminal", **kwargs)

    def get_stores_under_account(self, request="", **kwargs):
        return self.client.call_api(request, self.service, "getStoresUnderAccount", **kwargs)

    def get_terminal_details(self, request="", **kwargs):
        return self.client.call_api(request, self.service, "getTerminalDetails", **kwargs)

    def get_terminals_under_account(self, request="", **kwargs):
        return self.client.call_api(request, self.service, "getTerminalsUnderAccount", **kwargs)