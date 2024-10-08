from ..base import AdyenServiceBase


class DonationsApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(DonationsApi, self).__init__(client=client)
        self.service = "checkout"
        self.baseUrl = "https://checkout-test.adyen.com/v71"

    def donation_campaigns(self, request, idempotency_key=None, **kwargs):
        """
        Get a list of donation campaigns.
        """
        endpoint = self.baseUrl + f"/donationCampaigns"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def donations(self, request, idempotency_key=None, **kwargs):
        """
        Start a transaction for donations
        """
        endpoint = self.baseUrl + f"/donations"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

