import Adyen
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_adyen_api_key():
    adyen_api_key = os.environ.get("ADYEN_API_KEY")

    if not adyen_api_key:
        raise Exception("Missing ADYEN_API_KEY in .env")

    return adyen_api_key

def get_adyen_merchant_account():
    adyen_merchant_account = os.environ.get("ADYEN_MERCHANT_ACCOUNT")

    if not adyen_merchant_account:
        raise Exception("Missing ADYEN_MERCHANT_ACCOUNT in .env")

    return adyen_merchant_account


adyen = Adyen.Adyen()
adyen.payment.client.xapikey = get_adyen_api_key()
adyen.payment.client.platform = "test" # change to live for production
adyen.payment.client.merchant_account = get_adyen_merchant_account()

request = {}

request['amount'] = {"value": "1000", "currency": "EUR"}
request['reference'] = f"Reference test"  # provide your unique payment reference
# set redirect URL required for some payment methods
request['returnUrl'] = f"/redirect?shopperOrder=myRef"
request['countryCode'] = "NL"

result = adyen.management.get_list_of_merchant_accounts()
#result = adyen.management.activate_merchant_accounts(path_param="AntoniStroinski") #API Exception 422, resource not found
# result = adyen.management.create_merchant_account({
#   "companyId": "AdyenTechSupport",
#   "legalEntityId": "LE322KH223222D5FJ89349536",
#   "businessLineId": "SE322KT223222D5FJ7TJN2986",
#   "description": "Testing API account",
#   "reference": "AntoniStroinski2"
# }) Not implemented as well
print(result)

