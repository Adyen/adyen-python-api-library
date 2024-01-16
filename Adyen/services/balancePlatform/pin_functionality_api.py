from ..base import AdyenServiceBase


class PINFunctionalityApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(PINFunctionalityApi, self).__init__(client=client)
        self.service = "balancePlatform"
        self.baseUrl = "https://balanceplatform-api-test.adyen.com/bcl/v2"

    def get_rsa_publickey(self, idempotency_key=None, **kwargs):
        """
        Get RSA publicKey
        """
        endpoint = self.baseUrl + f"/pins/publicKey"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def change_pin(self, request, idempotency_key=None, **kwargs):
        """
        Change Pin
        """
        endpoint = self.baseUrl + f"/pins/change"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def reveal_pin(self, request, idempotency_key=None, **kwargs):
        """
        Reveal Pin
        """
        endpoint = self.baseUrl + f"/pins/reveal"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

