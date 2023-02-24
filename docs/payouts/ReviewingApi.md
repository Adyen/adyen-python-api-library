# payouts

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/Payout/v68*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_payout**](ReviewingApi.md#confirm_payout) | **POST** /confirmThirdParty | Confirm a payout
[**cancel_payout**](ReviewingApi.md#cancel_payout) | **POST** /declineThirdParty | Cancel a payout




# confirm_payout
### Example

```python
from Adyen import payouts

apiClient = payouts
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;response&quot; : &quot;response&quot;,
  &quot;additionalData&quot; : {
    &quot;key&quot; : &quot;additionalData&quot;
  },
  &quot;pspReference&quot; : &quot;pspReference&quot;
}

response = apiClient.reviewing_api.confirm_payout(request)

```




# cancel_payout
### Example

```python
from Adyen import payouts

apiClient = payouts
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;response&quot; : &quot;response&quot;,
  &quot;additionalData&quot; : {
    &quot;key&quot; : &quot;additionalData&quot;
  },
  &quot;pspReference&quot; : &quot;pspReference&quot;
}

response = apiClient.reviewing_api.cancel_payout(request)

```


