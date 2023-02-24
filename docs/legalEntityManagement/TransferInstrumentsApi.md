# legalEntityManagement

All URIs are relative to *https://kyc-test.adyen.com/lem/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_transfer_instrument**](TransferInstrumentsApi.md#delete_transfer_instrument) | **DELETE** /transferInstruments/{id} | Delete a transfer instrument
[**get_transfer_instrument**](TransferInstrumentsApi.md#get_transfer_instrument) | **GET** /transferInstruments/{id} | Get a transfer instrument
[**update_transfer_instrument**](TransferInstrumentsApi.md#update_transfer_instrument) | **PATCH** /transferInstruments/{id} | Update a transfer instrument
[**create_transfer_instrument**](TransferInstrumentsApi.md#create_transfer_instrument) | **POST** /transferInstruments | Create a transfer instrument




# delete_transfer_instrument
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.transfer_instruments_api.delete_transfer_instrument()

```




# get_transfer_instrument
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.transfer_instruments_api.get_transfer_instrument()

```




# update_transfer_instrument
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;bankAccount&quot; : {
    &quot;branchCode&quot; : &quot;branchCode&quot;,
    &quot;bankCode&quot; : &quot;bankCode&quot;,
    &quot;bankBicSwift&quot; : &quot;bankBicSwift&quot;,
    &quot;countryCode&quot; : &quot;countryCode&quot;,
    &quot;accountType&quot; : &quot;accountType&quot;,
    &quot;iban&quot; : &quot;iban&quot;,
    &quot;bankName&quot; : &quot;bankName&quot;,
    &quot;accountNumber&quot; : &quot;accountNumber&quot;,
    &quot;currencyCode&quot; : &quot;currencyCode&quot;,
    &quot;bankCity&quot; : &quot;bankCity&quot;,
    &quot;checkCode&quot; : &quot;checkCode&quot;
  },
  &quot;documentDetails&quot; : [ {
    &quot;fileName&quot; : &quot;fileName&quot;,
    &quot;modificationDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
    &quot;active&quot; : true,
    &quot;description&quot; : &quot;description&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;type&quot; : &quot;type&quot;
  }, {
    &quot;fileName&quot; : &quot;fileName&quot;,
    &quot;modificationDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
    &quot;active&quot; : true,
    &quot;description&quot; : &quot;description&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;type&quot; : &quot;type&quot;
  } ],
  &quot;legalEntityId&quot; : &quot;legalEntityId&quot;,
  &quot;id&quot; : &quot;id&quot;,
  &quot;type&quot; : &quot;bankAccount&quot;
}

response = apiClient.transfer_instruments_api.update_transfer_instrument(request)

```




# create_transfer_instrument
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;bankAccount&quot; : {
    &quot;branchCode&quot; : &quot;branchCode&quot;,
    &quot;bankCode&quot; : &quot;bankCode&quot;,
    &quot;bankBicSwift&quot; : &quot;bankBicSwift&quot;,
    &quot;countryCode&quot; : &quot;countryCode&quot;,
    &quot;accountType&quot; : &quot;accountType&quot;,
    &quot;iban&quot; : &quot;iban&quot;,
    &quot;bankName&quot; : &quot;bankName&quot;,
    &quot;accountNumber&quot; : &quot;accountNumber&quot;,
    &quot;currencyCode&quot; : &quot;currencyCode&quot;,
    &quot;bankCity&quot; : &quot;bankCity&quot;,
    &quot;checkCode&quot; : &quot;checkCode&quot;
  },
  &quot;documentDetails&quot; : [ {
    &quot;fileName&quot; : &quot;fileName&quot;,
    &quot;modificationDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
    &quot;active&quot; : true,
    &quot;description&quot; : &quot;description&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;type&quot; : &quot;type&quot;
  }, {
    &quot;fileName&quot; : &quot;fileName&quot;,
    &quot;modificationDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
    &quot;active&quot; : true,
    &quot;description&quot; : &quot;description&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;type&quot; : &quot;type&quot;
  } ],
  &quot;legalEntityId&quot; : &quot;legalEntityId&quot;,
  &quot;id&quot; : &quot;id&quot;,
  &quot;type&quot; : &quot;bankAccount&quot;
}

response = apiClient.transfer_instruments_api.create_transfer_instrument(request)

```


