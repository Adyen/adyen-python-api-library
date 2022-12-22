install:
	@pip install requests pycurl mock coveralls pylint pycodestyle

tests:
	@python -m unittest discover -s test -p '*Test.py'

coverage:
	@coverage run -m unittest discover -s test -p '*Test.py'


generator:=python
openapi-generator-cli:=java -jar openapi-generator-cli-6.0.1.jar
services:=balancePlatform binlookup checkout dataProtection legalEntityManagement management payments payouts platformsAccount platformsFund platformsHostedOnboardingPage platformsNotificationConfiguration recurring storedValue terminalManagement transfer

binlookup: spec=BinLookupService-v52
checkout: spec=CheckoutService-v69
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

$(services): build/spec
	rm -rf Adyen/services/$@_dir
	$(openapi-generator-cli) generate \
		-i build/spec/json/$(spec).json \
		-g $(generator) \
		-c ./templates/config.yaml \
		-o build \
		--global-property apis,apiTests=false,apiDocs=false,supportingFiles=api-single.py\
		--additional-properties serviceName=$@
	mkdir -p Adyen/services
	cp build/api/api-single.py Adyen/services/$@.py
	cp -r build/openapi_client/api Adyen/services/$@_dir
	touch Adyen/services/$@_dir/__init__.py
	touch Adyen/services/__init__.py
	rm -rf build

build/spec:
	git clone https://github.com/Adyen/adyen-openapi.git build/spec
	sed -i 's/"openapi" : "3.[0-9].[0-9]"/"openapi" : "3.0.0"/' build/spec/json/*.json


