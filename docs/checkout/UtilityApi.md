# checkout

All URIs are relative to *https://checkout-test.adyen.com/v70*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_apple_pay_session**](UtilityApi.md#get_apple_pay_session) | **POST** /applePay/sessions | Get an Apple Pay session
[**create_originkey_values_for_domains**](UtilityApi.md#create_originkey_values_for_domains) | **POST** /originKeys | Create originKey values for domains




# get_apple_pay_session
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.utility_api.get_apple_pay_session(request)

```


# create_originkey_values_for_domains
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.utility_api.create_originkey_values_for_domains(request)

```
