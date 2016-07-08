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


class AdyenTest_Recurring(AdyenTest):
	def test_list_recurring_detail(self):
		"""Test list recurring detail call"""
		result = self.AdyenObject.recurring.list_recurring_details( 
			request ={
				'shopper_reference':SHOPPER_REF,
				'recurring':{
					'contract':'RECURRING'
				}
			}
		)

		self.assertTrue(result.shopperReference, "Did not receive a result.")

		#return result for other test functions uses.
		return result

	def test_empty_list_recurring_detail(self):
		"""Test list recurring detail call with non existant Shopper"""
		result = self.AdyenObject.recurring.list_recurring_details( 
			request ={
				'shopper_reference':'Non Existant Shopper',
				'recurring':{
					'contract':'RECURRING'
				}
			}
		)

		self.assertFalse(result.message, "Received a result when not expected.")
