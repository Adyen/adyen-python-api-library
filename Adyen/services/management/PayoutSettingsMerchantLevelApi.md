# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_payout_setting**](PayoutSettingsMerchantLevelApi.md#delete_payout_setting) | **DELETE** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Delete a payout setting
[**list_payout_settings**](PayoutSettingsMerchantLevelApi.md#list_payout_settings) | **GET** /merchants/{merchantId}/payoutSettings | Get a list of payout settings
[**get_payout_setting**](PayoutSettingsMerchantLevelApi.md#get_payout_setting) | **GET** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Get a payout setting
[**update_payout_setting**](PayoutSettingsMerchantLevelApi.md#update_payout_setting) | **PATCH** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Update a payout setting
[**add_payout_setting**](PayoutSettingsMerchantLevelApi.md#add_payout_setting) | **POST** /merchants/{merchantId}/payoutSettings | Add a payout setting




# delete_payout_setting
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payout_settings_merchant_level_api.delete_payout_setting(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# list_payout_settings
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payout_settings_merchant_level_api.list_payout_settings(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# get_payout_setting
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payout_settings_merchant_level_api.get_payout_setting(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# update_payout_setting
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payout_settings_merchant_level_api.update_payout_setting(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# add_payout_setting
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payout_settings_merchant_level_api.add_payout_setting(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params


