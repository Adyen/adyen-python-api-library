# management

All URIs are relative to *https://management-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_terminal_logo**](TerminalSettingsStoreLevelApi.md#get_terminal_logo) | **GET** /merchants/{merchantId}/stores/{reference}/terminalLogos | Get the terminal logo
[**get_terminal_settings**](TerminalSettingsStoreLevelApi.md#get_terminal_settings) | **GET** /merchants/{merchantId}/stores/{reference}/terminalSettings | Get terminal settings
[**get_terminal_logo_by_store_id**](TerminalSettingsStoreLevelApi.md#get_terminal_logo_by_store_id) | **GET** /stores/{storeId}/terminalLogos | Get the terminal logo
[**get_terminal_settings_by_store_id**](TerminalSettingsStoreLevelApi.md#get_terminal_settings_by_store_id) | **GET** /stores/{storeId}/terminalSettings | Get terminal settings
[**update_terminal_logo**](TerminalSettingsStoreLevelApi.md#update_terminal_logo) | **PATCH** /merchants/{merchantId}/stores/{reference}/terminalLogos | Update the terminal logo
[**update_terminal_settings**](TerminalSettingsStoreLevelApi.md#update_terminal_settings) | **PATCH** /merchants/{merchantId}/stores/{reference}/terminalSettings | Update terminal settings
[**update_terminal_logo_by_store_id**](TerminalSettingsStoreLevelApi.md#update_terminal_logo_by_store_id) | **PATCH** /stores/{storeId}/terminalLogos | Update the terminal logo
[**update_terminal_settings_by_store_id**](TerminalSettingsStoreLevelApi.md#update_terminal_settings_by_store_id) | **PATCH** /stores/{storeId}/terminalSettings | Update terminal settings




# get_terminal_logo
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.terminal_settings_store_level_api.get_terminal_logo()

```




# get_terminal_settings
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.terminal_settings_store_level_api.get_terminal_settings()

```




# get_terminal_logo_by_store_id
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.terminal_settings_store_level_api.get_terminal_logo_by_store_id()

```




# get_terminal_settings_by_store_id
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.terminal_settings_store_level_api.get_terminal_settings_by_store_id()

```




# update_terminal_logo
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;data&quot; : &quot;data&quot;
}

response = apiClient.terminal_settings_store_level_api.update_terminal_logo(request)

```




# update_terminal_settings
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;surcharge&quot; : {
    &quot;configurations&quot; : [ {
      &quot;sources&quot; : [ &quot;sources&quot;, &quot;sources&quot; ],
      &quot;brand&quot; : &quot;brand&quot;,
      &quot;currencies&quot; : [ {
        &quot;amount&quot; : 5,
        &quot;currencyCode&quot; : &quot;currencyCode&quot;
      }, {
        &quot;amount&quot; : 5,
        &quot;currencyCode&quot; : &quot;currencyCode&quot;
      } ]
    }, {
      &quot;sources&quot; : [ &quot;sources&quot;, &quot;sources&quot; ],
      &quot;brand&quot; : &quot;brand&quot;,
      &quot;currencies&quot; : [ {
        &quot;amount&quot; : 5,
        &quot;currencyCode&quot; : &quot;currencyCode&quot;
      }, {
        &quot;amount&quot; : 5,
        &quot;currencyCode&quot; : &quot;currencyCode&quot;
      } ]
    } ],
    &quot;askConfirmation&quot; : true
  },
  &quot;signature&quot; : {
    &quot;skipSignature&quot; : true,
    &quot;deviceSlogan&quot; : &quot;deviceSlogan&quot;,
    &quot;deviceName&quot; : &quot;deviceName&quot;,
    &quot;askSignatureOnScreen&quot; : true
  },
  &quot;passcodes&quot; : {
    &quot;refundPin&quot; : &quot;refundPin&quot;,
    &quot;screenLockPin&quot; : &quot;screenLockPin&quot;,
    &quot;adminMenuPin&quot; : &quot;adminMenuPin&quot;,
    &quot;txMenuPin&quot; : &quot;txMenuPin&quot;
  },
  &quot;cardholderReceipt&quot; : {
    &quot;headerForAuthorizedReceipt&quot; : &quot;headerForAuthorizedReceipt&quot;
  },
  &quot;standalone&quot; : {
    &quot;enableStandalone&quot; : true,
    &quot;currencyCode&quot; : &quot;currencyCode&quot;
  },
  &quot;timeouts&quot; : {
    &quot;fromActiveToSleep&quot; : 2
  },
  &quot;opi&quot; : {
    &quot;enablePayAtTable&quot; : true,
    &quot;payAtTableURL&quot; : &quot;payAtTableURL&quot;,
    &quot;payAtTableStoreNumber&quot; : &quot;payAtTableStoreNumber&quot;
  },
  &quot;wifiProfiles&quot; : {
    &quot;settings&quot; : {
      &quot;roaming&quot; : true,
      &quot;band&quot; : &quot;band&quot;,
      &quot;timeout&quot; : 9
    },
    &quot;profiles&quot; : [ {
      &quot;bssType&quot; : &quot;bssType&quot;,
      &quot;eapCaCert&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;autoWifi&quot; : true,
      &quot;channel&quot; : 7,
      &quot;psk&quot; : &quot;psk&quot;,
      &quot;defaultProfile&quot; : true,
      &quot;eapClientCert&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;eapClientPwd&quot; : &quot;eapClientPwd&quot;,
      &quot;eapPwd&quot; : &quot;eapPwd&quot;,
      &quot;ssid&quot; : &quot;ssid&quot;,
      &quot;wsec&quot; : &quot;wsec&quot;,
      &quot;eapClientKey&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;eapIdentity&quot; : &quot;eapIdentity&quot;,
      &quot;eap&quot; : &quot;eap&quot;,
      &quot;name&quot; : &quot;name&quot;,
      &quot;eapIntermediateCert&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;authType&quot; : &quot;authType&quot;,
      &quot;hiddenSsid&quot; : true
    }, {
      &quot;bssType&quot; : &quot;bssType&quot;,
      &quot;eapCaCert&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;autoWifi&quot; : true,
      &quot;channel&quot; : 7,
      &quot;psk&quot; : &quot;psk&quot;,
      &quot;defaultProfile&quot; : true,
      &quot;eapClientCert&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;eapClientPwd&quot; : &quot;eapClientPwd&quot;,
      &quot;eapPwd&quot; : &quot;eapPwd&quot;,
      &quot;ssid&quot; : &quot;ssid&quot;,
      &quot;wsec&quot; : &quot;wsec&quot;,
      &quot;eapClientKey&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;eapIdentity&quot; : &quot;eapIdentity&quot;,
      &quot;eap&quot; : &quot;eap&quot;,
      &quot;name&quot; : &quot;name&quot;,
      &quot;eapIntermediateCert&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;authType&quot; : &quot;authType&quot;,
      &quot;hiddenSsid&quot; : true
    } ]
  },
  &quot;receiptPrinting&quot; : {
    &quot;merchantApproved&quot; : true,
    &quot;merchantCancelled&quot; : true,
    &quot;shopperCancelled&quot; : true,
    &quot;shopperCaptureRefused&quot; : true,
    &quot;merchantCaptureRefused&quot; : true,
    &quot;merchantRefundRefused&quot; : true,
    &quot;shopperRefused&quot; : true,
    &quot;shopperApproved&quot; : true,
    &quot;shopperCaptureApproved&quot; : true,
    &quot;merchantRefused&quot; : true,
    &quot;shopperRefundApproved&quot; : true,
    &quot;shopperRefundRefused&quot; : true,
    &quot;merchantRefundApproved&quot; : true,
    &quot;merchantVoid&quot; : true,
    &quot;merchantCaptureApproved&quot; : true,
    &quot;shopperVoid&quot; : true
  },
  &quot;connectivity&quot; : {
    &quot;simcardStatus&quot; : &quot;ACTIVATED&quot;
  },
  &quot;gratuities&quot; : [ {
    &quot;predefinedTipEntries&quot; : [ &quot;predefinedTipEntries&quot;, &quot;predefinedTipEntries&quot; ],
    &quot;allowCustomAmount&quot; : true,
    &quot;usePredefinedTipEntries&quot; : true,
    &quot;currency&quot; : &quot;currency&quot;
  }, {
    &quot;predefinedTipEntries&quot; : [ &quot;predefinedTipEntries&quot;, &quot;predefinedTipEntries&quot; ],
    &quot;allowCustomAmount&quot; : true,
    &quot;usePredefinedTipEntries&quot; : true,
    &quot;currency&quot; : &quot;currency&quot;
  } ],
  &quot;offlineProcessing&quot; : {
    &quot;chipFloorLimit&quot; : 1,
    &quot;offlineSwipeLimits&quot; : [ {
      &quot;amount&quot; : 5,
      &quot;currencyCode&quot; : &quot;currencyCode&quot;
    }, {
      &quot;amount&quot; : 5,
      &quot;currencyCode&quot; : &quot;currencyCode&quot;
    } ]
  },
  &quot;receiptOptions&quot; : {
    &quot;qrCodeData&quot; : &quot;qrCodeData&quot;,
    &quot;logo&quot; : &quot;logo&quot;
  },
  &quot;nexo&quot; : {
    &quot;nexoEventUrls&quot; : [ &quot;nexoEventUrls&quot;, &quot;nexoEventUrls&quot; ],
    &quot;eventUrls&quot; : {
      &quot;eventLocalUrls&quot; : [ {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      }, {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      } ],
      &quot;eventPublicUrls&quot; : [ {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      }, {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      } ]
    },
    &quot;displayUrls&quot; : {
      &quot;localUrls&quot; : [ {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      }, {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      } ],
      &quot;publicUrls&quot; : [ {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      }, {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      } ]
    },
    &quot;encryptionKey&quot; : {
      &quot;identifier&quot; : &quot;identifier&quot;,
      &quot;passphrase&quot; : &quot;passphrase&quot;,
      &quot;version&quot; : 6
    }
  },
  &quot;hardware&quot; : {
    &quot;displayMaximumBackLight&quot; : 0
  }
}

response = apiClient.terminal_settings_store_level_api.update_terminal_settings(request)

```




# update_terminal_logo_by_store_id
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;data&quot; : &quot;data&quot;
}

response = apiClient.terminal_settings_store_level_api.update_terminal_logo_by_store_id(request)

```




# update_terminal_settings_by_store_id
### Example

```python
from Adyen import management

apiClient = management
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;surcharge&quot; : {
    &quot;configurations&quot; : [ {
      &quot;sources&quot; : [ &quot;sources&quot;, &quot;sources&quot; ],
      &quot;brand&quot; : &quot;brand&quot;,
      &quot;currencies&quot; : [ {
        &quot;amount&quot; : 5,
        &quot;currencyCode&quot; : &quot;currencyCode&quot;
      }, {
        &quot;amount&quot; : 5,
        &quot;currencyCode&quot; : &quot;currencyCode&quot;
      } ]
    }, {
      &quot;sources&quot; : [ &quot;sources&quot;, &quot;sources&quot; ],
      &quot;brand&quot; : &quot;brand&quot;,
      &quot;currencies&quot; : [ {
        &quot;amount&quot; : 5,
        &quot;currencyCode&quot; : &quot;currencyCode&quot;
      }, {
        &quot;amount&quot; : 5,
        &quot;currencyCode&quot; : &quot;currencyCode&quot;
      } ]
    } ],
    &quot;askConfirmation&quot; : true
  },
  &quot;signature&quot; : {
    &quot;skipSignature&quot; : true,
    &quot;deviceSlogan&quot; : &quot;deviceSlogan&quot;,
    &quot;deviceName&quot; : &quot;deviceName&quot;,
    &quot;askSignatureOnScreen&quot; : true
  },
  &quot;passcodes&quot; : {
    &quot;refundPin&quot; : &quot;refundPin&quot;,
    &quot;screenLockPin&quot; : &quot;screenLockPin&quot;,
    &quot;adminMenuPin&quot; : &quot;adminMenuPin&quot;,
    &quot;txMenuPin&quot; : &quot;txMenuPin&quot;
  },
  &quot;cardholderReceipt&quot; : {
    &quot;headerForAuthorizedReceipt&quot; : &quot;headerForAuthorizedReceipt&quot;
  },
  &quot;standalone&quot; : {
    &quot;enableStandalone&quot; : true,
    &quot;currencyCode&quot; : &quot;currencyCode&quot;
  },
  &quot;timeouts&quot; : {
    &quot;fromActiveToSleep&quot; : 2
  },
  &quot;opi&quot; : {
    &quot;enablePayAtTable&quot; : true,
    &quot;payAtTableURL&quot; : &quot;payAtTableURL&quot;,
    &quot;payAtTableStoreNumber&quot; : &quot;payAtTableStoreNumber&quot;
  },
  &quot;wifiProfiles&quot; : {
    &quot;settings&quot; : {
      &quot;roaming&quot; : true,
      &quot;band&quot; : &quot;band&quot;,
      &quot;timeout&quot; : 9
    },
    &quot;profiles&quot; : [ {
      &quot;bssType&quot; : &quot;bssType&quot;,
      &quot;eapCaCert&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;autoWifi&quot; : true,
      &quot;channel&quot; : 7,
      &quot;psk&quot; : &quot;psk&quot;,
      &quot;defaultProfile&quot; : true,
      &quot;eapClientCert&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;eapClientPwd&quot; : &quot;eapClientPwd&quot;,
      &quot;eapPwd&quot; : &quot;eapPwd&quot;,
      &quot;ssid&quot; : &quot;ssid&quot;,
      &quot;wsec&quot; : &quot;wsec&quot;,
      &quot;eapClientKey&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;eapIdentity&quot; : &quot;eapIdentity&quot;,
      &quot;eap&quot; : &quot;eap&quot;,
      &quot;name&quot; : &quot;name&quot;,
      &quot;eapIntermediateCert&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;authType&quot; : &quot;authType&quot;,
      &quot;hiddenSsid&quot; : true
    }, {
      &quot;bssType&quot; : &quot;bssType&quot;,
      &quot;eapCaCert&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;autoWifi&quot; : true,
      &quot;channel&quot; : 7,
      &quot;psk&quot; : &quot;psk&quot;,
      &quot;defaultProfile&quot; : true,
      &quot;eapClientCert&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;eapClientPwd&quot; : &quot;eapClientPwd&quot;,
      &quot;eapPwd&quot; : &quot;eapPwd&quot;,
      &quot;ssid&quot; : &quot;ssid&quot;,
      &quot;wsec&quot; : &quot;wsec&quot;,
      &quot;eapClientKey&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;eapIdentity&quot; : &quot;eapIdentity&quot;,
      &quot;eap&quot; : &quot;eap&quot;,
      &quot;name&quot; : &quot;name&quot;,
      &quot;eapIntermediateCert&quot; : {
        &quot;data&quot; : &quot;data&quot;,
        &quot;name&quot; : &quot;name&quot;
      },
      &quot;authType&quot; : &quot;authType&quot;,
      &quot;hiddenSsid&quot; : true
    } ]
  },
  &quot;receiptPrinting&quot; : {
    &quot;merchantApproved&quot; : true,
    &quot;merchantCancelled&quot; : true,
    &quot;shopperCancelled&quot; : true,
    &quot;shopperCaptureRefused&quot; : true,
    &quot;merchantCaptureRefused&quot; : true,
    &quot;merchantRefundRefused&quot; : true,
    &quot;shopperRefused&quot; : true,
    &quot;shopperApproved&quot; : true,
    &quot;shopperCaptureApproved&quot; : true,
    &quot;merchantRefused&quot; : true,
    &quot;shopperRefundApproved&quot; : true,
    &quot;shopperRefundRefused&quot; : true,
    &quot;merchantRefundApproved&quot; : true,
    &quot;merchantVoid&quot; : true,
    &quot;merchantCaptureApproved&quot; : true,
    &quot;shopperVoid&quot; : true
  },
  &quot;connectivity&quot; : {
    &quot;simcardStatus&quot; : &quot;ACTIVATED&quot;
  },
  &quot;gratuities&quot; : [ {
    &quot;predefinedTipEntries&quot; : [ &quot;predefinedTipEntries&quot;, &quot;predefinedTipEntries&quot; ],
    &quot;allowCustomAmount&quot; : true,
    &quot;usePredefinedTipEntries&quot; : true,
    &quot;currency&quot; : &quot;currency&quot;
  }, {
    &quot;predefinedTipEntries&quot; : [ &quot;predefinedTipEntries&quot;, &quot;predefinedTipEntries&quot; ],
    &quot;allowCustomAmount&quot; : true,
    &quot;usePredefinedTipEntries&quot; : true,
    &quot;currency&quot; : &quot;currency&quot;
  } ],
  &quot;offlineProcessing&quot; : {
    &quot;chipFloorLimit&quot; : 1,
    &quot;offlineSwipeLimits&quot; : [ {
      &quot;amount&quot; : 5,
      &quot;currencyCode&quot; : &quot;currencyCode&quot;
    }, {
      &quot;amount&quot; : 5,
      &quot;currencyCode&quot; : &quot;currencyCode&quot;
    } ]
  },
  &quot;receiptOptions&quot; : {
    &quot;qrCodeData&quot; : &quot;qrCodeData&quot;,
    &quot;logo&quot; : &quot;logo&quot;
  },
  &quot;nexo&quot; : {
    &quot;nexoEventUrls&quot; : [ &quot;nexoEventUrls&quot;, &quot;nexoEventUrls&quot; ],
    &quot;eventUrls&quot; : {
      &quot;eventLocalUrls&quot; : [ {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      }, {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      } ],
      &quot;eventPublicUrls&quot; : [ {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      }, {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      } ]
    },
    &quot;displayUrls&quot; : {
      &quot;localUrls&quot; : [ {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      }, {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      } ],
      &quot;publicUrls&quot; : [ {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      }, {
        &quot;password&quot; : &quot;password&quot;,
        &quot;url&quot; : &quot;url&quot;,
        &quot;username&quot; : &quot;username&quot;
      } ]
    },
    &quot;encryptionKey&quot; : {
      &quot;identifier&quot; : &quot;identifier&quot;,
      &quot;passphrase&quot; : &quot;passphrase&quot;,
      &quot;version&quot; : 6
    }
  },
  &quot;hardware&quot; : {
    &quot;displayMaximumBackLight&quot; : 0
  }
}

response = apiClient.terminal_settings_store_level_api.update_terminal_settings_by_store_id(request)

```


