import pytest
import Adyen

def test_capture_success(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        'merchantAccount': "YourMerchantAccount",
        'reference': "YourReference",
        'modificationAmount': {"value": "1234", "currency": "EUR"},
        'originalReference': "YourOriginalReference"
    }
    adyen_instance.client = mock_client(200, request,
                                         'test/mocks/'
                                         'capture-success'
                                         '.json')
    result = adyen_instance.payment.modifications_api.capture(request)
    assert result.message['response'] == "[capture-received]"

def test_capture_error_167(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        'merchantAccount': "YourMerchantAccount",
        'reference': "YourReference",
        'modificationAmount': {"value": "1234", "currency": "EUR"},
        'originalReference': "YourOriginalReference"
    }
    adyen_instance.client = mock_client(422, request,
                                         'test/mocks/'
                                         'capture-error-167'
                                         '.json')
    with pytest.raises(Adyen.AdyenAPIUnprocessableEntity) as excinfo:
        adyen_instance.payment.modifications_api.capture(request)
    assert "Original pspReference required for this operation" in str(excinfo.value)

def test_cancel_or_refund_received(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        'merchantAccount': "YourMerchantAccount",
        'reference': "YourReference",
        'originalReference': "YourOriginalReference"
    }
    adyen_instance.client = mock_client(200, request,
                                         'test/mocks/'
                                         'cancelOrRefund'
                                         '-received.json')
    result = adyen_instance.payment.modifications_api.cancel_or_refund(request)
    assert result.message['response'] == "[cancelOrRefund-received]"

def test_refund_received(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        'merchantAccount': "YourMerchantAccount",
        'reference': "YourReference",
        'originalReference': "YourOriginalReference",
        'modificationAmount': {"value": "1234", "currency": "EUR"}
    }
    adyen_instance.client = mock_client(200, request,
                                         'test/mocks/'
                                         'refund-received'
                                         '.json')
    result = adyen_instance.payment.modifications_api.refund(request)
    assert result.message['response'] == "[refund-received]"

def test_cancel_received(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        'merchantAccount': "YourMerchantAccount",
        'reference': "YourReference",
        'originalReference': "YourOriginalReference"
    }
    adyen_instance.client = mock_client(200, request,
                                         'test/mocks/'
                                         'cancel-received'
                                         '.json')
    result = adyen_instance.payment.modifications_api.cancel(request)
    assert result.message['response'] == "[cancel-received]"

def test_adjust_authorisation_received(adyen_instance, mock_client):
    adyen_instance.client.username = "YourWSUser"
    adyen_instance.client.password = "YourWSPassword"
    request = {
        'merchantAccount': "YourMerchantAccount",
        'reference': "YourReference",
        'modificationAmount': {"value": "1234", "currency": "EUR"},
        'originalReference': "YourOriginalReference"
    }
    adyen_instance.client = mock_client(200, request,
                                         'test/mocks/'
                                         'adjust-'
                                         'authorisation-'
                                         'received.json')
    result = adyen_instance.payment.modifications_api.adjust_authorisation(request)
    assert result.message['response'] == "[adjustAuthorisation-received]"
