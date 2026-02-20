import pytest

from Adyen.exceptions import AdyenEndpointInvalidFormat
from Adyen.services.posMobile import AdyenPosMobileApi


@pytest.fixture
def checkout_url(adyen_instance):
    return adyen_instance.checkout.payments_api.baseUrl

@pytest.fixture
def checkout_version(checkout_url):
    return checkout_url.split('/')[-1]

@pytest.fixture
def payment_url(adyen_instance):
    return adyen_instance.payment.payments_api.baseUrl

@pytest.fixture
def payment_version(payment_url):
    return payment_url.split('/')[-1]

@pytest.fixture
def binlookup_url(adyen_instance):
    return adyen_instance.binlookup.bin_lookup_api.baseUrl

@pytest.fixture
def management_url(adyen_instance):
    return adyen_instance.management.account_merchant_level_api.baseUrl

@pytest.fixture
def sessionauth_url(adyen_instance):
    return adyen_instance.sessionAuthentication.session_authentication_api.baseUrl

@pytest.fixture
def sessionauth_version(sessionauth_url):
    return sessionauth_url.split('/')[-1]

@pytest.fixture
def capital_url(adyen_instance):
    return adyen_instance.capital.grants_api.baseUrl

@pytest.fixture
def capital_version(capital_url):
    return capital_url.split('/')[-1]

def test_checkout_api_url_custom(adyen_instance, checkout_url, checkout_version):
    adyen_instance.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
    url = adyen_instance.client._determine_api_url("live", checkout_url + "/payments")
    assert url == f"https://1797a841fbb37ca7-AdyenDemo-checkout-live.adyenpayments.com/checkout/{checkout_version}/payments"

def test_pos_mobile_api_url_live(adyen_instance):
    adyen_instance.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
    pos_mobile = AdyenPosMobileApi(adyen_instance.client)
    pos_mobile_url = pos_mobile.pos_mobile_api.baseUrl
    pos_mobile_version = pos_mobile_url.split('/')[-1]
    url = adyen_instance.client._determine_api_url("live", pos_mobile_url + "/sessions")
    assert url == f"https://1797a841fbb37ca7-AdyenDemo-checkout-live.adyenpayments.com/checkout/possdk/{pos_mobile_version}/sessions"

def test_checkout_api_url(adyen_instance, checkout_url):
    adyen_instance.client.live_endpoint_prefix = None
    url = adyen_instance.client._determine_api_url("test", checkout_url + "/payments/details")
    assert url == f"{checkout_url}/payments/details"

def test_payments_invalid_platform(adyen_instance):
    request = {
        'amount': {"value": "100000", "currency": "EUR"},
        "reference": "Your order number",
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

    adyen_instance.client.platform = "live"
    adyen_instance.client.live_endpoint_prefix = None
    adyen_instance.client.xapikey = "dummy"

    with pytest.raises(AdyenEndpointInvalidFormat):
        adyen_instance.checkout.payments_api.sessions(request)

def test_pal_url_live_endpoint_prefix_live_platform(adyen_instance, payment_url, payment_version):
    adyen_instance.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
    url = adyen_instance.client._determine_api_url("live", payment_url + "/payments")
    assert url == f"https://1797a841fbb37ca7-AdyenDemo-pal-live.adyenpayments.com/pal/servlet/Payment/{payment_version}/payments"

def test_pal_url_live_endpoint_prefix_test_platform(adyen_instance, payment_url):
    adyen_instance.client.live_endpoint_prefix = "1797a841fbb37ca7-AdyenDemo"
    url = adyen_instance.client._determine_api_url("test", payment_url + "/payments")
    assert url == f"{payment_url}/payments"

def test_pal_url_no_live_endpoint_prefix_test_platform(adyen_instance, payment_url):
    adyen_instance.client.live_endpoint_prefix = None
    url = adyen_instance.client._determine_api_url("test", payment_url + "/payments")
    assert url == f"{payment_url}/payments"

def test_binlookup_url_no_live_endpoint_prefix_test_platform(adyen_instance, binlookup_url):
    adyen_instance.client.live_endpoint_prefix = None
    url = adyen_instance.client._determine_api_url("test", binlookup_url + "/get3dsAvailability")
    assert url == f"{binlookup_url}/get3dsAvailability"

def test_checkout_api_url_orders(adyen_instance, checkout_url):
    adyen_instance.client.live_endpoint_prefix = None
    url = adyen_instance.client._determine_api_url("test", checkout_url + "/orders")
    assert url == f"{checkout_url}/orders"

def test_checkout_api_url_order_cancel(adyen_instance, checkout_url):
    adyen_instance.client.live_endpoint_prefix = None
    url = adyen_instance.client._determine_api_url("test", checkout_url + "/orders/cancel")
    assert url == f"{checkout_url}/orders/cancel"

def test_checkout_api_url_order_payment_methods_balance(adyen_instance, checkout_url):
    adyen_instance.client.live_endpoint_prefix = None
    url = adyen_instance.client._determine_api_url("test", checkout_url + "/paymentMethods/balance")
    assert url == f"{checkout_url}/paymentMethods/balance"

def test_checkout_api_url_sessions(adyen_instance, checkout_url):
    adyen_instance.client.live_endpoint_prefix = None
    url = adyen_instance.client._determine_api_url("test", checkout_url + "/sessions")
    assert url == f"{checkout_url}/sessions"

def test_management_api_url_companies(adyen_instance, management_url):
    companyId = "YOUR_COMPANY_ID"
    url = adyen_instance.client._determine_api_url("test", management_url + f'/companies/{companyId}/users')
    assert url == f"{management_url}/companies/{companyId}/users"

def test_secureauthentication_api_url(adyen_instance, sessionauth_url):
    url = adyen_instance.client._determine_api_url("test", sessionauth_url)
    assert url == sessionauth_url

def test_live_secureauthentication_api_url(adyen_instance, sessionauth_url, sessionauth_version):
    url = adyen_instance.client._determine_api_url("live", sessionauth_url + "/sessions")
    assert url == f"https://authe-live.adyen.com/authe/api/{sessionauth_version}/sessions"

def test_capital_api_url(adyen_instance, capital_url):
    url = adyen_instance.client._determine_api_url("test", capital_url)
    assert url == capital_url

def test_live_capital_api_url(adyen_instance, capital_url, capital_version):
    url = adyen_instance.client._determine_api_url("live", capital_url)
    assert url == f"https://balanceplatform-api-live.adyen.com/capital/{capital_version}"
