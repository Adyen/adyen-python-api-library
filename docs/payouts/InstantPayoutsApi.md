# payouts

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/Payout/v68*

Method | HTTP request | Description
------------- | ------------- | -------------
[**make_instant_card_payout**](InstantPayoutsApi.md#make_instant_card_payout) | **POST** /payout | Make an instant card payout




# make_instant_card_payout
### Example

```python
from Adyen import payouts

apiClient = payouts
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;authCode&quot; : &quot;authCode&quot;,
  &quot;paRequest&quot; : &quot;paRequest&quot;,
  &quot;issuerUrl&quot; : &quot;issuerUrl&quot;,
  &quot;md&quot; : &quot;md&quot;,
  &quot;dccSignature&quot; : &quot;dccSignature&quot;,
  &quot;resultCode&quot; : &quot;AuthenticationFinished&quot;,
  &quot;refusalReason&quot; : &quot;refusalReason&quot;,
  &quot;additionalData&quot; : {
    &quot;key&quot; : &quot;additionalData&quot;
  },
  &quot;dccAmount&quot; : {
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

response = apiClient.instant_payouts_api.make_instant_card_payout(request)

```


