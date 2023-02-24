## Documentation for API Endpoints

All URIs are relative to *https://management-test.adyen.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*api_credentials_company_level_api* | [**list_api_credentials**](./APICredentialsCompanyLevelApi.md#list_api_credentials) | **GET** /companies/{companyId}/apiCredentials | Get a list of API credentials
*api_credentials_company_level_api* | [**get_api_credential**](./APICredentialsCompanyLevelApi.md#get_api_credential) | **GET** /companies/{companyId}/apiCredentials/{apiCredentialId} | Get an API credential
*api_credentials_company_level_api* | [**update_api_credential**](./APICredentialsCompanyLevelApi.md#update_api_credential) | **PATCH** /companies/{companyId}/apiCredentials/{apiCredentialId} | Update an API credential.
*api_credentials_company_level_api* | [**create_api_credential**](./APICredentialsCompanyLevelApi.md#create_api_credential) | **POST** /companies/{companyId}/apiCredentials | Create an API credential.
*api_credentials_merchant_level_api* | [**list_api_credentials**](./APICredentialsMerchantLevelApi.md#list_api_credentials) | **GET** /merchants/{merchantId}/apiCredentials | Get a list of API credentials
*api_credentials_merchant_level_api* | [**get_api_credential**](./APICredentialsMerchantLevelApi.md#get_api_credential) | **GET** /merchants/{merchantId}/apiCredentials/{apiCredentialId} | Get an API credential
*api_credentials_merchant_level_api* | [**update_api_credential**](./APICredentialsMerchantLevelApi.md#update_api_credential) | **PATCH** /merchants/{merchantId}/apiCredentials/{apiCredentialId} | Update an API credential
*api_credentials_merchant_level_api* | [**create_api_credential**](./APICredentialsMerchantLevelApi.md#create_api_credential) | **POST** /merchants/{merchantId}/apiCredentials | Create an API credential
*api_key_company_level_api* | [**generate_new_api_key**](./APIKeyCompanyLevelApi.md#generate_new_api_key) | **POST** /companies/{companyId}/apiCredentials/{apiCredentialId}/generateApiKey | Generate new API key
*api_key_merchant_level_api* | [**generate_new_api_key**](./APIKeyMerchantLevelApi.md#generate_new_api_key) | **POST** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey | Generate new API key
*account_company_level_api* | [**list_company_accounts**](./AccountCompanyLevelApi.md#list_company_accounts) | **GET** /companies | Get a list of company accounts
*account_company_level_api* | [**get_company_account**](./AccountCompanyLevelApi.md#get_company_account) | **GET** /companies/{companyId} | Get a company account
*account_company_level_api* | [**list_merchant_accounts**](./AccountCompanyLevelApi.md#list_merchant_accounts) | **GET** /companies/{companyId}/merchants | Get a list of merchant accounts
*account_merchant_level_api* | [**list_merchant_accounts**](./AccountMerchantLevelApi.md#list_merchant_accounts) | **GET** /merchants | Get a list of merchant accounts
*account_merchant_level_api* | [**get_merchant_account**](./AccountMerchantLevelApi.md#get_merchant_account) | **GET** /merchants/{merchantId} | Get a merchant account
*account_merchant_level_api* | [**create_merchant_account**](./AccountMerchantLevelApi.md#create_merchant_account) | **POST** /merchants | Create a merchant account
*account_merchant_level_api* | [**request_to_activate_merchant_account**](./AccountMerchantLevelApi.md#request_to_activate_merchant_account) | **POST** /merchants/{merchantId}/activate | Request to activate a merchant account
*account_store_level_api* | [**list_stores_by_merchant_id**](./AccountStoreLevelApi.md#list_stores_by_merchant_id) | **GET** /merchants/{merchantId}/stores | Get a list of stores
*account_store_level_api* | [**get_store**](./AccountStoreLevelApi.md#get_store) | **GET** /merchants/{merchantId}/stores/{storeId} | Get a store
*account_store_level_api* | [**list_stores**](./AccountStoreLevelApi.md#list_stores) | **GET** /stores | Get a list of stores
*account_store_level_api* | [**get_store_by_id**](./AccountStoreLevelApi.md#get_store_by_id) | **GET** /stores/{storeId} | Get a store
*account_store_level_api* | [**update_store**](./AccountStoreLevelApi.md#update_store) | **PATCH** /merchants/{merchantId}/stores/{storeId} | Update a store
*account_store_level_api* | [**update_store_by_id**](./AccountStoreLevelApi.md#update_store_by_id) | **PATCH** /stores/{storeId} | Update a store
*account_store_level_api* | [**create_store_by_merchant_id**](./AccountStoreLevelApi.md#create_store_by_merchant_id) | **POST** /merchants/{merchantId}/stores | Create a store
*account_store_level_api* | [**create_store**](./AccountStoreLevelApi.md#create_store) | **POST** /stores | Create a store
*allowed_origins_company_level_api* | [**delete_allowed_origin**](./AllowedOriginsCompanyLevelApi.md#delete_allowed_origin) | **DELETE** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | Delete an allowed origin
*allowed_origins_company_level_api* | [**list_allowed_origins**](./AllowedOriginsCompanyLevelApi.md#list_allowed_origins) | **GET** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | Get a list of allowed origins
*allowed_origins_company_level_api* | [**get_allowed_origin**](./AllowedOriginsCompanyLevelApi.md#get_allowed_origin) | **GET** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | Get an allowed origin
*allowed_origins_company_level_api* | [**create_allowed_origin**](./AllowedOriginsCompanyLevelApi.md#create_allowed_origin) | **POST** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | Create an allowed origin
*allowed_origins_merchant_level_api* | [**delete_allowed_origin**](./AllowedOriginsMerchantLevelApi.md#delete_allowed_origin) | **DELETE** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | Delete an allowed origin
*allowed_origins_merchant_level_api* | [**list_allowed_origins**](./AllowedOriginsMerchantLevelApi.md#list_allowed_origins) | **GET** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins | Get a list of allowed origins
*allowed_origins_merchant_level_api* | [**get_allowed_origin**](./AllowedOriginsMerchantLevelApi.md#get_allowed_origin) | **GET** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | Get an allowed origin
*allowed_origins_merchant_level_api* | [**create_allowed_origin**](./AllowedOriginsMerchantLevelApi.md#create_allowed_origin) | **POST** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins | Create an allowed origin
*client_key_company_level_api* | [**generate_new_client_key**](./ClientKeyCompanyLevelApi.md#generate_new_client_key) | **POST** /companies/{companyId}/apiCredentials/{apiCredentialId}/generateClientKey | Generate new client key
*client_key_merchant_level_api* | [**generate_new_client_key**](./ClientKeyMerchantLevelApi.md#generate_new_client_key) | **POST** /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateClientKey | Generate new client key
*my_api_credential_api* | [**remove_allowed_origin**](./MyAPICredentialApi.md#remove_allowed_origin) | **DELETE** /me/allowedOrigins/{originId} | Remove allowed origin
*my_api_credential_api* | [**get_api_credential_details**](./MyAPICredentialApi.md#get_api_credential_details) | **GET** /me | Get API credential details
*my_api_credential_api* | [**get_allowed_origins**](./MyAPICredentialApi.md#get_allowed_origins) | **GET** /me/allowedOrigins | Get allowed origins
*my_api_credential_api* | [**get_allowed_origin_details**](./MyAPICredentialApi.md#get_allowed_origin_details) | **GET** /me/allowedOrigins/{originId} | Get allowed origin details
*my_api_credential_api* | [**add_allowed_origin**](./MyAPICredentialApi.md#add_allowed_origin) | **POST** /me/allowedOrigins | Add allowed origin
*payment_methods_merchant_level_api* | [**get_all_payment_methods**](./PaymentMethodsMerchantLevelApi.md#get_all_payment_methods) | **GET** /merchants/{merchantId}/paymentMethodSettings | Get all payment methods
*payment_methods_merchant_level_api* | [**get_payment_method_details**](./PaymentMethodsMerchantLevelApi.md#get_payment_method_details) | **GET** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | Get payment method details
*payment_methods_merchant_level_api* | [**get_apple_pay_domains**](./PaymentMethodsMerchantLevelApi.md#get_apple_pay_domains) | **GET** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/getApplePayDomains | Get Apple Pay domains
*payment_methods_merchant_level_api* | [**update_payment_method**](./PaymentMethodsMerchantLevelApi.md#update_payment_method) | **PATCH** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId} | Update a payment method
*payment_methods_merchant_level_api* | [**request_payment_method**](./PaymentMethodsMerchantLevelApi.md#request_payment_method) | **POST** /merchants/{merchantId}/paymentMethodSettings | Request a payment method
*payment_methods_merchant_level_api* | [**add_apple_pay_domain**](./PaymentMethodsMerchantLevelApi.md#add_apple_pay_domain) | **POST** /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/addApplePayDomains | Add an Apple Pay domain
*payout_settings_merchant_level_api* | [**delete_payout_setting**](./PayoutSettingsMerchantLevelApi.md#delete_payout_setting) | **DELETE** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Delete a payout setting
*payout_settings_merchant_level_api* | [**list_payout_settings**](./PayoutSettingsMerchantLevelApi.md#list_payout_settings) | **GET** /merchants/{merchantId}/payoutSettings | Get a list of payout settings
*payout_settings_merchant_level_api* | [**get_payout_setting**](./PayoutSettingsMerchantLevelApi.md#get_payout_setting) | **GET** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Get a payout setting
*payout_settings_merchant_level_api* | [**update_payout_setting**](./PayoutSettingsMerchantLevelApi.md#update_payout_setting) | **PATCH** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Update a payout setting
*payout_settings_merchant_level_api* | [**add_payout_setting**](./PayoutSettingsMerchantLevelApi.md#add_payout_setting) | **POST** /merchants/{merchantId}/payoutSettings | Add a payout setting
*terminal_actions_company_level_api* | [**list_android_apps**](./TerminalActionsCompanyLevelApi.md#list_android_apps) | **GET** /companies/{companyId}/androidApps | Get a list of Android apps
*terminal_actions_company_level_api* | [**list_android_certificates**](./TerminalActionsCompanyLevelApi.md#list_android_certificates) | **GET** /companies/{companyId}/androidCertificates | Get a list of Android certificates
*terminal_actions_company_level_api* | [**list_terminal_actions**](./TerminalActionsCompanyLevelApi.md#list_terminal_actions) | **GET** /companies/{companyId}/terminalActions | Get a list of terminal actions
*terminal_actions_company_level_api* | [**get_terminal_action**](./TerminalActionsCompanyLevelApi.md#get_terminal_action) | **GET** /companies/{companyId}/terminalActions/{actionId} | Get terminal action
*terminal_actions_terminal_level_api* | [**create_terminal_action**](./TerminalActionsTerminalLevelApi.md#create_terminal_action) | **POST** /terminals/scheduleActions | Create a terminal action
*terminal_orders_company_level_api* | [**list_billing_entities**](./TerminalOrdersCompanyLevelApi.md#list_billing_entities) | **GET** /companies/{companyId}/billingEntities | Get a list of billing entities
*terminal_orders_company_level_api* | [**list_shipping_locations**](./TerminalOrdersCompanyLevelApi.md#list_shipping_locations) | **GET** /companies/{companyId}/shippingLocations | Get a list of shipping locations
*terminal_orders_company_level_api* | [**list_terminal_models**](./TerminalOrdersCompanyLevelApi.md#list_terminal_models) | **GET** /companies/{companyId}/terminalModels | Get a list of terminal models
*terminal_orders_company_level_api* | [**list_orders**](./TerminalOrdersCompanyLevelApi.md#list_orders) | **GET** /companies/{companyId}/terminalOrders | Get a list of orders
*terminal_orders_company_level_api* | [**get_order**](./TerminalOrdersCompanyLevelApi.md#get_order) | **GET** /companies/{companyId}/terminalOrders/{orderId} | Get an order
*terminal_orders_company_level_api* | [**list_terminal_products**](./TerminalOrdersCompanyLevelApi.md#list_terminal_products) | **GET** /companies/{companyId}/terminalProducts | Get a list of terminal products
*terminal_orders_company_level_api* | [**update_order**](./TerminalOrdersCompanyLevelApi.md#update_order) | **PATCH** /companies/{companyId}/terminalOrders/{orderId} | Update an order
*terminal_orders_company_level_api* | [**create_shipping_location**](./TerminalOrdersCompanyLevelApi.md#create_shipping_location) | **POST** /companies/{companyId}/shippingLocations | Create a shipping location
*terminal_orders_company_level_api* | [**create_order**](./TerminalOrdersCompanyLevelApi.md#create_order) | **POST** /companies/{companyId}/terminalOrders | Create an order
*terminal_orders_company_level_api* | [**cancel_order**](./TerminalOrdersCompanyLevelApi.md#cancel_order) | **POST** /companies/{companyId}/terminalOrders/{orderId}/cancel | Cancel an order
*terminal_orders_merchant_level_api* | [**list_billing_entities**](./TerminalOrdersMerchantLevelApi.md#list_billing_entities) | **GET** /merchants/{merchantId}/billingEntities | Get a list of billing entities
*terminal_orders_merchant_level_api* | [**list_shipping_locations**](./TerminalOrdersMerchantLevelApi.md#list_shipping_locations) | **GET** /merchants/{merchantId}/shippingLocations | Get a list of shipping locations
*terminal_orders_merchant_level_api* | [**list_terminal_models**](./TerminalOrdersMerchantLevelApi.md#list_terminal_models) | **GET** /merchants/{merchantId}/terminalModels | Get a list of terminal models
*terminal_orders_merchant_level_api* | [**list_orders**](./TerminalOrdersMerchantLevelApi.md#list_orders) | **GET** /merchants/{merchantId}/terminalOrders | Get a list of orders
*terminal_orders_merchant_level_api* | [**get_order**](./TerminalOrdersMerchantLevelApi.md#get_order) | **GET** /merchants/{merchantId}/terminalOrders/{orderId} | Get an order
*terminal_orders_merchant_level_api* | [**list_terminal_products**](./TerminalOrdersMerchantLevelApi.md#list_terminal_products) | **GET** /merchants/{merchantId}/terminalProducts | Get a list of terminal products
*terminal_orders_merchant_level_api* | [**update_order**](./TerminalOrdersMerchantLevelApi.md#update_order) | **PATCH** /merchants/{merchantId}/terminalOrders/{orderId} | Update an order
*terminal_orders_merchant_level_api* | [**create_shipping_location**](./TerminalOrdersMerchantLevelApi.md#create_shipping_location) | **POST** /merchants/{merchantId}/shippingLocations | Create a shipping location
*terminal_orders_merchant_level_api* | [**create_order**](./TerminalOrdersMerchantLevelApi.md#create_order) | **POST** /merchants/{merchantId}/terminalOrders | Create an order
*terminal_orders_merchant_level_api* | [**cancel_order**](./TerminalOrdersMerchantLevelApi.md#cancel_order) | **POST** /merchants/{merchantId}/terminalOrders/{orderId}/cancel | Cancel an order
*terminal_settings_company_level_api* | [**get_terminal_logo**](./TerminalSettingsCompanyLevelApi.md#get_terminal_logo) | **GET** /companies/{companyId}/terminalLogos | Get the terminal logo
*terminal_settings_company_level_api* | [**get_terminal_settings**](./TerminalSettingsCompanyLevelApi.md#get_terminal_settings) | **GET** /companies/{companyId}/terminalSettings | Get terminal settings
*terminal_settings_company_level_api* | [**update_terminal_logo**](./TerminalSettingsCompanyLevelApi.md#update_terminal_logo) | **PATCH** /companies/{companyId}/terminalLogos | Update the terminal logo
*terminal_settings_company_level_api* | [**update_terminal_settings**](./TerminalSettingsCompanyLevelApi.md#update_terminal_settings) | **PATCH** /companies/{companyId}/terminalSettings | Update terminal settings
*terminal_settings_merchant_level_api* | [**get_terminal_logo**](./TerminalSettingsMerchantLevelApi.md#get_terminal_logo) | **GET** /merchants/{merchantId}/terminalLogos | Get the terminal logo
*terminal_settings_merchant_level_api* | [**get_terminal_settings**](./TerminalSettingsMerchantLevelApi.md#get_terminal_settings) | **GET** /merchants/{merchantId}/terminalSettings | Get terminal settings
*terminal_settings_merchant_level_api* | [**update_terminal_logo**](./TerminalSettingsMerchantLevelApi.md#update_terminal_logo) | **PATCH** /merchants/{merchantId}/terminalLogos | Update the terminal logo
*terminal_settings_merchant_level_api* | [**update_terminal_settings**](./TerminalSettingsMerchantLevelApi.md#update_terminal_settings) | **PATCH** /merchants/{merchantId}/terminalSettings | Update terminal settings
*terminal_settings_store_level_api* | [**get_terminal_logo**](./TerminalSettingsStoreLevelApi.md#get_terminal_logo) | **GET** /merchants/{merchantId}/stores/{reference}/terminalLogos | Get the terminal logo
*terminal_settings_store_level_api* | [**get_terminal_settings**](./TerminalSettingsStoreLevelApi.md#get_terminal_settings) | **GET** /merchants/{merchantId}/stores/{reference}/terminalSettings | Get terminal settings
*terminal_settings_store_level_api* | [**get_terminal_logo_by_store_id**](./TerminalSettingsStoreLevelApi.md#get_terminal_logo_by_store_id) | **GET** /stores/{storeId}/terminalLogos | Get the terminal logo
*terminal_settings_store_level_api* | [**get_terminal_settings_by_store_id**](./TerminalSettingsStoreLevelApi.md#get_terminal_settings_by_store_id) | **GET** /stores/{storeId}/terminalSettings | Get terminal settings
*terminal_settings_store_level_api* | [**update_terminal_logo**](./TerminalSettingsStoreLevelApi.md#update_terminal_logo) | **PATCH** /merchants/{merchantId}/stores/{reference}/terminalLogos | Update the terminal logo
*terminal_settings_store_level_api* | [**update_terminal_settings**](./TerminalSettingsStoreLevelApi.md#update_terminal_settings) | **PATCH** /merchants/{merchantId}/stores/{reference}/terminalSettings | Update terminal settings
*terminal_settings_store_level_api* | [**update_terminal_logo_by_store_id**](./TerminalSettingsStoreLevelApi.md#update_terminal_logo_by_store_id) | **PATCH** /stores/{storeId}/terminalLogos | Update the terminal logo
*terminal_settings_store_level_api* | [**update_terminal_settings_by_store_id**](./TerminalSettingsStoreLevelApi.md#update_terminal_settings_by_store_id) | **PATCH** /stores/{storeId}/terminalSettings | Update terminal settings
*terminal_settings_terminal_level_api* | [**get_terminal_logo**](./TerminalSettingsTerminalLevelApi.md#get_terminal_logo) | **GET** /terminals/{terminalId}/terminalLogos | Get the terminal logo
*terminal_settings_terminal_level_api* | [**get_terminal_settings**](./TerminalSettingsTerminalLevelApi.md#get_terminal_settings) | **GET** /terminals/{terminalId}/terminalSettings | Get terminal settings
*terminal_settings_terminal_level_api* | [**update_logo**](./TerminalSettingsTerminalLevelApi.md#update_logo) | **PATCH** /terminals/{terminalId}/terminalLogos | Update the logo
*terminal_settings_terminal_level_api* | [**update_terminal_settings**](./TerminalSettingsTerminalLevelApi.md#update_terminal_settings) | **PATCH** /terminals/{terminalId}/terminalSettings | Update terminal settings
*terminals_terminal_level_api* | [**list_terminals**](./TerminalsTerminalLevelApi.md#list_terminals) | **GET** /terminals | Get a list of terminals
*users_company_level_api* | [**list_users**](./UsersCompanyLevelApi.md#list_users) | **GET** /companies/{companyId}/users | Get a list of users
*users_company_level_api* | [**get_user_details**](./UsersCompanyLevelApi.md#get_user_details) | **GET** /companies/{companyId}/users/{userId} | Get user details
*users_company_level_api* | [**update_user_details**](./UsersCompanyLevelApi.md#update_user_details) | **PATCH** /companies/{companyId}/users/{userId} | Update user details
*users_company_level_api* | [**create_new_user**](./UsersCompanyLevelApi.md#create_new_user) | **POST** /companies/{companyId}/users | Create a new user
*users_merchant_level_api* | [**list_users**](./UsersMerchantLevelApi.md#list_users) | **GET** /merchants/{merchantId}/users | Get a list of users
*users_merchant_level_api* | [**get_user_details**](./UsersMerchantLevelApi.md#get_user_details) | **GET** /merchants/{merchantId}/users/{userId} | Get user details
*users_merchant_level_api* | [**update_user**](./UsersMerchantLevelApi.md#update_user) | **PATCH** /merchants/{merchantId}/users/{userId} | Update a user
*users_merchant_level_api* | [**create_new_user**](./UsersMerchantLevelApi.md#create_new_user) | **POST** /merchants/{merchantId}/users | Create a new user
*webhooks_company_level_api* | [**remove_webhook**](./WebhooksCompanyLevelApi.md#remove_webhook) | **DELETE** /companies/{companyId}/webhooks/{webhookId} | Remove a webhook
*webhooks_company_level_api* | [**list_all_webhooks**](./WebhooksCompanyLevelApi.md#list_all_webhooks) | **GET** /companies/{companyId}/webhooks | List all webhooks
*webhooks_company_level_api* | [**get_webhook**](./WebhooksCompanyLevelApi.md#get_webhook) | **GET** /companies/{companyId}/webhooks/{webhookId} | Get a webhook
*webhooks_company_level_api* | [**update_webhook**](./WebhooksCompanyLevelApi.md#update_webhook) | **PATCH** /companies/{companyId}/webhooks/{webhookId} | Update a webhook
*webhooks_company_level_api* | [**set_up_webhook**](./WebhooksCompanyLevelApi.md#set_up_webhook) | **POST** /companies/{companyId}/webhooks | Set up a webhook
*webhooks_company_level_api* | [**generate_hmac_key**](./WebhooksCompanyLevelApi.md#generate_hmac_key) | **POST** /companies/{companyId}/webhooks/{webhookId}/generateHmac | Generate an HMAC key
*webhooks_company_level_api* | [**test_webhook**](./WebhooksCompanyLevelApi.md#test_webhook) | **POST** /companies/{companyId}/webhooks/{webhookId}/test | Test a webhook
*webhooks_merchant_level_api* | [**remove_webhook**](./WebhooksMerchantLevelApi.md#remove_webhook) | **DELETE** /merchants/{merchantId}/webhooks/{webhookId} | Remove a webhook
*webhooks_merchant_level_api* | [**list_all_webhooks**](./WebhooksMerchantLevelApi.md#list_all_webhooks) | **GET** /merchants/{merchantId}/webhooks | List all webhooks
*webhooks_merchant_level_api* | [**get_webhook**](./WebhooksMerchantLevelApi.md#get_webhook) | **GET** /merchants/{merchantId}/webhooks/{webhookId} | Get a webhook
*webhooks_merchant_level_api* | [**update_webhook**](./WebhooksMerchantLevelApi.md#update_webhook) | **PATCH** /merchants/{merchantId}/webhooks/{webhookId} | Update a webhook
*webhooks_merchant_level_api* | [**set_up_webhook**](./WebhooksMerchantLevelApi.md#set_up_webhook) | **POST** /merchants/{merchantId}/webhooks | Set up a webhook
*webhooks_merchant_level_api* | [**generate_hmac_key**](./WebhooksMerchantLevelApi.md#generate_hmac_key) | **POST** /merchants/{merchantId}/webhooks/{webhookId}/generateHmac | Generate an HMAC key
*webhooks_merchant_level_api* | [**test_webhook**](./WebhooksMerchantLevelApi.md#test_webhook) | **POST** /merchants/{merchantId}/webhooks/{webhookId}/test | Test a webhook
