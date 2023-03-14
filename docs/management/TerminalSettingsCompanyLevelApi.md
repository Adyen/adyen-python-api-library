# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_terminal_logo**](TerminalSettingsCompanyLevelApi.md#get_terminal_logo) | **GET** /companies/{companyId}/terminalLogos | Get the terminal logo
[**get_terminal_settings**](TerminalSettingsCompanyLevelApi.md#get_terminal_settings) | **GET** /companies/{companyId}/terminalSettings | Get terminal settings
[**update_terminal_logo**](TerminalSettingsCompanyLevelApi.md#update_terminal_logo) | **PATCH** /companies/{companyId}/terminalLogos | Update the terminal logo
[**update_terminal_settings**](TerminalSettingsCompanyLevelApi.md#update_terminal_settings) | **PATCH** /companies/{companyId}/terminalSettings | Update terminal settings




# get_terminal_logo
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_settings_company_level_api.get_terminal_logo()

```


# get_terminal_settings
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_settings_company_level_api.get_terminal_settings()

```


# update_terminal_logo
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_settings_company_level_api.update_terminal_logo(request)

```


# update_terminal_settings
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_settings_company_level_api.update_terminal_settings(request)

```
