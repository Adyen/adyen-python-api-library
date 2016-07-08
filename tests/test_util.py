#!/bin/python

import unittest2 as unittest
from Adyen.util import (
	dotdict, 
	underscore_to_camelcase,
	camelcase_to_underscore,
	under_to_camel_dict,
	camelcase_to_underscore,
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
	def test_dict_to_dotdict(self):
		"""Test dict to dotdict conversion"""
		dict_obj = {
			"_0_level_1_dict":{
				"_0_level_2_array": [
					"_0_level_3_str",
					{
						"_0_level_4_str": "_0_level_4_str_str",
						"_0_level_4_int": 1
					}
				]
			},
			"_1_level_1_array":[
				{
					"_1_level_2_dict":{
						"_1_level_3_str":"_1_level_3_str_str"
					}
				}
			],
			"_2_level_1_str":"_2_level_1_str_str"
		}
		test_dotdict = dotdict(dict_obj)
		self.assertTrue(test_dotdict)
		self.assertEqual(
			dict_obj['_0_level_1_dict']['_0_level_2_array'][1]['_0_level_4_str'],
			test_dotdict._0_level_1_dict._0_level_2_array[1]._0_level_4_str,
			"Failed to access dotdict by dot notation")
		test_val = 1
		self.assertEqual(
			test_dotdict._0_level_1_dict._0_level_2_array[1]._0_level_4_int, 
			test_val,
			"Was not able to to pull %d from dotdict" % test_val)

	def test_underscore_to_camelcase(self):
		"""Test underscore to camelcase conversion"""
		under_name = "bob_1_test_obliques"
		camel_name = "bob1TestObliques"

		new_camel_name = underscore_to_camelcase(camel_name)
		new_under_name = underscore_to_camelcase(under_name)

		self.assertEqual(new_under_name, camel_name,
			"Was not able to convert %s to %s. created value: %s" % (under_name, 
				camel_name, new_under_name))
		self.assertEqual(new_camel_name, camel_name,
			"Camcelcased name changed from %s to %s." % (camel_name, 
				new_camel_name))

	def test_camelcase_to_underscore(self):
		"""Test camelcase to underscore conversion"""
		under_name = "bob_1_test_obliques"
		camel_name = "bob1TestObliques"

		new_camel_name = camelcase_to_underscore(camel_name)
		new_under_name = camelcase_to_underscore(under_name)

		self.assertEqual(new_camel_name, under_name,
			"Was not able to convert %s to %s. created value: %s" % (camel_name, 
				under_name, new_camel_name))
		self.assertEqual(new_under_name,  under_name,
			"Underscored name changed from %s to %s ." % (under_name, 
				new_under_name))

	def test_under_to_camel_dict(self):
		"""Test underscore to camelcase conversion"""
		test_dict = {
			"bob": {
				"bob_bob": [
				{
					"bob_bob_bob":"bob_bob_bob",
					"bob_bob_bob_2":{
						"bob_bob_bob_bob":"bob_bob_bob_bob"
					}
				}
				]
			}
		}
		test_camel_dict = under_to_camel_dict(test_dict)
		self.assertEqual(
			test_camel_dict["bob"]["bobBob"][0]["bobBobBob2"]["bobBobBobBob"],
			"bob_bob_bob_bob",
			"Unable to convert nested dict with underscored names to camelCase names")

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
