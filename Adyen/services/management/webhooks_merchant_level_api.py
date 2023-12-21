from ..base import AdyenServiceBase


class WebhooksMerchantLevelApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(WebhooksMerchantLevelApi, self).__init__(client=client)
        self.service = "management"
        self.baseUrl = "https://management-test.adyen.com/v3"

    def generate_hmac_key(self, merchantId, webhookId, idempotency_key=None, **kwargs):
        """
        Generate an HMAC key
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/webhooks/{webhookId}/generateHmac"
        method = "POST"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_webhook(self, merchantId, webhookId, idempotency_key=None, **kwargs):
        """
        Get a webhook
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/webhooks/{webhookId}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def list_all_webhooks(self, merchantId, idempotency_key=None, **kwargs):
        """
        List all webhooks
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/webhooks"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def remove_webhook(self, merchantId, webhookId, idempotency_key=None, **kwargs):
        """
        Remove a webhook
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/webhooks/{webhookId}"
        method = "DELETE"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def set_up_webhook(self, request, merchantId, idempotency_key=None, **kwargs):
        """
        Set up a webhook
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/webhooks"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def test_webhook(self, request, merchantId, webhookId, idempotency_key=None, **kwargs):
        """
        Test a webhook
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/webhooks/{webhookId}/test"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_webhook(self, request, merchantId, webhookId, idempotency_key=None, **kwargs):
        """
        Update a webhook
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/webhooks/{webhookId}"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

