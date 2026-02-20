import pytest

from Adyen import settings


@pytest.fixture
def terminal_url(adyen_instance):
    return adyen_instance.terminal.baseUrl

def test_assign_terminals(adyen_instance, mock_client, terminal_url):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    adyen_instance.client.platform = "test"
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "companyAccount": "YOUR_COMPANY_ACCOUNT",
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        "store": "YOUR_STORE",
        "terminals": [
            "P400Plus-275479597"
        ]
    }
    mock_client(
        200, request, "test/mocks/terminal/assignTerminals.json"
    )
    result = adyen_instance.terminal.assign_terminals(request=request)
    assert "P400Plus-275479597" in result.message["results"]

    adyen_instance.client.http_client.request.assert_called_once_with(
        "POST",
        f"{terminal_url}/assignTerminals",
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json={
            "companyAccount": "YOUR_COMPANY_ACCOUNT",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "store": "YOUR_STORE",
            "terminals": [
                "P400Plus-275479597"
            ]
        },
        xapikey="YourXapikey"
    )

def test_assign_terminals_422(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "companyAccount": "YOUR_COMPANY_ACCOUNT",
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        "store": "YOUR_STORE",
        "terminals": [
            "P400Plus-123456789"
        ]
    }
    mock_client(
        200, request, "test/mocks/terminal/assignTerminals-422.json"
    )
    result = adyen_instance.terminal.assign_terminals(request=request)
    assert result.message["status"] == 422
    assert result.message["errorCode"] == "000"
    assert result.message["message"] == "Terminals not found: P400Plus-123456789"
    assert result.message["errorType"] == "validation"

def test_find_terminal(adyen_instance, mock_client, terminal_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "terminal": "P400Plus-275479597",
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
    }
    mock_client(
        200, request, "test/mocks/terminal/findTerminal.json"
    )
    result = adyen_instance.terminal.find_terminal(request=request)
    assert "P400Plus-275479597" in result.message["terminal"]

    adyen_instance.client.http_client.request.assert_called_once_with(
        "POST",
        f"{terminal_url}/findTerminal",
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json={
            "terminal": "P400Plus-275479597",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        },
        xapikey="YourXapikey"
    )

def test_find_terminal_422(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "terminal": "P400Plus-123456789"
    }
    mock_client(
        200, request, "test/mocks/terminal/findTerminal-422.json"
    )
    result = adyen_instance.terminal.find_terminal(request=request)
    assert result.message["status"] == 422
    assert result.message["errorCode"] == "000"
    assert result.message["message"] == "Terminal not found"
    assert result.message["errorType"] == "validation"

def test_get_stores_under_account(adyen_instance, mock_client, terminal_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "companyAccount": "YOUR_COMPANY_ACCOUNT",
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
    }
    mock_client(
        200, request, "test/mocks/terminal/getStoresUnderAccount.json"
    )
    result = adyen_instance.terminal.get_stores_under_account(request=request)
    assert result.message["stores"] == [
        {
            "store": "YOUR_STORE",
            "description": "YOUR_STORE",
            "address": {
                "city": "The City",
                "countryCode": "NL",
                "postalCode": "1234",
                "streetAddress": "The Street"
            },
            "status": "Active",
            "merchantAccountCode": "YOUR_MERCHANT_ACCOUNT"
        }
    ]

    adyen_instance.client.http_client.request.assert_called_once_with(
        "POST",
        f"{terminal_url}/getStoresUnderAccount",
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json={
           "companyAccount": "YOUR_COMPANY_ACCOUNT",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        },
        xapikey="YourXapikey"
    )

def test_get_terminal_details(adyen_instance, mock_client, terminal_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "terminal": "P400Plus-275479597",
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
    }

    mock_client(
        200, request, "test/mocks/terminal/getTerminalDetails.json"
    )
    result = adyen_instance.terminal.get_terminal_details(request=request)

    assert result.message["deviceModel"] == "P400Plus"
    assert result.message["terminal"] == "P400Plus-275479597"

    adyen_instance.client.http_client.request.assert_called_once_with(
        "POST",
        f"{terminal_url}/getTerminalDetails",
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json={
            "terminal": "P400Plus-275479597",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        },
        xapikey="YourXapikey"
    )

def test_get_terminal_details_422(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "terminal": "P400Plus-123456789"
    }
    mock_client(
        200, request, "test/mocks/terminal/getTerminalDetails-422.json"
    )
    result = adyen_instance.terminal.get_terminal_details(request=request)
    assert result.message["status"] == 422
    assert result.message["errorCode"] == "000"
    assert result.message["message"] == "Terminal not found"
    assert result.message["errorType"] == "validation"

def test_get_terminals_under_account(adyen_instance, mock_client, terminal_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "companyAccount": "YOUR_COMPANY_ACCOUNT",
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
    }

    mock_client(
        200, request, "test/mocks/terminal/getTerminalsUnderAccount.json"
    )
    result = adyen_instance.terminal.get_terminals_under_account(request=request)

    assert result.message["merchantAccounts"] == [
        {
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "inStoreTerminals": [
                "P400Plus-275479597"
            ],
            "stores": [
                {
                    "store": "YOUR_STORE",
                    "inStoreTerminals": [
                        "M400-401972715"
                    ]
                }
            ]
        }
    ]

    adyen_instance.client.http_client.request.assert_called_once_with(
        "POST",
        f"{terminal_url}/getTerminalsUnderAccount",
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json={
            "companyAccount": "YOUR_COMPANY_ACCOUNT",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        },
        xapikey="YourXapikey"
    )

def test_get_terminals_under_account_store(adyen_instance, mock_client, terminal_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "companyAccount": "YOUR_COMPANY_ACCOUNT",
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        "store": "YOUR_STORE"
    }

    mock_client(
        200, request, "test/mocks/terminal/getTerminalsUnderAccount-store.json"
    )
    result = adyen_instance.terminal.get_terminals_under_account(request=request)

    assert result.message["merchantAccounts"] == [
        {
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "stores": [
                {
                    "store": "YOUR_STORE",
                    "inStoreTerminals": [
                        "M400-401972715"
                    ]
                }
            ]
        }
    ]

    adyen_instance.client.http_client.request.assert_called_once_with(
        "POST",
        f"{terminal_url}/getTerminalsUnderAccount",
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json={
            "companyAccount": "YOUR_COMPANY_ACCOUNT",
            "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
            "store": "YOUR_STORE",
        },
        xapikey="YourXapikey"
    )
