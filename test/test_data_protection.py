import pytest

from Adyen import settings


@pytest.fixture
def data_protection_url(adyen_instance):
    return adyen_instance.dataProtection.data_protection_api.baseUrl

def test_data_erasure(adyen_instance, mock_client, data_protection_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        "pspReference": "9915520502347613",
        "forceErasure": True
    }
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/dataProtection/erasure-response.json")
    result = adyen_instance.dataProtection.data_protection_api.request_subject_erasure(request)
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{data_protection_url}'
        '/requestSubjectErasure',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        xapikey="YourXapikey",
        json=request
    )
    assert result.message["result"] == "SUCCESS"
