import pytest

from Adyen import settings


@pytest.fixture
def session_url(adyen_instance):
    return adyen_instance.sessionAuthentication.session_authentication_api.baseUrl

def test_create_session_token(adyen_instance, mock_client, session_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "allowOrigin": 'https://www.your-website.com',
        "product": "platform",
        "policy": {
            "resources": [
                {
                    "type": "accountHolder",
                    "accountHolderId": "AH00000000000000000000001"
                }
            ],
            "roles": [
                "Transactions Overview Component: View",
                "Payouts Overview Component: View"
            ]
        }
    }
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/sessionAuthentication/"
                                         "authentication-session-created.json")

    result = adyen_instance.sessionAuthentication.session_authentication_api.create_authentication_session(request)
    assert result.message["sessionToken"] == "long_session_token_string"
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{session_url}/sessions',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )
