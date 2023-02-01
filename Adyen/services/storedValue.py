"""
    Adyen Stored Value API

    A set of API endpoints to manage stored value products.  # noqa: E501

    The version of the OpenAPI document: 46
    Contact: developer-experience@adyen.com
    Generated by: https://openapi-generator.tech
"""

from .base import AdyenServiceBase


class AdyenStoredValueApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(AdyenStoredValueApi, self).__init__(client=client)
        self.service = "storedValue"

    def changes_the_status_of_the_payment_method(self, request, idempotency_key=None, **kwargs):
        """
        Changes the status of the payment method.
        """
        endpoint = f"/changeStatus"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def checks_the_balance(self, request, idempotency_key=None, **kwargs):
        """
        Checks the balance.
        """
        endpoint = f"/checkBalance"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def issues_new_card(self, request, idempotency_key=None, **kwargs):
        """
        Issues a new card.
        """
        endpoint = f"/issue"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def loads_the_payment_method(self, request, idempotency_key=None, **kwargs):
        """
        Loads the payment method.
        """
        endpoint = f"/load"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def merge_the_balance_of_two_cards(self, request, idempotency_key=None, **kwargs):
        """
        Merge the balance of two cards.
        """
        endpoint = f"/mergeBalance"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def voids_transaction(self, request, idempotency_key=None, **kwargs):
        """
        Voids a transaction.
        """
        endpoint = f"/voidTransaction"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

