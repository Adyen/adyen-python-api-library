from ..base import AdyenServiceBase


class GrantOffersApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(GrantOffersApi, self).__init__(client=client)
        self.service = "balancePlatform"
        self.baseUrl = "https://balanceplatform-api-test.adyen.com/bcl/v2"

    def get_all_available_grant_offers(self, idempotency_key=None, **kwargs):
        """
        Get all available grant offers

        Deprecated since Configuration API v2
        Use the `/grantOffers` endpoint from the [Capital API](https://docs.adyen.com/api-explorer/capital/latest/get/grantOffers) instead.
        """
        endpoint = self.baseUrl + f"/grantOffers"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_grant_offer(self, grantOfferId, idempotency_key=None, **kwargs):
        """
        Get a grant offer

        Deprecated since Configuration API v2
        Use the `/grantOffers/{id}` endpoint from the [Capital API](https://docs.adyen.com/api-explorer/capital/latest/get/grantOffers/(id)) instead.
        """
        endpoint = self.baseUrl + f"/grantOffers/{grantOfferId}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

