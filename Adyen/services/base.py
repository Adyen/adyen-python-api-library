from urllib.parse import quote

from Adyen import AdyenClient
from Adyen.exceptions import AdyenInvalidRequestError


class AdyenBase:
    def __setattr__(self, attr, value):
        client_attr = ["username", "password", "platform"]
        if attr in client_attr:
            if value:
                self.client[attr] = value
        else:
            super().__setattr__(attr, value)

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

    @staticmethod
    def _build_path(template, /, **path_params):
        """Fill in the path parameters of an endpoint template.

        Each value is percent-encoded so it always stays a single path segment:
        '/', '?' and '#' in an id can no longer change the path or the query string.
        """
        return template.format(
            **{name: _encode_path_segment(name, value) for name, value in path_params.items()}
        )


def _encode_path_segment(name, value):
    segment = quote(str(value), safe="")
    if segment in (".", ".."):
        # requests and pycurl resolve these as dot segments, even when percent-encoded
        raise AdyenInvalidRequestError(f"Path parameter '{name}' cannot be '{segment}'")
    return segment
