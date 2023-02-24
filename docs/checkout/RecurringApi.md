# checkout

All URIs are relative to *https://checkout-test.adyen.com/v70*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_token_for_stored_payment_details**](RecurringApi.md#delete_token_for_stored_payment_details) | **DELETE** /storedPaymentMethods/{recurringId} | Delete a token for stored payment details
[**get_tokens_for_stored_payment_details**](RecurringApi.md#get_tokens_for_stored_payment_details) | **GET** /storedPaymentMethods | Get tokens for stored payment details




# delete_token_for_stored_payment_details
### Example

```python
from Adyen import checkout

apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
apiClient.recurring_api.delete_token_for_stored_payment_details()

```




# get_tokens_for_stored_payment_details
### Example

```python
from Adyen import checkout

apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
apiClient.recurring_api.get_tokens_for_stored_payment_details()

```


