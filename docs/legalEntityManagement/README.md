## Documentation for API Endpoints

All URIs are relative to *https://kyc-test.adyen.com/lem/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*business_lines_api* | [**delete_business_line**](./BusinessLinesApi.md#delete_business_line) | **DELETE** /businessLines/{id} | Delete a business line
*business_lines_api* | [**get_business_line**](./BusinessLinesApi.md#get_business_line) | **GET** /businessLines/{id} | Get a business line
*business_lines_api* | [**update_business_line**](./BusinessLinesApi.md#update_business_line) | **PATCH** /businessLines/{id} | Update a business line
*business_lines_api* | [**create_business_line**](./BusinessLinesApi.md#create_business_line) | **POST** /businessLines | Create a business line
*documents_api* | [**delete_document**](./DocumentsApi.md#delete_document) | **DELETE** /documents/{id} | Delete a document
*documents_api* | [**get_document**](./DocumentsApi.md#get_document) | **GET** /documents/{id} | Get a document
*documents_api* | [**update_document**](./DocumentsApi.md#update_document) | **PATCH** /documents/{id} | Update a document
*documents_api* | [**upload_document_for_verification_checks**](./DocumentsApi.md#upload_document_for_verification_checks) | **POST** /documents | Upload a document for verification checks
*hosted_onboarding_api* | [**list_hosted_onboarding_page_themes**](./HostedOnboardingApi.md#list_hosted_onboarding_page_themes) | **GET** /themes | Get a list of hosted onboarding page themes
*hosted_onboarding_api* | [**get_onboarding_link_theme**](./HostedOnboardingApi.md#get_onboarding_link_theme) | **GET** /themes/{id} | Get an onboarding link theme
*hosted_onboarding_api* | [**get_link_to_adyenhosted_onboarding_page**](./HostedOnboardingApi.md#get_link_to_adyenhosted_onboarding_page) | **POST** /legalEntities/{id}/onboardingLinks | Get a link to an Adyen-hosted onboarding page
*legal_entities_api* | [**get_legal_entity**](./LegalEntitiesApi.md#get_legal_entity) | **GET** /legalEntities/{id} | Get a legal entity
*legal_entities_api* | [**get_all_business_lines_under_legal_entity**](./LegalEntitiesApi.md#get_all_business_lines_under_legal_entity) | **GET** /legalEntities/{id}/businessLines | Get all business lines under a legal entity
*legal_entities_api* | [**update_legal_entity**](./LegalEntitiesApi.md#update_legal_entity) | **PATCH** /legalEntities/{id} | Update a legal entity
*legal_entities_api* | [**create_legal_entity**](./LegalEntitiesApi.md#create_legal_entity) | **POST** /legalEntities | Create a legal entity
*terms_of_service_api* | [**get_terms_of_service_information_for_legal_entity**](./TermsOfServiceApi.md#get_terms_of_service_information_for_legal_entity) | **GET** /legalEntities/{id}/termsOfServiceAcceptanceInfos | Get Terms of Service information for a legal entity
*terms_of_service_api* | [**get_terms_of_service_status**](./TermsOfServiceApi.md#get_terms_of_service_status) | **GET** /legalEntities/{id}/termsOfServiceStatus | Get Terms of Service status
*terms_of_service_api* | [**accept_terms_of_service**](./TermsOfServiceApi.md#accept_terms_of_service) | **PATCH** /legalEntities/{id}/termsOfService/{termsofservicedocumentid} | Accept Terms of Service
*terms_of_service_api* | [**get_terms_of_service_document**](./TermsOfServiceApi.md#get_terms_of_service_document) | **POST** /legalEntities/{id}/termsOfService | Get Terms of Service document
*transfer_instruments_api* | [**delete_transfer_instrument**](./TransferInstrumentsApi.md#delete_transfer_instrument) | **DELETE** /transferInstruments/{id} | Delete a transfer instrument
*transfer_instruments_api* | [**get_transfer_instrument**](./TransferInstrumentsApi.md#get_transfer_instrument) | **GET** /transferInstruments/{id} | Get a transfer instrument
*transfer_instruments_api* | [**update_transfer_instrument**](./TransferInstrumentsApi.md#update_transfer_instrument) | **PATCH** /transferInstruments/{id} | Update a transfer instrument
*transfer_instruments_api* | [**create_transfer_instrument**](./TransferInstrumentsApi.md#create_transfer_instrument) | **POST** /transferInstruments | Create a transfer instrument
