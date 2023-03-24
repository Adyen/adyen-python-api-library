
try:
    import mock
except Exception:
    from unittest import mock
import json
from Adyen import httpclient


class BaseTest():
    def __init__(self, adyen):
        self.ady = adyen

    def create_client_from_file(self, status, request, filename=None):
        if filename:
            with open(filename) as data_file:
                data = json.load(data_file)
                st = open(filename)
                strjson = st.read()
        else:
            data = {}
            st = ""
            strjson = ""

        self.ady.client.http_client = httpclient.HTTPClient
        self.ady.client.http_init = True
        self.ady.client.http_client.request = mock.MagicMock(
            return_value=[strjson, request, status, data])

        mockclient = self.ady.client
        if st:
            st.close()
        return mockclient
