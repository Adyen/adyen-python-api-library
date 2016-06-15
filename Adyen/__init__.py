#!/bin/python 
from . import util
from .util import generate_hpp_sig
from .exceptions import (
    AdyenAPICommunicationError,
    AdyenAPIAuthenticationError,
    AdyenAPIInvalidPermission,
    AdyenAPIValidationError, 
    AdyenInvalidRequestError,
    AdyenError
)
from .apiclient import AdyenAPIClient
from .services import (
    AdyenBase,
    AdyenRecurring,
    AdyenPayment,
    AdyenHPP,
    AdyenPayout)


username = ""
password = ""
review_payout_username = ""
review_payout_password = ""
store_payout_username = ""
store_payout_password = ""
platform = "test"
merchant_account = ""
merchant_specific_url = ""
hmac = ""


class Adyen(AdyenBase):
    def __init__(self, **kwargs):
        self.api_client = AdyenAPIClient(**kwargs)
        self.payment = AdyenPayment(api_client=self.api_client)
        self.hpp = AdyenHPP(api_client=self.api_client)
        self.recurring = AdyenRecurring(api_client=self.api_client)
        self.payout = AdyenPayout(api_client=self.api_client)


_base_adyen_client = Adyen()
recurring = _base_adyen_client.recurring
hpp = _base_adyen_client.hpp
payment = _base_adyen_client.payment
payout = _base_adyen_client.payout
