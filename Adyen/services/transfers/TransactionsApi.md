# transfers

All URIs are relative to *https://balanceplatform-api-test.adyen.com/btl/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_transactions**](TransactionsApi.md#get_all_transactions) | **GET** /transactions | Get all transactions
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /transactions/{id} | Get a transaction




# get_all_transactions
### Example

```python
from Adyen import transfers


apiClient = transfers
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.transactions_api.get_all_transactions(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# get_transaction
### Example

```python
from Adyen import transfers


apiClient = transfers
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.transactions_api.get_transaction(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params


