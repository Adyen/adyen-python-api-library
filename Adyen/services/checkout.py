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
        endpoint = "paymentMethods"
        if 'merchantAccount' in request:
            if request['merchantAccount'] == '':
                raise ValueError(
                    'merchantAccount must contain the merchant account'
                    ' when retrieving payment methods.')

        return self.client.call_checkout_api(request, endpoint, **kwargs)

    def payments(self, request, idempotency_key=None, **kwargs):
        endpoint = "payments"
        return self.client.call_checkout_api(request, endpoint, idempotency_key,
                                             **kwargs)

    def payments_details(self, request=None, idempotency_key=None, **kwargs):
        endpoint = "payments/details"
        return self.client.call_checkout_api(request, endpoint, idempotency_key,
                                             **kwargs)

    def payment_session(self, request=None, **kwargs):
        endpoint = "paymentSession"
        return self.client.call_checkout_api(request, endpoint, **kwargs)

    def payment_result(self, request=None, **kwargs):
        endpoint = "payments/result"
        return self.client.call_checkout_api(request, endpoint, **kwargs)

    def payments_captures(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param == "":
            raise ValueError(
                'must contain a pspReference in the path_param, path_param cannot be empty'
            )
        endpoint = f"payments/{path_param}/captures"
        return self.client.call_checkout_api(request, endpoint, idempotency_key, **kwargs)

    def payments_cancels_without_reference(self, request, idempotency_key=None, **kwargs):
        endpoint = "cancels"
        return self.client.call_checkout_api(request, endpoint, idempotency_key, **kwargs)

    def payments_cancels_with_reference(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param == "":
            raise ValueError(
                'must contain a pspReference in the path_param, path_param cannot be empty'
            )
        endpoint = f"payments/{path_param}/cancels"
        return self.client.call_checkout_api(request, endpoint, idempotency_key, **kwargs)

    def payments_reversals(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param == "":
            raise ValueError(
                'must contain a pspReference in the path_param, path_param cannot be empty'
            )
        endpoint = f"payments/{path_param}/reversals"
        return self.client.call_checkout_api(request, endpoint, idempotency_key, **kwargs)

    def payments_refunds(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param == "":
            raise ValueError(
                'must contain a pspReference in the path_param, path_param cannot be empty'
            )
        endpoint = f"payments/{path_param}/refunds"
        return self.client.call_checkout_api(request, endpoint, idempotency_key, **kwargs)

    def origin_keys(self, request=None, **kwargs):
        endpoint = "originKeys"
        return self.client.call_checkout_api(request, endpoint, **kwargs)

    def sessions(self, request=None, **kwargs):
        endpoint = "sessions"
        return self.client.call_checkout_api(request, endpoint, **kwargs)
    # Orders endpoints

    # /paymentMethods/balance
    def payment_methods_balance(self, request, **kwargs):
        endpoint = "paymentMethods/balance"
        return self.client.call_checkout_api(request, endpoint, **kwargs)

    # /orders
    def orders(self, request, **kwargs):
        endpoint = "orders"
        return self.client.call_checkout_api(request, endpoint, **kwargs)

    # /orders/cancel
    def orders_cancel(self, request, **kwargs):
        endpoint = "orders/cancel"
        return self.client.call_checkout_api(request, endpoint, **kwargs)
