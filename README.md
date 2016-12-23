# Adyen APIs Library for Python

The Adyen API Library for Python enables you to work with Adyen APIs.

## Requirements

Make sure you have an Adyen account. If you don't have this you can request it <a href="https://www.adyen.com/home/discover/test-account-signup#form" target="_blank">here</a>
To make the automatice testing cases working for your account change the credentials in the tests/test.ini file.

## Installation

Adyen Python library is not yet published on PIP. To install, please download this repository, and include the Adyen folder
with your application.

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

## Documentation

Follow the rest our guides from the documentation on how to use this library.
<insert documentation link here>

## Licence

MIT license see LICENSE
