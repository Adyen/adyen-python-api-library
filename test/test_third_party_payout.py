import pytest
import Adyen
from Adyen import settings

@pytest.fixture
def payout_url(adyen_instance):
    return adyen_instance.payout.initialization_api.baseUrl

def test_confirm_success(adyen_instance, mock_client, payout_url):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "merchantAccount": "YourMerchantAccount",
        "originalReference": "YourReference"
    }
    resp = 'test/mocks/payout/confirm-success.json'
    adyen_instance.client = mock_client(200, request, resp)
    result = adyen_instance.payout.reviewing_api.confirm_third_party(request)
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{payout_url}/confirmThirdParty',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        username='YourWSUser',
        password='YourWSPassword',
    )
    assert result.message['pspReference'] is not None
    assert result.message['resultCode'] == "[payout-confirm-received]"

def test_confirm_missing_reference(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "merchantAccount": "YourMerchantAccount",
        "originalReference": ""
    }
    resp = 'test/mocks/payout/confirm-missing-reference.json'
    adyen_instance.client = mock_client(500, request, resp)
    with pytest.raises(Adyen.AdyenAPICommunicationError) as excinfo:
        adyen_instance.payout.reviewing_api.confirm_third_party(request)
    assert "Required field 'merchantAccount' is null" in str(excinfo.value)

def test_decline_success(adyen_instance, mock_client, payout_url):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "merchantAccount": "YourMerchantAccount",
        "originalReference": "YourReference"
    }
    resp = 'test/mocks/payout/decline-success.json'
    adyen_instance.client = mock_client(200, request, resp)
    result = adyen_instance.payout.reviewing_api.decline_third_party(request)
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{payout_url}/declineThirdParty',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        username='YourWSUser',
        password='YourWSPassword',
    )
    assert result.message['pspReference'] is not None
    assert result.message['resultCode'] == "[payout-decline-received]"

def test_decline_missing_reference(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "merchantAccount": "YourMerchantAccount",
        "originalReference": ""
    }
    resp = 'test/mocks/payout/decline-missing-reference.json'
    adyen_instance.client = mock_client(500, request, resp)
    with pytest.raises(Adyen.AdyenAPICommunicationError) as excinfo:
        adyen_instance.payout.reviewing_api.confirm_third_party(request)
    assert "Required field 'merchantAccount' is null" in str(excinfo.value)

def test_store_detail_bank_success(adyen_instance, mock_client, payout_url):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "bank": {
            "bankName": "AbnAmro",
            "bic": "ABNANL2A",
            "countryCode": "NL",
            "iban": "NL32ABNA0515071439",
            "ownerName": "Adyen",
            "bankCity": "Amsterdam",
            "taxId": "bankTaxId"
        },
        "merchantAccount": "YourMerchantAccount",
        "recurring": {
            "contract": "PAYOUT"
        },
        "shopperEmail": "ref@email.com",
        "shopperReference": "ref"
    }
    resp = 'test/mocks/payout/storeDetail-success.json'
    adyen_instance.client = mock_client(200, request, resp)
    result = adyen_instance.payout.initialization_api.store_detail(request)
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{payout_url}/storeDetail',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        username='YourWSUser',
        password='YourWSPassword'
    )
    assert result.message['pspReference'] is not None
    assert result.message['recurringDetailReference'] is not None
    assert result.message['resultCode'] == "Success"

def test_submit_success(adyen_instance, mock_client, payout_url):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "amount": {
            "value": "100000",
            "currency": "EUR"
        },
        "reference": "payout-test", "recurring": {
            "contract": "PAYOUT"
        },
        "merchantAccount": "YourMerchantAccount",
        "shopperEmail": "ref@email.com",
        "shopperReference": "ref",
        "selectedRecurringDetailReference": "LATEST"
    }
    resp = 'test/mocks/payout/submit-success.json'
    adyen_instance.client = mock_client(200, request, resp)
    result = adyen_instance.payout.initialization_api.submit_third_party(request)
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{payout_url}/submitThirdParty',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        username='YourWSUser',
        password='YourWSPassword'
    )
    assert result.message['pspReference'] is not None
    assert result.message['resultCode'] == "[payout-submit-received]"

def test_submit_invalid_recurring_reference(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "amount": {
            "value": "100000",
            "currency": "EUR"
        },
        "reference": "payout-test", "recurring": {
            "contract": "PAYOUT"
        },
        "merchantAccount": "YourMerchantAccount",
        "shopperEmail": "ref@email.com",
        "shopperReference": "ref",
        "selectedRecurringDetailReference": "1234"
    }
    resp = 'test/mocks/payout/submit-invalid-reference.json'
    adyen_instance.client = mock_client(422, request, resp)
    with pytest.raises(Adyen.AdyenAPIUnprocessableEntity) as excinfo:
        adyen_instance.payout.initialization_api.submit_third_party(request)
    assert "Contract not found" in str(excinfo.value)

def test_store_detail_and_submit_missing_reference(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "amount": {
            "value": "100000",
            "currency": "EUR"
        },
        "merchantAccount": "YourMerchantAccount",
        "recurring": {
            "contract": "PAYOUT"
        },
        "shopperEmail": "ref@email.com",
        "shopperReference": "ref",
        "bank": {
            "iban": "NL32ABNA0515071439",
            "ownerName": "Adyen",
            "countryCode": "NL",
        }
    }

    resp = 'test/mocks/payout/submit-missing-reference.json'
    adyen_instance.client = mock_client(422, request, resp)

    with pytest.raises(Adyen.AdyenAPIUnprocessableEntity) as excinfo:
        adyen_instance.payout.initialization_api.store_detail_and_submit_third_party(request)
    assert "Contract not found" in str(excinfo.value)

def test_store_detail_and_submit_missing_payment(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "amount": {
            "value": "100000",
            "currency": "EUR"
        },
        "merchantAccount": "YourMerchantAccount",
        "reference": "payout-test",
        "recurring": {
            "contract": "PAYOUT"
        },
        "shopperEmail": "ref@email.com",
        "shopperReference": "ref"
    }
    resp = 'test/mocks/payout/storeDetailAndSubmit-missing-payment.json'
    adyen_instance.client = mock_client(422, request, resp)
    with pytest.raises(Adyen.AdyenAPIUnprocessableEntity) as excinfo:
        adyen_instance.payout.initialization_api.store_detail_and_submit_third_party(request)
    assert "Please supply paymentDetails" in str(excinfo.value)

def test_store_detail_and_submit_invalid_iban(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "amount": {
            "value": "100000",
            "currency": "EUR"
        },
        "merchantAccount": "YourMerchantAccount",
        "reference": "payout-test",
        "recurring": {
            "contract": "PAYOUT"
        },
        "shopperEmail": "ref@email.com",
        "shopperReference": "ref",
        "bank": {
            "countryCode": "NL",
            "iban": "4111111111111111",
            "ownerName": "Adyen",
        }
    }
    resp = 'test/mocks/payout/storeDetailAndSubmit-invalid-iban.json'
    adyen_instance.client = mock_client(422, request, resp)
    with pytest.raises(Adyen.AdyenAPIUnprocessableEntity) as excinfo:
        adyen_instance.payout.initialization_api.store_detail_and_submit_third_party(request)
    assert "Invalid iban" in str(excinfo.value)

def test_store_detail_and_submit_card_success(adyen_instance, mock_client, payout_url):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "amount": {
            "value": "100000",
            "currency": "EUR"
        },
        "merchantAccount": "YourMerchantAccount",
        "reference": "payout-test",
        "recurring": {
            "contract": "PAYOUT"
        },
        "shopperEmail": "ref@email.com",
        "shopperReference": "ref",
        "card": {
            "number": "4111111111111111",
            "expiryMonth": "08",
            "expiryYear": "2018",
            "cvc": "737",
            "holderName": "John Smith"
        }
    }
    resp = 'test/mocks/payout/storeDetailAndSubmit-card-success.json'
    adyen_instance.client = mock_client(200, request, resp)
    result = adyen_instance.payout.initialization_api.store_detail_and_submit_third_party(request)
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{payout_url}/storeDetailAndSubmitThirdParty',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        username='YourWSUser',
        password='YourWSPassword'
    )
    assert result.message['pspReference'] is not None
    assert result.message['resultCode'] == "[payout-submit-received]"

def test_store_detail_and_submit_bank_success(adyen_instance, mock_client, payout_url):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "amount": {
            "value": "100000",
            "currency": "EUR"
        },
        "bank": {
            "countryCode": "NL",
            "iban": "NL32ABNA0515071439",
            "ownerName": "Adyen",
        },
        "merchantAccount": "YourMerchantAccount",
        "recurring": {
            "contract": "PAYOUT"
        },
        "reference": "YourReference",
        "shopperEmail": "ref@email.com",
        "shopperReference": "ref"
    }
    resp = 'test/mocks/payout/storeDetailAndSubmit-bank-success.json'
    adyen_instance.client = mock_client(200, request, resp)
    result = adyen_instance.payout.initialization_api.store_detail_and_submit_third_party(request)
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{payout_url}/storeDetailAndSubmitThirdParty',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        username='YourWSUser',
        password='YourWSPassword'
    )
    assert result.message['pspReference'] is not None
    assert result.message['resultCode'] == "[payout-submit-received]"
