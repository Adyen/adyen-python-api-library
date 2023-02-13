# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_api_credentials**](APICredentialsMerchantLevelApi.md#list_api_credentials) | **GET** /merchants/{merchantId}/apiCredentials | Get a list of API credentials
[**get_api_credential**](APICredentialsMerchantLevelApi.md#get_api_credential) | **GET** /merchants/{merchantId}/apiCredentials/{apiCredentialId} | Get an API credential
[**update_api_credential**](APICredentialsMerchantLevelApi.md#update_api_credential) | **PATCH** /merchants/{merchantId}/apiCredentials/{apiCredentialId} | Update an API credential
[**create_api_credential**](APICredentialsMerchantLevelApi.md#create_api_credential) | **POST** /merchants/{merchantId}/apiCredentials | Create an API credential




# list_api_credentials
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.api_credentials_merchant_level_api.list_api_credentials(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# get_api_credential
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.api_credentials_merchant_level_api.get_api_credential(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# update_api_credential
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.api_credentials_merchant_level_api.update_api_credential(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# create_api_credential
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.api_credentials_merchant_level_api.create_api_credential(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params


