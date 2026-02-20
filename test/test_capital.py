def test_request_grant(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {}
    adyen_instance.client = mock_client(
        200,
        request,
        "test/mocks/capital/grants-success.json"
    )
    result = adyen_instance.capital.grants_api.request_grant(request)
    assert len(result.message['grants']) == 1
    assert result.message['grants'][0]['id'] == "GR00000000000000000000001"

def test_get_all_grant_offers(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {}
    adyen_instance.client = mock_client(
        200,
        request,
        "test/mocks/capital/grant-offers-success.json"
    )
    result = adyen_instance.capital.grant_offers_api.get_all_grant_offers(request)
    assert len(result.message['grantOffers']) == 1
    assert result.message['grantOffers'][0]['id'] == "GO00000000000000000000001"

def test_get_all_grants(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {}
    adyen_instance.client = mock_client(
        200,
        request,
        "test/mocks/capital/grants-success.json"
    )
    result = adyen_instance.capital.grants_api.get_all_grants(counterparty_account_holder_id="AH00000000000000000000001")
    assert len(result.message['grants']) == 1
    assert result.message['grants'][0]['id'] == "GR00000000000000000000001"

def test_get_grant(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {}
    adyen_instance.client = mock_client(
        200,
        request,
        "test/mocks/capital/get-grant-success.json"
    )
    result = adyen_instance.capital.grants_api.get_grant(grantId="GR00000000000000000000001")
    assert result.message['id'] == "GR00000000000000000000001"

def test_get_all_grant_disbursements(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {}
    adyen_instance.client = mock_client(
        200,
        request,
        "test/mocks/capital/get-grant-disbursements-success.json"
    )
    result = adyen_instance.capital.grants_api.get_all_grant_disbursements(grantId="GR00000000000000000000001")
    assert len(result.message['disbursements']) == 1
    assert result.message['disbursements'][0]['id'] == "DI00000000000000000000001"

def test_get_grant_disbursement(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {}
    adyen_instance.client = mock_client(
        200,
        request,
        "test/mocks/capital/get-grant-disbursement-success.json"
    )
    result = adyen_instance.capital.grants_api.get_grant_disbursement(grantId="GR00000000000000000000001",
                                                                       disbursementId="DI00000000000000000000001")
    assert result.message['id'] == "DI00000000000000000000001"

def test_update_grant_disbursement(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {}
    adyen_instance.client = mock_client(
        200,
        request,
        "test/mocks/capital/update-grant-disbursement-success.json"
    )
    result = adyen_instance.capital.grants_api.update_grant_disbursement(request, grantId="GR00000000000000000000001",
                                                                          disbursementId="DI00000000000000000000001")
    assert result.message['repayment']['basisPoints'] == 1500

def test_get_grant_account_information(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {}
    adyen_instance.client = mock_client(
        200,
        request,
        "test/mocks/capital/get-grant-account-success.json"
    )
    result = adyen_instance.capital.grant_accounts_api.get_grant_account_information(id="CG00000000000000000000001")
    assert result.message['id'] == "CG00000000000000000000001"

def test_get_grant_offer(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {}
    adyen_instance.client = mock_client(
        200,
        request,
        "test/mocks/capital/get-grant-offer-success.json"
    )
    result = adyen_instance.capital.grant_offers_api.get_grant_offer(id="GO00000000000000000000001")
    assert result.message['id'] == "GO00000000000000000000001"
