# checkout

All URIs are relative to *https://checkout-test.adyen.com/v70*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_session**](ClassicCheckoutSDKApi.md#payment_session) | **POST** /paymentSession | Create a payment session
[**verify_payment_result**](ClassicCheckoutSDKApi.md#verify_payment_result) | **POST** /payments/result | Verify a payment result




# payment_session
### Example

```python
from Adyen import checkout

apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;recurringDetails&quot; : [ {
    &quot;storedDetails&quot; : {
      &quot;bank&quot; : {
        &quot;ownerName&quot; : &quot;ownerName&quot;,
        &quot;countryCode&quot; : &quot;countryCode&quot;,
        &quot;taxId&quot; : &quot;taxId&quot;,
        &quot;iban&quot; : &quot;iban&quot;,
        &quot;bankAccountNumber&quot; : &quot;bankAccountNumber&quot;,
        &quot;bankName&quot; : &quot;bankName&quot;,
        &quot;bankLocationId&quot; : &quot;bankLocationId&quot;,
        &quot;bic&quot; : &quot;bic&quot;,
        &quot;bankCity&quot; : &quot;bankCity&quot;
      },
      &quot;emailAddress&quot; : &quot;emailAddress&quot;,
      &quot;card&quot; : {
        &quot;cvc&quot; : &quot;cvc&quot;,
        &quot;number&quot; : &quot;number&quot;,
        &quot;holderName&quot; : &quot;holderName&quot;,
        &quot;startMonth&quot; : &quot;startMonth&quot;,
        &quot;issueNumber&quot; : &quot;issueNumber&quot;,
        &quot;expiryMonth&quot; : &quot;expiryMonth&quot;,
        &quot;startYear&quot; : &quot;startYear&quot;,
        &quot;expiryYear&quot; : &quot;expiryYear&quot;
      }
    },
    &quot;brands&quot; : [ &quot;brands&quot;, &quot;brands&quot; ],
    &quot;configuration&quot; : {
      &quot;key&quot; : &quot;configuration&quot;
    },
    &quot;name&quot; : &quot;name&quot;,
    &quot;recurringDetailReference&quot; : &quot;recurringDetailReference&quot;,
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
    &quot;storedDetails&quot; : {
      &quot;bank&quot; : {
        &quot;ownerName&quot; : &quot;ownerName&quot;,
        &quot;countryCode&quot; : &quot;countryCode&quot;,
        &quot;taxId&quot; : &quot;taxId&quot;,
        &quot;iban&quot; : &quot;iban&quot;,
        &quot;bankAccountNumber&quot; : &quot;bankAccountNumber&quot;,
        &quot;bankName&quot; : &quot;bankName&quot;,
        &quot;bankLocationId&quot; : &quot;bankLocationId&quot;,
        &quot;bic&quot; : &quot;bic&quot;,
        &quot;bankCity&quot; : &quot;bankCity&quot;
      },
      &quot;emailAddress&quot; : &quot;emailAddress&quot;,
      &quot;card&quot; : {
        &quot;cvc&quot; : &quot;cvc&quot;,
        &quot;number&quot; : &quot;number&quot;,
        &quot;holderName&quot; : &quot;holderName&quot;,
        &quot;startMonth&quot; : &quot;startMonth&quot;,
        &quot;issueNumber&quot; : &quot;issueNumber&quot;,
        &quot;expiryMonth&quot; : &quot;expiryMonth&quot;,
        &quot;startYear&quot; : &quot;startYear&quot;,
        &quot;expiryYear&quot; : &quot;expiryYear&quot;
      }
    },
    &quot;brands&quot; : [ &quot;brands&quot;, &quot;brands&quot; ],
    &quot;configuration&quot; : {
      &quot;key&quot; : &quot;configuration&quot;
    },
    &quot;name&quot; : &quot;name&quot;,
    &quot;recurringDetailReference&quot; : &quot;recurringDetailReference&quot;,
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
  &quot;paymentSession&quot; : &quot;paymentSession&quot;
}

apiClient.classic_checkout_sdk_api.payment_session(request)

```




# verify_payment_result
### Example

```python
from Adyen import checkout

apiClient = checkout
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;refusalReasonCode&quot; : &quot;refusalReasonCode&quot;,
  &quot;serviceError&quot; : {
    &quot;errorType&quot; : &quot;errorType&quot;,
    &quot;errorCode&quot; : &quot;errorCode&quot;,
    &quot;message&quot; : &quot;message&quot;,
    &quot;pspReference&quot; : &quot;pspReference&quot;
  },
  &quot;resultCode&quot; : &quot;AuthenticationFinished&quot;,
  &quot;refusalReason&quot; : &quot;refusalReason&quot;,
  &quot;additionalData&quot; : {
    &quot;key&quot; : &quot;additionalData&quot;
  },
  &quot;shopperLocale&quot; : &quot;shopperLocale&quot;,
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

apiClient.classic_checkout_sdk_api.verify_payment_result(request)

```


