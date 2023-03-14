# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_new_client_key**](ClientKeyMerchantLevelApi.md#generate_new_client_key) | **POST** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateClientKey | Generate new client key




# generate_new_client_key
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.client_key_merchant_level_api.generate_new_client_key()

```
