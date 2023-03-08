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
    AdyenPaymentsApi,
    AdyenBinlookupApi,
    AdyenRecurringApi,
    AdyenPayoutsApi,
    AdyenManagementApi,
    AdyenCheckoutApi,
    AdyenTerminalApi,
    AdyenLegalEntityManagementApi,
    AdyenDataProtectionApi,
    AdyenTransfersApi,
    AdyenStoredValueApi,
    AdyenBalancePlatformApi
)

from .httpclient import HTTPClient


class Adyen(AdyenBase):
    def __init__(self, **kwargs):
        self.client = AdyenClient(**kwargs)
        self.payment = AdyenPaymentsApi(client=self.client)
        self.binlookup = AdyenBinlookupApi(client=self.client)
        self.payout = AdyenPayoutsApi(client=self.client)
        self.recurring = AdyenRecurringApi(client=self.client)
        self.checkout = AdyenCheckoutApi(client=self.client)
        self.terminal = AdyenTerminalApi(client=self.client)
        self.management = AdyenManagementApi(client=self.client)
        self.legalEntityManagement = AdyenLegalEntityManagementApi(client=self.client)
        self.dataProtection = AdyenDataProtectionApi(client=self.client)
        self.transfers = AdyenTransfersApi(client=self.client)
        self.storedValue = AdyenStoredValueApi(client=self.client)
        self.balancePlatform = AdyenBalancePlatformApi(client=self.client)


_base_adyen_obj = Adyen()
recurring = _base_adyen_obj.recurring
payment = _base_adyen_obj.payment
payout = _base_adyen_obj.payout
checkout = _base_adyen_obj.checkout
binlookup = _base_adyen_obj.binlookup
terminal = _base_adyen_obj.terminal
management = _base_adyen_obj.management
legalEntityManagement = _base_adyen_obj.legalEntityManagement
dataProtection = _base_adyen_obj.dataProtection
transfers = _base_adyen_obj.transfers
storedValue = _base_adyen_obj.storedValue
balancePlatform = _base_adyen_obj.balancePlatform
