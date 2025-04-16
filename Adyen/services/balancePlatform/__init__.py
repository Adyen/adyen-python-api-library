from ..base import AdyenServiceBase
from .account_holders_api import AccountHoldersApi
from .balance_accounts_api import BalanceAccountsApi
from .balances_api import BalancesApi
from .bank_account_validation_api import BankAccountValidationApi
from .card_orders_api import CardOrdersApi
from .grant_accounts_api import GrantAccountsApi
from .grant_offers_api import GrantOffersApi
from .manage_sca_devices_api import ManageSCADevicesApi
from .manage_card_pin_api import ManageCardPINApi
from .network_tokens_api import NetworkTokensApi
from .payment_instrument_groups_api import PaymentInstrumentGroupsApi
from .payment_instruments_api import PaymentInstrumentsApi
from .platform_api import PlatformApi
from .transaction_rules_api import TransactionRulesApi
from .transfer_routes_api import TransferRoutesApi


class AdyenBalancePlatformApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(AdyenBalancePlatformApi, self).__init__(client=client)
        self.account_holders_api = AccountHoldersApi(client=client)
        self.balance_accounts_api = BalanceAccountsApi(client=client)
        self.balances_api = BalancesApi(client=client)
        self.bank_account_validation_api = BankAccountValidationApi(client=client)
        self.card_orders_api = CardOrdersApi(client=client)
        self.grant_accounts_api = GrantAccountsApi(client=client)
        self.grant_offers_api = GrantOffersApi(client=client)
        self.manage_sca_devices_api = ManageSCADevicesApi(client=client)
        self.manage_card_pin_api = ManageCardPINApi(client=client)
        self.network_tokens_api = NetworkTokensApi(client=client)
        self.payment_instrument_groups_api = PaymentInstrumentGroupsApi(client=client)
        self.payment_instruments_api = PaymentInstrumentsApi(client=client)
        self.platform_api = PlatformApi(client=client)
        self.transaction_rules_api = TransactionRulesApi(client=client)
        self.transfer_routes_api = TransferRoutesApi(client=client)
