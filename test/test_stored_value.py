import pytest

from Adyen import settings


@pytest.fixture
def stored_value_url(adyen_instance):
    return adyen_instance.storedValue.stored_value_api.baseUrl

def test_issue(adyen_instance, mock_client, stored_value_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        "store": "YOUR_STORE_ID",
        "paymentMethod": {
            "type": "valuelink"
        },
        "giftCardPromoCode": "1324",
        "reference": "YOUR_REFERENCE"
    }

    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/storedValue/issue-giftcard.json")
    result = adyen_instance.storedValue.stored_value_api.issue(request)
    assert result.message['paymentMethod']['type'] == 'givex'
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{stored_value_url}/issue',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )

def test_activate_giftcard(adyen_instance, mock_client, stored_value_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "status": "active",
        "amount": {
            "currency": "USD",
            "value": 1000
        },
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        "store": "YOUR_STORE_ID",
        "paymentMethod": {
            "type": "svs",
            "number": "6006491286999921374",
            "securityCode": "1111"
        },
        "reference": "YOUR_REFERENCE"
    }
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/storedValue/activate-giftcards.json")
    result = adyen_instance.storedValue.stored_value_api.change_status(request)
    assert result.message['currentBalance']['value'] == 1000
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{stored_value_url}/changeStatus',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )

def test_load_funds(adyen_instance, mock_client, stored_value_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "amount": {
            "currency": "USD",
            "value": 2000
        },
        "loadType": "merchandiseReturn",
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        "store": "YOUR_STORE_ID",
        "paymentMethod": {
            "type": "svs",
            "number": "6006491286999921374",
            "securityCode": "1111"
        },
        "reference": "YOUR_REFERENCE"
    }
    adyen_instance.client = mock_client(200, request, "test/mocks/storedValue/load-funds.json")
    result = adyen_instance.storedValue.stored_value_api.load(request)
    assert result.message['resultCode'] == 'Success'
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{stored_value_url}/load',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )

def test_check_balance(adyen_instance, mock_client, stored_value_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        "store": "YOUR_STORE_ID",
        "paymentMethod": {
            "type": "svs",
            "number": "603628672882001915092",
            "securityCode": "5754"
        },
        "reference": "YOUR_REFERENCE"
    }
    adyen_instance.client = mock_client(200, request, "test/mocks/storedValue/check-balance.json")
    result = adyen_instance.storedValue.stored_value_api.check_balance(request)
    assert result.message['currentBalance']['value'] == 5600
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{stored_value_url}/checkBalance',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )

def test_merge_balance(adyen_instance, mock_client, stored_value_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        "store": "YOUR_STORE_ID",
        "sourcePaymentMethod": {
            "number": "7777182708544835",
            "securityCode": "2329"
        },
        "paymentMethod": {
            "type": "valuelink",
            "number": "8888182708544836",
            "securityCode": "2330"
        },
        "reference": "YOUR_REFERENCE"
    }
    adyen_instance.client = mock_client(200, request, "test/mocks/storedValue/merge-balance.json")
    result = adyen_instance.storedValue.stored_value_api.merge_balance(request)
    assert result.message['pspReference'] == "881564657480267D"
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{stored_value_url}/mergeBalance',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )

def test_void_transaction(adyen_instance, mock_client, stored_value_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
        "originalReference": "851564654294247B",
        "reference": "YOUR_REFERENCE"
    }
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/storedValue/undo-transaction.json")
    result = adyen_instance.storedValue.stored_value_api.void_transaction(request)
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{stored_value_url}/voidTransaction',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )
