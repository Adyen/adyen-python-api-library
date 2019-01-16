from __future__ import absolute_import, division, unicode_literals
import re

actions = {}
actions['listRecurringDetails'] = ["shopperReference"]
actions['disable'] = ["shopperReference"]
actions['directory'] = ["currencyCode", "paymentAmount",
                        "merchantReference", "sessionValidity"]
actions['skipDetails'] = ["sessionValidity", "currencyCode", "paymentAmount",
                          "merchantReference", "brandCode", "issuerId"]
actions['select'] = ["sessionValidity", "currencyCode",
                     "paymentAmount", "merchantReference"]
actions['authorise'] = ["amount", "reference"]
actions['authorise3d'] = ["md", "paResponse", "browserInfo"]
actions['cancel'] = ["originalReference"]
actions['capture'] = ["modificationAmount", "originalReference"]
actions['refund'] = ["modificationAmount", "originalReference"]
actions['cancelOrRefund'] = ["originalReference"]

actions['paymentMethods'] = ["merchantAccount"]
actions['payments'] = ["amount", "reference", "paymentMethod",
                       "merchantAccount", "returnUrl"]
actions['paymentsDetails'] = ["paymentData", "details"]
actions['paymentSession'] = ["amount", "reference", "shopperReference",
                             "channel", "returnUrl", "countryCode",
                             "shopperLocale", "sessionValidity",
                             "merchantAccount"]
actions['paymentsResult'] = ["payload"]
actions['originKeys'] = ["originDomains"]

payout_required_fields = {
    'confirmThirdParty': (
        'merchantAccount',
        'originalReference'
    ),
    'declineThirdParty': (
        'merchantAccount',
        'originalReference'
    ),
    'storeDetail': (
        'merchantAccount',
        'recurring.contract',
    ),
    'submitThirdParty': (
        'amount.currency',
        'amount.value',
        'merchantAccount',
        'recurring.contract',
        'reference',
        'shopperEmail',
        'shopperReference',
        'selectedRecurringDetailReference'
    ),
    'storeDetailAndSubmitThirdParty': (
        'amount.currency',
        'amount.value',
        'merchantAccount',
        'recurring.contract',
        'reference',
        'shopperEmail',
        'shopperReference',
    )
}

actions.update(payout_required_fields)


def check_in(request, action):
    """This function checks for missing properties in the request dict
    for the corresponding action."""
    if not request:
        req_str = ""
        for idx, val in enumerate(actions[action]):
            req_str += "\n" + val
        erstr = "Provide a request dict with the following properties:" \
                " %s" % req_str
        raise ValueError(erstr)

    required_fields = actions[action]
    missing = []
    for field in required_fields:
        if not is_key_present(request, field):
            missing.append(field)
    if missing:
        missing_string = ""
        for idx, val in enumerate(missing):
            missing_string += "\n" + val
        erstr = "Provide the required request parameters to" \
                " complete this request: %s" % missing_string
        raise ValueError(erstr)

    return True


def is_key_present(request, key):
    m = re.search(r'([^\.]+)\.(.+)', key)
    if m:
        parent_key = m.group(1)
        child_key = m.group(2)
        if parent_key in request:
            return is_key_present(request[parent_key], child_key)
    elif key in request:
        return True
    return False
