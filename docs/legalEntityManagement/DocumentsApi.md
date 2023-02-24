# legalEntityManagement

All URIs are relative to *https://kyc-test.adyen.com/lem/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /documents/{id} | Delete a document
[**get_document**](DocumentsApi.md#get_document) | **GET** /documents/{id} | Get a document
[**update_document**](DocumentsApi.md#update_document) | **PATCH** /documents/{id} | Update a document
[**upload_document_for_verification_checks**](DocumentsApi.md#upload_document_for_verification_checks) | **POST** /documents | Upload a document for verification checks




# delete_document
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.documents_api.delete_document()

```




# get_document
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.documents_api.get_document()

```




# update_document
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;issuerState&quot; : &quot;issuerState&quot;,
  &quot;owner&quot; : {
    &quot;id&quot; : &quot;id&quot;,
    &quot;type&quot; : &quot;type&quot;
  },
  &quot;fileName&quot; : &quot;fileName&quot;,
  &quot;attachments&quot; : [ {
    &quot;filename&quot; : &quot;filename&quot;,
    &quot;pageType&quot; : &quot;pageType&quot;,
    &quot;contentType&quot; : &quot;contentType&quot;,
    &quot;pageName&quot; : &quot;pageName&quot;,
    &quot;content&quot; : &quot;content&quot;
  }, {
    &quot;filename&quot; : &quot;filename&quot;,
    &quot;pageType&quot; : &quot;pageType&quot;,
    &quot;contentType&quot; : &quot;contentType&quot;,
    &quot;pageName&quot; : &quot;pageName&quot;,
    &quot;content&quot; : &quot;content&quot;
  } ],
  &quot;description&quot; : &quot;description&quot;,
  &quot;creationDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
  &quot;type&quot; : &quot;bankStatement&quot;,
  &quot;expiryDate&quot; : &quot;expiryDate&quot;,
  &quot;issuerCountry&quot; : &quot;issuerCountry&quot;,
  &quot;number&quot; : &quot;number&quot;,
  &quot;modificationDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
  &quot;attachment&quot; : {
    &quot;filename&quot; : &quot;filename&quot;,
    &quot;pageType&quot; : &quot;pageType&quot;,
    &quot;contentType&quot; : &quot;contentType&quot;,
    &quot;pageName&quot; : &quot;pageName&quot;,
    &quot;content&quot; : &quot;content&quot;
  },
  &quot;id&quot; : &quot;id&quot;
}

response = apiClient.documents_api.update_document(request)

```




# upload_document_for_verification_checks
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;issuerState&quot; : &quot;issuerState&quot;,
  &quot;owner&quot; : {
    &quot;id&quot; : &quot;id&quot;,
    &quot;type&quot; : &quot;type&quot;
  },
  &quot;fileName&quot; : &quot;fileName&quot;,
  &quot;attachments&quot; : [ {
    &quot;filename&quot; : &quot;filename&quot;,
    &quot;pageType&quot; : &quot;pageType&quot;,
    &quot;contentType&quot; : &quot;contentType&quot;,
    &quot;pageName&quot; : &quot;pageName&quot;,
    &quot;content&quot; : &quot;content&quot;
  }, {
    &quot;filename&quot; : &quot;filename&quot;,
    &quot;pageType&quot; : &quot;pageType&quot;,
    &quot;contentType&quot; : &quot;contentType&quot;,
    &quot;pageName&quot; : &quot;pageName&quot;,
    &quot;content&quot; : &quot;content&quot;
  } ],
  &quot;description&quot; : &quot;description&quot;,
  &quot;creationDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
  &quot;type&quot; : &quot;bankStatement&quot;,
  &quot;expiryDate&quot; : &quot;expiryDate&quot;,
  &quot;issuerCountry&quot; : &quot;issuerCountry&quot;,
  &quot;number&quot; : &quot;number&quot;,
  &quot;modificationDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
  &quot;attachment&quot; : {
    &quot;filename&quot; : &quot;filename&quot;,
    &quot;pageType&quot; : &quot;pageType&quot;,
    &quot;contentType&quot; : &quot;contentType&quot;,
    &quot;pageName&quot; : &quot;pageName&quot;,
    &quot;content&quot; : &quot;content&quot;
  },
  &quot;id&quot; : &quot;id&quot;
}

response = apiClient.documents_api.upload_document_for_verification_checks(request)

```


