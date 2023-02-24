# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_webhook**](WebhooksCompanyLevelApi.md#remove_webhook) | **DELETE** /companies/{companyId}/webhooks/{webhookId} | Remove a webhook
[**list_all_webhooks**](WebhooksCompanyLevelApi.md#list_all_webhooks) | **GET** /companies/{companyId}/webhooks | List all webhooks
[**get_webhook**](WebhooksCompanyLevelApi.md#get_webhook) | **GET** /companies/{companyId}/webhooks/{webhookId} | Get a webhook
[**update_webhook**](WebhooksCompanyLevelApi.md#update_webhook) | **PATCH** /companies/{companyId}/webhooks/{webhookId} | Update a webhook
[**set_up_webhook**](WebhooksCompanyLevelApi.md#set_up_webhook) | **POST** /companies/{companyId}/webhooks | Set up a webhook
[**generate_hmac_key**](WebhooksCompanyLevelApi.md#generate_hmac_key) | **POST** /companies/{companyId}/webhooks/{webhookId}/generateHmac | Generate an HMAC key
[**test_webhook**](WebhooksCompanyLevelApi.md#test_webhook) | **POST** /companies/{companyId}/webhooks/{webhookId}/test | Test a webhook




# remove_webhook
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.webhooks_company_level_api.remove_webhook()

```




# list_all_webhooks
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.webhooks_company_level_api.list_all_webhooks()

```




# get_webhook
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.webhooks_company_level_api.get_webhook()

```




# update_webhook
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;communicationFormat&quot; : &quot;SOAP&quot;,
  &quot;accountReference&quot; : &quot;accountReference&quot;,
  &quot;sslVersion&quot; : &quot;TLSv1.2&quot;,
  &quot;_links&quot; : {
    &quot;generateHmac&quot; : {
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
    &quot;testWebhook&quot; : {
      &quot;href&quot; : &quot;href&quot;
    }
  },
  &quot;acceptsUntrustedRootCertificate&quot; : true,
  &quot;filterMerchantAccountType&quot; : &quot;EXCLUDE_LIST&quot;,
  &quot;filterMerchantAccounts&quot; : [ &quot;filterMerchantAccounts&quot;, &quot;filterMerchantAccounts&quot; ],
  &quot;active&quot; : true,
  &quot;description&quot; : &quot;description&quot;,
  &quot;acceptsSelfSignedCertificate&quot; : true,
  &quot;certificateAlias&quot; : &quot;certificateAlias&quot;,
  &quot;hasPassword&quot; : true,
  &quot;type&quot; : &quot;type&quot;,
  &quot;url&quot; : &quot;http://www.adyen.com&quot;,
  &quot;additionalSettings&quot; : {
    &quot;includeEventCodes&quot; : [ &quot;includeEventCodes&quot;, &quot;includeEventCodes&quot; ],
    &quot;excludeEventCodes&quot; : [ &quot;excludeEventCodes&quot;, &quot;excludeEventCodes&quot; ],
    &quot;properties&quot; : {
      &quot;key&quot; : true
    }
  },
  &quot;acceptsExpiredCertificate&quot; : true,
  &quot;hasError&quot; : true,
  &quot;id&quot; : &quot;id&quot;,
  &quot;hmacKeyCheckValue&quot; : &quot;hmacKeyCheckValue&quot;,
  &quot;networkType&quot; : &quot;LOCAL&quot;,
  &quot;populateSoapActionHeader&quot; : true,
  &quot;username&quot; : &quot;username&quot;
}

response = apiClient.webhooks_company_level_api.update_webhook(request)

```




# set_up_webhook
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;communicationFormat&quot; : &quot;SOAP&quot;,
  &quot;accountReference&quot; : &quot;accountReference&quot;,
  &quot;sslVersion&quot; : &quot;TLSv1.2&quot;,
  &quot;_links&quot; : {
    &quot;generateHmac&quot; : {
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
    &quot;testWebhook&quot; : {
      &quot;href&quot; : &quot;href&quot;
    }
  },
  &quot;acceptsUntrustedRootCertificate&quot; : true,
  &quot;filterMerchantAccountType&quot; : &quot;EXCLUDE_LIST&quot;,
  &quot;filterMerchantAccounts&quot; : [ &quot;filterMerchantAccounts&quot;, &quot;filterMerchantAccounts&quot; ],
  &quot;active&quot; : true,
  &quot;description&quot; : &quot;description&quot;,
  &quot;acceptsSelfSignedCertificate&quot; : true,
  &quot;certificateAlias&quot; : &quot;certificateAlias&quot;,
  &quot;hasPassword&quot; : true,
  &quot;type&quot; : &quot;type&quot;,
  &quot;url&quot; : &quot;http://www.adyen.com&quot;,
  &quot;additionalSettings&quot; : {
    &quot;includeEventCodes&quot; : [ &quot;includeEventCodes&quot;, &quot;includeEventCodes&quot; ],
    &quot;excludeEventCodes&quot; : [ &quot;excludeEventCodes&quot;, &quot;excludeEventCodes&quot; ],
    &quot;properties&quot; : {
      &quot;key&quot; : true
    }
  },
  &quot;acceptsExpiredCertificate&quot; : true,
  &quot;hasError&quot; : true,
  &quot;id&quot; : &quot;id&quot;,
  &quot;hmacKeyCheckValue&quot; : &quot;hmacKeyCheckValue&quot;,
  &quot;networkType&quot; : &quot;LOCAL&quot;,
  &quot;populateSoapActionHeader&quot; : true,
  &quot;username&quot; : &quot;username&quot;
}

response = apiClient.webhooks_company_level_api.set_up_webhook(request)

```




# generate_hmac_key
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.webhooks_company_level_api.generate_hmac_key()

```




# test_webhook
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;data&quot; : [ {
    &quot;output&quot; : &quot;output&quot;,
    &quot;merchantId&quot; : &quot;merchantId&quot;,
    &quot;responseTime&quot; : &quot;responseTime&quot;,
    &quot;requestSent&quot; : &quot;requestSent&quot;,
    &quot;responseCode&quot; : &quot;200&quot;,
    &quot;status&quot; : &quot;status&quot;
  }, {
    &quot;output&quot; : &quot;output&quot;,
    &quot;merchantId&quot; : &quot;merchantId&quot;,
    &quot;responseTime&quot; : &quot;responseTime&quot;,
    &quot;requestSent&quot; : &quot;requestSent&quot;,
    &quot;responseCode&quot; : &quot;200&quot;,
    &quot;status&quot; : &quot;status&quot;
  } ]
}

response = apiClient.webhooks_company_level_api.test_webhook(request)

```


