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
    https://docs.adyen.com/online-payments/tokenization

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
    https://docs.adyen.com/online-payments/classic-integrations/hosted-payment-pages/directory-lookup

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
    Please refer to our API Explorer for specifics around these APIs.
    https://docs.adyen.com/api-explorer/

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
    """This represents the Adyen Payouts Service.
    https://docs.adyen.com/api-explorer/#/Payout/overview

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

        Modifications:
        capture
        refunds
        cancels
        reversals


    Please refer to the checkout documentation for specifics around the API.
    https://docs.adyen.com/online-payments

    The AdyenCheckout class, is accessible as adyen.checkout.method(args)

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

    def payments_captures(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param == "":
            raise ValueError(
                'must contain a pspReference in the path_param, path_param cannot be empty'
            )
        action = "paymentsCapture"
        return self.client.call_checkout_api(request, action, idempotency_key, path_param, **kwargs)

    def payments_cancels_without_reference(self, request, idempotency_key=None, **kwargs):
        action = "cancels"
        return self.client.call_checkout_api(request, action, idempotency_key, **kwargs)

    def payments_cancels_with_reference(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param == "":
            raise ValueError(
                'must contain a pspReference in the path_param, path_param cannot be empty'
            )
        action = "paymentsCancelsWithReference"
        return self.client.call_checkout_api(request, action, idempotency_key, path_param, **kwargs)

    def payments_reversals(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param == "":
            raise ValueError(
                'must contain a pspReference in the path_param, path_param cannot be empty'
            )
        action = "paymentsReversals"
        return self.client.call_checkout_api(request, action, idempotency_key, path_param, **kwargs)

    def payments_refunds(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param == "":
            raise ValueError(
                'must contain a pspReference in the path_param, path_param cannot be empty'
            )
        action = "paymentsRefunds"
        return self.client.call_checkout_api(request, action, idempotency_key, path_param, **kwargs)

    def origin_keys(self, request=None, **kwargs):
        action = "originKeys"
        return self.client.call_checkout_api(request, action, **kwargs)

    def sessions(self, request=None, **kwargs):
        action = "sessions"
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
    https://docs.adyen.com/api-explorer/#/BinLookup/

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


class AdyenTerminal(AdyenServiceBase):
    """This represents the Adyen API Terminal service.

    API call currently implemented:
        - assignTerminals
        - findTerminal
        - getStoreUnderAccount
        - getTerminalDetails
        - getTerminalsUnderAccount
    Please refer to the Terminal Manual for specifics around the API.
    https://docs.adyen.com/api-explorer/#/postfmapi/

    Args:
        client (AdyenAPIClient, optional): An API client for the service to
            use. If not provided, a new API client will be created.
    """

    def __init__(self, client=None):
        super(AdyenTerminal, self).__init__(client=client)
        self.service = "terminal"

    def assign_terminals(self, request="", **kwargs):
        return self.client.call_api(request, self.service, "assignTerminals", **kwargs)

    def find_terminal(self, request="", **kwargs):
        return self.client.call_api(request, self.service, "findTerminal", **kwargs)

    def get_stores_under_account(self, request="", **kwargs):
        return self.client.call_api(request, self.service, "getStoresUnderAccount", **kwargs)

    def get_terminal_details(self, request="", **kwargs):
        return self.client.call_api(request, self.service, "getTerminalDetails", **kwargs)

    def get_terminals_under_account(self, request="", **kwargs):
        return self.client.call_api(request, self.service, "getTerminalsUnderAccount", **kwargs)


class AdyenManagementApi(AdyenServiceBase):
    """This represents the Adyen Management API .

        API calls currently implemented:


        Please refer to the checkout documentation for specifics around the API.
        https://docs.adyen.com/online-payments

        The AdyenCheckout class, is accessible as adyen.management.method(args)

        Args:
            client (AdyenAPIClient, optional): An API client for the service to
                use. If not provided, a new API client will be created.
        """

    def __init__(self, client=None):
        super(AdyenManagementApi, self).__init__(client=client)
        self.service = "management"

    # Account - company level

    def get_list_of_company_accounts(self, request=None, idempotency_key=None, **kwargs):
        action = "getListOfCompanyAccounts"
        return self.client.call_management_api(request, action, idempotency_key, **kwargs)

    def get_company_account(self, request=None, idempotency_key=None, path_param=None, **kwargs):
        if path_param == None:
            raise ValueError(
                'must contain a companyId in the path_param, path_param cannot be empty'
            )
        action = "getCompanyAccount"
        return self.client.call_management_api(request, action, idempotency_key, path_param, **kwargs)

    def get_list_of_merchant_accounts_under_company(self, request=None, idempotency_key=None, path_param=None,
                                                    **kwargs):
        if path_param == None:
            raise ValueError(
                'must contain a companyId in the path_param, path_param cannot be empty'
            )
        action = "getListOfMerchantAccountsUnderCompany"
        return self.client.call_management_api(request, action, idempotency_key, path_param, **kwargs)

    # Account - merchant level

    def create_merchant_account(self, request, idempotency_key=None, **kwargs):
        action = "createMerchants"
        return self.client.call_management_api(request, action, idempotency_key, **kwargs)

    def activate_merchant_accounts(self, request=None, idempotency_key=None, path_param=None, **kwargs):
        if path_param is None:
            raise ValueError(
                'must contain a merchantAccountId in the path_param, path_param cannot be empty'
            )
        action = "activateMerchant"
        return self.client.call_management_api(request, action, idempotency_key, path_param, **kwargs)

    def get_merchant_account(self, request=None, idempotency_key=None, path_param=None, **kwargs):
        if path_param is None:
            raise ValueError(
                'must contain a merchantAccountId in the path_param, path_param cannot be empty'
            )
        action = "getMerchantAccount"
        return self.client.call_management_api(request, action, idempotency_key, path_param, **kwargs)

    def get_list_of_merchant_accounts(self, request=None, idempotency_key=None, **kwargs):
        action = "getListOfMerchantAccounts"
        return self.client.call_management_api(request, action, idempotency_key, **kwargs)

    # Accounts - store level

    def create_store(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param is None:
            raise ValueError(
                'must contain a merchantAccountId in the path_param, path_param cannot be empty'
            )
        action = "createStore"
        return self.client.call_management_api(request, action, idempotency_key, path_param, **kwargs)

    def get_list_of_stores_under_merchant_account(self, request=None, idempotency_key=None, path_param=None, **kwargs):
        if path_param is None:
            raise ValueError(
                'must contain a merchantAccountId in the path_param, path_param cannot be empty'
            )
        action = "getListOfStoresUnderMerchantAccounts"
        return self.client.call_management_api(request, action, idempotency_key, path_param, **kwargs)

    def get_store_under_merchant_account(self, request=None, idempotency_key=None, path_param=None, **kwargs):
        if path_param is None or path_param.find(',') == -1:
            raise ValueError(
                'must contain a merchantAccountId and storeId comma'
                'separated in the path_param, path_param cannot be empty'
            )
        action = "getStoreUnderMerchantAccount"
        return self.client.call_management_api(request, action, idempotency_key, path_param, **kwargs)

    def update_store_under_merchant_account(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param is None or path_param.find(',') == -1:
            raise ValueError(
                'must contain a merchantAccountId and storeId comma'
                'separated in the path_param, path_param cannot be empty'
            )
        action = "updateStoreUnderMerchantAccount"
        return self.client.call_management_api(request, action, idempotency_key, path_param, **kwargs)

    def get_list_of_stores(self, request=None, idempotency_key=None, path_param=None, **kwargs):
        action = "getListOfStores"
        return self.client.call_management_api(request, action, idempotency_key, path_param, **kwargs)

    def create_store(self, request, idempotency_key=None, path_param=None, **kwargs):
        action = "createStore"
        return self.client.call_management_api(request, action, idempotency_key, path_param, **kwargs)

    def get_store(self, request = None, idempotency_key=None, path_param=None, **kwargs):
        if path_param is None:
            raise ValueError(
                'must contain a storeId in the path_param, path_param cannot be empty'
            )
        action = "getStore"
        return self.client.call_management_api(request, action, idempotency_key, path_param, **kwargs)

    def update_store(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param is None:
            raise ValueError(
                'must contain a storeId in the path_param, path_param cannot be empty'
            )
        action = "updateStore"
        return self.client.call_management_api(request, action, idempotency_key, path_param, **kwargs)

