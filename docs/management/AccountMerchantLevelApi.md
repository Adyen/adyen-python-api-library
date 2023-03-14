# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_merchant_accounts**](AccountMerchantLevelApi.md#list_merchant_accounts) | **GET** /merchants | Get a list of merchant accounts
[**get_merchant_account**](AccountMerchantLevelApi.md#get_merchant_account) | **GET** /merchants/{merchantId} | Get a merchant account
[**create_merchant_account**](AccountMerchantLevelApi.md#create_merchant_account) | **POST** /merchants | Create a merchant account
[**request_to_activate_merchant_account**](AccountMerchantLevelApi.md#request_to_activate_merchant_account) | **POST** /merchants/{merchantId}/activate | Request to activate a merchant account




# list_merchant_accounts
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.account_merchant_level_api.list_merchant_accounts()

```


# get_merchant_account
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.account_merchant_level_api.get_merchant_account()

```


# create_merchant_account
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.account_merchant_level_api.create_merchant_account(request)

```


# request_to_activate_merchant_account
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.account_merchant_level_api.request_to_activate_merchant_account()

```
