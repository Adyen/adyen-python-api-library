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
import Adyen3
#Used for testing Recurring Authorization
from test_recurring import AdyenTest_Recurring


class AdyenTest_Payments(AdyenTest):

	def test_exception_API_no_credentials(self):
		"""Test basic auth without any credentials"""
		Adyen.username = None
		Adyen.password = None
		self.AdyenObject.username = None
		self.AdyenObject.password = None
		reference = self.get_reference("test_API_no_credentials")
		with self.assertRaises(AdyenAPIInvalidPermission):
			result = self.AdyenObject.payment.authorise(
				request= {
					'amount': {
						'value':100,
						'currency': 'USD'
					},
					'reference':reference,
					'card': {
						#Required
						'expiry_month':06,
						'expiry_year':2016,
						'number':'4111-1111-1111-1111',
						'holder_name':'John Doe',
						'cvc':737
					},
					'merchant_account':MERCHANT_ACCT
				}
			)
		self.AdyenObject.username = USRNAME
		self.AdyenObject.password = PASSWD
		Adyen.username = USRNAME
		Adyen.password = PASSWD


	def test_exception_API_incorrect_credentials(self):
		"""Test basic auth with incorrect credentials"""
		Adyen.username = "bob"
		Adyen.password = "bob"
		self.AdyenObject.username = "bob"
		self.AdyenObject.password = "bob"
		reference = self.get_reference("test_API_incorrect_credentials")
		with self.assertRaises(AdyenAPIAuthenticationError):
			result = self.AdyenObject.payment.authorise(
				request= {
					'amount': {
						'value':100,
						'currency': 'USD'
					},
					'reference':reference,
					'card': {
						#Required
						'expiry_month':06,
						'expiry_year':2016,
						'number':'4111-1111-1111-1111',
						'holder_name':'John Doe',
						'cvc':737
					},
					'merchant_account':MERCHANT_ACCT
				}
			)
		self.AdyenObject.username = USRNAME
		self.AdyenObject.password = PASSWD
		Adyen.username = USRNAME
		Adyen.password = PASSWD


	def test_exception_API_card_auth_no_merchant(self):
		"""Test basic card authorization with no merchant set"""
		Adyen.merchant_account = None

		self.AdyenObject.merchant_account = None

		reference = self.get_reference("test_API_card_auth_no_merchant")
		with self.assertRaises(AdyenInvalidRequestError) as cm:
			result = self.AdyenObject.payment.authorise(
				request= {
					'amount': {
						'value':100,
						'currency': 'USD'
					},
					'reference':reference,
					'card': {
						#Required
						'expiry_month':06,
						'expiry_year':2016,
						'number':'4111-1111-1111-1111',
						'holder_name':'John Doe',
						'cvc':737
					}
				}
			)

		Adyen.merchant_account = MERCHANT_ACCT
		self.AdyenObject.merchant_account = MERCHANT_ACCT


	def test_API_card_auth_merchant_in_request(self):
		"""Test basic card authorization with merchant in request body"""

		Adyen.merchant_account = None
		self.AdyenObject.merchant_account = None
		reference = self.get_reference("test_API_card_auth_merchant_in_request")
		result = self.AdyenObject.payment.authorise(
			request= {
				'amount': {
					'value':100,
					'currency': 'USD'
				},
				'reference':reference,
				'card': {
					#Required
					'expiry_month':06,
					'expiry_year':2016,
					'number':'4111-1111-1111-1111',
					'holder_name':'John Doe',
					'cvc':737
				},
				'merchant_account':MERCHANT_ACCT,
			}
		)
		#Checking camelCase and snake_case are matching
		self.assertEquals(result.psp_reference, result.pspReference,
			"Psp_reference did not equal pspReference. "
			"psp_reference = %s. pspReference = %s" % (result.psp_reference,
				result.pspReference))
		self.assertEquals(result.resultCode, "Authorised",
			"Test Payment wasn't authorised. PSP:%s" % (result.psp))

		Adyen.merchant_account = MERCHANT_ACCT
		self.AdyenObject.merchant_account = MERCHANT_ACCT

		#Used for other tests
		return result


	def test_API_card_auth_merchant_in_module(self):
		"""Test basic card authorization with merchant set at module level"""

		self.AdyenObject.merchant_account = None

		reference = self.get_reference("test_API_card_auth_merchant_in_module")
		result = self.AdyenObject.payment.authorise(
			request= {
				'amount': {
					'value':100,
					'currency': 'USD'
				},
				'reference':reference,
				'card': {
					#Required
					'expiry_month':06,
					'expiry_year':2016,
					'number':'4111-1111-1111-1111',
					'holder_name':'John Doe',
					'cvc':737
				},
			}
		)
		#Checking camelCase and snake_case are matching
		self.assertEquals(result.psp_reference, result.pspReference,
			"psp_reference did not equal pspReference. psp_reference = %s. "
			"pspReference = %s" % ( result.psp_reference, result.pspReference))
		self.assertEquals(result.resultCode, "Authorised",
			"Test Payment wasn't authorised. PSP:%s" % (result.psp))

		self.AdyenObject.merchant_account = MERCHANT_ACCT


	def test_API_card_auth_merchant_in_instance(self):
		"""Test basic card authorization with merchant set at module level"""

		Adyen.merchant_account = None
		reference = self.get_reference("test_API_card_auth_merchant_in_module")
		result = self.AdyenObject.payment.authorise(
			request= {
				'amount': {
					'value':100,
					'currency': 'USD'
				},
				'reference':reference,
				'card': {
					#Required
					'expiry_month':06,
					'expiry_year':2016,
					'number':'4111-1111-1111-1111',
					'holder_name':'John Doe',
					'cvc':737
				}
			}
		)
		#Checking camelCase and snake_case are matching
		self.assertEquals(result.psp_reference, result.pspReference,
			"psp_reference did not equal pspReference. psp_reference = %s. "
			"pspReference = %s" % (result.psp_reference, result.pspReference))
		self.assertEquals(result.resultCode, "Authorised",
			"Test Payment wasn't authorised. PSP:%s" % (result.psp))

		Adyen.merchant_account = MERCHANT_ACCT


	def test_API_card_auth_AVS(self):
		"""Test passing in AVS for card auth"""

		reference = self.get_reference("test_API_card_auth_AVS")
		result = self.AdyenObject.payment.authorise(
			request = {
				#Required
				'amount': {
					'value':100,
					'currency': 'USD'
				},
				'reference':reference,
				'card':{
					#Required
					'expiry_month':06,
					'expiry_year':2016,
					'number':'4400000000000008',
					'holder_name':'John Doe',
					'cvc':737
				},
				'billing_address':{
					'street':'Jump Street',
					'house_number_or_name': '1',
					'postalCode' : '95014',
					'city':'Nowhereville',
					'state_or_province':'CA',
					'country':'US'
				}
			}
		)

		self.assertEquals(result.resultCode, "Authorised",
			"Test Payment wasn't authorised. PSP:%s" % (result.psp))
		self.assertEquals(result.additionalData.avsResultRaw, "7",
			"Received Unexpected result for AVS test. avsResultRaw:%s" % (
				result.additionalData.avsResultRaw))


	def test_API_SEPA_auth(self):
		"""Test SEPA authorization"""

		reference = self.get_reference("test_API_SEPA_auth")
		result = self.AdyenObject.payment.authorise(
			request = {
				'amount': {
					'value':100,
					'currency': 'EUR'
				},
				'reference':reference,
				'bankAccount':{
					'iban':'NL13TEST0123456789',
					'owner_name':'John Doe',
					'countryCode':'NL'
				},
				"selected_brand":"sepadirectdebit"
			}
		)

		self.assertEquals(result.resultCode, "Received",
			"Test Payment didn't return Received resultCode. PSP:%s" % (
				result.psp))
		self.assertTrue(result.additionalData['sepadirectdebit.mandateId'])


	def test_API_create_recurring_card_with_auth(self):
		"""Test creating a recurring card contract with 0-auth"""
		reference = self.get_reference("test_API_create_recurring_card")
		result = self.AdyenObject.payment.authorise(
			request = {
				#Required
				'amount': {
					'value':0,
					'currency': 'USD'
				},
				'reference':reference,
				'shopper_email':'test@adyen.com',
				'recurring':{
					'contract':'RECURRING,ONECLICK'
				},
				'shopper_reference':SHOPPER_REF,
				'card':{
					#Required
					'expiry_month':06,
					'expiry_year':2016,
					'number':'4111-1111-1111-1111',
					'holder_name':'John Doe',
					'cvc':737
				}
			}
		)

		self.assertEquals(result.resultCode, "Authorised")

	def test_recurring_auth(self):
		"""Test recurring authorization with recurring detail reference"""

		reference = self.get_reference("test_recurring_auth")
		at_recur = AdyenTest_Recurring("test_list_recurring_detail")
		at_recur.setUp()
		lrd_results = at_recur.test_list_recurring_detail()
		self.assertTrue(hasattr(lrd_results, "recurringDetails"), "Expected results "
			"from list recurring details call. Received %s" % (
				lrd_results.message))
		recurring_detail = lrd_results.recurringDetails[0]
		recur_detail_ref = recurring_detail.recurringDetailReference
		contract = recurring_detail.contractTypes[1]
		result = self.AdyenObject.payment.authorise(
			request = {
				#Required
				'amount':{
					'currency': 'USD',
					'value': 1000
				},
				'reference':reference,
				'selected_recurring_detail_reference':recur_detail_ref,
				'shopper_interaction':'ContAuth',
				'recurring':{
					"contract" : contract
				},
				'shopper_email':'test@adyen.com',
				'shopper_reference':SHOPPER_REF
			}
		)

		self.assertEquals(result.resultCode, "Authorised")

	def test_exception_recurring_auth_incorrect_details(self):
		"""Test recurring authorization with incorrect shopper reference"""

		reference = self.get_reference(
			"test_exception_recurring_auth_incorrect_details")
		with self.assertRaises(AdyenAPIValidationError):
			result = self.AdyenObject.payment.authorise(
				request = {
					"amount":{
						"currency":"USD",
						"value": 1000
					},
					'reference':reference,
					'selected_recurring_detail_reference':"Non Existant Shopper",
					'shopper_interaction':'ContAuth',
					'recurring':{
						"contract" : "RECURRING"
					},
					'shopper_email':'test@adyen.com',
					'shopper_reference':SHOPPER_REF
				}
			)

	def test_modification_capture(self):
		"""Test capture modification"""

		reference = self.get_reference("test_modification_capture")
		auth_result = self.test_API_card_auth_merchant_in_request()
		result = self.AdyenObject.payment.capture(
			request = {
				'modificationAmount':{
					'currency':'USD',
					'value':100
				},
				'originalReference': auth_result.psp,
				#optional
				'reference':reference
			}
		)

		self.assertEquals(result.response,"[capture-received]")

	def test_modification_refund(self):
		"""Test refund modification"""

		reference = self.get_reference("test_modification_refund")
		auth_result = self.test_API_card_auth_merchant_in_request()
		result = self.AdyenObject.payment.refund(
			request = {
				'modificationAmount':{
					'currency':'USD',
					'value':100
				},
				'originalReference': auth_result.psp,
				#optional
				'reference':reference
			}
		)

		self.assertEquals(result.response,"[refund-received]")
