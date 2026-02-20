def test_checkout_api_structure(adyen_instance):
    checkout = adyen_instance.checkout
    assert checkout.donations_api is not None
    assert checkout.modifications_api is not None
    assert checkout.orders_api is not None
    assert checkout.payment_links_api is not None
    assert checkout.payments_api is not None
    assert checkout.recurring_api is not None
    assert checkout.utility_api is not None

def test_modifications_api_methods(adyen_instance):
    client = adyen_instance.checkout.modifications_api
    assert client.cancel_authorised_payment is not None
    assert client.update_authorised_amount is not None
    assert client.cancel_authorised_payment_by_psp_reference is not None
    assert client.capture_authorised_payment is not None
    assert client.refund_captured_payment is not None
    assert client.refund_or_cancel_payment is not None

def test_orders_api_methods(adyen_instance):
    client = adyen_instance.checkout.orders_api
    assert client.orders is not None
    assert client.cancel_order is not None
    assert client.get_balance_of_gift_card is not None

def test_payment_links_api_methods(adyen_instance):
    client = adyen_instance.checkout.payment_links_api
    assert client.get_payment_link is not None
    assert client.update_payment_link is not None
    assert client.payment_links is not None

def test_payments_api_methods(adyen_instance):
    client = adyen_instance.checkout.payments_api
    assert client.card_details is not None
    assert client.payment_methods is not None
    assert client.payments is not None
    assert client.payments_details is not None
    assert client.sessions is not None

def test_recurring_api_methods(adyen_instance):
    client = adyen_instance.checkout.recurring_api
    assert client.delete_token_for_stored_payment_details is not None
    assert client.get_tokens_for_stored_payment_details is not None

def test_utility_api_methods(adyen_instance):
    client = adyen_instance.checkout.utility_api
    assert client.get_apple_pay_session is not None
