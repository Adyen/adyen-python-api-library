# transfers

All URIs are relative to *https://balanceplatform-api-test.adyen.com/btl/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfer_funds**](TransfersApi.md#transfer_funds) | **POST** /transfers | Transfer funds




# transfer_funds
### Example

```python
from Adyen import transfers

apiClient = transfers
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;reason&quot; : &quot;amountLimitExceded&quot;,
  &quot;amount&quot; : {
    &quot;currency&quot; : &quot;currency&quot;,
    &quot;value&quot; : 0
  },
  &quot;description&quot; : &quot;description&quot;,
  &quot;paymentInstrumentId&quot; : &quot;paymentInstrumentId&quot;,
  &quot;priority&quot; : &quot;crossBorder&quot;,
  &quot;balanceAccountId&quot; : &quot;balanceAccountId&quot;,
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;referenceForBeneficiary&quot; : &quot;referenceForBeneficiary&quot;,
  &quot;counterparty&quot; : {
    &quot;balanceAccountId&quot; : &quot;balanceAccountId&quot;,
    &quot;bankAccount&quot; : {
      &quot;accountHolder&quot; : {
        &quot;firstName&quot; : &quot;firstName&quot;,
        &quot;lastName&quot; : &quot;lastName&quot;,
        &quot;address&quot; : {
          &quot;country&quot; : &quot;country&quot;,
          &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
          &quot;city&quot; : &quot;city&quot;,
          &quot;postalCode&quot; : &quot;postalCode&quot;,
          &quot;line2&quot; : &quot;line2&quot;,
          &quot;line1&quot; : &quot;line1&quot;
        },
        &quot;fullName&quot; : &quot;fullName&quot;,
        &quot;type&quot; : &quot;unknown&quot;
      }
    },
    &quot;merchant&quot; : {
      &quot;merchantId&quot; : &quot;merchantId&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;nameLocation&quot; : {
        &quot;country&quot; : &quot;country&quot;,
        &quot;city&quot; : &quot;city&quot;,
        &quot;name&quot; : &quot;name&quot;,
        &quot;countryOfOrigin&quot; : &quot;countryOfOrigin&quot;,
        &quot;rawData&quot; : &quot;rawData&quot;,
        &quot;state&quot; : &quot;state&quot;
      },
      &quot;mcc&quot; : &quot;mcc&quot;
    },
    &quot;transferInstrumentId&quot; : &quot;transferInstrumentId&quot;
  },
  &quot;id&quot; : &quot;id&quot;,
  &quot;category&quot; : &quot;bank&quot;,
  &quot;direction&quot; : &quot;incoming&quot;,
  &quot;status&quot; : &quot;atmWithdrawal&quot;
}

response = apiClient.transfers_api.transfer_funds(request)

```


