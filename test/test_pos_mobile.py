def test_create_communication_session(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {}
    adyen_instance.client = mock_client(
        200,
        request,
        "test/mocks/posMobile/create-communication-session-success.json"
    )
    result = adyen_instance.posMobile.pos_mobile_api.create_communication_session(request)
    assert result.message['id'] == "CS00000000000000000000001"
    assert result.message['sessionData'] == "session_data_example"
