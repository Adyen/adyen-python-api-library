from .base import AdyenServiceBase


class AdyenRecurring(AdyenServiceBase):
    """This represents the Adyen API Recurring Service.

    API calls currently implemented: listRecurringDetails and disable. Please
    refer to the Recurring Manual for specifics around the API.
    https://docs.adyen.com/online-payments/tokenization

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """

    def __init__(self, client=None):
        super(AdyenRecurring, self).__init__(client=client)
        self.service = "Recurring"

    def list_recurring_details(self, request, **kwargs):

        endpoint = "listRecurringDetails"
        method = "POST"

        return self.client.call_api(request, self.service, method,
                                    endpoint, **kwargs)

    def disable(self, request, **kwargs):

        endpoint = "disable"
        method = "POST"

        if 'recurringDetailReference' not in request:
            raise ValueError("Include a 'recurringDetailReference'"
                             " to disable a specific recurring contract.")
        else:
            return self.client.call_api(request, self.service, method,
                                        endpoint, **kwargs)
