# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_stores_by_merchant_id**](AccountStoreLevelApi.md#list_stores_by_merchant_id) | **GET** /merchants/{merchantId}/stores | Get a list of stores
[**get_store**](AccountStoreLevelApi.md#get_store) | **GET** /merchants/{merchantId}/stores/{storeId} | Get a store
[**list_stores**](AccountStoreLevelApi.md#list_stores) | **GET** /stores | Get a list of stores
[**get_store_by_id**](AccountStoreLevelApi.md#get_store_by_id) | **GET** /stores/{storeId} | Get a store
[**update_store**](AccountStoreLevelApi.md#update_store) | **PATCH** /merchants/{merchantId}/stores/{storeId} | Update a store
[**update_store_by_id**](AccountStoreLevelApi.md#update_store_by_id) | **PATCH** /stores/{storeId} | Update a store
[**create_store_by_merchant_id**](AccountStoreLevelApi.md#create_store_by_merchant_id) | **POST** /merchants/{merchantId}/stores | Create a store
[**create_store**](AccountStoreLevelApi.md#create_store) | **POST** /stores | Create a store




# list_stores_by_merchant_id
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.account_store_level_api.list_stores_by_merchant_id(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# get_store
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.account_store_level_api.get_store(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# list_stores
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.account_store_level_api.list_stores(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# get_store_by_id
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.account_store_level_api.get_store_by_id(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# update_store
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.account_store_level_api.update_store(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# update_store_by_id
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.account_store_level_api.update_store_by_id(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# create_store_by_merchant_id
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.account_store_level_api.create_store_by_merchant_id(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# create_store
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.account_store_level_api.create_store(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params


