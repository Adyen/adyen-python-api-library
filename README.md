![Python](https://user-images.githubusercontent.com/55943882/212274988-4e58b807-d39b-4274-b712-06008b1ef5fc.png)

# Adyen APIs Library for Python

[![version](https://img.shields.io/badge/version-8.0.0-blue.svg)](https://docs.adyen.com/development-resources/libraries)

This is the officially supported Python library for using Adyen's APIs.

## Supported API versions
| API | Description | Service Name | Supported version |
| --- | ----------- | ------------ | ----------------- | 
|[BIN lookup API](https://docs.adyen.com/api-explorer/#/BinLookup/v52/overview) | The BIN Lookup API provides endpoints for retrieving information based on a given BIN. | binLookup | **v52** |
| [Balance Platform API](https://docs.adyen.com/api-explorer/balanceplatform/1/overview) | The Balance Platform API enables you to create a platform where you can onboard your users as account holders and create balance accounts, cards, and business accounts. | balancePlatform | **v2** |
| [Checkout API](https://docs.adyen.com/api-explorer/#/CheckoutService/v69/overview)| Our latest integration for accepting online payments. | checkout | **v70** |
| [Data Protection API](https://docs.adyen.com/development-resources/data-protection-api) | Endpoint for requesting data erasure. | dataProtection | **v1** |
| [Legal Entity Management API](https://docs.adyen.com/api-explorer/legalentity/latest/overview) | Endpoint to manage legal entities | legalEntityManagement | **v2** |
| [Management API](https://docs.adyen.com/api-explorer/#/ManagementService/v1/overview)| Configure and manage your Adyen company and merchant accounts, stores, and payment terminals. | management | **v1** |
| [Payments API](https://docs.adyen.com/api-explorer/#/Payment/v68/overview)| Our classic integration for online payments. | payments | **v68** |
| [Payouts API](https://docs.adyen.com/api-explorer/#/Payout/v68/overview)| Endpoints for sending funds to your customers. | payouts | **v68** |
| [POS Terminal Management API](https://docs.adyen.com/api-explorer/#/postfmapi/v1/overview)| Endpoints for managing your point-of-sale payment terminals. | terminal | **v1** |
| [Recurring API](https://docs.adyen.com/api-explorer/#/Recurring/v68/overview)| Endpoints for managing saved payment details. | recurring | **v68** |
| [Stored Value API](https://docs.adyen.com/payment-methods/gift-cards/stored-value-api) | Endpoints for managing gift cards. | storedValue | **v46** |
| [Transfers API](https://docs.adyen.com/api-explorer/transfers/3/overview) | Endpoints for managing transfers, getting information about transactions or moving fund | transfers | **v3** |

For more information, refer to our [documentation](https://docs.adyen.com/) or the [API Explorer](https://docs.adyen.com/api-explorer/).



 
 
## Prerequisites
 
-   [Adyen test account](https://docs.adyen.com/get-started-with-adyen)
-   [API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key). For testing, your API credential needs to have the [API PCI Payments role](https://docs.adyen.com/development-resources/api-credentials#roles).
- Python 3.6
- Packages (optional): requests or pycurl  
 

 ## Installation

### For development purposes

Clone this repository and run 
~~~~ bash 
make install
~~~~

### For usage propose

Use pip command: 
~~~~ bash 
pip install Adyen
~~~~

## Using the library
 
 
### General use with API key
 
~~~~ python
import Adyen

adyen = Adyen.Adyen()

adyen.payment.client.xapikey = "YourXapikey"
adyen.payment.client.hmac = "YourHMACkey"
adyen.payment.client.platform = "test" # Environment to use the library in.
adyen.payment.client.merchant_account = "merchant account name from CA"
~~~~
### Consuming Services
Every API the library supports is represented by a service object. The name of the service matching the corresponding API is listed in the [Integrations](#supported-api-versions) section of this document.
#### Using all services
~~~~python
import Adyen
adyen = Adyen.Adyen()
adyen.payment.client.xapikey = "YourXapikey"
adyen.payment.client.platform = "test"  # change to live for production
request = {
      "amount": {
        "currency": "USD",
        "value": 1000 # value in minor units
      },
      "reference": "Your order number",
      "paymentMethod": {
        "type": "visa",
        "encryptedCardNumber": "test_4111111111111111",
        "encryptedExpiryMonth": "test_03",
        "encryptedExpiryYear": "test_2030",
        "encryptedSecurityCode": "test_737"
      },
      "shopperReference": "YOUR_UNIQUE_SHOPPER_ID_IOfW3k9G2PvXFu2j",
      "returnUrl": "https://your-company.com/...",
      "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
    }
result = adyen.checkout.payments_api.payments(request)
~~~~
#### Using one of the services
~~~~python
from Adyen import checkout
checkout.client.xapikey = "YourXapikey"
checkout.client.platform = "test"  # change to live for production
request = {
      "amount": {
        "currency": "USD",
        "value": 1000 # value in minor units
      },
      "reference": "Your order number",
      "paymentMethod": {
        "type": "visa",
        "encryptedCardNumber": "test_4111111111111111",
        "encryptedExpiryMonth": "test_03",
        "encryptedExpiryYear": "test_2030",
        "encryptedSecurityCode": "test_737"
      },
      "shopperReference": "YOUR_UNIQUE_SHOPPER_ID_IOfW3k9G2PvXFu2j",
      "returnUrl": "https://your-company.com/...",
      "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
    }
result = checkout.payments_api.payments(request)
~~~~
#### Force HTTP library
~~~~python
import Adyen
adyen = Adyen.Adyen()
adyen.client.http_force = 'requests' # or 'pycurl'
~~~~
### Using query parameters (management API only)
Define a dictionary with query parameters that you want to use.
~~~~ python
query_parameters = {
   'pageSize':10,
   'pageNumber':3
 }
~~~~
pass the dictionary to the method as an additional argument.
~~~~ python
adyen.management.account_company_level_api.get_companies(query_parameters=query_parameters)
~~~~
### Handling exceptions
Adyen service exceptions extend the AdyenError class. After you catch this exception, you can access the 
class arguments for the specifics around this error or use the debug method which prints all the arguments.
~~~~python
try:
    adyen.checkout.payments(request)
except Adyen.exceptions.AdyenErorr as error:
    error.debug()
~~~~
<details><summary>List of exceptions</summary>
<p>AdyenInvalidRequestError</p>
<p>AdyenAPIResponseError</p>
<p>AdyenAPIAuthenticationError</p>
<p>AdyenAPIInvalidPermission</p>
<p>AdyenAPICommunicationError</p>
<p>AdyenAPIValidationError</p>
<p>AdyenAPIUnprocessableEntity</p>
<p>AdyenAPIInvalidFormat</p>
<p>AdyenEndpointInvalidFormat</p>
</details>

### Example integration
 
For a closer look at how our Python library works, clone our [example integration](https://github.com/adyen-examples/adyen-python-online-payments). This includes commented code, highlighting key features and concepts, and examples of API calls that can be made using the library.


## Contributing
 
We encourage you to contribute to this repository, so everyone can benefit from new features, bug fixes, and any other improvements.
 
 
Have a look at our [contributing guidelines](https://github.com/Adyen/adyen-python-api-library/blob/develop/CONTRIBUTING.md) to find out how to raise a pull request.
 
 
## Support
If you have a feature request, or spotted a bug or a technical problem, [create an issue here](https://github.com/Adyen/adyen-web/issues/new/choose).
 
For other questions, [contact our Support Team](https://www.adyen.help/hc/en-us/requests/new?ticket_form_id=360000705420).
 
 
## Licence
This repository is available under the [MIT license](https://github.com/Adyen/adyen-python-api-library/blob/main/LICENSE.md).
 
 
## See also
* [Example integration](https://github.com/adyen-examples/adyen-python-online-payments)
* [Adyen docs](https://docs.adyen.com/)
* [API Explorer](https://docs.adyen.com/api-explorer/)
