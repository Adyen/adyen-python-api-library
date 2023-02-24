# legalEntityManagement

All URIs are relative to *https://kyc-test.adyen.com/lem/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_hosted_onboarding_page_themes**](HostedOnboardingApi.md#list_hosted_onboarding_page_themes) | **GET** /themes | Get a list of hosted onboarding page themes
[**get_onboarding_link_theme**](HostedOnboardingApi.md#get_onboarding_link_theme) | **GET** /themes/{id} | Get an onboarding link theme
[**get_link_to_adyenhosted_onboarding_page**](HostedOnboardingApi.md#get_link_to_adyenhosted_onboarding_page) | **POST** /legalEntities/{id}/onboardingLinks | Get a link to an Adyen-hosted onboarding page




# list_hosted_onboarding_page_themes
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.hosted_onboarding_api.list_hosted_onboarding_page_themes()

```




# get_onboarding_link_theme
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.hosted_onboarding_api.get_onboarding_link_theme()

```




# get_link_to_adyenhosted_onboarding_page
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;url&quot; : &quot;url&quot;
}

response = apiClient.hosted_onboarding_api.get_link_to_adyenhosted_onboarding_page(request)

```


