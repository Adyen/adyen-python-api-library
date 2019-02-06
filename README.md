[![Build Status](https://travis-ci.org/Adyen/adyen-python-api-library.svg?branch=master)](https://travis-ci.org/Adyen/adyen-python-api-library)
[![Coverage Status](https://coveralls.io/repos/github/Adyen/adyen-python-api-library/badge.svg?branch=master)](https://coveralls.io/github/Adyen/adyen-python-api-library?branch=master)

# Adyen APIs Library for Python

This library simplifies working with Adyen APIs and allows you to integrate Adyen
payments within any Python application.

## Integration
The Library supports all APIs under the following services:

* checkout
* checkout utility
* payments
* modifications
* payouts
* recurring

## Requirements

- Python 2.7 or 3.6
- Packages: requests or pycurl ( optional )
- Adyen account. If you don't have this you can request it here: https://www.adyen.com/home/discover/test-account-signup#form

## Installation

Clone this git repository or use pip: ```pip install Adyen```

## Usage

Create a class instance of the 'Adyen' class.

```python
import Adyen

ady = Adyen.Adyen()

ady.payment.client.username = "webservice user name"
ady.payment.client.skin_code = "skin code for Hosted Payment pages"
ady.payment.client.hmac = "HMAC key for skin code"
ady.payment.client.platform = "test" # Environment to use the library in.
ady.payment.client.merchant_account = "merchant account name from CA"
ady.payment.client.password = "webservice user password"
ady.payment.client.app_name = "your app name"
```

## Documentation
* https://docs.adyen.com/developers/development-resources/libraries
* https://docs.adyen.com/developers/checkout/api-integration

## Licence
MIT license see LICENSE
