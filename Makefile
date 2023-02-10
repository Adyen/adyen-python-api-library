install:
	@pip install requests pycurl mock coveralls pylint pycodestyle

tests:
	@python -m unittest discover -s test -p '*Test.py'

coverage:
	@coverage run -m unittest discover -s test -p '*Test.py'


generator:=python
openapi-generator-cli:=java -jar build/openapi-generator-cli.jar
services:=balancePlatform checkout legalEntityManagement management payments payouts platformsAccount platformsFund platformsHostedOnboardingPage platformsNotificationConfiguration terminalManagement transfer
smallServices:=balanceControlService binlookup dataProtection recurring storedValue

binlookup: spec=BinLookupService-v52
checkout: spec=CheckoutService-v70
dataProtection: spec=DataProtectionService-v1
storedValue: spec=StoredValueService-v46
terminalManagement: spec=TfmAPIService-v1
payments: spec=PaymentService-v68
recurring: spec=RecurringService-v68
payouts: spec=PayoutService-v68
management: spec=ManagementService-v1
legalEntityManagement: spec=LegalEntityService-v2
balancePlatform: spec=BalancePlatformService-v2
platformsAccount: spec=AccountService-v6
platformsFund: spec=FundService-v6
platformsNotificationConfiguration: spec=NotificationConfigurationService-v6
platformsHostedOnboardingPage: spec=HopService-v6
transfer: spec=TransferService-v3
balanceControlService: spec=BalanceControlService-v1

$(services): build/spec
	wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.0.1/openapi-generator-cli-6.0.1.jar -O build/openapi-generator-cli.jar
	rm -rf Adyen/services/$@
	$(openapi-generator-cli) generate \
		-i build/spec/json/$(spec).json \
		-g $(generator) \
		-c ./templates/config.yaml \
		-o build \
		--global-property apis,apiTests=false,apiDocs=false,supportingFiles=api-single.py\
		--additional-properties serviceName=$@\
		--skip-validate-spec
	mkdir -p Adyen/services
	cp -r build/openapi_client/api Adyen/services/$@
	rm -f Adyen/services/$@/*-small.py
	cp build/api/api-single.py Adyen/services/$@/__init__.py
	rm -rf build

$(smallServices): build/spec
	wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.0.1/openapi-generator-cli-6.0.1.jar -O build/openapi-generator-cli.jar
	rm -rf Adyen/services/$@
	$(openapi-generator-cli) generate \
		-i build/spec/json/$(spec).json \
		-g $(generator) \
		-c ./templates/config.yaml \
		-o build \
		--global-property apis,apiTests=false,apiDocs=false\
		--additional-properties serviceName=$@\
		--skip-validate-spec
	mkdir -p Adyen/services
	cp build/openapi_client/api/general_api-small.py Adyen/services/$@.py
	rm -rf build


build/spec:
	git clone https://github.com/Adyen/adyen-openapi.git build/spec
	sed -i 's/"openapi" : "3.[0-9].[0-9]"/"openapi" : "3.0.0"/' build/spec/json/*.json
