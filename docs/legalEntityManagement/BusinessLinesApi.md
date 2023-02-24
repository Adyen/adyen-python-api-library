# legalEntityManagement

All URIs are relative to *https://kyc-test.adyen.com/lem/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_business_line**](BusinessLinesApi.md#delete_business_line) | **DELETE** /businessLines/{id} | Delete a business line
[**get_business_line**](BusinessLinesApi.md#get_business_line) | **GET** /businessLines/{id} | Get a business line
[**update_business_line**](BusinessLinesApi.md#update_business_line) | **PATCH** /businessLines/{id} | Update a business line
[**create_business_line**](BusinessLinesApi.md#create_business_line) | **POST** /businessLines | Create a business line




# delete_business_line
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.business_lines_api.delete_business_line()

```




# get_business_line
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.business_lines_api.get_business_line()

```




# update_business_line
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;salesChannels&quot; : [ &quot;salesChannels&quot;, &quot;salesChannels&quot; ],
  &quot;capability&quot; : &quot;capability&quot;,
  &quot;legalEntityId&quot; : &quot;legalEntityId&quot;,
  &quot;webDataExemption&quot; : {
    &quot;reason&quot; : &quot;noOnlinePresence&quot;
  },
  &quot;sourceOfFunds&quot; : {
    &quot;description&quot; : &quot;description&quot;,
    &quot;adyenProcessedFunds&quot; : true,
    &quot;type&quot; : &quot;business&quot;,
    &quot;acquiringBusinessLineId&quot; : &quot;acquiringBusinessLineId&quot;
  },
  &quot;webData&quot; : [ {
    &quot;webAddressId&quot; : &quot;webAddressId&quot;,
    &quot;webAddress&quot; : &quot;webAddress&quot;
  }, {
    &quot;webAddressId&quot; : &quot;webAddressId&quot;,
    &quot;webAddress&quot; : &quot;webAddress&quot;
  } ],
  &quot;id&quot; : &quot;id&quot;,
  &quot;industryCode&quot; : &quot;industryCode&quot;
}

response = apiClient.business_lines_api.update_business_line(request)

```




# create_business_line
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;salesChannels&quot; : [ &quot;salesChannels&quot;, &quot;salesChannels&quot; ],
  &quot;capability&quot; : &quot;capability&quot;,
  &quot;legalEntityId&quot; : &quot;legalEntityId&quot;,
  &quot;webDataExemption&quot; : {
    &quot;reason&quot; : &quot;noOnlinePresence&quot;
  },
  &quot;sourceOfFunds&quot; : {
    &quot;description&quot; : &quot;description&quot;,
    &quot;adyenProcessedFunds&quot; : true,
    &quot;type&quot; : &quot;business&quot;,
    &quot;acquiringBusinessLineId&quot; : &quot;acquiringBusinessLineId&quot;
  },
  &quot;webData&quot; : [ {
    &quot;webAddressId&quot; : &quot;webAddressId&quot;,
    &quot;webAddress&quot; : &quot;webAddress&quot;
  }, {
    &quot;webAddressId&quot; : &quot;webAddressId&quot;,
    &quot;webAddress&quot; : &quot;webAddress&quot;
  } ],
  &quot;id&quot; : &quot;id&quot;,
  &quot;industryCode&quot; : &quot;industryCode&quot;
}

response = apiClient.business_lines_api.create_business_line(request)

```


