import pytest

from Adyen import settings


@pytest.fixture
def transfers_url(adyen_instance):
    return adyen_instance.transfers.transfers_api.baseUrl

def test_transfer_fund(adyen_instance, mock_client, transfers_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "amount": {
            "value": 110000,
            "currency": "EUR"
        },
        "balanceAccountId": "BAB8B2C3D4E5F6G7H8D9J6GD4",
        "category": "bank",
        "counterparty": {
            "bankAccount": {
                "accountHolder": {
                    "fullName": "A. Klaassen",
                    "address": {
                        "city": "San Francisco",
                        "country": "US",
                        "postalCode": "94678",
                        "stateOrProvince": "CA",
                        "street": "Brannan Street",
                        "street2": "274"
                    }
                }
            },
            "accountIdentification": {
                "type": "numberAndBic",
                "accountNumber": "123456789",
                "bic": "BOFAUS3NXXX"
            }
        },
        "priority": "wire",
        "referenceForBeneficiary": "Your reference sent to the beneficiary",
        "reference": "Your internal reference for the transfer",
        "description": "Your description for the transfer"
    }
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/transfers/"
                                         "make-transfer-response.json")
    result = adyen_instance.transfers.transfers_api.transfer_funds(request)

    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{transfers_url}/transfers',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )

def test_get_all_transactions(adyen_instance, mock_client, transfers_url):
    adyen_instance.client.xapikey = "YourXapikey"
    adyen_instance.client = mock_client(200, None, "test/mocks/transfers/"
                                                     "get-all-transactions.json")

    result = adyen_instance.transfers.transactions_api.get_all_transactions()
    adyen_instance.client.http_client.request.assert_called_once_with(
        'GET',
        f'{transfers_url}/transactions',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=None,
        xapikey="YourXapikey"
    )

def test_get_transaction(adyen_instance, mock_client, transfers_url):
    adyen_instance.client.xapikey = "YourXapikey"
    transacion_id="123"
    adyen_instance.client = mock_client(200, None, "test/mocks/transfers/"
                                                     "get-transaction.json")
    result = adyen_instance.transfers.transactions_api.get_transaction(transacion_id)
    adyen_instance.client.http_client.request.assert_called_once_with(
        'GET',
        f'{transfers_url}/transactions/{transacion_id}',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=None,
        xapikey="YourXapikey"
    )
