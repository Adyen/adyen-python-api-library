# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_payment_methods**](PaymentMethodsMerchantLevelApi.md#get_all_payment_methods) | **GET** /merchants/{merchantId}/paymentMethodSettings | Get all payment methods
[**get_payment_method_details**](PaymentMethodsMerchantLevelApi.md#get_payment_method_details) | **GET** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | Get payment method details
[**get_apple_pay_domains**](PaymentMethodsMerchantLevelApi.md#get_apple_pay_domains) | **GET** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/getApplePayDomains | Get Apple Pay domains
[**update_payment_method**](PaymentMethodsMerchantLevelApi.md#update_payment_method) | **PATCH** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | Update a payment method
[**request_payment_method**](PaymentMethodsMerchantLevelApi.md#request_payment_method) | **POST** /merchants/{merchantId}/paymentMethodSettings | Request a payment method
[**add_apple_pay_domain**](PaymentMethodsMerchantLevelApi.md#add_apple_pay_domain) | **POST** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/addApplePayDomains | Add an Apple Pay domain




# get_all_payment_methods
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payment_methods_merchant_level_api.get_all_payment_methods(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# get_payment_method_details
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payment_methods_merchant_level_api.get_payment_method_details(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# get_apple_pay_domains
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payment_methods_merchant_level_api.get_apple_pay_domains(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# update_payment_method
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payment_methods_merchant_level_api.update_payment_method(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# request_payment_method
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payment_methods_merchant_level_api.request_payment_method(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# add_apple_pay_domain
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payment_methods_merchant_level_api.add_apple_pay_domain(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params


