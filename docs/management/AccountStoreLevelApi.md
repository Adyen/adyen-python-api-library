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
response = apiClient.account_store_level_api.list_stores_by_merchant_id()

```




# get_store
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.account_store_level_api.get_store()

```




# list_stores
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.account_store_level_api.list_stores()

```




# get_store_by_id
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.account_store_level_api.get_store_by_id()

```




# update_store
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;externalReferenceId&quot; : &quot;externalReferenceId&quot;,
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;address&quot; : {
    &quot;country&quot; : &quot;country&quot;,
    &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
    &quot;city&quot; : &quot;city&quot;,
    &quot;postalCode&quot; : &quot;postalCode&quot;,
    &quot;line3&quot; : &quot;line3&quot;,
    &quot;line2&quot; : &quot;line2&quot;,
    &quot;line1&quot; : &quot;line1&quot;
  },
  &quot;phoneNumber&quot; : &quot;phoneNumber&quot;,
  &quot;_links&quot; : {
    &quot;self&quot; : {
      &quot;href&quot; : &quot;href&quot;
    }
  },
  &quot;merchantId&quot; : &quot;merchantId&quot;,
  &quot;description&quot; : &quot;description&quot;,
  &quot;id&quot; : &quot;id&quot;,
  &quot;businessLineIds&quot; : [ &quot;businessLineIds&quot;, &quot;businessLineIds&quot; ],
  &quot;shopperStatement&quot; : &quot;shopperStatement&quot;,
  &quot;splitConfiguration&quot; : {
    &quot;balanceAccountId&quot; : &quot;balanceAccountId&quot;,
    &quot;splitConfigurationId&quot; : &quot;splitConfigurationId&quot;
  },
  &quot;status&quot; : &quot;active&quot;
}

response = apiClient.account_store_level_api.update_store(request)

```




# update_store_by_id
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;externalReferenceId&quot; : &quot;externalReferenceId&quot;,
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;address&quot; : {
    &quot;country&quot; : &quot;country&quot;,
    &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
    &quot;city&quot; : &quot;city&quot;,
    &quot;postalCode&quot; : &quot;postalCode&quot;,
    &quot;line3&quot; : &quot;line3&quot;,
    &quot;line2&quot; : &quot;line2&quot;,
    &quot;line1&quot; : &quot;line1&quot;
  },
  &quot;phoneNumber&quot; : &quot;phoneNumber&quot;,
  &quot;_links&quot; : {
    &quot;self&quot; : {
      &quot;href&quot; : &quot;href&quot;
    }
  },
  &quot;merchantId&quot; : &quot;merchantId&quot;,
  &quot;description&quot; : &quot;description&quot;,
  &quot;id&quot; : &quot;id&quot;,
  &quot;businessLineIds&quot; : [ &quot;businessLineIds&quot;, &quot;businessLineIds&quot; ],
  &quot;shopperStatement&quot; : &quot;shopperStatement&quot;,
  &quot;splitConfiguration&quot; : {
    &quot;balanceAccountId&quot; : &quot;balanceAccountId&quot;,
    &quot;splitConfigurationId&quot; : &quot;splitConfigurationId&quot;
  },
  &quot;status&quot; : &quot;active&quot;
}

response = apiClient.account_store_level_api.update_store_by_id(request)

```




# create_store_by_merchant_id
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;externalReferenceId&quot; : &quot;externalReferenceId&quot;,
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;address&quot; : {
    &quot;country&quot; : &quot;country&quot;,
    &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
    &quot;city&quot; : &quot;city&quot;,
    &quot;postalCode&quot; : &quot;postalCode&quot;,
    &quot;line3&quot; : &quot;line3&quot;,
    &quot;line2&quot; : &quot;line2&quot;,
    &quot;line1&quot; : &quot;line1&quot;
  },
  &quot;phoneNumber&quot; : &quot;phoneNumber&quot;,
  &quot;_links&quot; : {
    &quot;self&quot; : {
      &quot;href&quot; : &quot;href&quot;
    }
  },
  &quot;merchantId&quot; : &quot;merchantId&quot;,
  &quot;description&quot; : &quot;description&quot;,
  &quot;id&quot; : &quot;id&quot;,
  &quot;businessLineIds&quot; : [ &quot;businessLineIds&quot;, &quot;businessLineIds&quot; ],
  &quot;shopperStatement&quot; : &quot;shopperStatement&quot;,
  &quot;splitConfiguration&quot; : {
    &quot;balanceAccountId&quot; : &quot;balanceAccountId&quot;,
    &quot;splitConfigurationId&quot; : &quot;splitConfigurationId&quot;
  },
  &quot;status&quot; : &quot;active&quot;
}

response = apiClient.account_store_level_api.create_store_by_merchant_id(request)

```




# create_store
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;externalReferenceId&quot; : &quot;externalReferenceId&quot;,
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;address&quot; : {
    &quot;country&quot; : &quot;country&quot;,
    &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
    &quot;city&quot; : &quot;city&quot;,
    &quot;postalCode&quot; : &quot;postalCode&quot;,
    &quot;line3&quot; : &quot;line3&quot;,
    &quot;line2&quot; : &quot;line2&quot;,
    &quot;line1&quot; : &quot;line1&quot;
  },
  &quot;phoneNumber&quot; : &quot;phoneNumber&quot;,
  &quot;_links&quot; : {
    &quot;self&quot; : {
      &quot;href&quot; : &quot;href&quot;
    }
  },
  &quot;merchantId&quot; : &quot;merchantId&quot;,
  &quot;description&quot; : &quot;description&quot;,
  &quot;id&quot; : &quot;id&quot;,
  &quot;businessLineIds&quot; : [ &quot;businessLineIds&quot;, &quot;businessLineIds&quot; ],
  &quot;shopperStatement&quot; : &quot;shopperStatement&quot;,
  &quot;splitConfiguration&quot; : {
    &quot;balanceAccountId&quot; : &quot;balanceAccountId&quot;,
    &quot;splitConfigurationId&quot; : &quot;splitConfigurationId&quot;
  },
  &quot;status&quot; : &quot;active&quot;
}

response = apiClient.account_store_level_api.create_store(request)

```


