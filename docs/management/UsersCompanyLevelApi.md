# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_users**](UsersCompanyLevelApi.md#list_users) | **GET** /companies/{companyId}/users | Get a list of users
[**get_user_details**](UsersCompanyLevelApi.md#get_user_details) | **GET** /companies/{companyId}/users/{userId} | Get user details
[**update_user_details**](UsersCompanyLevelApi.md#update_user_details) | **PATCH** /companies/{companyId}/users/{userId} | Update user details
[**create_new_user**](UsersCompanyLevelApi.md#create_new_user) | **POST** /companies/{companyId}/users | Create a new user




# list_users
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.users_company_level_api.list_users()

```




# get_user_details
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.users_company_level_api.get_user_details()

```




# update_user_details
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
  &quot;associatedMerchantAccounts&quot; : [ &quot;associatedMerchantAccounts&quot;, &quot;associatedMerchantAccounts&quot; ],
  &quot;id&quot; : &quot;id&quot;,
  &quot;accountGroups&quot; : [ &quot;accountGroups&quot;, &quot;accountGroups&quot; ],
  &quot;email&quot; : &quot;email&quot;,
  &quot;username&quot; : &quot;username&quot;
}

response = apiClient.users_company_level_api.update_user_details(request)

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
  &quot;associatedMerchantAccounts&quot; : [ &quot;associatedMerchantAccounts&quot;, &quot;associatedMerchantAccounts&quot; ],
  &quot;id&quot; : &quot;id&quot;,
  &quot;accountGroups&quot; : [ &quot;accountGroups&quot;, &quot;accountGroups&quot; ],
  &quot;email&quot; : &quot;email&quot;,
  &quot;username&quot; : &quot;username&quot;
}

response = apiClient.users_company_level_api.create_new_user(request)

```


