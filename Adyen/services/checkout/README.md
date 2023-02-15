## Documentation for API Endpoints

All URIs are relative to *https://checkout-test.adyen.com/v70*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*classic_checkout_sdk_api* | [**payment_session**](./ClassicCheckoutSDKApi.md#payment_session) | **POST** /paymentSession | Create a payment session
*classic_checkout_sdk_api* | [**verify_payment_result**](./ClassicCheckoutSDKApi.md#verify_payment_result) | **POST** /payments/result | Verify a payment result
*modifications_api* | [**cancel_authorised_payment**](./ModificationsApi.md#cancel_authorised_payment) | **POST** /cancels | Cancel an authorised payment
*modifications_api* | [**update_authorised_amount**](./ModificationsApi.md#update_authorised_amount) | **POST** /payments/{paymentPspReference}/amountUpdates | Update an authorised amount
*modifications_api* | [**cancel_authorised_payment_by_psp_reference**](./ModificationsApi.md#cancel_authorised_payment_by_psp_reference) | **POST** /payments/{paymentPspReference}/cancels | Cancel an authorised payment
*modifications_api* | [**capture_authorised_payment**](./ModificationsApi.md#capture_authorised_payment) | **POST** /payments/{paymentPspReference}/captures | Capture an authorised payment
*modifications_api* | [**refund_captured_payment**](./ModificationsApi.md#refund_captured_payment) | **POST** /payments/{paymentPspReference}/refunds | Refund a captured payment
*modifications_api* | [**refund_or_cancel_payment**](./ModificationsApi.md#refund_or_cancel_payment) | **POST** /payments/{paymentPspReference}/reversals | Refund or cancel a payment
*orders_api* | [**create_order**](./OrdersApi.md#create_order) | **POST** /orders | Create an order
*orders_api* | [**cancel_order**](./OrdersApi.md#cancel_order) | **POST** /orders/cancel | Cancel an order
*orders_api* | [**get_balance_of_gift_card**](./OrdersApi.md#get_balance_of_gift_card) | **POST** /paymentMethods/balance | Get the balance of a gift card
*payment_links_api* | [**get_payment_link**](./PaymentLinksApi.md#get_payment_link) | **GET** /paymentLinks/{linkId} | Get a payment link
*payment_links_api* | [**update_payment_link**](./PaymentLinksApi.md#update_payment_link) | **PATCH** /paymentLinks/{linkId} | Update the status of a payment link
*payment_links_api* | [**create_payment_link**](./PaymentLinksApi.md#create_payment_link) | **POST** /paymentLinks | Create a payment link
*payments_api* | [**list_brands_on_card**](./PaymentsApi.md#list_brands_on_card) | **POST** /cardDetails | Get the list of brands on the card
*payments_api* | [**donations**](./PaymentsApi.md#donations) | **POST** /donations | Start a transaction for donations
*payments_api* | [**payment_methods**](./PaymentsApi.md#payment_methods) | **POST** /paymentMethods | Get a list of available payment methods
*payments_api* | [**payments**](./PaymentsApi.md#payments) | **POST** /payments | Start a transaction
*payments_api* | [**payments_details**](./PaymentsApi.md#payments_details) | **POST** /payments/details | Submit details for a payment
*payments_api* | [**sessions**](./PaymentsApi.md#sessions) | **POST** /sessions | Create a payment session
*recurring_api* | [**delete_token_for_stored_payment_details**](./RecurringApi.md#delete_token_for_stored_payment_details) | **DELETE** /storedPaymentMethods/{recurringId} | Delete a token for stored payment details
*recurring_api* | [**get_tokens_for_stored_payment_details**](./RecurringApi.md#get_tokens_for_stored_payment_details) | **GET** /storedPaymentMethods | Get tokens for stored payment details
*utility_api* | [**get_apple_pay_session**](./UtilityApi.md#get_apple_pay_session) | **POST** /applePay/sessions | Get an Apple Pay session
*utility_api* | [**create_originkey_values_for_domains**](./UtilityApi.md#create_originkey_values_for_domains) | **POST** /originKeys | Create originKey values for domains
