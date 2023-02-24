# payouts

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/Payout/v68*

Method | HTTP request | Description
------------- | ------------- | -------------
[**store_payout_details**](InitializationApi.md#store_payout_details) | **POST** /storeDetail | Store payout details
[**store_details_and_submit_payout**](InitializationApi.md#store_details_and_submit_payout) | **POST** /storeDetailAndSubmitThirdParty | Store details and submit a payout
[**submit_payout**](InitializationApi.md#submit_payout) | **POST** /submitThirdParty | Submit a payout




# store_payout_details
### Example

```python
from Adyen import payouts

apiClient = payouts
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;resultCode&quot; : &quot;resultCode&quot;,
  &quot;recurringDetailReference&quot; : &quot;recurringDetailReference&quot;,
  &quot;additionalData&quot; : {
    &quot;key&quot; : &quot;additionalData&quot;
  },
  &quot;pspReference&quot; : &quot;pspReference&quot;
}

response = apiClient.initialization_api.store_payout_details(request)

```




# store_details_and_submit_payout
### Example

```python
from Adyen import payouts

apiClient = payouts
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;resultCode&quot; : &quot;resultCode&quot;,
  &quot;refusalReason&quot; : &quot;refusalReason&quot;,
  &quot;additionalData&quot; : {
    &quot;key&quot; : &quot;additionalData&quot;
  },
  &quot;pspReference&quot; : &quot;pspReference&quot;
}

response = apiClient.initialization_api.store_details_and_submit_payout(request)

```




# submit_payout
### Example

```python
from Adyen import payouts

apiClient = payouts
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;resultCode&quot; : &quot;resultCode&quot;,
  &quot;refusalReason&quot; : &quot;refusalReason&quot;,
  &quot;additionalData&quot; : {
    &quot;key&quot; : &quot;additionalData&quot;
  },
  &quot;pspReference&quot; : &quot;pspReference&quot;
}

response = apiClient.initialization_api.submit_payout(request)

```


