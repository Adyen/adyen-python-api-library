#!/bin/python

from __future__ import absolute_import, division, unicode_literals

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
    AdyenBinLookup,
    AdyenRecurring,
    AdyenPayment,
    AdyenThirdPartyPayout,
    AdyenHPP,
    AdyenCheckoutApi
)

from .httpclient import HTTPClient


class Adyen(AdyenBase):
    def __init__(self, **kwargs):
        self.client = AdyenClient(**kwargs)
        self.payment = AdyenPayment(client=self.client)
        self.binlookup = AdyenBinLookup(client=self.client)
        self.payout = AdyenThirdPartyPayout(client=self.client)
        self.hpp = AdyenHPP(client=self.client)
        self.recurring = AdyenRecurring(client=self.client)
        self.checkout = AdyenCheckoutApi(client=self.client)


_base_adyen_obj = Adyen()
recurring = _base_adyen_obj.recurring
hpp = _base_adyen_obj.hpp
payment = _base_adyen_obj.payment
payout = _base_adyen_obj.payout
checkout = _base_adyen_obj.checkout
binlookup = _base_adyen_obj.binlookup
