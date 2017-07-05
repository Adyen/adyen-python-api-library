import Adyen
import mock
import json
from Adyen import httpclient

class BaseTest():

    def __init__(self, adyen):
        self.ady = adyen

    def create_client_from_file(self, filename):
        with open(filename) as data_file:
            data = json.load(data_file)
        strjson = open(filename).read()
        self.ady.client.http_client = httpclient.HTTPClient
        self.ady.client.http_init = True
        self.ady.client.http_client.request = mock.MagicMock(return_value=[strjson,1,200,data])
        mockclient = self.ady.client
        return mockclient
