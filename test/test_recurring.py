import pytest
import Adyen
from Adyen import settings

@pytest.fixture
def recurring_url(adyen_instance):
    return adyen_instance.recurring.recurring_api.baseUrl

def test_list_recurring_details(adyen_instance, mock_client, recurring_url):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        'merchantAccount': "YourMerchantAccount",
        'reference': "YourReference",
        "shopperEmail": "ref@email.com",
        "shopperReference": "ref",
        'recurring': {'contract': "RECURRING"}
    }
    adyen_instance.client = mock_client(200, request,
                                         'test/mocks/'
                                         'recurring/'
                                         'listRecurring'
                                         'Details-'
                                         'success.json')
    result = adyen_instance.recurring.recurring_api.list_recurring_details(request)
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{recurring_url}/listRecurringDetails',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        username='YourWSUser',
        password='YourWSPassword'
    )
    assert len(result.message['details']) == 1
    assert len(result.message['details'][0]) == 1
    recurringDetail = result.message['details'][0]['RecurringDetail']
    assert recurringDetail['recurringDetailReference'] == "recurringReference"
    assert recurringDetail['alias'] == "cardAlias"
    assert recurringDetail['card']['number'] == "1111"

def test_disable(adyen_instance, mock_client, recurring_url):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "shopperEmail": "ref@email.com",
        "shopperReference": "ref",
        "recurringDetailReference": "12345678889"
    }
    adyen_instance.client = mock_client(200, request,
                                         'test/mocks/'
                                         'recurring/'
                                         'disable-success'
                                         '.json')
    result = adyen_instance.recurring.recurring_api.disable(request)
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{recurring_url}/disable',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        username='YourWSUser',
        password='YourWSPassword',
    )
    assert len(result.message['details']) == 1
    assert result.message['response'] == "[detail-successfully-disabled]"

def test_disable_803(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        "shopperEmail": "ref@email.com",
        "shopperReference": "ref",
        "recurringDetailReference": "12345678889"
    }
    adyen_instance.client = mock_client(422, request,
                                         'test/mocks/'
                                         'recurring/'
                                         'disable-error-803'
                                         '.json')
    with pytest.raises(Adyen.AdyenAPIUnprocessableEntity) as excinfo:
        adyen_instance.recurring.recurring_api.disable(request)
    assert "PaymentDetail not found" in str(excinfo.value)
