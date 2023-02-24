# checkout

All URIs are relative to *https://checkout-test.adyen.com/v70*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_brands_on_card**](PaymentsApi.md#list_brands_on_card) | **POST** /cardDetails | Get the list of brands on the card
[**donations**](PaymentsApi.md#donations) | **POST** /donations | Start a transaction for donations
[**payment_methods**](PaymentsApi.md#payment_methods) | **POST** /paymentMethods | Get a list of available payment methods
[**payments**](PaymentsApi.md#payments) | **POST** /payments | Start a transaction
[**payments_details**](PaymentsApi.md#payments_details) | **POST** /payments/details | Submit details for a payment
[**sessions**](PaymentsApi.md#sessions) | **POST** /sessions | Create a payment session




# list_brands_on_card
### Example

```python
from Adyen import checkout

apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;brands&quot; : [ {
    &quot;type&quot; : &quot;type&quot;,
    &quot;supported&quot; : true
  }, {
    &quot;type&quot; : &quot;type&quot;,
    &quot;supported&quot; : true
  } ]
}

response = apiClient.payments_api.list_brands_on_card(request)

```




# donations
### Example

```python
from Adyen import checkout

apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;amount&quot; : {
    &quot;currency&quot; : &quot;currency&quot;,
    &quot;value&quot; : 0
  },
  &quot;merchantAccount&quot; : &quot;merchantAccount&quot;,
  &quot;payment&quot; : {
    &quot;threeDS2Result&quot; : {
      &quot;whiteListStatus&quot; : &quot;whiteListStatus&quot;,
      &quot;exemptionIndicator&quot; : &quot;lowValue&quot;,
      &quot;challengeCancel&quot; : &quot;01&quot;,
      &quot;eci&quot; : &quot;eci&quot;,
      &quot;cavvAlgorithm&quot; : &quot;cavvAlgorithm&quot;,
      &quot;challengeIndicator&quot; : &quot;noPreference&quot;,
      &quot;dsTransID&quot; : &quot;dsTransID&quot;,
      &quot;transStatusReason&quot; : &quot;transStatusReason&quot;,
      &quot;messageVersion&quot; : &quot;messageVersion&quot;,
      &quot;riskScore&quot; : &quot;riskScore&quot;,
      &quot;authenticationValue&quot; : &quot;authenticationValue&quot;,
      &quot;transStatus&quot; : &quot;transStatus&quot;,
      &quot;threeDSServerTransID&quot; : &quot;threeDSServerTransID&quot;,
      &quot;timestamp&quot; : &quot;timestamp&quot;
    },
    &quot;amount&quot; : {
      &quot;currency&quot; : &quot;currency&quot;,
      &quot;value&quot; : 0
    },
    &quot;resultCode&quot; : &quot;AuthenticationFinished&quot;,
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
    &quot;donationToken&quot; : &quot;donationToken&quot;,
    &quot;refusalReasonCode&quot; : &quot;refusalReasonCode&quot;,
    &quot;threeDSPaymentData&quot; : &quot;threeDSPaymentData&quot;,
    &quot;paymentMethod&quot; : {
      &quot;type&quot; : &quot;type&quot;,
      &quot;brand&quot; : &quot;brand&quot;
    },
    &quot;threeDS2ResponseData&quot; : {
      &quot;acsTransID&quot; : &quot;acsTransID&quot;,
      &quot;exemptionIndicator&quot; : &quot;exemptionIndicator&quot;,
      &quot;cardHolderInfo&quot; : &quot;cardHolderInfo&quot;,
      &quot;sdkEphemPubKey&quot; : &quot;sdkEphemPubKey&quot;,
      &quot;acsURL&quot; : &quot;acsURL&quot;,
      &quot;dsReferenceNumber&quot; : &quot;dsReferenceNumber&quot;,
      &quot;acsReferenceNumber&quot; : &quot;acsReferenceNumber&quot;,
      &quot;cavvAlgorithm&quot; : &quot;cavvAlgorithm&quot;,
      &quot;challengeIndicator&quot; : &quot;challengeIndicator&quot;,
      &quot;dsTransID&quot; : &quot;dsTransID&quot;,
      &quot;transStatusReason&quot; : &quot;transStatusReason&quot;,
      &quot;acsOperatorID&quot; : &quot;acsOperatorID&quot;,
      &quot;authenticationType&quot; : &quot;authenticationType&quot;,
      &quot;messageVersion&quot; : &quot;messageVersion&quot;,
      &quot;riskScore&quot; : &quot;riskScore&quot;,
      &quot;acsSignedContent&quot; : &quot;acsSignedContent&quot;,
      &quot;acsChallengeMandated&quot; : &quot;acsChallengeMandated&quot;,
      &quot;transStatus&quot; : &quot;transStatus&quot;,
      &quot;threeDSServerTransID&quot; : &quot;threeDSServerTransID&quot;
    },
    &quot;refusalReason&quot; : &quot;refusalReason&quot;,
    &quot;additionalData&quot; : {
      &quot;key&quot; : &quot;additionalData&quot;
    },
    &quot;merchantReference&quot; : &quot;merchantReference&quot;,
    &quot;pspReference&quot; : &quot;pspReference&quot;,
    &quot;order&quot; : {
      &quot;reference&quot; : &quot;reference&quot;,
      &quot;remainingAmount&quot; : {
        &quot;currency&quot; : &quot;currency&quot;,
        &quot;value&quot; : 0
      },
      &quot;amount&quot; : {
        &quot;currency&quot; : &quot;currency&quot;,
        &quot;value&quot; : 0
      },
      &quot;orderData&quot; : &quot;orderData&quot;,
      &quot;pspReference&quot; : &quot;pspReference&quot;,
      &quot;expiresAt&quot; : &quot;expiresAt&quot;
    }
  },
  &quot;id&quot; : &quot;id&quot;,
  &quot;donationAccount&quot; : &quot;donationAccount&quot;,
  &quot;status&quot; : &quot;completed&quot;
}

response = apiClient.payments_api.donations(request)

```




# payment_methods
### Example

```python
from Adyen import checkout

apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;paymentMethods&quot; : [ {
    &quot;brands&quot; : [ &quot;brands&quot;, &quot;brands&quot; ],
    &quot;configuration&quot; : {
      &quot;key&quot; : &quot;configuration&quot;
    },
    &quot;name&quot; : &quot;name&quot;,
    &quot;inputDetails&quot; : [ {
      &quot;configuration&quot; : {
        &quot;key&quot; : &quot;configuration&quot;
      },
      &quot;details&quot; : [ {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      }, {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      } ],
      &quot;optional&quot; : true,
      &quot;inputDetails&quot; : [ {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      }, {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      } ],
      &quot;type&quot; : &quot;type&quot;,
      &quot;items&quot; : [ {
        &quot;name&quot; : &quot;name&quot;,
        &quot;id&quot; : &quot;id&quot;
      }, {
        &quot;name&quot; : &quot;name&quot;,
        &quot;id&quot; : &quot;id&quot;
      } ],
      &quot;value&quot; : &quot;value&quot;,
      &quot;key&quot; : &quot;key&quot;,
      &quot;itemSearchUrl&quot; : &quot;itemSearchUrl&quot;
    }, {
      &quot;configuration&quot; : {
        &quot;key&quot; : &quot;configuration&quot;
      },
      &quot;details&quot; : [ {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      }, {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      } ],
      &quot;optional&quot; : true,
      &quot;inputDetails&quot; : [ {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      }, {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      } ],
      &quot;type&quot; : &quot;type&quot;,
      &quot;items&quot; : [ {
        &quot;name&quot; : &quot;name&quot;,
        &quot;id&quot; : &quot;id&quot;
      }, {
        &quot;name&quot; : &quot;name&quot;,
        &quot;id&quot; : &quot;id&quot;
      } ],
      &quot;value&quot; : &quot;value&quot;,
      &quot;key&quot; : &quot;key&quot;,
      &quot;itemSearchUrl&quot; : &quot;itemSearchUrl&quot;
    } ],
    &quot;fundingSource&quot; : &quot;debit&quot;,
    &quot;issuers&quot; : [ {
      &quot;name&quot; : &quot;name&quot;,
      &quot;disabled&quot; : false,
      &quot;id&quot; : &quot;id&quot;
    }, {
      &quot;name&quot; : &quot;name&quot;,
      &quot;disabled&quot; : false,
      &quot;id&quot; : &quot;id&quot;
    } ],
    &quot;type&quot; : &quot;type&quot;,
    &quot;brand&quot; : &quot;brand&quot;,
    &quot;group&quot; : {
      &quot;paymentMethodData&quot; : &quot;paymentMethodData&quot;,
      &quot;name&quot; : &quot;name&quot;,
      &quot;type&quot; : &quot;type&quot;
    }
  }, {
    &quot;brands&quot; : [ &quot;brands&quot;, &quot;brands&quot; ],
    &quot;configuration&quot; : {
      &quot;key&quot; : &quot;configuration&quot;
    },
    &quot;name&quot; : &quot;name&quot;,
    &quot;inputDetails&quot; : [ {
      &quot;configuration&quot; : {
        &quot;key&quot; : &quot;configuration&quot;
      },
      &quot;details&quot; : [ {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      }, {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      } ],
      &quot;optional&quot; : true,
      &quot;inputDetails&quot; : [ {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      }, {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      } ],
      &quot;type&quot; : &quot;type&quot;,
      &quot;items&quot; : [ {
        &quot;name&quot; : &quot;name&quot;,
        &quot;id&quot; : &quot;id&quot;
      }, {
        &quot;name&quot; : &quot;name&quot;,
        &quot;id&quot; : &quot;id&quot;
      } ],
      &quot;value&quot; : &quot;value&quot;,
      &quot;key&quot; : &quot;key&quot;,
      &quot;itemSearchUrl&quot; : &quot;itemSearchUrl&quot;
    }, {
      &quot;configuration&quot; : {
        &quot;key&quot; : &quot;configuration&quot;
      },
      &quot;details&quot; : [ {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      }, {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      } ],
      &quot;optional&quot; : true,
      &quot;inputDetails&quot; : [ {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      }, {
        &quot;configuration&quot; : {
          &quot;key&quot; : &quot;configuration&quot;
        },
        &quot;optional&quot; : true,
        &quot;type&quot; : &quot;type&quot;,
        &quot;items&quot; : [ {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        }, {
          &quot;name&quot; : &quot;name&quot;,
          &quot;id&quot; : &quot;id&quot;
        } ],
        &quot;value&quot; : &quot;value&quot;,
        &quot;key&quot; : &quot;key&quot;
      } ],
      &quot;type&quot; : &quot;type&quot;,
      &quot;items&quot; : [ {
        &quot;name&quot; : &quot;name&quot;,
        &quot;id&quot; : &quot;id&quot;
      }, {
        &quot;name&quot; : &quot;name&quot;,
        &quot;id&quot; : &quot;id&quot;
      } ],
      &quot;value&quot; : &quot;value&quot;,
      &quot;key&quot; : &quot;key&quot;,
      &quot;itemSearchUrl&quot; : &quot;itemSearchUrl&quot;
    } ],
    &quot;fundingSource&quot; : &quot;debit&quot;,
    &quot;issuers&quot; : [ {
      &quot;name&quot; : &quot;name&quot;,
      &quot;disabled&quot; : false,
      &quot;id&quot; : &quot;id&quot;
    }, {
      &quot;name&quot; : &quot;name&quot;,
      &quot;disabled&quot; : false,
      &quot;id&quot; : &quot;id&quot;
    } ],
    &quot;type&quot; : &quot;type&quot;,
    &quot;brand&quot; : &quot;brand&quot;,
    &quot;group&quot; : {
      &quot;paymentMethodData&quot; : &quot;paymentMethodData&quot;,
      &quot;name&quot; : &quot;name&quot;,
      &quot;type&quot; : &quot;type&quot;
    }
  } ],
  &quot;storedPaymentMethods&quot; : [ {
    &quot;lastFour&quot; : &quot;lastFour&quot;,
    &quot;supportedRecurringProcessingModels&quot; : [ &quot;supportedRecurringProcessingModels&quot;, &quot;supportedRecurringProcessingModels&quot; ],
    &quot;holderName&quot; : &quot;holderName&quot;,
    &quot;expiryMonth&quot; : &quot;expiryMonth&quot;,
    &quot;networkTxReference&quot; : &quot;networkTxReference&quot;,
    &quot;shopperEmail&quot; : &quot;shopperEmail&quot;,
    &quot;expiryYear&quot; : &quot;expiryYear&quot;,
    &quot;type&quot; : &quot;type&quot;,
    &quot;ownerName&quot; : &quot;ownerName&quot;,
    &quot;iban&quot; : &quot;iban&quot;,
    &quot;name&quot; : &quot;name&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;supportedShopperInteractions&quot; : [ &quot;supportedShopperInteractions&quot;, &quot;supportedShopperInteractions&quot; ],
    &quot;brand&quot; : &quot;brand&quot;
  }, {
    &quot;lastFour&quot; : &quot;lastFour&quot;,
    &quot;supportedRecurringProcessingModels&quot; : [ &quot;supportedRecurringProcessingModels&quot;, &quot;supportedRecurringProcessingModels&quot; ],
    &quot;holderName&quot; : &quot;holderName&quot;,
    &quot;expiryMonth&quot; : &quot;expiryMonth&quot;,
    &quot;networkTxReference&quot; : &quot;networkTxReference&quot;,
    &quot;shopperEmail&quot; : &quot;shopperEmail&quot;,
    &quot;expiryYear&quot; : &quot;expiryYear&quot;,
    &quot;type&quot; : &quot;type&quot;,
    &quot;ownerName&quot; : &quot;ownerName&quot;,
    &quot;iban&quot; : &quot;iban&quot;,
    &quot;name&quot; : &quot;name&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;supportedShopperInteractions&quot; : [ &quot;supportedShopperInteractions&quot;, &quot;supportedShopperInteractions&quot; ],
    &quot;brand&quot; : &quot;brand&quot;
  } ]
}

response = apiClient.payments_api.payment_methods(request)

```




# payments
### Example

```python
from Adyen import checkout

apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;threeDS2Result&quot; : {
    &quot;whiteListStatus&quot; : &quot;whiteListStatus&quot;,
    &quot;exemptionIndicator&quot; : &quot;lowValue&quot;,
    &quot;challengeCancel&quot; : &quot;01&quot;,
    &quot;eci&quot; : &quot;eci&quot;,
    &quot;cavvAlgorithm&quot; : &quot;cavvAlgorithm&quot;,
    &quot;challengeIndicator&quot; : &quot;noPreference&quot;,
    &quot;dsTransID&quot; : &quot;dsTransID&quot;,
    &quot;transStatusReason&quot; : &quot;transStatusReason&quot;,
    &quot;messageVersion&quot; : &quot;messageVersion&quot;,
    &quot;riskScore&quot; : &quot;riskScore&quot;,
    &quot;authenticationValue&quot; : &quot;authenticationValue&quot;,
    &quot;transStatus&quot; : &quot;transStatus&quot;,
    &quot;threeDSServerTransID&quot; : &quot;threeDSServerTransID&quot;,
    &quot;timestamp&quot; : &quot;timestamp&quot;
  },
  &quot;amount&quot; : {
    &quot;currency&quot; : &quot;currency&quot;,
    &quot;value&quot; : 0
  },
  &quot;resultCode&quot; : &quot;AuthenticationFinished&quot;,
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
  &quot;donationToken&quot; : &quot;donationToken&quot;,
  &quot;refusalReasonCode&quot; : &quot;refusalReasonCode&quot;,
  &quot;threeDSPaymentData&quot; : &quot;threeDSPaymentData&quot;,
  &quot;paymentMethod&quot; : {
    &quot;type&quot; : &quot;type&quot;,
    &quot;brand&quot; : &quot;brand&quot;
  },
  &quot;threeDS2ResponseData&quot; : {
    &quot;acsTransID&quot; : &quot;acsTransID&quot;,
    &quot;exemptionIndicator&quot; : &quot;exemptionIndicator&quot;,
    &quot;cardHolderInfo&quot; : &quot;cardHolderInfo&quot;,
    &quot;sdkEphemPubKey&quot; : &quot;sdkEphemPubKey&quot;,
    &quot;acsURL&quot; : &quot;acsURL&quot;,
    &quot;dsReferenceNumber&quot; : &quot;dsReferenceNumber&quot;,
    &quot;acsReferenceNumber&quot; : &quot;acsReferenceNumber&quot;,
    &quot;cavvAlgorithm&quot; : &quot;cavvAlgorithm&quot;,
    &quot;challengeIndicator&quot; : &quot;challengeIndicator&quot;,
    &quot;dsTransID&quot; : &quot;dsTransID&quot;,
    &quot;transStatusReason&quot; : &quot;transStatusReason&quot;,
    &quot;acsOperatorID&quot; : &quot;acsOperatorID&quot;,
    &quot;authenticationType&quot; : &quot;authenticationType&quot;,
    &quot;messageVersion&quot; : &quot;messageVersion&quot;,
    &quot;riskScore&quot; : &quot;riskScore&quot;,
    &quot;acsSignedContent&quot; : &quot;acsSignedContent&quot;,
    &quot;acsChallengeMandated&quot; : &quot;acsChallengeMandated&quot;,
    &quot;transStatus&quot; : &quot;transStatus&quot;,
    &quot;threeDSServerTransID&quot; : &quot;threeDSServerTransID&quot;
  },
  &quot;refusalReason&quot; : &quot;refusalReason&quot;,
  &quot;additionalData&quot; : {
    &quot;key&quot; : &quot;additionalData&quot;
  },
  &quot;merchantReference&quot; : &quot;merchantReference&quot;,
  &quot;pspReference&quot; : &quot;pspReference&quot;,
  &quot;order&quot; : {
    &quot;reference&quot; : &quot;reference&quot;,
    &quot;remainingAmount&quot; : {
      &quot;currency&quot; : &quot;currency&quot;,
      &quot;value&quot; : 0
    },
    &quot;amount&quot; : {
      &quot;currency&quot; : &quot;currency&quot;,
      &quot;value&quot; : 0
    },
    &quot;orderData&quot; : &quot;orderData&quot;,
    &quot;pspReference&quot; : &quot;pspReference&quot;,
    &quot;expiresAt&quot; : &quot;expiresAt&quot;
  }
}

response = apiClient.payments_api.payments(request)

```




# payments_details
### Example

```python
from Adyen import checkout

apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;threeDS2Result&quot; : {
    &quot;whiteListStatus&quot; : &quot;whiteListStatus&quot;,
    &quot;exemptionIndicator&quot; : &quot;lowValue&quot;,
    &quot;challengeCancel&quot; : &quot;01&quot;,
    &quot;eci&quot; : &quot;eci&quot;,
    &quot;cavvAlgorithm&quot; : &quot;cavvAlgorithm&quot;,
    &quot;challengeIndicator&quot; : &quot;noPreference&quot;,
    &quot;dsTransID&quot; : &quot;dsTransID&quot;,
    &quot;transStatusReason&quot; : &quot;transStatusReason&quot;,
    &quot;messageVersion&quot; : &quot;messageVersion&quot;,
    &quot;riskScore&quot; : &quot;riskScore&quot;,
    &quot;authenticationValue&quot; : &quot;authenticationValue&quot;,
    &quot;transStatus&quot; : &quot;transStatus&quot;,
    &quot;threeDSServerTransID&quot; : &quot;threeDSServerTransID&quot;,
    &quot;timestamp&quot; : &quot;timestamp&quot;
  },
  &quot;amount&quot; : {
    &quot;currency&quot; : &quot;currency&quot;,
    &quot;value&quot; : 0
  },
  &quot;resultCode&quot; : &quot;AuthenticationFinished&quot;,
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
  &quot;donationToken&quot; : &quot;donationToken&quot;,
  &quot;refusalReasonCode&quot; : &quot;refusalReasonCode&quot;,
  &quot;threeDSPaymentData&quot; : &quot;threeDSPaymentData&quot;,
  &quot;paymentMethod&quot; : {
    &quot;type&quot; : &quot;type&quot;,
    &quot;brand&quot; : &quot;brand&quot;
  },
  &quot;threeDS2ResponseData&quot; : {
    &quot;acsTransID&quot; : &quot;acsTransID&quot;,
    &quot;exemptionIndicator&quot; : &quot;exemptionIndicator&quot;,
    &quot;cardHolderInfo&quot; : &quot;cardHolderInfo&quot;,
    &quot;sdkEphemPubKey&quot; : &quot;sdkEphemPubKey&quot;,
    &quot;acsURL&quot; : &quot;acsURL&quot;,
    &quot;dsReferenceNumber&quot; : &quot;dsReferenceNumber&quot;,
    &quot;acsReferenceNumber&quot; : &quot;acsReferenceNumber&quot;,
    &quot;cavvAlgorithm&quot; : &quot;cavvAlgorithm&quot;,
    &quot;challengeIndicator&quot; : &quot;challengeIndicator&quot;,
    &quot;dsTransID&quot; : &quot;dsTransID&quot;,
    &quot;transStatusReason&quot; : &quot;transStatusReason&quot;,
    &quot;acsOperatorID&quot; : &quot;acsOperatorID&quot;,
    &quot;authenticationType&quot; : &quot;authenticationType&quot;,
    &quot;messageVersion&quot; : &quot;messageVersion&quot;,
    &quot;riskScore&quot; : &quot;riskScore&quot;,
    &quot;acsSignedContent&quot; : &quot;acsSignedContent&quot;,
    &quot;acsChallengeMandated&quot; : &quot;acsChallengeMandated&quot;,
    &quot;transStatus&quot; : &quot;transStatus&quot;,
    &quot;threeDSServerTransID&quot; : &quot;threeDSServerTransID&quot;
  },
  &quot;refusalReason&quot; : &quot;refusalReason&quot;,
  &quot;additionalData&quot; : {
    &quot;key&quot; : &quot;additionalData&quot;
  },
  &quot;shopperLocale&quot; : &quot;shopperLocale&quot;,
  &quot;merchantReference&quot; : &quot;merchantReference&quot;,
  &quot;pspReference&quot; : &quot;pspReference&quot;,
  &quot;order&quot; : {
    &quot;reference&quot; : &quot;reference&quot;,
    &quot;remainingAmount&quot; : {
      &quot;currency&quot; : &quot;currency&quot;,
      &quot;value&quot; : 0
    },
    &quot;amount&quot; : {
      &quot;currency&quot; : &quot;currency&quot;,
      &quot;value&quot; : 0
    },
    &quot;orderData&quot; : &quot;orderData&quot;,
    &quot;pspReference&quot; : &quot;pspReference&quot;,
    &quot;expiresAt&quot; : &quot;expiresAt&quot;
  }
}

response = apiClient.payments_api.payments_details(request)

```




# sessions
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
  &quot;redirectToIssuerMethod&quot; : &quot;redirectToIssuerMethod&quot;,
  &quot;channel&quot; : &quot;iOS&quot;,
  &quot;mcc&quot; : &quot;mcc&quot;,
  &quot;threeDSAuthenticationOnly&quot; : false,
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
  &quot;mode&quot; : &quot;embedded&quot;,
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;deliveryAddress&quot; : {
    &quot;country&quot; : &quot;country&quot;,
    &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
    &quot;city&quot; : &quot;city&quot;,
    &quot;houseNumberOrName&quot; : &quot;houseNumberOrName&quot;,
    &quot;street&quot; : &quot;street&quot;,
    &quot;postalCode&quot; : &quot;postalCode&quot;
  },
  &quot;recurringProcessingModel&quot; : &quot;CardOnFile&quot;,
  &quot;additionalData&quot; : {
    &quot;key&quot; : &quot;additionalData&quot;
  },
  &quot;blockedPaymentMethods&quot; : [ &quot;blockedPaymentMethods&quot;, &quot;blockedPaymentMethods&quot; ],
  &quot;id&quot; : &quot;id&quot;,
  &quot;trustedShopper&quot; : true,
  &quot;enablePayOut&quot; : true,
  &quot;additionalAmount&quot; : {
    &quot;currency&quot; : &quot;currency&quot;,
    &quot;value&quot; : 0
  },
  &quot;shopperEmail&quot; : &quot;shopperEmail&quot;,
  &quot;enableOneClick&quot; : true,
  &quot;storePaymentMethodMode&quot; : &quot;askForConsent&quot;,
  &quot;deliverAt&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
  &quot;shopperLocale&quot; : &quot;shopperLocale&quot;,
  &quot;captureDelayHours&quot; : 0,
  &quot;applicationInfo&quot; : {
    &quot;adyenLibrary&quot; : {
      &quot;name&quot; : &quot;name&quot;,
      &quot;version&quot; : &quot;version&quot;
    },
    &quot;merchantApplication&quot; : {
      &quot;name&quot; : &quot;name&quot;,
      &quot;version&quot; : &quot;version&quot;
    },
    &quot;adyenPaymentSource&quot; : {
      &quot;name&quot; : &quot;name&quot;,
      &quot;version&quot; : &quot;version&quot;
    },
    &quot;merchantDevice&quot; : {
      &quot;reference&quot; : &quot;reference&quot;,
      &quot;os&quot; : &quot;os&quot;,
      &quot;osVersion&quot; : &quot;osVersion&quot;
    },
    &quot;shopperInteractionDevice&quot; : {
      &quot;os&quot; : &quot;os&quot;,
      &quot;osVersion&quot; : &quot;osVersion&quot;,
      &quot;locale&quot; : &quot;locale&quot;
    },
    &quot;externalPlatform&quot; : {
      &quot;name&quot; : &quot;name&quot;,
      &quot;integrator&quot; : &quot;integrator&quot;,
      &quot;version&quot; : &quot;version&quot;
    }
  },
  &quot;shopperReference&quot; : &quot;shopperReference&quot;,
  &quot;shopperStatement&quot; : &quot;shopperStatement&quot;,
  &quot;sessionData&quot; : &quot;sessionData&quot;,
  &quot;mandate&quot; : {
    &quot;amount&quot; : &quot;amount&quot;,
    &quot;amountRule&quot; : &quot;max&quot;,
    &quot;billingDay&quot; : &quot;billingDay&quot;,
    &quot;startsAt&quot; : &quot;startsAt&quot;,
    &quot;billingAttemptsRule&quot; : &quot;on&quot;,
    &quot;endsAt&quot; : &quot;endsAt&quot;,
    &quot;remarks&quot; : &quot;remarks&quot;,
    &quot;frequency&quot; : &quot;adhoc&quot;
  },
  &quot;recurringFrequency&quot; : &quot;recurringFrequency&quot;,
  &quot;telephoneNumber&quot; : &quot;telephoneNumber&quot;,
  &quot;socialSecurityNumber&quot; : &quot;socialSecurityNumber&quot;,
  &quot;splitCardFundingSources&quot; : false,
  &quot;shopperIP&quot; : &quot;shopperIP&quot;,
  &quot;fundOrigin&quot; : {
    &quot;shopperName&quot; : {
      &quot;firstName&quot; : &quot;firstName&quot;,
      &quot;lastName&quot; : &quot;lastName&quot;
    },
    &quot;billingAddress&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;houseNumberOrName&quot; : &quot;houseNumberOrName&quot;,
      &quot;street&quot; : &quot;street&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;
    }
  },
  &quot;recurringExpiry&quot; : &quot;recurringExpiry&quot;,
  &quot;shopperName&quot; : {
    &quot;firstName&quot; : &quot;firstName&quot;,
    &quot;lastName&quot; : &quot;lastName&quot;
  },
  &quot;countryCode&quot; : &quot;countryCode&quot;,
  &quot;shopperInteraction&quot; : &quot;Ecommerce&quot;,
  &quot;company&quot; : {
    &quot;registrationNumber&quot; : &quot;registrationNumber&quot;,
    &quot;registryLocation&quot; : &quot;registryLocation&quot;,
    &quot;taxId&quot; : &quot;taxId&quot;,
    &quot;name&quot; : &quot;name&quot;,
    &quot;type&quot; : &quot;type&quot;,
    &quot;homepage&quot; : &quot;homepage&quot;
  },
  &quot;returnUrl&quot; : &quot;returnUrl&quot;,
  &quot;accountInfo&quot; : {
    &quot;passwordChangeDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
    &quot;paymentAccountIndicator&quot; : &quot;notApplicable&quot;,
    &quot;suspiciousActivity&quot; : true,
    &quot;deliveryAddressUsageIndicator&quot; : &quot;thisTransaction&quot;,
    &quot;pastTransactionsYear&quot; : 1,
    &quot;accountType&quot; : &quot;notApplicable&quot;,
    &quot;homePhone&quot; : &quot;homePhone&quot;,
    &quot;paymentAccountAge&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
    &quot;accountAgeIndicator&quot; : &quot;notApplicable&quot;,
    &quot;deliveryAddressUsageDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
    &quot;accountChangeDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
    &quot;accountCreationDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
    &quot;mobilePhone&quot; : &quot;mobilePhone&quot;,
    &quot;pastTransactionsDay&quot; : 6,
    &quot;accountChangeIndicator&quot; : &quot;thisTransaction&quot;,
    &quot;passwordChangeIndicator&quot; : &quot;notApplicable&quot;,
    &quot;addCardAttemptsDay&quot; : 0,
    &quot;workPhone&quot; : &quot;workPhone&quot;,
    &quot;purchasesLast6Months&quot; : 5
  },
  &quot;authenticationData&quot; : {
    &quot;authenticationOnly&quot; : false,
    &quot;threeDSRequestData&quot; : {
      &quot;challengeWindowSize&quot; : &quot;01&quot;,
      &quot;dataOnly&quot; : &quot;false&quot;,
      &quot;threeDSVersion&quot; : &quot;2.1.0&quot;,
      &quot;nativeThreeDS&quot; : &quot;preferred&quot;
    },
    &quot;attemptAuthentication&quot; : &quot;always&quot;
  },
  &quot;merchantOrderReference&quot; : &quot;merchantOrderReference&quot;,
  &quot;amount&quot; : {
    &quot;currency&quot; : &quot;currency&quot;,
    &quot;value&quot; : 0
  },
  &quot;redirectFromIssuerMethod&quot; : &quot;redirectFromIssuerMethod&quot;,
  &quot;dateOfBirth&quot; : &quot;2000-01-23&quot;,
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
  &quot;expiresAt&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
  &quot;storePaymentMethod&quot; : true,
  &quot;merchantAccount&quot; : &quot;merchantAccount&quot;,
  &quot;installmentOptions&quot; : {
    &quot;key&quot; : {
      &quot;preselectedValue&quot; : 6,
      &quot;plans&quot; : [ &quot;regular&quot;, &quot;regular&quot; ],
      &quot;values&quot; : [ 1, 1 ]
    }
  },
  &quot;fundRecipient&quot; : {
    &quot;shopperName&quot; : {
      &quot;firstName&quot; : &quot;firstName&quot;,
      &quot;lastName&quot; : &quot;lastName&quot;
    },
    &quot;subMerchant&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;taxId&quot; : &quot;taxId&quot;,
      &quot;name&quot; : &quot;name&quot;,
      &quot;mcc&quot; : &quot;mcc&quot;
    },
    &quot;telephoneNumber&quot; : &quot;telephoneNumber&quot;,
    &quot;storedPaymentMethodId&quot; : &quot;storedPaymentMethodId&quot;,
    &quot;walletIdentifier&quot; : &quot;walletIdentifier&quot;,
    &quot;paymentMethod&quot; : {
      &quot;holderName&quot; : &quot;holderName&quot;,
      &quot;cupsecureplus.smscode&quot; : &quot;cupsecureplus.smscode&quot;,
      &quot;expiryMonth&quot; : &quot;expiryMonth&quot;,
      &quot;threeDS2SdkVersion&quot; : &quot;threeDS2SdkVersion&quot;,
      &quot;networkPaymentReference&quot; : &quot;networkPaymentReference&quot;,
      &quot;checkoutAttemptId&quot; : &quot;checkoutAttemptId&quot;,
      &quot;expiryYear&quot; : &quot;expiryYear&quot;,
      &quot;type&quot; : &quot;scheme&quot;,
      &quot;shopperNotificationReference&quot; : &quot;shopperNotificationReference&quot;,
      &quot;cvc&quot; : &quot;cvc&quot;,
      &quot;number&quot; : &quot;number&quot;,
      &quot;encryptedCardNumber&quot; : &quot;encryptedCardNumber&quot;,
      &quot;encryptedSecurityCode&quot; : &quot;encryptedSecurityCode&quot;,
      &quot;encryptedExpiryYear&quot; : &quot;encryptedExpiryYear&quot;,
      &quot;storedPaymentMethodId&quot; : &quot;storedPaymentMethodId&quot;,
      &quot;recurringDetailReference&quot; : &quot;recurringDetailReference&quot;,
      &quot;encryptedExpiryMonth&quot; : &quot;encryptedExpiryMonth&quot;,
      &quot;fundingSource&quot; : &quot;debit&quot;,
      &quot;brand&quot; : &quot;brand&quot;
    },
    &quot;shopperEmail&quot; : &quot;shopperEmail&quot;,
    &quot;walletOwnerTaxId&quot; : &quot;walletOwnerTaxId&quot;,
    &quot;billingAddress&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;houseNumberOrName&quot; : &quot;houseNumberOrName&quot;,
      &quot;street&quot; : &quot;street&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;
    },
    &quot;shopperReference&quot; : &quot;shopperReference&quot;
  },
  &quot;billingAddress&quot; : {
    &quot;country&quot; : &quot;country&quot;,
    &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
    &quot;city&quot; : &quot;city&quot;,
    &quot;houseNumberOrName&quot; : &quot;houseNumberOrName&quot;,
    &quot;street&quot; : &quot;street&quot;,
    &quot;postalCode&quot; : &quot;postalCode&quot;
  },
  &quot;enableRecurring&quot; : true,
  &quot;mpiData&quot; : {
    &quot;cavv&quot; : &quot;cavv&quot;,
    &quot;authenticationResponse&quot; : &quot;Y&quot;,
    &quot;xid&quot; : &quot;xid&quot;,
    &quot;cavvAlgorithm&quot; : &quot;cavvAlgorithm&quot;,
    &quot;dsTransID&quot; : &quot;dsTransID&quot;,
    &quot;tokenAuthenticationVerificationValue&quot; : &quot;tokenAuthenticationVerificationValue&quot;,
    &quot;transStatusReason&quot; : &quot;transStatusReason&quot;,
    &quot;challengeCancel&quot; : &quot;01&quot;,
    &quot;directoryResponse&quot; : &quot;A&quot;,
    &quot;eci&quot; : &quot;eci&quot;,
    &quot;riskScore&quot; : &quot;riskScore&quot;,
    &quot;threeDSVersion&quot; : &quot;threeDSVersion&quot;
  }
}

response = apiClient.payments_api.sessions(request)

```


