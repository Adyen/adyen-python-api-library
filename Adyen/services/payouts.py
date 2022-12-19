from .base import AdyenServiceBase


class AdyenThirdPartyPayout(AdyenServiceBase):
    """This represents the Adyen Payouts Service.
    https://docs.adyen.com/api-explorer/#/Payout/overview

    The AdyenThirdPartyPayout class is accessible as adyen.payout.method(args)

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """

    def __init__(self, client=None):
        super(AdyenThirdPartyPayout, self).__init__(client=client)
        self.service = "Payout"

    def confirm(self, request=None, **kwargs):
        endpoint = "confirmThirdParty"
        method = "POST"
        return self.client.call_adyen_api(
            request, self.service, method, endpoint, **kwargs
        )

    def decline(self, request=None, **kwargs):
        endpoint = "declineThirdParty"
        method = "POST"
        return self.client.call_adyen_api(
            request, self.service, method, endpoint, **kwargs
        )

    def store_detail(self, request=None, **kwargs):
        endpoint = "storeDetail"
        method = "POST"
        return self.client.call_adyen_api(
            request, self.service, method, endpoint, **kwargs
        )

    def submit(self, request=None, **kwargs):
        endpoint = "submitThirdParty"
        method = "POST"
        return self.client.call_adyen_api(
            request, self.service, method, endpoint, **kwargs
        )

    def store_detail_and_submit(self, request=None, **kwargs):
        endpoint = "storeDetailAndSubmitThirdParty"
        method = "POST"
        return self.client.call_adyen_api(
            request, self.service, method, endpoint, **kwargs
        )
