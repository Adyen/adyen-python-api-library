import pytest


@pytest.fixture
def checkout_utility_url(adyen_instance):
    return adyen_instance.checkout.utility_api.baseUrl

def test_origin_keys_success_mocked(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "originDomains": [
            "https://www.your-domain1.com",
            "https://www.your-domain2.com",
            "https://www.your-domain3.com"
        ]
    }

    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/"
                                         "checkoututility/"
                                         "originkeys"
                                         "-success.json")
    result = adyen_instance.checkout.utility_api.origin_keys(request)

    assert result.message['originKeys']['https://www.your-domain1.com'] == \
           "pub.v2.7814286629520534.aHR0cHM6Ly93d3cu" \
           "eW91ci1kb21haW4xLmNvbQ.UEwIBmW9-c_uXo5wS" \
           "Er2w8Hz8hVIpujXPHjpcEse3xI"

    assert result.message['originKeys']['https://www.your-domain3.com'] == \
           "pub.v2.7814286629520534.aHR0cHM6Ly93d3cu" \
           "eW91ci1kb21haW4zLmNvbQ.fUvflu-YIdZSsLEH8" \
           "Qqmr7ksE4ag_NYiiMXK0s6aq_4"

    assert result.message['originKeys']['https://www.your-domain2.com'] == \
           "pub.v2.7814286629520534.aHR0cHM6Ly93d3cue" \
           "W91ci1kb21haW4yLmNvbQ.EP6eXBJKk0t7-QIUl6e_" \
           "b1qMuMHGepxG_SlUqxAYrfY"

def test_checkout_utility_api_url_custom(adyen_instance, checkout_utility_url):
    url = adyen_instance.client._determine_api_url("test", checkout_utility_url + "/originKeys")
    assert url == f"{checkout_utility_url}/originKeys"

def test_applePay_session(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
      "displayName": "YOUR_MERCHANT_NAME",
      "domainName": "YOUR_DOMAIN_NAME",
      "merchantIdentifier": "YOUR_MERCHANT_ID"
    }
    adyen_instance.client = mock_client(200, request, "test/mocks/"
                                                         "checkoututility/"
                                                         "applepay-sessions"
                                                         "-success.json")
    result = adyen_instance.checkout.utility_api.get_apple_pay_session(request)
    assert result.message['data'] == "BASE_64_ENCODED_DATA"
