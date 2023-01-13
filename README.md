![Python](https://user-images.githubusercontent.com/55943882/212274988-4e58b807-d39b-4274-b712-06008b1ef5fc.png)

# Adyen APIs Library for Python

[![version](https://img.shields.io/badge/version-7.1.1-blue.svg)](https://docs.adyen.com/development-resources/libraries)

This is the officially supported Python library for using Adyen's APIs.

## Integration 
The library supports all APIs under the following services:
 
* [Checkout API](https://docs.adyen.com/api-explorer/#/CheckoutService/v69/overview): Our latest integration for accepting online payments. Current supported version:  **v69**
* [Payments API](https://docs.adyen.com/api-explorer/#/Payment/v64/overview): Our classic integration for online payments. Current supported version:  **v64**
* [Recurring API](https://docs.adyen.com/api-explorer/#/Recurring/v49/overview): Endpoints for managing saved payment details. Current supported version:  **v49**
* [Payouts API](https://docs.adyen.com/api-explorer/#/Payout/v64/overview): Endpoints for sending funds to your customers. Current supported version:  **v64**
* [Orders API](https://docs.adyen.com/api-explorer/#/CheckoutService/v67/post/orders): Endpoints for creating and canceling orders. Current supported version:  **v67**
* [Utility API](https://docs.adyen.com/api-explorer/#/CheckoutService/v67/post/originKeys): This operation takes the origin domains and returns a JSON object containing the corresponding origin keys for the domains. Current supported version:  **v67**
* [Terminal API](https://docs.adyen.com/api-explorer/#/postfmapi/v1/overview): Endpoints for interacting with POS terminals. **v1**
 
For more information, refer to our [documentation](https://docs.adyen.com/) or the [API Explorer](https://docs.adyen.com/api-explorer/).
 
 
## Prerequisites
 
-   [Adyen test account](https://docs.adyen.com/get-started-with-adyen)
-   [API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key). For testing, your API credential needs to have the [API PCI Payments role](https://docs.adyen.com/development-resources/api-credentials#roles).
- Python 2.7 **(Deprecated)** or 3.6
- Packages: requests or pycurl ( optional )
 

 ## Installation

### For development propose

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

ady = Adyen.Adyen()

ady.payment.client.xapikey = "YourXapikey"
ady.payment.client.skin_code = "skin code for Hosted Payment pages"
ady.payment.client.hmac = "HMAC key for skin code"
ady.payment.client.platform = "test" # Environment to use the library in.
ady.payment.client.merchant_account = "merchant account name from CA"
~~~~
### Using query parameters
Define a dictionary with query parameters that you want to use.
~~~~ python
query_parameters = {
   'pageSize':10,
   'pageNumber':3
 }
~~~~
pass the dictionary to the method as an additional argument.
~~~~ python
ady.management.account_company_level_api.get_companies(query_parameters=query_parameters)
~~~~
 
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
