# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_webhook**](WebhooksCompanyLevelApi.md#remove_webhook) | **DELETE** /companies/{companyId}/webhooks/{webhookId} | Remove a webhook
[**list_all_webhooks**](WebhooksCompanyLevelApi.md#list_all_webhooks) | **GET** /companies/{companyId}/webhooks | List all webhooks
[**get_webhook**](WebhooksCompanyLevelApi.md#get_webhook) | **GET** /companies/{companyId}/webhooks/{webhookId} | Get a webhook
[**update_webhook**](WebhooksCompanyLevelApi.md#update_webhook) | **PATCH** /companies/{companyId}/webhooks/{webhookId} | Update a webhook
[**set_up_webhook**](WebhooksCompanyLevelApi.md#set_up_webhook) | **POST** /companies/{companyId}/webhooks | Set up a webhook
[**generate_hmac_key**](WebhooksCompanyLevelApi.md#generate_hmac_key) | **POST** /companies/{companyId}/webhooks/{webhookId}/generateHmac | Generate an HMAC key
[**test_webhook**](WebhooksCompanyLevelApi.md#test_webhook) | **POST** /companies/{companyId}/webhooks/{webhookId}/test | Test a webhook




# remove_webhook
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.webhooks_company_level_api.remove_webhook()

```


# list_all_webhooks
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.webhooks_company_level_api.list_all_webhooks()

```


# get_webhook
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.webhooks_company_level_api.get_webhook()

```


# update_webhook
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.webhooks_company_level_api.update_webhook(request)

```


# set_up_webhook
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.webhooks_company_level_api.set_up_webhook(request)

```


# generate_hmac_key
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.webhooks_company_level_api.generate_hmac_key()

```


# test_webhook
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.webhooks_company_level_api.test_webhook(request)

```
