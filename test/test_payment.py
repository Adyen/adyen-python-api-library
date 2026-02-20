import pytest
import Adyen

def test_authorise_success_mocked(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        'merchantAccount': "YourMerchantAccount",
        'amount': {"value": "100000", "currency": "EUR"},
        'reference': "123456",
        'card': {
            "number": "5136333333333335",
            "expiryMonth": "08",
            "expiryYear": "2018",
            "cvc": "737",
            "holderName": "John Doe"
        }
    }
    adyen_instance.client = mock_client(200, request,
                                         'test/mocks/'
                                         'authorise'
                                         '-success'
                                         '.json')
    result = adyen_instance.payment.payments_api.authorise(request)
    assert result.message['resultCode'] == "Authorised"
    assert result.message['additionalData']['expiryDate'] == "8/2018"
    assert result.message['additionalData']['cardBin'] == "411111"
    assert result.message['additionalData']['cardSummary'] == "1111"
    assert result.message['additionalData']['cardHolderName'] == "Holder"
    assert result.message['additionalData']['threeDOffered'] == "true"
    assert result.message['additionalData']['threeDAuthenticated'] == "false"
    assert result.message['authCode'] == "69746"
    assert len(result.message['fraudResult']['results']) == 11
    fraud_checks = result.message['fraudResult']['results']
    fraud_check_result = fraud_checks[0]['FraudCheckResult']
    assert fraud_check_result['name'] == "CardChunkUsage"
    assert fraud_check_result['accountScore'] == 8
    assert fraud_check_result['checkId'] == 2

def test_authorise_error010_mocked(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        'merchantAccount': "testaccount",
        'amount': {"value": "100000", "currency": "EUR"},
        'reference': "123456",
        'card': {
            "number": "5136333333333335",
            "expiryMonth": "08",
            "expiryYear": "2018",
            "cvc": "737",
            "holderName": "John Doe"
        }
    }
    adyen_instance.client = mock_client(403, request,
                                         'test/mocks/'
                                         'authorise-error'
                                         '-010'
                                         '.json')
    with pytest.raises(Adyen.AdyenAPIInvalidPermission):
        adyen_instance.payment.payments_api.authorise(request)

def test_authorise_error_cvc_declined_mocked(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        'amount': {"value": "100000", "currency": "EUR"},
        'reference': "123456",
        'card': {
            "number": "5136333333333335",
            "expiryMonth": "08",
            "expiryYear": "2018",
            "cvc": "787",
            "holderName": "John Doe"
        }
    }
    adyen_instance.client = mock_client(200, request,
                                         'test/mocks/'
                                         'authorise'
                                         '-error-'
                                         'cvc-declined'
                                         '.json')
    result = adyen_instance.payment.payments_api.authorise(request)
    assert result.message['resultCode'] == "Refused"

def test_authorise_success_3d_mocked(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        'amount': {"value": "100000", "currency": "EUR"},
        'reference': "123456",
        'card': {
            "number": "5136333333333335",
            "expiryMonth": "08",
            "expiryYear": "2018",
            "cvc": "737",
            "holderName": "John Doe"
        }
    }
    adyen_instance.client = mock_client(200, request,
                                         'test/mocks/'
                                         'authorise'
                                         '-success-3d'
                                         '.json')
    result = adyen_instance.payment.payments_api.authorise(request)
    assert result.message['resultCode'] == "RedirectShopper"
