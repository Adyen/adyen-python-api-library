# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_billing_entities**](TerminalOrdersMerchantLevelApi.md#list_billing_entities) | **GET** /merchants/{merchantId}/billingEntities | Get a list of billing entities
[**list_shipping_locations**](TerminalOrdersMerchantLevelApi.md#list_shipping_locations) | **GET** /merchants/{merchantId}/shippingLocations | Get a list of shipping locations
[**list_terminal_models**](TerminalOrdersMerchantLevelApi.md#list_terminal_models) | **GET** /merchants/{merchantId}/terminalModels | Get a list of terminal models
[**list_orders**](TerminalOrdersMerchantLevelApi.md#list_orders) | **GET** /merchants/{merchantId}/terminalOrders | Get a list of orders
[**get_order**](TerminalOrdersMerchantLevelApi.md#get_order) | **GET** /merchants/{merchantId}/terminalOrders/{orderId} | Get an order
[**list_terminal_products**](TerminalOrdersMerchantLevelApi.md#list_terminal_products) | **GET** /merchants/{merchantId}/terminalProducts | Get a list of terminal products
[**update_order**](TerminalOrdersMerchantLevelApi.md#update_order) | **PATCH** /merchants/{merchantId}/terminalOrders/{orderId} | Update an order
[**create_shipping_location**](TerminalOrdersMerchantLevelApi.md#create_shipping_location) | **POST** /merchants/{merchantId}/shippingLocations | Create a shipping location
[**create_order**](TerminalOrdersMerchantLevelApi.md#create_order) | **POST** /merchants/{merchantId}/terminalOrders | Create an order
[**cancel_order**](TerminalOrdersMerchantLevelApi.md#cancel_order) | **POST** /merchants/{merchantId}/terminalOrders/{orderId}/cancel | Cancel an order




# list_billing_entities
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_orders_merchant_level_api.list_billing_entities()

```


# list_shipping_locations
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_orders_merchant_level_api.list_shipping_locations()

```


# list_terminal_models
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_orders_merchant_level_api.list_terminal_models()

```


# list_orders
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_orders_merchant_level_api.list_orders()

```


# get_order
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_orders_merchant_level_api.get_order()

```


# list_terminal_products
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_orders_merchant_level_api.list_terminal_products()

```


# update_order
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_orders_merchant_level_api.update_order(request)

```


# create_shipping_location
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_orders_merchant_level_api.create_shipping_location(request)

```


# create_order
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {} #your request

apiClient.terminal_orders_merchant_level_api.create_order(request)

```


# cancel_order
### Example

```python
from Adyen import management


apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"

apiClient.terminal_orders_merchant_level_api.cancel_order()

```
