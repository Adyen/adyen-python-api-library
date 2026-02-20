from Adyen import settings

def test_payment_methods_success_mocked(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {'merchantAccount': "YourMerchantAccount"}
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/"
                                         "checkout/"
                                         "paymentmethods"
                                         "-success.json")
    result = adyen_instance.checkout.payments_api.payment_methods(request)
    assert result.message['paymentMethods'][0]['name'] == "AliPay"
    assert result.message['paymentMethods'][2]['name'] == "Credit Card"
    assert result.message['paymentMethods'][3]['name'] == "Credit Card via AsiaPay"

def test_payment_methods_error_mocked(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {'merchantAccount': "YourMerchantAccount"}
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/"
                                         "checkout/"
                                         "paymentmethods-"
                                         "error-forbidden"
                                         "-403.json")
    result = adyen_instance.checkout.payments_api.payment_methods(request)
    assert result.message['status'] == 403
    assert result.message['errorCode'] == "901"
    assert result.message['message'] == "Invalid Merchant Account"
    assert result.message['errorType'] == "security"

def test_payments_success_mocked(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        'amount': {"value": "100000", "currency": "EUR"},
        'reference': "123456",
        'paymentMethod': {
            "type": "scheme",
            "number": "4111111111111111",
            "expiryMonth": "08",
            "expiryYear": "2018",
            "holderName": "John Smith",
            "cvc": "737"
        },
        'merchantAccount': "YourMerchantAccount",
        'returnUrl': "https://your-company.com/..."
    }

    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/"
                                         "checkout/"
                                         "payments"
                                         "-success"
                                         ".json")
    result = adyen_instance.checkout.payments_api.payments(request)
    assert result.message['pspReference'] == "8535296650153317"
    assert result.message['resultCode'] == "Authorised"
    assert result.message["additionalData"]['expiryDate'] == "8/2018"
    assert result.message["additionalData"]['fraudResultType'] == "GREEN"

def test_payments_error_mocked(adyen_instance, mock_client):
    adyen_instance.client.xapikey = "YourXapikey"
    request = {
        'amount': {"value": "100000", "currency": "EUR"},
        'reference': "54431",
        'paymentMethod': {
            "type": "scheme",
            "number": "4111111111111111",
            "expiryMonth": "08",
            "expiryYear": "2018",
            "holderName": "John Smith",
            "cvc": "737"
        },
        'merchantAccount': "YourMerchantAccount",
        'returnUrl': "https://your-company.com/..."
    }

    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/"
                                         "checkout/"
                                         "payments-error"
                                         "-invalid"
                                         "-data-422"
                                         ".json")
    result = adyen_instance.checkout.payments_api.payments(request)
    
    baseUrl = adyen_instance.checkout.payments_api.baseUrl
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'{baseUrl}/payments',
        headers={
            'adyen-library-name': settings.LIB_NAME,
            'adyen-library-version': settings.LIB_VERSION,
            'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION
        },
        json=request,
        xapikey="YourXapikey"
    )
