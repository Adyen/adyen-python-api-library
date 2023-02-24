# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_allowed_origin**](MyAPICredentialApi.md#remove_allowed_origin) | **DELETE** /me/allowedOrigins/{originId} | Remove allowed origin
[**get_api_credential_details**](MyAPICredentialApi.md#get_api_credential_details) | **GET** /me | Get API credential details
[**get_allowed_origins**](MyAPICredentialApi.md#get_allowed_origins) | **GET** /me/allowedOrigins | Get allowed origins
[**get_allowed_origin_details**](MyAPICredentialApi.md#get_allowed_origin_details) | **GET** /me/allowedOrigins/{originId} | Get allowed origin details
[**add_allowed_origin**](MyAPICredentialApi.md#add_allowed_origin) | **POST** /me/allowedOrigins | Add allowed origin




# remove_allowed_origin
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.my_api_credential_api.remove_allowed_origin()

```




# get_api_credential_details
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.my_api_credential_api.get_api_credential_details()

```




# get_allowed_origins
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.my_api_credential_api.get_allowed_origins()

```




# get_allowed_origin_details
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.my_api_credential_api.get_allowed_origin_details()

```




# add_allowed_origin
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;data&quot; : [ {
    &quot;_links&quot; : {
      &quot;self&quot; : {
        &quot;href&quot; : &quot;href&quot;
      }
    },
    &quot;domain&quot; : &quot;https://adyen.com&quot;,
    &quot;id&quot; : &quot;id&quot;
  }, {
    &quot;_links&quot; : {
      &quot;self&quot; : {
        &quot;href&quot; : &quot;href&quot;
      }
    },
    &quot;domain&quot; : &quot;https://adyen.com&quot;,
    &quot;id&quot; : &quot;id&quot;
  } ]
}

response = apiClient.my_api_credential_api.add_allowed_origin(request)

```


