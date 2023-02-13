# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_new_client_key**](ClientKeyCompanyLevelApi.md#generate_new_client_key) | **POST** /companies/{companyId}/apiCredentials/{apiCredentialId}/generateClientKey | Generate new client key




# generate_new_client_key
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.client_key_company_level_api.generate_new_client_key(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params


