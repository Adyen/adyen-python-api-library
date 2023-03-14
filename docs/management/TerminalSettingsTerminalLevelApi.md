# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_terminal_logo**](TerminalSettingsTerminalLevelApi.md#get_terminal_logo) | **GET** /terminals/{terminalId}/terminalLogos | Get the terminal logo
[**get_terminal_settings**](TerminalSettingsTerminalLevelApi.md#get_terminal_settings) | **GET** /terminals/{terminalId}/terminalSettings | Get terminal settings
[**update_logo**](TerminalSettingsTerminalLevelApi.md#update_logo) | **PATCH** /terminals/{terminalId}/terminalLogos | Update the logo
[**update_terminal_settings**](TerminalSettingsTerminalLevelApi.md#update_terminal_settings) | **PATCH** /terminals/{terminalId}/terminalSettings | Update terminal settings




# get_terminal_logo
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_settings_terminal_level_api.get_terminal_logo()

```


# get_terminal_settings
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_settings_terminal_level_api.get_terminal_settings()

```


# update_logo
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_settings_terminal_level_api.update_logo(request)

```


# update_terminal_settings
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_settings_terminal_level_api.update_terminal_settings(request)

```
