import pytest

from Adyen import settings


@pytest.fixture
def balance_platform_url(adyen_instance):
    return adyen_instance.balancePlatform.platform_api.baseUrl

def test_creating_balance_account(adyen_instance, mock_client, balance_platform_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "accountHolderId": "AH32272223222B59K6ZKBBFNQ",
        "description": "S.Hopper - Main balance account"
    }
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/configuration/"
                                         "balance-account-created.json")
    result = adyen_instance.balancePlatform.balance_accounts_api.create_balance_account(request)
    assert result.message['accountHolderId'] == 'AH32272223222B59K6ZKBBFNQ'
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{balance_platform_url}/balanceAccounts',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )

def test_creating_account_holder(adyen_instance, mock_client, balance_platform_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "description": "Liable account holder used for international payments and payouts",
        "reference": "S.Eller-001",
        "legalEntityId": "LE322JV223222D5GG42KN6869"
    }
    adyen_instance.client = mock_client(200, request, "test/mocks/configuration/"
                                                        "account-holder-created.json")
    result = adyen_instance.balancePlatform.account_holders_api.create_account_holder(request)
    assert result.message['legalEntityId'] == "LE322JV223222D5GG42KN6869"
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{balance_platform_url}/accountHolders',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )

def test_get_balance_platform(adyen_instance, mock_client, balance_platform_url):
    adyen_instance.client.xapikey = "YourXapikey"
    platform_id = "YOUR_BALANCE_PLATFORM"
    adyen_instance.client = mock_client(200, None, "test/mocks/configuration/"
                                                     "balance-platform-retrieved.json")
    result = adyen_instance.balancePlatform.platform_api.get_balance_platform(platform_id)
    assert result.message['id'] == platform_id
    adyen_instance.client.http_client.request.assert_called_once_with(
        'GET',
        f'{balance_platform_url}/balancePlatforms/{platform_id}',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=None,
        xapikey="YourXapikey"
    )

def test_creating_payment_instrument(adyen_instance, mock_client, balance_platform_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "type": "bankAccount",
        "description": "YOUR_DESCRIPTION",
        "balanceAccountId": "BA3227C223222B5CTBLR8BWJB",
        "issuingCountryCode": "NL"
    }
    adyen_instance.client = mock_client(200, request, "test/mocks/configuration/"
                                                        "business-account-created.json")
    result = adyen_instance.balancePlatform.payment_instruments_api.create_payment_instrument(request)
    assert result.message["balanceAccountId"] == "BA3227C223222B5CTBLR8BWJB"
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{balance_platform_url}/paymentInstruments',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )
