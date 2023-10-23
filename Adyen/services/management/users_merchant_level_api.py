from ..base import AdyenServiceBase


class UsersMerchantLevelApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(UsersMerchantLevelApi, self).__init__(client=client)
        self.service = "management"
        self.baseUrl = "https://management-test.adyen.com/v3"

    def list_users(self, merchantId, idempotency_key=None, **kwargs):
        """
        Get a list of users
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/users"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_user_details(self, merchantId, userId, idempotency_key=None, **kwargs):
        """
        Get user details
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/users/{userId}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_user(self, request, merchantId, userId, idempotency_key=None, **kwargs):
        """
        Update a user
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/users/{userId}"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def create_new_user(self, request, merchantId, idempotency_key=None, **kwargs):
        """
        Create a new user
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/users"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

