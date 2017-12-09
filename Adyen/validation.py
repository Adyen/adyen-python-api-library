from __future__ import absolute_import, division, unicode_literals

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
    # This function checks for missing properties in the request dict
    # for the corresponding action.

    if request:
        required_fields = actions[action]
        missing = []
        for field in required_fields:
            if "." in field:
                parent, child = field.split(".")
                if parent not in request or child not in request[parent]:
                    missing.append(field)
            elif field not in request:
                missing.append(field)
        if len(missing) > 0:
            missing_string = ""
            for idx, val in enumerate(missing):
                missing_string += "\n" + val
            erstr = "Provide the required request parameters to" \
                    " complete this request: %s" % missing_string
            raise ValueError(erstr)
        else:
            return True
    else:
        req_str = ""
        for idx, val in enumerate(actions[action]):
            req_str += "\n" + val
        erstr = "Provide a request dict with the following properties:" \
                " %s" % req_str
        raise ValueError(erstr)
