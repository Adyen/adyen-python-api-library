# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_terminal_action**](TerminalActionsTerminalLevelApi.md#create_terminal_action) | **POST** /terminals/scheduleActions | Create a terminal action




# create_terminal_action
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;totalScheduled&quot; : 6,
  &quot;totalErrors&quot; : 0,
  &quot;terminalsWithErrors&quot; : {
    &quot;key&quot; : [ &quot;terminalsWithErrors&quot;, &quot;terminalsWithErrors&quot; ]
  },
  &quot;storeId&quot; : &quot;storeId&quot;,
  &quot;terminalIds&quot; : [ &quot;terminalIds&quot;, &quot;terminalIds&quot; ],
  &quot;items&quot; : [ {
    &quot;id&quot; : &quot;id&quot;,
    &quot;terminalId&quot; : &quot;terminalId&quot;
  }, {
    &quot;id&quot; : &quot;id&quot;,
    &quot;terminalId&quot; : &quot;terminalId&quot;
  } ],
  &quot;scheduledAt&quot; : &quot;scheduledAt&quot;
}

response = apiClient.terminal_actions_terminal_level_api.create_terminal_action(request)

```


