# checkout

All URIs are relative to *https://checkout-test.adyen.com/v70*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_link**](PaymentLinksApi.md#get_payment_link) | **GET** /paymentLinks/{linkId} | Get a payment link
[**update_payment_link**](PaymentLinksApi.md#update_payment_link) | **PATCH** /paymentLinks/{linkId} | Update the status of a payment link
[**create_payment_link**](PaymentLinksApi.md#create_payment_link) | **POST** /paymentLinks | Create a payment link




# get_payment_link
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.payment_links_api.get_payment_link()

```


# update_payment_link
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payment_links_api.update_payment_link(request)

```


# create_payment_link
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.payment_links_api.create_payment_link(request)

```
