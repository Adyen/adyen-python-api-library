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


class AdyenTest_Payout(AdyenTest):
	def payout_store(self):
		reference = self.get_reference("default_payout_store")
		result = Adyen.payout.store_detail(
			request = {
				"bank" : {
			        "iban" : "GB85TEST12345612345678",
			        "countryCode" : "GB",
			        "ownerName" : "A. Smith"
			    },
			    "reference":reference,
			    "recurring" : {
			        "contract" : "PAYOUT"
			    },
			    "shopperEmail" : "shopper@email.com",    
			    "shopperReference" : SHOPPER_REF
			})
		self.assertEquals(result.result_code,'Success')
		return result

	def default_payout_submit(self,recur_detail_ref):
		reference = self.get_reference("default_payout_submit")
		result = Adyen.payout.submit(
			request={
				"amount":{
					"value":1234,
					"currency":"EUR"
				},
				"reference":reference,
				"shopperEmail":"test@email.com",
				"shopper_Reference":SHOPPER_REF,
				"recurring":{
					"contract" : "PAYOUT"
				},
				"selected_recurring_detail_reference":recur_detail_ref
			})

		self.assertEquals(result.resultCode,'[payout-submit-received]')
		return result

	def default_payout_store_and_submit(self):
		reference = self.get_reference("default_payout_store_submit")
		result = Adyen.payout.store_detail_and_submit(
			request={
				"bank" : {
			        "iban" : "GB85TEST12345612345678",
			        "countryCode" : "GB",
			        "ownerName" : "A. Smith"
			    },
			    "recurring" : {
			        "contract" : "PAYOUT"
			    },
			    "reference":reference,
			    "shopperEmail" : "shopper@email.com",    
			    "shopperReference" : SHOPPER_REF,
			    "amount":{
			    	"value":1234,
			    	"currency":"EUR"
			    }
			})
		self.assertEquals(result.resultCode,'[payout-submit-received]')
		return result

	def default_payout_confirm(self,psp):
		result = Adyen.payout.confirm(
			request={
				"originalReference":psp
			})
		self.assertEquals(result.response,'[payout-confirm-received]')
		return result

	def test_standard_payout_flow_seperate_store_submit(self):
		recur_detail_ref = self.payout_store().recurringDetailReference
		psp = self.default_payout_submit(recur_detail_ref).psp
		self.default_payout_confirm(psp)

	def test_standard_payout_flow_single_store_and_submit(self):
		psp =self.default_payout_store_and_submit().psp
		self.default_payout_confirm(psp)

### Payout Third Party

	def third_party_payout_submit(self,recur_detail_ref):
		reference = self.get_reference("third_party_payout_submit")
		result = Adyen.payout.submit_third_party(
			request={
				"amount":{
					"value":1234,
					"currency":"EUR"
				},
				"reference":reference,
				"shopperEmail":"test@email.com",
				"shopper_Reference":SHOPPER_REF,
				"recurring":{
					"contract" : "PAYOUT"
				},
				"selected_recurring_detail_reference":recur_detail_ref
			})

		self.assertEquals(result.resultCode,'[payout-submit-received]')
		return result

	def third_party_payout_store_and_submit(self):
		reference = self.get_reference("third_party_payout_store_submit")
		result = Adyen.payout.store_detail_and_submit_third_party(
			request={
				"bank" : {
			        "iban" : "GB85TEST12345612345678",
			        "countryCode" : "GB",
			        "ownerName" : "A. Smith"
			    },
			    "recurring" : {
			        "contract" : "PAYOUT"
			    },
			    "reference":reference,
			    "shopperEmail" : "shopper@email.com",    
			    "shopperReference" : SHOPPER_REF,
			    "amount":{
			    	"value":1234,
			    	"currency":"EUR"
			    }
			})
		self.assertEquals(result.resultCode,'[payout-submit-received]')
		return result

	def third_party_payout_confirm(self,psp):
		result = Adyen.payout.confirm_third_party(
			request={
				"originalReference":psp
			})
		self.assertEquals(result.response,'[payout-confirm-received]')
		return result

	def test_thirdparty_payout_flow_seperate_store_submit(self):
		"""Test whole flow of third pary payout for storeDetail, submit, and
		confirm"""
		recur_detail_ref = self.payout_store().recurringDetailReference
		psp = self.third_party_payout_submit(recur_detail_ref).psp
		self.third_party_payout_confirm(psp)

	def test_thirdparty_payout_flow_single_store_and_submit(self):
		"""Test whole flow of third party payout for storeDetailAndSubmit, and
		confirm"""
		psp =self.third_party_payout_store_and_submit().psp
		self.third_party_payout_confirm(psp)


