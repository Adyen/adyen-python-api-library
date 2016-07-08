#!/bin/python

import unittest2 as unittest
import datetime
import Adyen
import ConfigParser
import os

config = ConfigParser.ConfigParser()
#When ran from runtests.py, need to include path for config file.
config_path = os.path.dirname(__file__) + "/config/test.ini"
config.read(config_path)



USRNAME = config.get("AdyenCredentials","username")
PASSWD = config.get("AdyenCredentials","password")
MERCHANT_ACCT = config.get("AdyenCredentials","merchant_account")
SHOPPER_REF = config.get("AdyenCredentials","shopper_reference")
STORE_PAYOUT_USR = config.get("AdyenCredentials","store_payout_username")
STORE_PAYOUT_PASS = config.get("AdyenCredentials","store_payout_password")
REVIEW_PAYOUT_USR = config.get("AdyenCredentials","review_payout_username")
REVIEW_PAYOUT_PASS = config.get("AdyenCredentials","review_payout_password")
SKIN_CODE = config.get("AdyenCredentials","skin_code")
HMAC = config.get("AdyenCredentials","hmac_key")


#In case I need to make some customization specifically for Adyen
class AdyenTest(unittest.TestCase):
    def __init__(self,methodName='runTest'):
        super(AdyenTest, self).__init__(methodName)
        self.testDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def get_reference(self, preface="LibTest"):
        if len(preface) > 64:
            raise ValueError("reference preface can't be more than 62 characters")
        return "||".join([preface, self.testDate])

    def setUp(self):
        #Root Level object
        self.AdyenObject = Adyen.Adyen()
        #Add module level credentials
        Adyen.username = USRNAME
        Adyen.password = PASSWD 
        Adyen.merchant_account = MERCHANT_ACCT
        Adyen.store_payout_username = STORE_PAYOUT_USR
        Adyen.store_payout_password = STORE_PAYOUT_PASS
        Adyen.review_payout_username = REVIEW_PAYOUT_USR
        Adyen.review_payout_password = REVIEW_PAYOUT_PASS

        #Add instance level credentials
        self.AdyenObject.username = USRNAME
        self.AdyenObject.password = PASSWD
        self.AdyenObject.merchant_account = MERCHANT_ACCT
        self.AdyenObject.store_payout_username = STORE_PAYOUT_USR
        self.AdyenObject.store_payout_password = STORE_PAYOUT_PASS
        self.AdyenObject.review_payout_username = REVIEW_PAYOUT_USR
        self.AdyenObject.review_payout_password = REVIEW_PAYOUT_PASS
