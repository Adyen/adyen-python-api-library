# checkout

All URIs are relative to *https://checkout-test.adyen.com/v70*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_brands_on_card**](PaymentsApi.md#list_brands_on_card) | **POST** /cardDetails | Get the list of brands on the card
[**donations**](PaymentsApi.md#donations) | **POST** /donations | Start a transaction for donations
[**payment_methods**](PaymentsApi.md#payment_methods) | **POST** /paymentMethods | Get a list of available payment methods
[**payments**](PaymentsApi.md#payments) | **POST** /payments | Start a transaction
[**payments_details**](PaymentsApi.md#payments_details) | **POST** /payments/details | Submit details for a payment
[**sessions**](PaymentsApi.md#sessions) | **POST** /sessions | Create a payment session




# list_brands_on_card
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payments_api.list_brands_on_card(request)

```


# donations
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payments_api.donations(request)

```


# payment_methods
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payments_api.payment_methods(request)

```


# payments
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payments_api.payments(request)

```


# payments_details
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payments_api.payments_details(request)

```


# sessions
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payments_api.sessions(request)

```
