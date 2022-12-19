"""
    Management API

    Configure and manage your Adyen company and merchant accounts, stores, and payment terminals. ## Authentication Each request to the Management API must be signed with an API key. [Generate your API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in the Customer Area and then set this key to the `X-API-Key` header value.  To access the live endpoints, you need to generate a new API key in your live Customer Area. ## Versioning  Management API handles versioning as part of the endpoint URL. For example, to send a request to version 1 of the `/companies/{companyId}/webhooks` endpoint, use:  ```text https://management-test.adyen.com/v1/companies/{companyId}/webhooks ```  ## Going live  To access the live endpoints, you need an API key from your live Customer Area. Use this API key to make requests to:  ```text https://management-live.adyen.com/v1 ```  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: developer-experience@adyen.com
    Generated by: https://openapi-generator.tech
"""

from ..base import AdyenServiceBase


class AccountMerchantLevelApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(AccountMerchantLevelApi, self).__init__(client=client)
        self.service = "management"

    def get_merchants(self, idempotency_key=None, **kwargs):
        """
        Get a list of merchant accounts
        """
        endpoint = f"/merchants"
        endpoint = endpoint.replace('/','',1)
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_merchants_merchant_id(self, merchantId, idempotency_key=None, **kwargs):
        """
        Get a merchant account
        """
        endpoint = f"/merchants/{merchantId}"
        endpoint = endpoint.replace('/','',1)
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def post_merchants(self, request, idempotency_key=None, **kwargs):
        """
        Create a merchant account
        """
        endpoint = f"/merchants"
        endpoint = endpoint.replace('/','',1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def post_merchants_merchant_id_activate(self, merchantId, idempotency_key=None, **kwargs):
        """
        Request to activate a merchant account
        """
        endpoint = f"/merchants/{merchantId}/activate"
        endpoint = endpoint.replace('/','',1)
        method = "POST"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)



