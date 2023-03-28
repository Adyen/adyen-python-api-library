from ..base import AdyenServiceBase


class MyAPICredentialApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(MyAPICredentialApi, self).__init__(client=client)
        self.service = "management"

    def remove_allowed_origin(self, originId, idempotency_key=None, **kwargs):
        """
        Remove allowed origin
        """
        endpoint = f"/me/allowedOrigins/{originId}"
        method = "DELETE"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_api_credential_details(self, idempotency_key=None, **kwargs):
        """
        Get API credential details
        """
        endpoint = f"/me"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_allowed_origins(self, idempotency_key=None, **kwargs):
        """
        Get allowed origins
        """
        endpoint = f"/me/allowedOrigins"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_allowed_origin_details(self, originId, idempotency_key=None, **kwargs):
        """
        Get allowed origin details
        """
        endpoint = f"/me/allowedOrigins/{originId}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def add_allowed_origin(self, request, idempotency_key=None, **kwargs):
        """
        Add allowed origin
        """
        endpoint = f"/me/allowedOrigins"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)
