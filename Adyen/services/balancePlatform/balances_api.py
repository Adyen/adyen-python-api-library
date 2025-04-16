from ..base import AdyenServiceBase


class BalancesApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(BalancesApi, self).__init__(client=client)
        self.service = "balancePlatform"
        self.baseUrl = "https://balanceplatform-api-test.adyen.com/bcl/v2"

    def balance_platforms_balance_platform_id_webhooks_webhook_id_settings_get(self, balancePlatformId, webhookId, idempotency_key=None, **kwargs):
        """
        Get webhook settings
        """
        endpoint = self.baseUrl + f"/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def balance_platforms_balance_platform_id_webhooks_webhook_id_settings_post(self, request, balancePlatformId, webhookId, balanceWebhookSettingsRequest, idempotency_key=None, **kwargs):
        """
        Create a balance webhook setting
        """
        endpoint = self.baseUrl + f"/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_delete(self, balancePlatformId, webhookId, settingId, idempotency_key=None, **kwargs):
        """
        Delete a webhook setting
        """
        endpoint = self.baseUrl + f"/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId}"
        method = "DELETE"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_get(self, balancePlatformId, webhookId, settingId, idempotency_key=None, **kwargs):
        """
        Get a webhook setting
        """
        endpoint = self.baseUrl + f"/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id_patch(self, request, balancePlatformId, webhookId, settingId, patchableBalanceWebhookSettingsRequest, idempotency_key=None, **kwargs):
        """
        Update a webhook setting
        """
        endpoint = self.baseUrl + f"/balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId}"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

