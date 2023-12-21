from .base import AdyenServiceBase


class AdyenBinlookupApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(AdyenBinlookupApi, self).__init__(client=client)
        self.service = "binlookup"
        self.baseUrl = "https://pal-test.adyen.com/pal/servlet/BinLookup/v54"

    def get3ds_availability(self, request, idempotency_key=None, **kwargs):
        """
        Check if 3D Secure is available
        """
        endpoint = self.baseUrl + f"/get3dsAvailability"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_cost_estimate(self, request, idempotency_key=None, **kwargs):
        """
        Get a fees cost estimate
        """
        endpoint = self.baseUrl + f"/getCostEstimate"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

