#!/bin/python

from __future__ import absolute_import, division, unicode_literals

from . import util
from .exceptions import (
    AdyenAPICommunicationError,
    AdyenAPIAuthenticationError,
    AdyenAPIUnprocessableEntity,
    AdyenAPIInvalidPermission,
    AdyenAPIValidationError,
    AdyenInvalidRequestError,
    AdyenError
)
from .client import AdyenClient
from .services import (
    AdyenBase,
    AdyenBinlookupApi,
    AdyenRecurringApi,
    AdyenPayment,
    AdyenPayoutsApi,
    AdyenManagementApi,
    AdyenCheckoutApi,
    AdyenTerminal,
    AdyenLegalEntityManagementApi
)

from .httpclient import HTTPClient


class Adyen(AdyenBase):
    def __init__(self, **kwargs):
        self.client = AdyenClient(**kwargs)
        self.payment = AdyenPayment(client=self.client)
        self.binlookup = AdyenBinlookupApi(client=self.client)
        self.payout = AdyenPayoutsApi(client=self.client)
        self.recurring = AdyenRecurringApi(client=self.client)

        self.checkout = AdyenCheckoutApi(client=self.client)
        self.terminal = AdyenTerminal(client=self.client)
        self.management = AdyenManagementApi(client=self.client)
        self.legalEntityManagement = AdyenLegalEntityManagementApi(client=self.client)


_base_adyen_obj = Adyen()
recurring = _base_adyen_obj.recurring
payment = _base_adyen_obj.payment
payout = _base_adyen_obj.payout
checkout = _base_adyen_obj.checkout
binlookup = _base_adyen_obj.binlookup
terminal = _base_adyen_obj.terminal
management = _base_adyen_obj.management
legalEntityManagement = _base_adyen_obj.legalEntityManagement
