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
request = {
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;remainingAmount&quot; : {
    &quot;currency&quot; : &quot;currency&quot;,
    &quot;value&quot; : 0
  },
  &quot;amount&quot; : {
    &quot;currency&quot; : &quot;currency&quot;,
    &quot;value&quot; : 0
  },
  &quot;resultCode&quot; : &quot;Success&quot;,
  &quot;orderData&quot; : &quot;orderData&quot;,
  &quot;refusalReason&quot; : &quot;refusalReason&quot;,
  &quot;additionalData&quot; : {
    &quot;key&quot; : &quot;additionalData&quot;
  },
  &quot;fraudResult&quot; : {
    &quot;accountScore&quot; : 6,
    &quot;results&quot; : [ {
      &quot;accountScore&quot; : 1,
      &quot;name&quot; : &quot;name&quot;,
      &quot;checkId&quot; : 5
    }, {
      &quot;accountScore&quot; : 1,
      &quot;name&quot; : &quot;name&quot;,
      &quot;checkId&quot; : 5
    } ]
  },
  &quot;pspReference&quot; : &quot;pspReference&quot;,
  &quot;expiresAt&quot; : &quot;expiresAt&quot;
}

response = apiClient.orders_api.create_order(request)

```




# cancel_order
### Example

```python
from Adyen import checkout

apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;resultCode&quot; : &quot;Received&quot;,
  &quot;pspReference&quot; : &quot;pspReference&quot;
}

response = apiClient.orders_api.cancel_order(request)

```




# get_balance_of_gift_card
### Example

```python
from Adyen import checkout

apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;balance&quot; : {
    &quot;currency&quot; : &quot;currency&quot;,
    &quot;value&quot; : 0
  },
  &quot;resultCode&quot; : &quot;Success&quot;,
  &quot;refusalReason&quot; : &quot;refusalReason&quot;,
  &quot;additionalData&quot; : {
    &quot;key&quot; : &quot;additionalData&quot;
  },
  &quot;transactionLimit&quot; : {
    &quot;currency&quot; : &quot;currency&quot;,
    &quot;value&quot; : 0
  },
  &quot;fraudResult&quot; : {
    &quot;accountScore&quot; : 6,
    &quot;results&quot; : [ {
      &quot;accountScore&quot; : 1,
      &quot;name&quot; : &quot;name&quot;,
      &quot;checkId&quot; : 5
    }, {
      &quot;accountScore&quot; : 1,
      &quot;name&quot; : &quot;name&quot;,
      &quot;checkId&quot; : 5
    } ]
  },
  &quot;pspReference&quot; : &quot;pspReference&quot;
}

response = apiClient.orders_api.get_balance_of_gift_card(request)

```


