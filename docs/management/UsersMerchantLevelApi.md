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
response = apiClient.users_merchant_level_api.list_users()

```




# get_user_details
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.users_merchant_level_api.get_user_details()

```




# update_user
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;_links&quot; : {
    &quot;self&quot; : {
      &quot;href&quot; : &quot;href&quot;
    }
  },
  &quot;timeZoneCode&quot; : &quot;timeZoneCode&quot;,
  &quot;roles&quot; : [ &quot;roles&quot;, &quot;roles&quot; ],
  &quot;name&quot; : {
    &quot;firstName&quot; : &quot;firstName&quot;,
    &quot;lastName&quot; : &quot;lastName&quot;
  },
  &quot;active&quot; : true,
  &quot;id&quot; : &quot;id&quot;,
  &quot;accountGroups&quot; : [ &quot;accountGroups&quot;, &quot;accountGroups&quot; ],
  &quot;email&quot; : &quot;email&quot;,
  &quot;username&quot; : &quot;username&quot;
}

response = apiClient.users_merchant_level_api.update_user(request)

```




# create_new_user
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;_links&quot; : {
    &quot;self&quot; : {
      &quot;href&quot; : &quot;href&quot;
    }
  },
  &quot;timeZoneCode&quot; : &quot;timeZoneCode&quot;,
  &quot;roles&quot; : [ &quot;roles&quot;, &quot;roles&quot; ],
  &quot;name&quot; : {
    &quot;firstName&quot; : &quot;firstName&quot;,
    &quot;lastName&quot; : &quot;lastName&quot;
  },
  &quot;active&quot; : true,
  &quot;id&quot; : &quot;id&quot;,
  &quot;accountGroups&quot; : [ &quot;accountGroups&quot;, &quot;accountGroups&quot; ],
  &quot;email&quot; : &quot;email&quot;,
  &quot;username&quot; : &quot;username&quot;
}

response = apiClient.users_merchant_level_api.create_new_user(request)

```


