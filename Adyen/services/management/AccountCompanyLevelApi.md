# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_company_accounts**](AccountCompanyLevelApi.md#list_company_accounts) | **GET** /companies | Get a list of company accounts
[**get_company_account**](AccountCompanyLevelApi.md#get_company_account) | **GET** /companies/{companyId} | Get a company account
[**list_merchant_accounts**](AccountCompanyLevelApi.md#list_merchant_accounts) | **GET** /companies/{companyId}/merchants | Get a list of merchant accounts




# list_company_accounts
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.account_company_level_api.list_company_accounts(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# get_company_account
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.account_company_level_api.get_company_account(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# list_merchant_accounts
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.account_company_level_api.list_merchant_accounts(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params


