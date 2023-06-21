from ..base import AdyenServiceBase


class GeneralApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(GeneralApi, self).__init__(client=client)
        self.service = "platformsNotificationConfiguration"

    def create_notification_configuration(self, request, idempotency_key=None, **kwargs):
        """
        Subscribe to notifications
        """
        endpoint = f"/createNotificationConfiguration"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def delete_notification_configurations(self, request, idempotency_key=None, **kwargs):
        """
        Delete a notification subscription configuration
        """
        endpoint = f"/deleteNotificationConfigurations"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_notification_configuration(self, request, idempotency_key=None, **kwargs):
        """
        Get a notification subscription configuration
        """
        endpoint = f"/getNotificationConfiguration"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_notification_configuration_list(self, request, idempotency_key=None, **kwargs):
        """
        Get a list of notification subscription configurations
        """
        endpoint = f"/getNotificationConfigurationList"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def test_notification_configuration(self, request, idempotency_key=None, **kwargs):
        """
        Test a notification configuration
        """
        endpoint = f"/testNotificationConfiguration"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_notification_configuration(self, request, idempotency_key=None, **kwargs):
        """
        Update a notification subscription configuration
        """
        endpoint = f"/updateNotificationConfiguration"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

