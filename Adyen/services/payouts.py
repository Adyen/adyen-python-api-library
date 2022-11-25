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
        action = "confirmThirdParty"
        return self.client.call_api(
            request, self.service, action, **kwargs
        )

    def decline(self, request=None, **kwargs):
        action = "declineThirdParty"
        return self.client.call_api(
            request, self.service, action, **kwargs
        )

    def store_detail(self, request=None, **kwargs):
        action = "storeDetail"
        return self.client.call_api(
            request, self.service, action, **kwargs
        )

    def submit(self, request=None, **kwargs):
        action = "submitThirdParty"
        return self.client.call_api(
            request, self.service, action, **kwargs
        )

    def store_detail_and_submit(self, request=None, **kwargs):
        action = "storeDetailAndSubmitThirdParty"
        return self.client.call_api(
            request, self.service, action, **kwargs
        )
