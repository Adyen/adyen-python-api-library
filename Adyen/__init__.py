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
from .client import AdyenClient
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
        self.client = AdyenClient(**kwargs)
        self.payment = AdyenPayment(client=self.client)
        self.hpp = AdyenHPP(client=self.client)
        self.recurring = AdyenRecurring(client=self.client)
        self.payout = AdyenPayout(client=self.client)


_base_adyen_obj = Adyen()
recurring = _base_adyen_obj.recurring
hpp = _base_adyen_obj.hpp
payment = _base_adyen_obj.payment
payout = _base_adyen_obj.payout

