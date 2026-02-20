install:
	@pip install requests pycurl mock coveralls pylint pycodestyle

tests:
	pytest

coverage:
	pytest --cov=Adyen


generator:=python
openapi-generator-version:=6.0.1
openapi-generator-url:=https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/$(openapi-generator-version)/openapi-generator-cli-$(openapi-generator-version).jar
openapi-generator-jar:=build/openapi-generator-cli.jar
openapi-generator-cli:=java -jar $(openapi-generator-jar)
output:=build/out
services:=balancePlatform checkout legalEntityManagement management payments payouts transfers
smallServices:=binlookup dataProtection recurring storedValue terminal disputes

all: $(services) $(smallServices)

binlookup: spec=BinLookupService-v52
checkout: spec=CheckoutService-v71
dataProtection: spec=DataProtectionService-v1
storedValue: spec=StoredValueService-v46
terminal: spec=TfmAPIService-v1
payments: spec=PaymentService-v68
recurring: spec=RecurringService-v68
payouts: spec=PayoutService-v68
management: spec=ManagementService-v3
legalEntityManagement: spec=LegalEntityService-v3
balancePlatform: spec=BalancePlatformService-v2
platformsAccount: spec=AccountService-v6
platformsFund: spec=FundService-v6
platformsNotificationConfiguration: spec=NotificationConfigurationService-v6
platformsHostedOnboardingPage: spec=HopService-v6
transfers: spec=TransferService-v4
balanceControlService: spec=BalanceControlService-v1
disputes: spec=DisputeService-v30

$(services): build/spec $(openapi-generator-jar)
	rm -rf Adyen/services/$@ $(output)
	$(openapi-generator-cli) generate \
		-i build/spec/json/$(spec).json \
		-g $(generator) \
		-c ./templates/config.yaml \
		-o $(output) \
		--global-property apis,apiTests=false,apiDocs=false,supportingFiles=api-single.py\
		--additional-properties serviceName=$@\
		--skip-validate-spec
	mkdir -p Adyen/services
	cp -r $(output)/openapi_client/api Adyen/services/$@
	rm -f Adyen/services/$@/*-small.py
	cp $(output)/api/api-single.py Adyen/services/$@/__init__.py


$(smallServices): build/spec $(openapi-generator-jar)
	rm -rf Adyen/services/$@ $(output)
	$(openapi-generator-cli) generate \
		-i build/spec/json/$(spec).json \
		-g $(generator) \
		-c ./templates/config.yaml \
		-o $(output) \
		--global-property apis,apiTests=false,apiDocs=false\
		--additional-properties serviceName=$@\
		--skip-validate-spec
	mkdir -p Adyen/services
	cp $(output)/openapi_client/api/*-small.py Adyen/services/$@.py



build/spec:
	git clone https://github.com/Adyen/adyen-openapi.git build/spec
	perl -i -pe's/"openapi" : "3.[0-9].[0-9]"/"openapi" : "3.0.0"/' build/spec/json/*.json

# Download the generator
$(openapi-generator-jar):
	wget --quiet -o /dev/null $(openapi-generator-url) -O $(openapi-generator-jar)


generateCheckoutTest: build/spec $(openapi-generator-jar)
	$(openapi-generator-cli) generate \
		-i build/spec/json/CheckoutService-v70.json \
		-g $(generator) \
		-c ./templates/config.yaml \
		-o $(output) \
		--global-property apis,apiTests=false,supportingFiles=api-test.py\
		--additional-properties serviceName=checkout \
		--skip-validate-spec
	cp $(output)/api/api-test.py test/methodNamesTests/checkoutTest.py
	rm -rf build


.PHONY: $(services)