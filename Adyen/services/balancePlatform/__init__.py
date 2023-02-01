from ..base import AdyenServiceBase
from .account_holders_api import AccountHoldersApi
from .balance_accounts_api import BalanceAccountsApi
from .payment_instrument_groups_api import PaymentInstrumentGroupsApi
from .payment_instruments_api import PaymentInstrumentsApi
from .platform_api import PlatformApi
from .transaction_rules_api import TransactionRulesApi


class AdyenBalancePlatformApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(AdyenBalancePlatformApi, self).__init__(client=client)
        self.account_holders_api = AccountHoldersApi(client=client)
        self.balance_accounts_api = BalanceAccountsApi(client=client)
        self.payment_instrument_groups_api = PaymentInstrumentGroupsApi(client=client)
        self.payment_instruments_api = PaymentInstrumentsApi(client=client)
        self.platform_api = PlatformApi(client=client)
        self.transaction_rules_api = TransactionRulesApi(client=client)
