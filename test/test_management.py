import pytest

from Adyen import settings


@pytest.fixture
def management_url(adyen_instance):
    return adyen_instance.management.my_api_credential_api.baseUrl

def test_get_company_account(adyen_instance, mock_client, management_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = None
    company_id = "YOUR_COMPANY_ACCOUNT"
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/"
                                         "management/"
                                         "get_company_account"
                                         ".json")

    result = adyen_instance.management.account_company_level_api.get_company_account(companyId=company_id)

    assert result.message['id'] == company_id
    adyen_instance.client.http_client.request.assert_called_once_with(
        'GET',
        f'{management_url}/companies/{company_id}',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=None,
        xapikey="YourXapikey"
    )

def test_my_api_credential_api(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {"domain": "YOUR_DOMAIN"}
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/"
                                         "management/"
                                         "post_me_allowed"
                                         "_origins.json")

    result = adyen_instance.management.my_api_credential_api.add_allowed_origin(request)

    assert result.message['domain'] == "YOUR_DOMAIN"

def test_no_content(adyen_instance, mock_client, management_url):
    adyen_instance.client.xapikey = "YourXapikey"
    adyen_instance.client = mock_client(204, {},
                                         "test/mocks/"
                                         "management/"
                                         "no_content.json")
    origin_id = 'YOUR_DOMAIN_ID'

    adyen_instance.management.my_api_credential_api.remove_allowed_origin(origin_id)

    adyen_instance.client.http_client.request.assert_called_once_with(
        'DELETE',
        f'{management_url}/me/allowedOrigins/{origin_id}',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=None,
        xapikey="YourXapikey"
    )

def test_update_store(adyen_instance, mock_client, management_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "address": {
            "line1": "1776 West Pinewood Avenue",
            "line2": "Heartland Building",
            "line3": "",
            "postalCode": "20251"
        }
    }
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/"
                                         "management/"
                                         "update_a_store"
                                         ".json")
    store_id = "YOUR_STORE_ID"
    merchant_id = "YOUR_MERCHANT_ACCOUNT_ID"

    result = adyen_instance.management.account_store_level_api.update_store(request, merchant_id, store_id)

    adyen_instance.client.http_client.request.assert_called_once_with(
        'PATCH',
        f'{management_url}/merchants/{merchant_id}/stores/{store_id}',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )
    assert result.message['id'] == store_id
    assert result.message['address']['line1'] == "1776 West Pinewood Avenue"

def test_reassign_terminal(adyen_instance, mock_client, management_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        'storeId': 'ST123ABC',
        'inventory': False,
    }
    adyen_instance.client = mock_client(200, request)
    terminal_id = "AMS1-2345"

    result = adyen_instance.management.terminals_terminal_level_api.reassign_terminal(request, terminal_id)

    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{management_url}/terminals/{terminal_id}/reassign',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )
    assert result.status_code == 200
    assert result.message == {}

