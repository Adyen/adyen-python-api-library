# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_allowed_origin**](AllowedOriginsCompanyLevelApi.md#delete_allowed_origin) | **DELETE** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | Delete an allowed origin
[**list_allowed_origins**](AllowedOriginsCompanyLevelApi.md#list_allowed_origins) | **GET** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | Get a list of allowed origins
[**get_allowed_origin**](AllowedOriginsCompanyLevelApi.md#get_allowed_origin) | **GET** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | Get an allowed origin
[**create_allowed_origin**](AllowedOriginsCompanyLevelApi.md#create_allowed_origin) | **POST** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | Create an allowed origin




# delete_allowed_origin
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.allowed_origins_company_level_api.delete_allowed_origin()

```


# list_allowed_origins
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.allowed_origins_company_level_api.list_allowed_origins()

```


# get_allowed_origin
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.allowed_origins_company_level_api.get_allowed_origin()

```


# create_allowed_origin
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.allowed_origins_company_level_api.create_allowed_origin(request)

```
