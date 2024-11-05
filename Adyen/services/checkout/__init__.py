from ..base import AdyenServiceBase
from .donations_api import DonationsApi
from .modifications_api import ModificationsApi
from .orders_api import OrdersApi
from .payment_links_api import PaymentLinksApi
from .payments_api import PaymentsApi
from .recurring_api import RecurringApi
from .utility_api import UtilityApi


class AdyenCheckoutApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(AdyenCheckoutApi, self).__init__(client=client)
        self.donations_api = DonationsApi(client=client)
        self.modifications_api = ModificationsApi(client=client)
        self.orders_api = OrdersApi(client=client)
        self.payment_links_api = PaymentLinksApi(client=client)
        self.payments_api = PaymentsApi(client=client)
        self.recurring_api = RecurringApi(client=client)
        self.utility_api = UtilityApi(client=client)
