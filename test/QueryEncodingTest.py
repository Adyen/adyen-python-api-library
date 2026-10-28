import unittest
from unittest.mock import Mock
from urllib.parse import parse_qs, urlsplit

import Adyen
from Adyen.util import get_query


class TestQueryEncoding(unittest.TestCase):
    def test_reserved_characters_round_trip(self):
        parameters = {
            "reference": "Invoice A&B + 10% #café",
            "filter[key]&name": "x=y?z/1",
            "empty": "",
            "pageNumber": 0,
        }
        encoded = get_query(parameters)
        self.assertEqual(
            parse_qs(urlsplit("https://example.test/" + encoded).query, keep_blank_values=True),
            {key: [str(value)] for key, value in parameters.items()},
        )
        self.assertEqual(urlsplit("https://example.test/" + encoded).fragment, "")

    def test_public_service_preserves_query_values(self):
        adyen = Adyen.Adyen()
        adyen.client.platform = "test"
        adyen.client.xapikey = "test-api-key"
        adyen.client._init_http_client()
        request = Mock(return_value=["{}", {}, 200, {}])
        adyen.client.http_client.request = request
        parameters = {"reference": "A&B + # café", "pageNumber": 3}
        adyen.checkout.payments_api.payment_methods(
            {"merchantAccount": "test-merchant"}, query_parameters=parameters
        )
        url = request.call_args.args[1]
        self.assertEqual(
            parse_qs(urlsplit(url).query),
            {"reference": ["A&B + # café"], "pageNumber": ["3"]},
        )
        self.assertEqual(parameters, {"reference": "A&B + # café", "pageNumber": 3})

    def test_empty_query_keeps_existing_output(self):
        self.assertEqual(get_query({}), "?")
