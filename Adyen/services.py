from __future__ import absolute_import, division, unicode_literals

import datetime

from Adyen import AdyenClient


class AdyenBase(object):
    def __setattr__(self, attr, value):
        client_attr = ["username", "password", "platform"]
        if attr in client_attr:
            if value:
                self.client[attr] = value
        else:
            super(AdyenBase, self).__setattr__(attr, value)

    def __getattr__(self, attr):
        client_attr = ["username", "password", "platform"]
        if attr in client_attr:
            return self.client[attr]


class AdyenServiceBase(AdyenBase):
    def __init__(self, client=None):
        if client:
            self.client = client
        else:
            self.client = AdyenClient()


class AdyenRecurring(AdyenServiceBase):
    """This represents the Adyen API Recurring Service.

    API calls currently implemented: listRecurringDetails and disable. Please
    refer to the Recurring Manual for specifics around the API.
    https://docs.adyen.com/developers/recurring-manual

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """

    def __init__(self, client=None):
        super(AdyenRecurring, self).__init__(client=client)
        self.service = "Recurring"

    def list_recurring_details(self, request, **kwargs):

        action = "listRecurringDetails"

        return self.client.call_api(request, self.service,
                                    action, **kwargs)

    def disable(self, request, **kwargs):

        action = "disable"

        if 'recurringDetailReference' not in request:
            raise ValueError("Include a 'recurringDetailReference'"
                             " to disable a specific recurring contract.")
        else:
            return self.client.call_api(request, self.service,
                                        action, **kwargs)


class AdyenHPP(AdyenServiceBase):
    """This represents the Adyen HPP  Service.

    This currently only implements the directory_lookup request which will
    return the list of payment methods available for given shopper. Please
    refer to the HPP manual and the directory lookup section for the specifics.
    https://docs.adyen.com/developers/hpp-manual#directorylookup

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """

    def __init__(self, client=None):
        super(AdyenHPP, self).__init__(client=client)

    def directory_lookup(self, request, **kwargs):

        action = "directory"

        try:
            datetime.datetime.strptime(request['sessionValidity'],
                                       '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            raise ValueError(
                "Incorrect date format, should be Y-m-dH:M:SZ,"
                " use datetime.strftime('%Y-%m-%dT%H:%M:%SZ')"
                " to format a datetime object.")

        return self.client.call_hpp(request, action)

    def hpp_payment(self, request, skip_details=None, **kwargs):

        if skip_details:
            action = "skipDetails"
        else:
            action = "select"

        if action == "skipDetails":
            if "issuerId" not in request:
                request['issuerId'] = ""
        if type(request['sessionValidity']) is not str:
            raise TypeError(
                'HPP: sessionValidity must be type of str,'
                ' use datetime.strftime to convert and format.')
        if all(k in request for k in ("shopperEmail", "shopperReference",
                                      "recurringContract")):
            recc = request['recurringContract']
            if recc != 'ONECLICK' and recc != 'RECURRING' \
                    and recc != 'ONECLICK,RECURRING':
                raise ValueError(
                    "HPP: recurringContract must be on of the following"
                    " values: 'ONECLICK', 'RECURRING',"
                    " 'ONECLICK,RECURRING'")

        result = self.client.hpp_payment(request, action)
        return result


class AdyenPayment(AdyenServiceBase):
    """This represents the Adyen API Payment Service.

    API calls currently implemented:
        authorise
        authorise3d
        adjustAuthorisation
        cancel
        capture
        refund
        cancelOrRefund
    Please refer to the Recurring Manual for specifics around the API.
    https://docs.adyen.com/developers/recurring-manual

    The AdyenPayment class, is accessible as adyen.payment.method(args)

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """

    def __init__(self, client=None):
        super(AdyenPayment, self).__init__(client=client)
        self.service = "Payment"

    def authorise(self, request, idempotency_key=None, **kwargs):

        action = "authorise"

        if 'shopperEmail' in request:
            if request['shopperEmail'] == '':
                raise ValueError(
                    'shopperEmail must contain the shopper email'
                    ' when authorising recurring contracts.')
        if 'shopperReference' in request:
            if request['shopperReference'] == '':
                raise ValueError(
                    'shopperReference must contain the shopper'
                    ' name when authorising recurring contracts.')

        return self.client.call_api(request, self.service,
                                    action, idempotency_key, **kwargs)

    def authorise3d(self, request, idempotency_key=None, **kwargs):
        action = "authorise3d"

        return self.client.call_api(request, self.service,
                                    action, idempotency_key, **kwargs)

    def adjustAuthorisation(self, request, **kwargs):
        action = "adjustAuthorisation"

        return self.client.call_api(request, self.service,
                                    action, **kwargs)

    def cancel(self, request, idempotency_key=None, **kwargs):
        action = "cancel"

        return self.client.call_api(request, self.service,
                                    action, idempotency_key, **kwargs)

    def capture(self, request, idempotency_key=None, **kwargs):

        action = "capture"

        if request['modificationAmount']["value"] == "" or \
                request['modificationAmount']['value'] == "0":
            raise ValueError(
                "Set the 'modificationAmount' to the original transaction"
                " amount, or less for a partial capture. "
                "modificationAmount should be an object with the following"
                " keys: {'currency':,'value':}")
        if request['originalReference'] == "":
            raise ValueError("Set the 'originalReference' to the psp "
                             "reference of the transaction to be modified")

        response = self.client.call_api(request, self.service,
                                        action, idempotency_key, **kwargs)
        return response

    def refund(self, request, idempotency_key=None, **kwargs):

        action = "refund"

        if request['modificationAmount']['value'] == "" or \
                request['modificationAmount']['value'] == "0":
            raise ValueError(
                "To refund this payment, provide the original value. "
                "Set the value to less than the original amount, "
                "to partially refund this payment.")
        else:
            return self.client.call_api(request, self.service,
                                        action, idempotency_key, **kwargs)

    def cancel_or_refund(self, request, idempotency_key=None, **kwargs):
        action = "cancelOrRefund"

        return self.client.call_api(
            request, self.service, action, idempotency_key, **kwargs
        )


class AdyenThirdPartyPayout(AdyenServiceBase):
    """This represents the Adyen API Third Party Payouts Service.

    https://docs.adyen.com/developers/api-reference/third-party-payouts-api

    The AdyenThirdPartyPayout class is accessible as adyen.payout.method(args)

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """

    def __init__(self, client=None):
        super(AdyenThirdPartyPayout, self).__init__(client=client)
        self.service = "Payout"

    def confirm(self, request=None, **kwargs):
        action = "confirmThirdParty"
        return self.client.call_api(
            request, self.service, action, **kwargs
        )

    def decline(self, request=None, **kwargs):
        action = "declineThirdParty"
        return self.client.call_api(
            request, self.service, action, **kwargs
        )

    def store_detail(self, request=None, **kwargs):
        action = "storeDetail"
        return self.client.call_api(
            request, self.service, action, **kwargs
        )

    def submit(self, request=None, **kwargs):
        action = "submitThirdParty"
        return self.client.call_api(
            request, self.service, action, **kwargs
        )

    def store_detail_and_submit(self, request=None, **kwargs):
        action = "storeDetailAndSubmitThirdParty"
        return self.client.call_api(
            request, self.service, action, **kwargs
        )


class AdyenCheckoutApi(AdyenServiceBase):
    """This represents the Adyen Checkout API .

    API calls currently implemented:
        paymentMethods
        payments
        payments/details
        originKeys

    Please refer to the checkout documentation for specifics around the API.
    https://docs.adyen.com/developers/checkout

    The AdyenPayment class, is accessible as adyen.payment.method(args)

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """

    def __init__(self, client=None):
        super(AdyenCheckoutApi, self).__init__(client=client)
        self.service = "Checkout"

    def payment_methods(self, request, **kwargs):
        action = "paymentMethods"
        if 'merchantAccount' in request:
            if request['merchantAccount'] == '':
                raise ValueError(
                    'merchantAccount must contain the merchant account'
                    ' when retrieving payment methods.')

        return self.client.call_checkout_api(request, action, **kwargs)

    def payments(self, request, idempotency_key=None, **kwargs):
        action = "payments"
        return self.client.call_checkout_api(request, action, idempotency_key,
                                             **kwargs)

    def payments_details(self, request=None, idempotency_key=None, **kwargs):
        action = "paymentsDetails"
        return self.client.call_checkout_api(request, action, idempotency_key,
                                             **kwargs)

    def payment_session(self, request=None, **kwargs):
        action = "paymentSession"
        return self.client.call_checkout_api(request, action, **kwargs)

    def payment_result(self, request=None, **kwargs):
        action = "paymentsResult"
        return self.client.call_checkout_api(request, action, **kwargs)

    def origin_keys(self, request=None, **kwargs):
        action = "originKeys"
        return self.client.call_checkout_api(request, action, **kwargs)

    # Orders endpoints

    # /paymentMethods/balance
    def payment_methods_balance(self, request, **kwargs):
        action = "paymentMethodsBalance"
        return self.client.call_checkout_api(request, action, **kwargs)

    # /orders
    def orders(self, request, **kwargs):
        action = "orders"
        return self.client.call_checkout_api(request, action, **kwargs)

    # /orders/cancel
    def orders_cancel(self, request, **kwargs):
        action = "ordersCancel"
        return self.client.call_checkout_api(request, action, **kwargs)


class AdyenBinLookup(AdyenServiceBase):
    """This represents the Adyen API Bin Lookup service.

    API call currently implemented: getCostEstimate.
    Please refer to the Bin Lookup Manual for specifics around the API.
    https://docs.adyen.com/api-explorer/#/BinLookup/v50/overview

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """

    def __init__(self, client=None):
        super(AdyenBinLookup, self).__init__(client=client)
        self.service = "BinLookup"

    def get_cost_estimate(self, request="", **kwargs):

        action = "getCostEstimate"

        return self.client.call_api(request, self.service, action, **kwargs)
