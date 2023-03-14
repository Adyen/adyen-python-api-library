# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_terminal_logo**](TerminalSettingsStoreLevelApi.md#get_terminal_logo) | **GET** /merchants/{merchantId}/stores/{reference}/terminalLogos | Get the terminal logo
[**get_terminal_settings**](TerminalSettingsStoreLevelApi.md#get_terminal_settings) | **GET** /merchants/{merchantId}/stores/{reference}/terminalSettings | Get terminal settings
[**get_terminal_logo_by_store_id**](TerminalSettingsStoreLevelApi.md#get_terminal_logo_by_store_id) | **GET** /stores/{storeId}/terminalLogos | Get the terminal logo
[**get_terminal_settings_by_store_id**](TerminalSettingsStoreLevelApi.md#get_terminal_settings_by_store_id) | **GET** /stores/{storeId}/terminalSettings | Get terminal settings
[**update_terminal_logo**](TerminalSettingsStoreLevelApi.md#update_terminal_logo) | **PATCH** /merchants/{merchantId}/stores/{reference}/terminalLogos | Update the terminal logo
[**update_terminal_settings**](TerminalSettingsStoreLevelApi.md#update_terminal_settings) | **PATCH** /merchants/{merchantId}/stores/{reference}/terminalSettings | Update terminal settings
[**update_terminal_logo_by_store_id**](TerminalSettingsStoreLevelApi.md#update_terminal_logo_by_store_id) | **PATCH** /stores/{storeId}/terminalLogos | Update the terminal logo
[**update_terminal_settings_by_store_id**](TerminalSettingsStoreLevelApi.md#update_terminal_settings_by_store_id) | **PATCH** /stores/{storeId}/terminalSettings | Update terminal settings




# get_terminal_logo
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_settings_store_level_api.get_terminal_logo()

```


# get_terminal_settings
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_settings_store_level_api.get_terminal_settings()

```


# get_terminal_logo_by_store_id
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_settings_store_level_api.get_terminal_logo_by_store_id()

```


# get_terminal_settings_by_store_id
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_settings_store_level_api.get_terminal_settings_by_store_id()

```


# update_terminal_logo
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_settings_store_level_api.update_terminal_logo(request)

```


# update_terminal_settings
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_settings_store_level_api.update_terminal_settings(request)

```


# update_terminal_logo_by_store_id
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_settings_store_level_api.update_terminal_logo_by_store_id(request)

```


# update_terminal_settings_by_store_id
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_settings_store_level_api.update_terminal_settings_by_store_id(request)

```
