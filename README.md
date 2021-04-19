[![Build Status](https://travis-ci.org/Adyen/adyen-python-api-library.svg?branch=master)](https://travis-ci.org/Adyen/adyen-python-api-library)
[![Coverage Status](https://coveralls.io/repos/github/Adyen/adyen-python-api-library/badge.svg?branch=master)](https://coveralls.io/github/Adyen/adyen-python-api-library?branch=master)

This is the officially supported python library for using Adyen's APIs.
## Integration 
The library supports all APIs under the following services:
 
* [Checkout API](https://docs.adyen.com/api-explorer/#/CheckoutService/v67/overview): Our latest integration for accepting online payments. Current supported version: **v[insert version nr]**
* [Payments API](https://docs.adyen.com/api-explorer/#/Payment/v64/overview): Our classic integration for online payments. Current supported version: **v[insert version nr]**
* [Recurring API](https://docs.adyen.com/api-explorer/#/Recurring/v49/overview): Endpoints for managing saved payment details. Current supported version: **v[insert version nr]**
* [Payouts API](https://docs.adyen.com/api-explorer/#/Payout/v64/overview): Endpoints for sending funds to your customers. Current supported version: **v[insert version nr]**
* [Orders API](https://docs.adyen.com/api-explorer/#/CheckoutService/v67/post/orders): Endpoints for creating and canceling orders. Current supported version: **v[insert version nr]**
* [Utility API](https://docs.adyen.com/api-explorer/#/CheckoutService/v1/post/originKeys): This operation takes the origin domains and returns a JSON object containing the corresponding origin keys for the domains. Current supported version: **v[insert version nr]**
 
For more information, refer to our [documentation](https://docs.adyen.com/) or the [API Explorer](https://docs.adyen.com/api-explorer/).
 
 
## Prerequisites
 
-   [Adyen test account](https://docs.adyen.com/get-started-with-adyen)
-   [API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key). For testing, your API credential needs to have the [API PCI Payments role](https://docs.adyen.com/development-resources/api-credentials#roles).
- Python 2.7 or 3.6
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
 
 
### General use with basic auth
 
~~~~ python
import Adyen

ady = Adyen.Adyen()

ady.payment.client.username = "webservice user name"
ady.payment.client.password = "webservice user password"
ady.payment.client.skin_code = "skin code for Hosted Payment pages"
ady.payment.client.hmac = "HMAC key for skin code"
ady.payment.client.platform = "test" # Environment to use the library in.
ady.payment.client.merchant_account = "merchant account name from CA"
~~~~
 
### Example integration
 
For a closer look at how our python library works, clone our [example integration](https://github.com/adyen-examples/adyen-python-online-payments). This includes commented code, highlighting key features and concepts, and examples of API calls that can be made using the library.


## Contributing
 
We encourage you to contribute to this repository, so everyone can benefit from new features, bug fixes, and any other improvements.
 
 
Have a look at our [contributing guidelines](https://github.com/Adyen/adyen-python-api-library/blob/develop/CONTRIBUTING.md) to find out how to raise a pull request.
 
 
## Support
If you have a feature request, or spotted a bug or a technical problem, [create an issue here](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2FAdyen%2Fadyen-web%2Fissues%2Fnew%2Fchoose).
 
For other questions, [contact our Support Team](https://www.adyen.help/hc/en-us/requests/new?ticket_form_id=360000705420).
 
 
## Licence
This repository is available under the [MIT license](https://github.com/Adyen/adyen-python-api-library/blob/master/LICENSE.md).
 
 
## See also
* [Example integration](https://github.com/adyen-examples/adyen-python-online-payments)
* [Adyen docs](https://docs.adyen.com/)
* [API Explorer](https://docs.adyen.com/api-explorer/)

