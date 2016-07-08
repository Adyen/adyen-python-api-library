#!/bin/python

import unittest2 as unittest
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
from Adyen.exceptions import (
	AdyenAPICommunicationError,
    AdyenAPIAuthenticationError,
    AdyenAPIInvalidPermission,
    AdyenAPIValidationError, 
    AdyenInvalidRequestError,
    AdyenError
)
import datetime
import Adyen


class AdyenTest_HPP(AdyenTest):
	def setUp(self):
		super(AdyenTest_HPP, self).setUp()
		Adyen.hmac = HMAC

	def test_directory_lookup_NL(self):
		"""Test directory lookup in NL"""
		reference = self.get_reference("test_directory_lookup")
		sessionValidity = datetime.datetime.utcnow() + datetime.timedelta(days=1)
		sessionValidity = sessionValidity.strftime("%Y-%m-%dT%H:%M:%S%z")
		result = Adyen.hpp.directory_lookup( 
	        request = {
	            "countryCode":"NL",
	            "currencyCode":"EUR",
	            "merchantAccount":MERCHANT_ACCT,
	            "merchantReference":reference,
	            "paymentAmount":2000,
	            "sessionValidity":sessionValidity,
	            "skinCode":SKIN_CODE
	        })
		brand_code_list = [pm.brand_code for pm in result.payment_methods]
		self.assertTrue('ideal' in brand_code_list, "ideal not in "
			"result.payment_methods. result.payment_methods: %s" % (
				str(result.payment_methods)))

	def test_directory_lookup_DE(self):
		"""Test directory lookup in DE"""
		reference = self.get_reference("test_directory_lookup")
		sessionValidity = datetime.datetime.utcnow() + datetime.timedelta(days=1)
		sessionValidity = sessionValidity.strftime("%Y-%m-%dT%H:%M:%S%z")
		result = Adyen.hpp.directory_lookup( 
	        request = {
	            "countryCode":"DE",
	            "currencyCode":"EUR",
	            "merchantAccount":MERCHANT_ACCT,
	            "merchantReference":reference,
	            "paymentAmount":2000,
	            "sessionValidity":sessionValidity,
	            "skinCode":SKIN_CODE
	        })
		brand_code_list = [pm.brand_code for pm in result.payment_methods]
		self.assertTrue('directEbanking' in brand_code_list,
			"directEbanking not in result.payment_methods. "
			"result.payment_methods: %s" % (str(brand_code_list)))