import pytest

from Adyen import settings


@pytest.fixture
def lem_url(adyen_instance):
    return adyen_instance.legalEntityManagement.legal_entities_api.baseUrl

def test_creating_legal_entity(adyen_instance, mock_client, lem_url):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        "type": "individual",
        "individual": {
            "residentialAddress": {
                "city": "Amsterdam",
                "country": "NL",
                "postalCode": "1011DJ",
                "street": "Simon Carmiggeltstraat 6 - 50"
            },
            "name": {
                "firstName": "Shelly",
                "lastName": "Eller"
            },
            "birthData": {
                "dateOfBirth": "1990-06-21"
            },
            "email": "s.eller@example.com"
        }
    }
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/legalEntityManagement/"
                                         "individual_legal_entity_created.json")
    result = adyen_instance.legalEntityManagement.legal_entities_api.create_legal_entity(request)
    assert result.message['individual']['name']['firstName'] == 'Shelly'
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{lem_url}/legalEntities',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )

def test_get_transfer_instrument(adyen_instance, mock_client, lem_url):
    adyen_instance.client.xapikey = "YourXapikey"
    instrumentId = "SE322JV223222F5GNXSR89TMW"
    adyen_instance.client = mock_client(200, None, "test/mocks/legalEntityManagement/"
                                                     "details_of_trainsfer_instrument.json")
    result = adyen_instance.legalEntityManagement.transfer_instruments_api.get_transfer_instrument(instrumentId)
    assert result.message['id'] == instrumentId
    adyen_instance.client.http_client.request.assert_called_once_with(
        'GET',
        f'{lem_url}/transferInstruments/{instrumentId}',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=None,
        xapikey="YourXapikey"
    )

def test_update_business_line(adyen_instance, mock_client, lem_url):
    adyen_instance.client.xapikey = "YourXapikey"
    businessLineId = "SE322JV223222F5GVGMLNB83F"
    request = {
        "industryCode": "55",
        "webData": [
            {
                "webAddress": "https://www.example.com"
            }
        ]
    }
    adyen_instance.client = mock_client(200, request, "test/mocks/legalEntityManagement/"
                                                        "business_line_updated.json")
    result = adyen_instance.legalEntityManagement.business_lines_api.update_business_line(request, businessLineId)
    assert result.message['id'] == businessLineId
    adyen_instance.client.http_client.request.assert_called_once_with(
        'PATCH',
        f'{lem_url}/businessLines/{businessLineId}',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )

def test_accept_terms_of_service(adyen_instance, mock_client, lem_url):
    adyen_instance.client.xapikey = "YourXapikey"
    legalEntityId = "legalId"
    documentId = "documentId"
    request = {
        'acceptedBy': "UserId",
        'ipAddress': "UserIpAddress"
    }
    adyen_instance.client = mock_client(204, request)
    adyen_instance.legalEntityManagement.terms_of_service_api.accept_terms_of_service(request, legalEntityId,
                                                                                  documentId)
    adyen_instance.client.http_client.request.assert_called_once_with(
        'PATCH',
        f'{lem_url}/legalEntities/{legalEntityId}/termsOfService/{documentId}',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )
