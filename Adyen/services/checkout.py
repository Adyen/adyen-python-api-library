from .base import AdyenServiceBase


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
