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
request = {
  &quot;metadata&quot; : {
    &quot;key&quot; : &quot;metadata&quot;
  },
  &quot;splits&quot; : [ {
    &quot;reference&quot; : &quot;reference&quot;,
    &quot;amount&quot; : {
      &quot;currency&quot; : &quot;currency&quot;,
      &quot;value&quot; : 5
    },
    &quot;description&quot; : &quot;description&quot;,
    &quot;type&quot; : &quot;BalanceAccount&quot;,
    &quot;account&quot; : &quot;account&quot;
  }, {
    &quot;reference&quot; : &quot;reference&quot;,
    &quot;amount&quot; : {
      &quot;currency&quot; : &quot;currency&quot;,
      &quot;value&quot; : 5
    },
    &quot;description&quot; : &quot;description&quot;,
    &quot;type&quot; : &quot;BalanceAccount&quot;,
    &quot;account&quot; : &quot;account&quot;
  } ],
  &quot;telephoneNumber&quot; : &quot;telephoneNumber&quot;,
  &quot;socialSecurityNumber&quot; : &quot;socialSecurityNumber&quot;,
  &quot;splitCardFundingSources&quot; : false,
  &quot;description&quot; : &quot;description&quot;,
  &quot;themeId&quot; : &quot;themeId&quot;,
  &quot;mcc&quot; : &quot;mcc&quot;,
  &quot;lineItems&quot; : [ {
    &quot;quantity&quot; : 1,
    &quot;color&quot; : &quot;color&quot;,
    &quot;itemCategory&quot; : &quot;itemCategory&quot;,
    &quot;amountExcludingTax&quot; : 1,
    &quot;taxPercentage&quot; : 7,
    &quot;description&quot; : &quot;description&quot;,
    &quot;upc&quot; : &quot;upc&quot;,
    &quot;manufacturer&quot; : &quot;manufacturer&quot;,
    &quot;size&quot; : &quot;size&quot;,
    &quot;imageUrl&quot; : &quot;imageUrl&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;amountIncludingTax&quot; : 1,
    &quot;productUrl&quot; : &quot;productUrl&quot;,
    &quot;sku&quot; : &quot;sku&quot;,
    &quot;taxAmount&quot; : 6,
    &quot;brand&quot; : &quot;brand&quot;,
    &quot;receiverEmail&quot; : &quot;receiverEmail&quot;
  }, {
    &quot;quantity&quot; : 1,
    &quot;color&quot; : &quot;color&quot;,
    &quot;itemCategory&quot; : &quot;itemCategory&quot;,
    &quot;amountExcludingTax&quot; : 1,
    &quot;taxPercentage&quot; : 7,
    &quot;description&quot; : &quot;description&quot;,
    &quot;upc&quot; : &quot;upc&quot;,
    &quot;manufacturer&quot; : &quot;manufacturer&quot;,
    &quot;size&quot; : &quot;size&quot;,
    &quot;imageUrl&quot; : &quot;imageUrl&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;amountIncludingTax&quot; : 1,
    &quot;productUrl&quot; : &quot;productUrl&quot;,
    &quot;sku&quot; : &quot;sku&quot;,
    &quot;taxAmount&quot; : 6,
    &quot;brand&quot; : &quot;brand&quot;,
    &quot;receiverEmail&quot; : &quot;receiverEmail&quot;
  } ],
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;shopperName&quot; : {
    &quot;firstName&quot; : &quot;firstName&quot;,
    &quot;lastName&quot; : &quot;lastName&quot;
  },
  &quot;deliveryAddress&quot; : {
    &quot;country&quot; : &quot;country&quot;,
    &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
    &quot;city&quot; : &quot;city&quot;,
    &quot;houseNumberOrName&quot; : &quot;houseNumberOrName&quot;,
    &quot;street&quot; : &quot;street&quot;,
    &quot;postalCode&quot; : &quot;postalCode&quot;
  },
  &quot;countryCode&quot; : &quot;countryCode&quot;,
  &quot;recurringProcessingModel&quot; : &quot;CardOnFile&quot;,
  &quot;blockedPaymentMethods&quot; : [ &quot;blockedPaymentMethods&quot;, &quot;blockedPaymentMethods&quot; ],
  &quot;id&quot; : &quot;id&quot;,
  &quot;returnUrl&quot; : &quot;returnUrl&quot;,
  &quot;updatedAt&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
  &quot;merchantOrderReference&quot; : &quot;merchantOrderReference&quot;,
  &quot;amount&quot; : {
    &quot;currency&quot; : &quot;currency&quot;,
    &quot;value&quot; : 0
  },
  &quot;manualCapture&quot; : true,
  &quot;dateOfBirth&quot; : &quot;2000-01-23&quot;,
  &quot;shopperEmail&quot; : &quot;shopperEmail&quot;,
  &quot;store&quot; : &quot;store&quot;,
  &quot;allowedPaymentMethods&quot; : [ &quot;allowedPaymentMethods&quot;, &quot;allowedPaymentMethods&quot; ],
  &quot;riskData&quot; : {
    &quot;fraudOffset&quot; : 4,
    &quot;customFields&quot; : {
      &quot;key&quot; : &quot;customFields&quot;
    },
    &quot;profileReference&quot; : &quot;profileReference&quot;,
    &quot;clientData&quot; : &quot;clientData&quot;
  },
  &quot;expiresAt&quot; : &quot;expiresAt&quot;,
  &quot;url&quot; : &quot;url&quot;,
  &quot;reusable&quot; : true,
  &quot;storePaymentMethodMode&quot; : &quot;askForConsent&quot;,
  &quot;merchantAccount&quot; : &quot;merchantAccount&quot;,
  &quot;installmentOptions&quot; : {
    &quot;key&quot; : {
      &quot;preselectedValue&quot; : 1,
      &quot;maxValue&quot; : 6,
      &quot;plans&quot; : [ &quot;regular&quot;, &quot;regular&quot; ],
      &quot;values&quot; : [ 5, 5 ]
    }
  },
  &quot;deliverAt&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
  &quot;requiredShopperFields&quot; : [ &quot;billingAddress&quot;, &quot;billingAddress&quot; ],
  &quot;showRemovePaymentMethodButton&quot; : true,
  &quot;billingAddress&quot; : {
    &quot;country&quot; : &quot;country&quot;,
    &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
    &quot;city&quot; : &quot;city&quot;,
    &quot;houseNumberOrName&quot; : &quot;houseNumberOrName&quot;,
    &quot;street&quot; : &quot;street&quot;,
    &quot;postalCode&quot; : &quot;postalCode&quot;
  },
  &quot;shopperLocale&quot; : &quot;shopperLocale&quot;,
  &quot;captureDelayHours&quot; : 0,
  &quot;shopperReference&quot; : &quot;shopperReference&quot;,
  &quot;shopperStatement&quot; : &quot;shopperStatement&quot;,
  &quot;status&quot; : &quot;active&quot;
}

apiClient.payment_links_api.update_payment_link(request)

```




# create_payment_link
### Example

```python
from Adyen import checkout

apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;metadata&quot; : {
    &quot;key&quot; : &quot;metadata&quot;
  },
  &quot;splits&quot; : [ {
    &quot;reference&quot; : &quot;reference&quot;,
    &quot;amount&quot; : {
      &quot;currency&quot; : &quot;currency&quot;,
      &quot;value&quot; : 5
    },
    &quot;description&quot; : &quot;description&quot;,
    &quot;type&quot; : &quot;BalanceAccount&quot;,
    &quot;account&quot; : &quot;account&quot;
  }, {
    &quot;reference&quot; : &quot;reference&quot;,
    &quot;amount&quot; : {
      &quot;currency&quot; : &quot;currency&quot;,
      &quot;value&quot; : 5
    },
    &quot;description&quot; : &quot;description&quot;,
    &quot;type&quot; : &quot;BalanceAccount&quot;,
    &quot;account&quot; : &quot;account&quot;
  } ],
  &quot;telephoneNumber&quot; : &quot;telephoneNumber&quot;,
  &quot;socialSecurityNumber&quot; : &quot;socialSecurityNumber&quot;,
  &quot;splitCardFundingSources&quot; : false,
  &quot;description&quot; : &quot;description&quot;,
  &quot;themeId&quot; : &quot;themeId&quot;,
  &quot;mcc&quot; : &quot;mcc&quot;,
  &quot;lineItems&quot; : [ {
    &quot;quantity&quot; : 1,
    &quot;color&quot; : &quot;color&quot;,
    &quot;itemCategory&quot; : &quot;itemCategory&quot;,
    &quot;amountExcludingTax&quot; : 1,
    &quot;taxPercentage&quot; : 7,
    &quot;description&quot; : &quot;description&quot;,
    &quot;upc&quot; : &quot;upc&quot;,
    &quot;manufacturer&quot; : &quot;manufacturer&quot;,
    &quot;size&quot; : &quot;size&quot;,
    &quot;imageUrl&quot; : &quot;imageUrl&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;amountIncludingTax&quot; : 1,
    &quot;productUrl&quot; : &quot;productUrl&quot;,
    &quot;sku&quot; : &quot;sku&quot;,
    &quot;taxAmount&quot; : 6,
    &quot;brand&quot; : &quot;brand&quot;,
    &quot;receiverEmail&quot; : &quot;receiverEmail&quot;
  }, {
    &quot;quantity&quot; : 1,
    &quot;color&quot; : &quot;color&quot;,
    &quot;itemCategory&quot; : &quot;itemCategory&quot;,
    &quot;amountExcludingTax&quot; : 1,
    &quot;taxPercentage&quot; : 7,
    &quot;description&quot; : &quot;description&quot;,
    &quot;upc&quot; : &quot;upc&quot;,
    &quot;manufacturer&quot; : &quot;manufacturer&quot;,
    &quot;size&quot; : &quot;size&quot;,
    &quot;imageUrl&quot; : &quot;imageUrl&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;amountIncludingTax&quot; : 1,
    &quot;productUrl&quot; : &quot;productUrl&quot;,
    &quot;sku&quot; : &quot;sku&quot;,
    &quot;taxAmount&quot; : 6,
    &quot;brand&quot; : &quot;brand&quot;,
    &quot;receiverEmail&quot; : &quot;receiverEmail&quot;
  } ],
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;shopperName&quot; : {
    &quot;firstName&quot; : &quot;firstName&quot;,
    &quot;lastName&quot; : &quot;lastName&quot;
  },
  &quot;deliveryAddress&quot; : {
    &quot;country&quot; : &quot;country&quot;,
    &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
    &quot;city&quot; : &quot;city&quot;,
    &quot;houseNumberOrName&quot; : &quot;houseNumberOrName&quot;,
    &quot;street&quot; : &quot;street&quot;,
    &quot;postalCode&quot; : &quot;postalCode&quot;
  },
  &quot;countryCode&quot; : &quot;countryCode&quot;,
  &quot;recurringProcessingModel&quot; : &quot;CardOnFile&quot;,
  &quot;blockedPaymentMethods&quot; : [ &quot;blockedPaymentMethods&quot;, &quot;blockedPaymentMethods&quot; ],
  &quot;id&quot; : &quot;id&quot;,
  &quot;returnUrl&quot; : &quot;returnUrl&quot;,
  &quot;updatedAt&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
  &quot;merchantOrderReference&quot; : &quot;merchantOrderReference&quot;,
  &quot;amount&quot; : {
    &quot;currency&quot; : &quot;currency&quot;,
    &quot;value&quot; : 0
  },
  &quot;manualCapture&quot; : true,
  &quot;dateOfBirth&quot; : &quot;2000-01-23&quot;,
  &quot;shopperEmail&quot; : &quot;shopperEmail&quot;,
  &quot;store&quot; : &quot;store&quot;,
  &quot;allowedPaymentMethods&quot; : [ &quot;allowedPaymentMethods&quot;, &quot;allowedPaymentMethods&quot; ],
  &quot;riskData&quot; : {
    &quot;fraudOffset&quot; : 4,
    &quot;customFields&quot; : {
      &quot;key&quot; : &quot;customFields&quot;
    },
    &quot;profileReference&quot; : &quot;profileReference&quot;,
    &quot;clientData&quot; : &quot;clientData&quot;
  },
  &quot;expiresAt&quot; : &quot;expiresAt&quot;,
  &quot;url&quot; : &quot;url&quot;,
  &quot;reusable&quot; : true,
  &quot;storePaymentMethodMode&quot; : &quot;askForConsent&quot;,
  &quot;merchantAccount&quot; : &quot;merchantAccount&quot;,
  &quot;installmentOptions&quot; : {
    &quot;key&quot; : {
      &quot;preselectedValue&quot; : 1,
      &quot;maxValue&quot; : 6,
      &quot;plans&quot; : [ &quot;regular&quot;, &quot;regular&quot; ],
      &quot;values&quot; : [ 5, 5 ]
    }
  },
  &quot;deliverAt&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
  &quot;requiredShopperFields&quot; : [ &quot;billingAddress&quot;, &quot;billingAddress&quot; ],
  &quot;showRemovePaymentMethodButton&quot; : true,
  &quot;billingAddress&quot; : {
    &quot;country&quot; : &quot;country&quot;,
    &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
    &quot;city&quot; : &quot;city&quot;,
    &quot;houseNumberOrName&quot; : &quot;houseNumberOrName&quot;,
    &quot;street&quot; : &quot;street&quot;,
    &quot;postalCode&quot; : &quot;postalCode&quot;
  },
  &quot;shopperLocale&quot; : &quot;shopperLocale&quot;,
  &quot;captureDelayHours&quot; : 0,
  &quot;shopperReference&quot; : &quot;shopperReference&quot;,
  &quot;shopperStatement&quot; : &quot;shopperStatement&quot;,
  &quot;status&quot; : &quot;active&quot;
}

apiClient.payment_links_api.create_payment_link(request)

```


