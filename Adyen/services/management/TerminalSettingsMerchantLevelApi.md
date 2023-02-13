# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_terminal_logo**](TerminalSettingsMerchantLevelApi.md#get_terminal_logo) | **GET** /merchants/{merchantId}/terminalLogos | Get the terminal logo
[**get_terminal_settings**](TerminalSettingsMerchantLevelApi.md#get_terminal_settings) | **GET** /merchants/{merchantId}/terminalSettings | Get terminal settings
[**update_terminal_logo**](TerminalSettingsMerchantLevelApi.md#update_terminal_logo) | **PATCH** /merchants/{merchantId}/terminalLogos | Update the terminal logo
[**update_terminal_settings**](TerminalSettingsMerchantLevelApi.md#update_terminal_settings) | **PATCH** /merchants/{merchantId}/terminalSettings | Update terminal settings




# get_terminal_logo
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_settings_merchant_level_api.get_terminal_logo(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# get_terminal_settings
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_settings_merchant_level_api.get_terminal_settings(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# update_terminal_logo
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_settings_merchant_level_api.update_terminal_logo(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# update_terminal_settings
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_settings_merchant_level_api.update_terminal_settings(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params


