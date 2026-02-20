import pytest

from Adyen import settings


@pytest.fixture
def REQUEST_KWARGS():
    return {
        'merchantAccount': 'YourMerchantAccount',
        'amount': '1000'
    }

@pytest.fixture
def binLookup_version(adyen_instance):
    return adyen_instance.binlookup.bin_lookup_api.baseUrl.split('/')[-1]

def test_get_cost_estimate_success(adyen_instance, mock_client, REQUEST_KWARGS, binLookup_version):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    adyen_instance.client.platform = "test"
    
    expected = {
        'cardBin': {
            'bin': '458012',
            'commercial': False,
            'fundingSource': 'CHARGE',
            'fundsAvailability': 'N',
            'issuingBank': 'Bank Of America',
            'issuingCountry': 'US', 'issuingCurrency': 'USD',
            'paymentMethod': 'Y',
            'summary': '6789'
        },
        'costEstimateAmount': {
            'currency': 'USD', 'value': 1234
        },
        'resultCode': 'Success',
        'surchargeType': 'PASSTHROUGH'
    }

    adyen_instance.client = mock_client(
        status=200,
        request=REQUEST_KWARGS,
        filename='test/mocks/binlookup/getcostestimate-success.json'
    )

    result = adyen_instance.binlookup.bin_lookup_api.get_cost_estimate(REQUEST_KWARGS)
    assert result.message == expected
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        'https://pal-test.adyen.com/pal/servlet/'
        f'BinLookup/{binLookup_version}/getCostEstimate',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json={
            'merchantAccount': 'YourMerchantAccount',
            'amount': '1000',
            },
        password='YourWSPassword',
        username='YourWSUser'
    )

def test_get_cost_estimate_error_mocked(adyen_instance, mock_client, REQUEST_KWARGS):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    adyen_instance.client.platform = "test"

    adyen_instance.client = mock_client(
        status=200,
        request=REQUEST_KWARGS,
        filename=(
            "test/mocks/binlookup/"
            "getcostestimate-error-invalid-data-422.json"
        )
    )

    result = adyen_instance.binlookup.bin_lookup_api.get_cost_estimate(REQUEST_KWARGS)
    assert result.message['status'] == 422
    assert result.message['errorCode'] == "101"
    assert result.message['message'] == "Invalid card number"
    assert result.message['errorType'] == "validation"
