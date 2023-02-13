# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_users**](UsersMerchantLevelApi.md#list_users) | **GET** /merchants/{merchantId}/users | Get a list of users
[**get_user_details**](UsersMerchantLevelApi.md#get_user_details) | **GET** /merchants/{merchantId}/users/{userId} | Get user details
[**update_user**](UsersMerchantLevelApi.md#update_user) | **PATCH** /merchants/{merchantId}/users/{userId} | Update a user
[**create_new_user**](UsersMerchantLevelApi.md#create_new_user) | **POST** /merchants/{merchantId}/users | Create a new user




# list_users
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.users_merchant_level_api.list_users(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# get_user_details
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.users_merchant_level_api.get_user_details(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# update_user
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.users_merchant_level_api.update_user(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# create_new_user
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.users_merchant_level_api.create_new_user(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params


