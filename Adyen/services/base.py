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