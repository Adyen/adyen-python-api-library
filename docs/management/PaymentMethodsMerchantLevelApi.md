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
response = apiClient.payment_methods_merchant_level_api.get_all_payment_methods()

```




# get_payment_method_details
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.payment_methods_merchant_level_api.get_payment_method_details()

```




# get_apple_pay_domains
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.payment_methods_merchant_level_api.get_apple_pay_domains()

```




# update_payment_method
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;giroPay&quot; : {
    &quot;supportEmail&quot; : &quot;supportEmail&quot;
  },
  &quot;customRoutingFlags&quot; : [ &quot;customRoutingFlags&quot;, &quot;customRoutingFlags&quot; ],
  &quot;applePay&quot; : {
    &quot;domains&quot; : [ &quot;domains&quot;, &quot;domains&quot; ]
  },
  &quot;verificationStatus&quot; : &quot;valid&quot;,
  &quot;allowed&quot; : true,
  &quot;countries&quot; : [ &quot;countries&quot;, &quot;countries&quot; ],
  &quot;googlePay&quot; : {
    &quot;merchantId&quot; : &quot;merchantId&quot;
  },
  &quot;storeId&quot; : &quot;storeId&quot;,
  &quot;type&quot; : &quot;type&quot;,
  &quot;enabled&quot; : true,
  &quot;sofort&quot; : {
    &quot;logo&quot; : &quot;logo&quot;,
    &quot;currencyCode&quot; : &quot;currencyCode&quot;
  },
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;mealVoucher_FR&quot; : {
    &quot;conecsId&quot; : &quot;conecsId&quot;,
    &quot;subTypes&quot; : [ &quot;subTypes&quot;, &quot;subTypes&quot; ],
    &quot;siret&quot; : &quot;siret&quot;
  },
  &quot;klarna&quot; : {
    &quot;autoCapture&quot; : true,
    &quot;supportEmail&quot; : &quot;supportEmail&quot;,
    &quot;region&quot; : &quot;NA&quot;,
    &quot;disputeEmail&quot; : &quot;disputeEmail&quot;
  },
  &quot;swish&quot; : {
    &quot;swishNumber&quot; : &quot;swishNumber&quot;
  },
  &quot;bcmc&quot; : {
    &quot;enableBcmcMobile&quot; : true
  },
  &quot;cartesBancaires&quot; : {
    &quot;siret&quot; : &quot;siret&quot;
  },
  &quot;shopperInteraction&quot; : &quot;shopperInteraction&quot;,
  &quot;id&quot; : &quot;id&quot;,
  &quot;paypal&quot; : {
    &quot;subject&quot; : &quot;subject&quot;,
    &quot;payerId&quot; : &quot;payerId&quot;,
    &quot;directCapture&quot; : true
  },
  &quot;businessLineId&quot; : &quot;businessLineId&quot;,
  &quot;currencies&quot; : [ &quot;currencies&quot;, &quot;currencies&quot; ]
}

response = apiClient.payment_methods_merchant_level_api.update_payment_method(request)

```




# request_payment_method
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;giroPay&quot; : {
    &quot;supportEmail&quot; : &quot;supportEmail&quot;
  },
  &quot;customRoutingFlags&quot; : [ &quot;customRoutingFlags&quot;, &quot;customRoutingFlags&quot; ],
  &quot;applePay&quot; : {
    &quot;domains&quot; : [ &quot;domains&quot;, &quot;domains&quot; ]
  },
  &quot;verificationStatus&quot; : &quot;valid&quot;,
  &quot;allowed&quot; : true,
  &quot;countries&quot; : [ &quot;countries&quot;, &quot;countries&quot; ],
  &quot;googlePay&quot; : {
    &quot;merchantId&quot; : &quot;merchantId&quot;
  },
  &quot;storeId&quot; : &quot;storeId&quot;,
  &quot;type&quot; : &quot;type&quot;,
  &quot;enabled&quot; : true,
  &quot;sofort&quot; : {
    &quot;logo&quot; : &quot;logo&quot;,
    &quot;currencyCode&quot; : &quot;currencyCode&quot;
  },
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;mealVoucher_FR&quot; : {
    &quot;conecsId&quot; : &quot;conecsId&quot;,
    &quot;subTypes&quot; : [ &quot;subTypes&quot;, &quot;subTypes&quot; ],
    &quot;siret&quot; : &quot;siret&quot;
  },
  &quot;klarna&quot; : {
    &quot;autoCapture&quot; : true,
    &quot;supportEmail&quot; : &quot;supportEmail&quot;,
    &quot;region&quot; : &quot;NA&quot;,
    &quot;disputeEmail&quot; : &quot;disputeEmail&quot;
  },
  &quot;swish&quot; : {
    &quot;swishNumber&quot; : &quot;swishNumber&quot;
  },
  &quot;bcmc&quot; : {
    &quot;enableBcmcMobile&quot; : true
  },
  &quot;cartesBancaires&quot; : {
    &quot;siret&quot; : &quot;siret&quot;
  },
  &quot;shopperInteraction&quot; : &quot;shopperInteraction&quot;,
  &quot;id&quot; : &quot;id&quot;,
  &quot;paypal&quot; : {
    &quot;subject&quot; : &quot;subject&quot;,
    &quot;payerId&quot; : &quot;payerId&quot;,
    &quot;directCapture&quot; : true
  },
  &quot;businessLineId&quot; : &quot;businessLineId&quot;,
  &quot;currencies&quot; : [ &quot;currencies&quot;, &quot;currencies&quot; ]
}

response = apiClient.payment_methods_merchant_level_api.request_payment_method(request)

```




# add_apple_pay_domain
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

request = {} #your request
response = apiClient.payment_methods_merchant_level_api.add_apple_pay_domain(request)

```


