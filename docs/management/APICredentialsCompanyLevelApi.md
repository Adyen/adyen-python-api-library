# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_api_credentials**](APICredentialsCompanyLevelApi.md#list_api_credentials) | **GET** /companies/{companyId}/apiCredentials | Get a list of API credentials
[**get_api_credential**](APICredentialsCompanyLevelApi.md#get_api_credential) | **GET** /companies/{companyId}/apiCredentials/{apiCredentialId} | Get an API credential
[**update_api_credential**](APICredentialsCompanyLevelApi.md#update_api_credential) | **PATCH** /companies/{companyId}/apiCredentials/{apiCredentialId} | Update an API credential.
[**create_api_credential**](APICredentialsCompanyLevelApi.md#create_api_credential) | **POST** /companies/{companyId}/apiCredentials | Create an API credential.




# list_api_credentials
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.api_credentials_company_level_api.list_api_credentials()

```




# get_api_credential
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.api_credentials_company_level_api.get_api_credential()

```




# update_api_credential
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;allowedOrigins&quot; : [ {
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
  } ],
  &quot;_links&quot; : {
    &quot;allowedOrigins&quot; : {
      &quot;href&quot; : &quot;href&quot;
    },
    &quot;generateApiKey&quot; : {
      &quot;href&quot; : &quot;href&quot;
    },
    &quot;merchant&quot; : {
      &quot;href&quot; : &quot;href&quot;
    },
    &quot;self&quot; : {
      &quot;href&quot; : &quot;href&quot;
    },
    &quot;company&quot; : {
      &quot;href&quot; : &quot;href&quot;
    },
    &quot;generateClientKey&quot; : {
      &quot;href&quot; : &quot;href&quot;
    }
  },
  &quot;allowedIpAddresses&quot; : [ &quot;allowedIpAddresses&quot;, &quot;allowedIpAddresses&quot; ],
  &quot;clientKey&quot; : &quot;clientKey&quot;,
  &quot;roles&quot; : [ &quot;roles&quot;, &quot;roles&quot; ],
  &quot;active&quot; : true,
  &quot;description&quot; : &quot;description&quot;,
  &quot;associatedMerchantAccounts&quot; : [ &quot;associatedMerchantAccounts&quot;, &quot;associatedMerchantAccounts&quot; ],
  &quot;id&quot; : &quot;id&quot;,
  &quot;username&quot; : &quot;username&quot;
}

response = apiClient.api_credentials_company_level_api.update_api_credential(request)

```




# create_api_credential
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;password&quot; : &quot;password&quot;,
  &quot;allowedOrigins&quot; : [ {
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
  } ],
  &quot;apiKey&quot; : &quot;apiKey&quot;,
  &quot;_links&quot; : {
    &quot;allowedOrigins&quot; : {
      &quot;href&quot; : &quot;href&quot;
    },
    &quot;generateApiKey&quot; : {
      &quot;href&quot; : &quot;href&quot;
    },
    &quot;merchant&quot; : {
      &quot;href&quot; : &quot;href&quot;
    },
    &quot;self&quot; : {
      &quot;href&quot; : &quot;href&quot;
    },
    &quot;company&quot; : {
      &quot;href&quot; : &quot;href&quot;
    },
    &quot;generateClientKey&quot; : {
      &quot;href&quot; : &quot;href&quot;
    }
  },
  &quot;allowedIpAddresses&quot; : [ &quot;allowedIpAddresses&quot;, &quot;allowedIpAddresses&quot; ],
  &quot;clientKey&quot; : &quot;clientKey&quot;,
  &quot;roles&quot; : [ &quot;roles&quot;, &quot;roles&quot; ],
  &quot;active&quot; : true,
  &quot;description&quot; : &quot;description&quot;,
  &quot;associatedMerchantAccounts&quot; : [ &quot;associatedMerchantAccounts&quot;, &quot;associatedMerchantAccounts&quot; ],
  &quot;id&quot; : &quot;id&quot;,
  &quot;username&quot; : &quot;username&quot;
}

response = apiClient.api_credentials_company_level_api.create_api_credential(request)

```


