# checkout

All URIs are relative to *https://checkout-test.adyen.com/v70*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order**](OrdersApi.md#create_order) | **POST** /orders | Create an order
[**cancel_order**](OrdersApi.md#cancel_order) | **POST** /orders/cancel | Cancel an order
[**get_balance_of_gift_card**](OrdersApi.md#get_balance_of_gift_card) | **POST** /paymentMethods/balance | Get the balance of a gift card




# create_order
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.orders_api.create_order(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# cancel_order
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.orders_api.cancel_order(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params




# get_balance_of_gift_card
### Example

```python
from Adyen import checkout


apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.orders_api.get_balance_of_gift_card(request)

```

#for future work
### required params
### Request/Body Parameters
### Query params
### Path params


