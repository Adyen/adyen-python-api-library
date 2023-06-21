from ..base import AdyenServiceBase


class GeneralApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(GeneralApi, self).__init__(client=client)
        self.service = "platformsFund"

    def account_holder_balance(self, request, idempotency_key=None, **kwargs):
        """
        Get the balances of an account holder
        """
        endpoint = f"/accountHolderBalance"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def account_holder_transaction_list(self, request, idempotency_key=None, **kwargs):
        """
        Get a list of transactions
        """
        endpoint = f"/accountHolderTransactionList"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def debit_account_holder(self, request, idempotency_key=None, **kwargs):
        """
        Send a direct debit request
        """
        endpoint = f"/debitAccountHolder"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def payout_account_holder(self, request, idempotency_key=None, **kwargs):
        """
        Pay out from an account to the account holder
        """
        endpoint = f"/payoutAccountHolder"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def refund_funds_transfer(self, request, idempotency_key=None, **kwargs):
        """
        Refund a funds transfer
        """
        endpoint = f"/refundFundsTransfer"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def refund_not_paid_out_transfers(self, request, idempotency_key=None, **kwargs):
        """
        Refund all transactions of an account since the most recent payout
        """
        endpoint = f"/refundNotPaidOutTransfers"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def setup_beneficiary(self, request, idempotency_key=None, **kwargs):
        """
        Designate a beneficiary account and transfer the benefactor's current balance
        """
        endpoint = f"/setupBeneficiary"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def transfer_funds(self, request, idempotency_key=None, **kwargs):
        """
        Transfer funds between platform accounts
        """
        endpoint = f"/transferFunds"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

