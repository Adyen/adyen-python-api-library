from .base import AdyenServiceBase


class AdyenBinLookup(AdyenServiceBase):
    """This represents the Adyen API Bin Lookup service.

    API call currently implemented: getCostEstimate.
    Please refer to the Bin Lookup Manual for specifics around the API.
    https://docs.adyen.com/api-explorer/#/BinLookup/

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """

    def __init__(self, client=None):
        super(AdyenBinLookup, self).__init__(client=client)
        self.service = "BinLookup"

    def get_cost_estimate(self, request="", **kwargs):

        action = "getCostEstimate"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, action, **kwargs)
