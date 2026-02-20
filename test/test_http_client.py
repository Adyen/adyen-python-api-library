from Adyen import settings

def test_user_agent_without_application_name(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "TEST_XAPI_KEY"
    # Mock the http_client.request method
    mock_client(200, {}, "test/mocks/checkout/paymentmethods-success.json")

    # Call a dummy API method
    _ = adyen_instance.checkout.payments_api.payment_methods({})

    # Assert that http_client.request was called with the correct headers
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{adyen_instance.checkout.payments_api.baseUrl}/paymentMethods',
        headers={
            'adyen-library-name': settings.LIB_NAME,
            'adyen-library-version': settings.LIB_VERSION,
            'User-Agent': settings.LIB_NAME + "/" + settings.LIB_VERSION
        },
        json={},
        xapikey='TEST_XAPI_KEY'
    )

def test_user_agent_with_application_name(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "TEST_XAPI_KEY"
    adyen_instance.client.application_name = "MyTestApp"

    # Mock the http_client.request method
    mock_client(200, {}, "test/mocks/checkout/paymentmethods-success.json")

    # Call a dummy API method
    _ = adyen_instance.checkout.payments_api.payment_methods({})

    # Assert that http_client.request was called with the correct headers
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{adyen_instance.checkout.payments_api.baseUrl}/paymentMethods',
        headers={
            'adyen-library-name': settings.LIB_NAME,
            'adyen-library-version': settings.LIB_VERSION,
            'User-Agent': "MyTestApp " + settings.LIB_NAME + "/" + settings.LIB_VERSION
        },
        json={},
        xapikey='TEST_XAPI_KEY'
    )
