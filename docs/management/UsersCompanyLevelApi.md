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

apiClient.users_company_level_api.list_users()

```


# get_user_details
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.users_company_level_api.get_user_details()

```


# update_user_details
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.users_company_level_api.update_user_details(request)

```


# create_new_user
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.users_company_level_api.create_new_user(request)

```
