# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_android_apps**](TerminalActionsCompanyLevelApi.md#list_android_apps) | **GET** /companies/{companyId}/androidApps | Get a list of Android apps
[**list_android_certificates**](TerminalActionsCompanyLevelApi.md#list_android_certificates) | **GET** /companies/{companyId}/androidCertificates | Get a list of Android certificates
[**list_terminal_actions**](TerminalActionsCompanyLevelApi.md#list_terminal_actions) | **GET** /companies/{companyId}/terminalActions | Get a list of terminal actions
[**get_terminal_action**](TerminalActionsCompanyLevelApi.md#get_terminal_action) | **GET** /companies/{companyId}/terminalActions/{actionId} | Get terminal action




# list_android_apps
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_actions_company_level_api.list_android_apps()

```


# list_android_certificates
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_actions_company_level_api.list_android_certificates()

```


# list_terminal_actions
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_actions_company_level_api.list_terminal_actions()

```


# get_terminal_action
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_actions_company_level_api.get_terminal_action()

```
