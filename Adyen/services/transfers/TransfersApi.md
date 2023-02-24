# transfers

All URIs are relative to *https://balanceplatform-api-test.adyen.com/btl/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfer_funds**](TransfersApi.md#transfer_funds) | **POST** /transfers | Transfer funds




# transfer_funds
### Example

```python
from Adyen import transfers


apiClient = transfers
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.transfers_api.transfer_funds(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params


