#!/bin/python

import unittest2 as unittest
from Adyen.util import (
	generate_hpp_sig,
	_generate_signing_string
)
from testbase import (
	USRNAME,
	PASSWD,
	MERCHANT_ACCT,
	SHOPPER_REF,
	STORE_PAYOUT_USR,
	STORE_PAYOUT_PASS,
	REVIEW_PAYOUT_USR,
	REVIEW_PAYOUT_PASS,
	SKIN_CODE,
	HMAC,
	AdyenTest
)
import datetime

class AdyenTest_Util(AdyenTest):
	def test_generate_hppsig(self):
		"""Test signing string and merchant sig generation"""
		hmacKey = "8725128704DF6C9B048E38748DB3F9906ABC3A65A4C85EDA349D2F8C97496470"
		hpp_values = {
			"countryCode":"NL",
			"currencyCode":"EUR",
			"merchantAccount":"LucasBledsoe",
			"merchantReference":"TEST-PAYMENT-2016-06-20-21:43:22",
			"paymentAmount":"199",
			"sessionValidity":"2016-06-21T21:43:22+00:00",
			"shipBeforeDate":"2016-06-23",
			"shopperEmail":"lucas@adyen.com",
			"shopperLocale":"en_US",
			"skinCode":"NVUmTF7q"
		}

		merchant_sig = "Wrd2Dmmg3AU0AQeFtRb6QCOaXCZczmwvWGGmc01vG/I="
		signing_string = "countryCode:currencyCode:merchantAccount:"\
			"merchantReference:paymentAmount:sessionValidity:shipBeforeDate:"\
			"shopperEmail:shopperLocale:skinCode:NL:EUR:LucasBledsoe:"\
			"TEST-PAYMENT-2016-06-20-21\:43\:22:199:2016-06-21T21\:43\:22+00\:00:"\
			"2016-06-23:lucas@adyen.com:en_US:NVUmTF7q"

		gen_signing_string = _generate_signing_string(hpp_values)
		self.assertEqual(signing_string, gen_signing_string,
			"Generated signing string mismatch. created %s, expected %s" % (
				gen_signing_string, signing_string))

		gen_merchant_sig = generate_hpp_sig(hpp_values, hmacKey)
		self.assertEqual(gen_merchant_sig, merchant_sig,
			"Generated merchant signature mismatch. Generated %s, expected %s" % (
				gen_merchant_sig, merchant_sig))
