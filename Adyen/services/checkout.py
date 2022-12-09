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
        method = "POST"

        return self.client.call_checkout_api(request, method, endpoint, **kwargs)

    def payments(self, request, idempotency_key=None, **kwargs):
        endpoint = "payments"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, idempotency_key,
                                             **kwargs)

    def payments_details(self, request=None, idempotency_key=None, **kwargs):
        endpoint = "payments/details"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, idempotency_key,
                                             **kwargs)

    def payment_session(self, request=None, **kwargs):
        endpoint = "paymentSession"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, **kwargs)

    def payment_result(self, request=None, **kwargs):
        endpoint = "payments/result"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, **kwargs)

    def payments_captures(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param == "":
            raise ValueError(
                'must contain a pspReference in the path_param, path_param cannot be empty'
            )
        endpoint = f"payments/{path_param}/captures"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, idempotency_key, **kwargs)

    def payments_cancels_without_reference(self, request, idempotency_key=None, **kwargs):
        endpoint = "cancels"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, idempotency_key, **kwargs)

    def payments_cancels_with_reference(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param == "":
            raise ValueError(
                'must contain a pspReference in the path_param, path_param cannot be empty'
            )
        endpoint = f"payments/{path_param}/cancels"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, idempotency_key, **kwargs)

    def payments_reversals(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param == "":
            raise ValueError(
                'must contain a pspReference in the path_param, path_param cannot be empty'
            )
        endpoint = f"payments/{path_param}/reversals"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, idempotency_key, **kwargs)

    def payments_refunds(self, request, idempotency_key=None, path_param=None, **kwargs):
        if path_param == "":
            raise ValueError(
                'must contain a pspReference in the path_param, path_param cannot be empty'
            )
        endpoint = f"payments/{path_param}/refunds"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, idempotency_key, **kwargs)

    def origin_keys(self, request=None, **kwargs):
        endpoint = "originKeys"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, **kwargs)

    def sessions(self, request=None, **kwargs):
        endpoint = "sessions"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, **kwargs)
    # Orders endpoints

    # /paymentMethods/balance
    def payment_methods_balance(self, request, **kwargs):
        endpoint = "paymentMethods/balance"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, **kwargs)

    # /orders
    def orders(self, request, **kwargs):
        endpoint = "orders"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, **kwargs)

    # /orders/cancel
    def orders_cancel(self, request, **kwargs):
        endpoint = "orders/cancel"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, **kwargs)

    # Apple Pay session validation
    def applepay_session(self, request, **kwargs):
        endpoint = "applePay/sessions"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, **kwargs)

    # Payment links endpoints
    def payment_links(self, request, idempotency_key=None, **kwargs):
        endpoint = "paymentLinks"
        method = "POST"
        return self.client.call_checkout_api(request, method, endpoint, idempotency_key, **kwargs)

    def get_payment_link(self, path_param=None, idempotency_key=None, **kwargs):
        endpoint = f"paymentLinks/{path_param}"
        method = "GET"
        return self.client.call_checkout_api(None, method, endpoint, idempotency_key, **kwargs)

    def update_payment_link(self, request, path_param=None, idempotency_key=None, **kwargs):
        endpoint = f"paymentLinks/{path_param}"
        method = "PATCH"
        return self.client.call_checkout_api(request, method, endpoint, idempotency_key, **kwargs)
