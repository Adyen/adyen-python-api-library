from json import load

from Adyen import settings
from Adyen.util import (
    generate_notification_sig,
    is_valid_hmac_payload,
    is_valid_hmac_notification,
    get_query
)


def test_notification_request_item_hmac():
    request = {
        "pspReference": "7914073381342284",
        "merchantReference": "TestPayment-1407325143704",
        "merchantAccountCode": "TestMerchant",
        "amount": {
            "currency": "EUR",
            "value": 1130
        },
        "eventCode": "AUTHORISATION",
        "success": "true",
        "eventDate": "2019-05-06T17:15:34.121+02:00",
        "operations": [
            "CANCEL",
            "CAPTURE",
            "REFUND"
        ],
        "paymentMethod": "visa",
    }
    key = "44782DEF547AAA06C910C43932B1EB0C" \
          "71FC68D9D0C057550C48EC2ACF6BA056"
    hmac_calculation = generate_notification_sig(request, key)
    hmac_calculation_str = hmac_calculation.decode("utf-8")
    expected_hmac = "coqCmt/IZ4E3CzPvMY8zTjQVL5hYJUiBRg8UU+iCWo0="
    assert hmac_calculation_str != ""
    assert hmac_calculation_str == expected_hmac
    request['additionalData'] = {'hmacSignature': hmac_calculation_str}
    hmac_validate = is_valid_hmac_notification(request, key)
    assert 'additionalData' in request
    assert request['additionalData'] == {'hmacSignature': hmac_calculation_str}
    assert hmac_validate

def test_webhooks_with_slashes():
    hmac_key = "74F490DD33F7327BAECC88B2947C011FC02D014A473AAA33A8EC93E4DC069174"
    with open('test/mocks/util/backslash_notification.json') as file:
        backslash_notification = load(file)
        assert is_valid_hmac_notification(backslash_notification, hmac_key)
    with open('test/mocks/util/colon_notification.json') as file:
        colon_notification = load(file)
        assert is_valid_hmac_notification(colon_notification, hmac_key)
    with open('test/mocks/util/forwardslash_notification.json') as file:
        forwardslash_notification = load(file)
        assert is_valid_hmac_notification(forwardslash_notification, hmac_key)
    with open('test/mocks/util/mixed_notification.json') as file:
        mixed_notification = load(file)
        assert is_valid_hmac_notification(mixed_notification, hmac_key)

def test_query_string_creation():
    query_parameters = {
        "pageSize": 7,
        "pageNumber": 3
    }
    query_string = get_query(query_parameters)
    assert query_string == '?pageSize=7&pageNumber=3'

def test_passing_xapikey_in_method(adyen_instance, mock_client):
    request = {'merchantAccount': "YourMerchantAccount"}
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/"
                                         "checkout/"
                                         "paymentmethods"
                                         "-success.json")
    result = adyen_instance.checkout.payments_api.payment_methods(request, xapikey="YourXapikey")
    assert result.message['paymentMethods'][0]['name'] == "AliPay"
    assert result.message['paymentMethods'][2]['name'] == "Credit Card"
    assert result.message['paymentMethods'][3]['name'] == "Credit Card via AsiaPay"

def test_custom_version(adyen_instance, mock_client):
    adyen_instance.client.api_checkout_version = 60
    request = {'merchantAccount': "YourMerchantAccount"}
    adyen_instance.client = mock_client(200, request,
                                         "test/mocks/"
                                         "checkout/"
                                         "paymentmethods"
                                         "-success.json")
    result = adyen_instance.checkout.payments_api.payment_methods(request, xapikey="YourXapikey")
    adyen_instance.client.http_client.request.assert_called_once_with(
        'POST',
        f'https://checkout-test.adyen.com/v{adyen_instance.client.api_checkout_version}/paymentMethods',
        headers={'adyen-library-name': settings.LIB_NAME, 'adyen-library-version': settings.LIB_VERSION, 'User-Agent': settings.LIB_NAME + '/' + settings.LIB_VERSION},
        json=request,
        xapikey="YourXapikey"
    )

def test_is_valid_hmac_notification_removes_additional_data():
    notification = {
        "live": "false",
        "notificationItems": [
            {
                "NotificationRequestItem": {
                    "additionalData": {
                        "hmacSignature": "11aa",
                        "fraudResultType": "GREEN",
                        "fraudManualReview": "false",
                        "totalFraudScore": "75"
                    },
                    "amount": {
                        "currency": "USD",
                        "value": 10000
                    },
                    "success": "true"

                }
            }
        ]}
    is_valid_hmac_notification(notification, "11aa")
    assert notification['notificationItems'][0]['NotificationRequestItem']['additionalData'] is not None

import textwrap

def test_is_valid_hmac_payload():

    payload = textwrap.dedent('''\
        {
            "type": "merchant.created",
            "environment": "test",
            "createdAt": "01-01-2024",
            "data": {
                "capabilities": {
                    "sendToTransferInstrument": {
                        "requested": true,
                        "requestedLevel": "notApplicable"
                    }
                },
                "companyId": "YOUR_COMPANY_ID",
                "merchantId": "YOUR_MERCHANT_ACCOUNT",
                "status": "PreActive"
            }
        }''')
    hmac_key = "44782DEF547AAA06C910C43932B1EB0C71FC68D9D0C057550C48EC2ACF6BA056"
    expected_hmac = "NiqA5vsdV5etZMOaR27+GBSG4i6JeP6j1wkCM6t53vA="

    assert is_valid_hmac_payload(expected_hmac, hmac_key, payload.encode("utf-8"))

def test_is_invalid_hmac_payload():
    payload = '''{
    "type": "merchant.created",
    "environment": "test",
    "createdAt": "01-01-2024",
    "data": {
        "capabilities": {
            "sendToTransferInstrument": {
                "requested": true,
                "requestedLevel": "notApplicable"
            }
        },
        "companyId": "YOUR_COMPANY_ID",
        "merchantId": "YOUR_MERCHANT_ACCOUNT",
        "status": "PreActive"
    }
}'''
    hmac_key = "44782DEF547AAA06C910C43932B1EB0C71FC68D9D0C057550C48EC2ACF6BA056"
    expected_hmac = "MismatchingHmacKey="

    assert not is_valid_hmac_payload(expected_hmac, hmac_key, payload.encode("utf-8"))
