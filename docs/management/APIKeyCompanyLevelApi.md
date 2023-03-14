# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_new_api_key**](APIKeyCompanyLevelApi.md#generate_new_api_key) | **POST** /companies/{companyId}/apiCredentials/{apiCredentialId}/generateApiKey | Generate new API key




# generate_new_api_key
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.api_key_company_level_api.generate_new_api_key()

```
