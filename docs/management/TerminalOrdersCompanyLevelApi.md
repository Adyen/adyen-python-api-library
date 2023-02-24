# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_billing_entities**](TerminalOrdersCompanyLevelApi.md#list_billing_entities) | **GET** /companies/{companyId}/billingEntities | Get a list of billing entities
[**list_shipping_locations**](TerminalOrdersCompanyLevelApi.md#list_shipping_locations) | **GET** /companies/{companyId}/shippingLocations | Get a list of shipping locations
[**list_terminal_models**](TerminalOrdersCompanyLevelApi.md#list_terminal_models) | **GET** /companies/{companyId}/terminalModels | Get a list of terminal models
[**list_orders**](TerminalOrdersCompanyLevelApi.md#list_orders) | **GET** /companies/{companyId}/terminalOrders | Get a list of orders
[**get_order**](TerminalOrdersCompanyLevelApi.md#get_order) | **GET** /companies/{companyId}/terminalOrders/{orderId} | Get an order
[**list_terminal_products**](TerminalOrdersCompanyLevelApi.md#list_terminal_products) | **GET** /companies/{companyId}/terminalProducts | Get a list of terminal products
[**update_order**](TerminalOrdersCompanyLevelApi.md#update_order) | **PATCH** /companies/{companyId}/terminalOrders/{orderId} | Update an order
[**create_shipping_location**](TerminalOrdersCompanyLevelApi.md#create_shipping_location) | **POST** /companies/{companyId}/shippingLocations | Create a shipping location
[**create_order**](TerminalOrdersCompanyLevelApi.md#create_order) | **POST** /companies/{companyId}/terminalOrders | Create an order
[**cancel_order**](TerminalOrdersCompanyLevelApi.md#cancel_order) | **POST** /companies/{companyId}/terminalOrders/{orderId}/cancel | Cancel an order




# list_billing_entities
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.terminal_orders_company_level_api.list_billing_entities()

```




# list_shipping_locations
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.terminal_orders_company_level_api.list_shipping_locations()

```




# list_terminal_models
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.terminal_orders_company_level_api.list_terminal_models()

```




# list_orders
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.terminal_orders_company_level_api.list_orders()

```




# get_order
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.terminal_orders_company_level_api.get_order()

```




# list_terminal_products
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.terminal_orders_company_level_api.list_terminal_products()

```




# update_order
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;customerOrderReference&quot; : &quot;customerOrderReference&quot;,
  &quot;trackingUrl&quot; : &quot;trackingUrl&quot;,
  &quot;shippingLocation&quot; : {
    &quot;address&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;streetAddress&quot; : &quot;streetAddress&quot;,
      &quot;companyName&quot; : &quot;companyName&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;streetAddress2&quot; : &quot;streetAddress2&quot;
    },
    &quot;contact&quot; : {
      &quot;firstName&quot; : &quot;firstName&quot;,
      &quot;lastName&quot; : &quot;lastName&quot;,
      &quot;phoneNumber&quot; : &quot;phoneNumber&quot;,
      &quot;infix&quot; : &quot;infix&quot;,
      &quot;email&quot; : &quot;email&quot;
    },
    &quot;name&quot; : &quot;name&quot;,
    &quot;id&quot; : &quot;id&quot;
  },
  &quot;id&quot; : &quot;id&quot;,
  &quot;billingEntity&quot; : {
    &quot;address&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;streetAddress&quot; : &quot;streetAddress&quot;,
      &quot;companyName&quot; : &quot;companyName&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;streetAddress2&quot; : &quot;streetAddress2&quot;
    },
    &quot;taxId&quot; : &quot;taxId&quot;,
    &quot;name&quot; : &quot;name&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;email&quot; : &quot;email&quot;
  },
  &quot;items&quot; : [ {
    &quot;quantity&quot; : 0,
    &quot;name&quot; : &quot;name&quot;,
    &quot;id&quot; : &quot;id&quot;
  }, {
    &quot;quantity&quot; : 0,
    &quot;name&quot; : &quot;name&quot;,
    &quot;id&quot; : &quot;id&quot;
  } ],
  &quot;orderDate&quot; : &quot;orderDate&quot;,
  &quot;status&quot; : &quot;status&quot;
}

response = apiClient.terminal_orders_company_level_api.update_order(request)

```




# create_shipping_location
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;address&quot; : {
    &quot;country&quot; : &quot;country&quot;,
    &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
    &quot;city&quot; : &quot;city&quot;,
    &quot;streetAddress&quot; : &quot;streetAddress&quot;,
    &quot;companyName&quot; : &quot;companyName&quot;,
    &quot;postalCode&quot; : &quot;postalCode&quot;,
    &quot;streetAddress2&quot; : &quot;streetAddress2&quot;
  },
  &quot;contact&quot; : {
    &quot;firstName&quot; : &quot;firstName&quot;,
    &quot;lastName&quot; : &quot;lastName&quot;,
    &quot;phoneNumber&quot; : &quot;phoneNumber&quot;,
    &quot;infix&quot; : &quot;infix&quot;,
    &quot;email&quot; : &quot;email&quot;
  },
  &quot;name&quot; : &quot;name&quot;,
  &quot;id&quot; : &quot;id&quot;
}

response = apiClient.terminal_orders_company_level_api.create_shipping_location(request)

```




# create_order
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;customerOrderReference&quot; : &quot;customerOrderReference&quot;,
  &quot;trackingUrl&quot; : &quot;trackingUrl&quot;,
  &quot;shippingLocation&quot; : {
    &quot;address&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;streetAddress&quot; : &quot;streetAddress&quot;,
      &quot;companyName&quot; : &quot;companyName&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;streetAddress2&quot; : &quot;streetAddress2&quot;
    },
    &quot;contact&quot; : {
      &quot;firstName&quot; : &quot;firstName&quot;,
      &quot;lastName&quot; : &quot;lastName&quot;,
      &quot;phoneNumber&quot; : &quot;phoneNumber&quot;,
      &quot;infix&quot; : &quot;infix&quot;,
      &quot;email&quot; : &quot;email&quot;
    },
    &quot;name&quot; : &quot;name&quot;,
    &quot;id&quot; : &quot;id&quot;
  },
  &quot;id&quot; : &quot;id&quot;,
  &quot;billingEntity&quot; : {
    &quot;address&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;streetAddress&quot; : &quot;streetAddress&quot;,
      &quot;companyName&quot; : &quot;companyName&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;streetAddress2&quot; : &quot;streetAddress2&quot;
    },
    &quot;taxId&quot; : &quot;taxId&quot;,
    &quot;name&quot; : &quot;name&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;email&quot; : &quot;email&quot;
  },
  &quot;items&quot; : [ {
    &quot;quantity&quot; : 0,
    &quot;name&quot; : &quot;name&quot;,
    &quot;id&quot; : &quot;id&quot;
  }, {
    &quot;quantity&quot; : 0,
    &quot;name&quot; : &quot;name&quot;,
    &quot;id&quot; : &quot;id&quot;
  } ],
  &quot;orderDate&quot; : &quot;orderDate&quot;,
  &quot;status&quot; : &quot;status&quot;
}

response = apiClient.terminal_orders_company_level_api.create_order(request)

```




# cancel_order
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.terminal_orders_company_level_api.cancel_order()

```


