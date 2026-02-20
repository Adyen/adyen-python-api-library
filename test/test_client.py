def test_client_initialization(adyen_instance):
    assert adyen_instance.client.platform == "test"
    assert adyen_instance.client.http_timeout == 30

def test_client_credentials(adyen_instance):
    adyen_instance.client.xapikey = "YOUR_API_KEY"
    assert adyen_instance.client.xapikey == "YOUR_API_KEY"
