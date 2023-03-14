# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_terminals**](TerminalsTerminalLevelApi.md#list_terminals) | **GET** /terminals | Get a list of terminals




# list_terminals
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminals_terminal_level_api.list_terminals()

```
