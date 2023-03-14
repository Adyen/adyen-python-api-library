# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_webhook**](WebhooksMerchantLevelApi.md#remove_webhook) | **DELETE** /merchants/{merchantId}/webhooks/{webhookId} | Remove a webhook
[**list_all_webhooks**](WebhooksMerchantLevelApi.md#list_all_webhooks) | **GET** /merchants/{merchantId}/webhooks | List all webhooks
[**get_webhook**](WebhooksMerchantLevelApi.md#get_webhook) | **GET** /merchants/{merchantId}/webhooks/{webhookId} | Get a webhook
[**update_webhook**](WebhooksMerchantLevelApi.md#update_webhook) | **PATCH** /merchants/{merchantId}/webhooks/{webhookId} | Update a webhook
[**set_up_webhook**](WebhooksMerchantLevelApi.md#set_up_webhook) | **POST** /merchants/{merchantId}/webhooks | Set up a webhook
[**generate_hmac_key**](WebhooksMerchantLevelApi.md#generate_hmac_key) | **POST** /merchants/{merchantId}/webhooks/{webhookId}/generateHmac | Generate an HMAC key
[**test_webhook**](WebhooksMerchantLevelApi.md#test_webhook) | **POST** /merchants/{merchantId}/webhooks/{webhookId}/test | Test a webhook




# remove_webhook
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.webhooks_merchant_level_api.remove_webhook()

```


# list_all_webhooks
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.webhooks_merchant_level_api.list_all_webhooks()

```


# get_webhook
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.webhooks_merchant_level_api.get_webhook()

```


# update_webhook
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.webhooks_merchant_level_api.update_webhook(request)

```


# set_up_webhook
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.webhooks_merchant_level_api.set_up_webhook(request)

```


# generate_hmac_key
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.webhooks_merchant_level_api.generate_hmac_key()

```


# test_webhook
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.webhooks_merchant_level_api.test_webhook(request)

```
