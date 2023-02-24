# checkout

All URIs are relative to *https://checkout-test.adyen.com/v70*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_session**](ClassicCheckoutSDKApi.md#payment_session) | **POST** /paymentSession | Create a payment session
[**verify_payment_result**](ClassicCheckoutSDKApi.md#verify_payment_result) | **POST** /payments/result | Verify a payment result




# payment_session
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.classic_checkout_sdk_api.payment_session(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# verify_payment_result
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.classic_checkout_sdk_api.verify_payment_result(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params


