# checkout

All URIs are relative to *https://checkout-test.adyen.com/v70*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_authorised_payment**](ModificationsApi.md#cancel_authorised_payment) | **POST** /cancels | Cancel an authorised payment
[**update_authorised_amount**](ModificationsApi.md#update_authorised_amount) | **POST** /payments/{paymentPspReference}/amountUpdates | Update an authorised amount
[**cancel_authorised_payment_by_psp_reference**](ModificationsApi.md#cancel_authorised_payment_by_psp_reference) | **POST** /payments/{paymentPspReference}/cancels | Cancel an authorised payment
[**capture_authorised_payment**](ModificationsApi.md#capture_authorised_payment) | **POST** /payments/{paymentPspReference}/captures | Capture an authorised payment
[**refund_captured_payment**](ModificationsApi.md#refund_captured_payment) | **POST** /payments/{paymentPspReference}/refunds | Refund a captured payment
[**refund_or_cancel_payment**](ModificationsApi.md#refund_or_cancel_payment) | **POST** /payments/{paymentPspReference}/reversals | Refund or cancel a payment




# cancel_authorised_payment
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.modifications_api.cancel_authorised_payment(request)

```


# update_authorised_amount
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.modifications_api.update_authorised_amount(request)

```


# cancel_authorised_payment_by_psp_reference
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.modifications_api.cancel_authorised_payment_by_psp_reference(request)

```


# capture_authorised_payment
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.modifications_api.capture_authorised_payment(request)

```


# refund_captured_payment
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.modifications_api.refund_captured_payment(request)

```


# refund_or_cancel_payment
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.modifications_api.refund_or_cancel_payment(request)

```
