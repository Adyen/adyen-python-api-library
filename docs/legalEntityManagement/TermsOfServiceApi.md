# legalEntityManagement

All URIs are relative to *https://kyc-test.adyen.com/lem/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_terms_of_service_information_for_legal_entity**](TermsOfServiceApi.md#get_terms_of_service_information_for_legal_entity) | **GET** /legalEntities/{id}/termsOfServiceAcceptanceInfos | Get Terms of Service information for a legal entity
[**get_terms_of_service_status**](TermsOfServiceApi.md#get_terms_of_service_status) | **GET** /legalEntities/{id}/termsOfServiceStatus | Get Terms of Service status
[**accept_terms_of_service**](TermsOfServiceApi.md#accept_terms_of_service) | **PATCH** /legalEntities/{id}/termsOfService/{termsofservicedocumentid} | Accept Terms of Service
[**get_terms_of_service_document**](TermsOfServiceApi.md#get_terms_of_service_document) | **POST** /legalEntities/{id}/termsOfService | Get Terms of Service document




# get_terms_of_service_information_for_legal_entity
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.terms_of_service_api.get_terms_of_service_information_for_legal_entity()

```




# get_terms_of_service_status
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.terms_of_service_api.get_terms_of_service_status()

```




# accept_terms_of_service
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;ipAddress&quot; : &quot;ipAddress&quot;,
  &quot;termsOfServiceDocumentId&quot; : &quot;termsOfServiceDocumentId&quot;,
  &quot;language&quot; : &quot;language&quot;,
  &quot;acceptedBy&quot; : &quot;acceptedBy&quot;,
  &quot;id&quot; : &quot;id&quot;,
  &quot;type&quot; : &quot;adyenAccount&quot;
}

response = apiClient.terms_of_service_api.accept_terms_of_service(request)

```




# get_terms_of_service_document
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;document&quot; : &quot;document&quot;,
  &quot;termsOfServiceDocumentId&quot; : &quot;termsOfServiceDocumentId&quot;,
  &quot;language&quot; : &quot;language&quot;,
  &quot;id&quot; : &quot;id&quot;,
  &quot;type&quot; : &quot;adyenAccount&quot;
}

response = apiClient.terms_of_service_api.get_terms_of_service_document(request)

```


