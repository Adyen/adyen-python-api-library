from ..base import AdyenServiceBase


class AuthorizedCardUsersApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(AuthorizedCardUsersApi, self).__init__(client=client)
        self.service = "balancePlatform"
        self.baseUrl = "https://balanceplatform-api-test.adyen.com/bcl/v2"

    def create_authorised_card_users(self, request, paymentInstrumentId, authorisedCardUsers, idempotency_key=None, **kwargs):
        """
        Create authorized users for a card.
        """
        endpoint = self.baseUrl + f"/paymentInstruments/{paymentInstrumentId}/authorisedCardUsers"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def delete_authorised_card_users(self, paymentInstrumentId, idempotency_key=None, **kwargs):
        """
        Delete the authorized users for a card.
        """
        endpoint = self.baseUrl + f"/paymentInstruments/{paymentInstrumentId}/authorisedCardUsers"
        method = "DELETE"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_all_authorised_card_users(self, paymentInstrumentId, idempotency_key=None, **kwargs):
        """
        Get authorized users for a card.
        """
        endpoint = self.baseUrl + f"/paymentInstruments/{paymentInstrumentId}/authorisedCardUsers"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_authorised_card_users(self, request, paymentInstrumentId, authorisedCardUsers, idempotency_key=None, **kwargs):
        """
        Update the authorized users for a card.
        """
        endpoint = self.baseUrl + f"/paymentInstruments/{paymentInstrumentId}/authorisedCardUsers"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

