# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_new_api_key**](APIKeyMerchantLevelApi.md#generate_new_api_key) | **POST** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey | Generate new API key




# generate_new_api_key
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.api_key_merchant_level_api.generate_new_api_key(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params

