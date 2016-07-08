#!/bin/python

import unittest2 as unittest
import sys, os

from tests import (
	test_hpp, 
	test_payments, 
	test_payout, 
	test_recurring, 
	test_util
)

#This is necessary for the test modules to import Adyen
sys.path.insert(0, os.path.dirname(__file__))

if __name__ == '__main__':
	pyLib_testSuite = unittest.TestSuite()
	
	pyLib_testSuite.addTest(unittest.makeSuite(test_util.AdyenTest_Util))
	pyLib_testSuite.addTest(unittest.makeSuite(test_payments.AdyenTest_Payments))
	pyLib_testSuite.addTest(unittest.makeSuite(test_recurring.AdyenTest_Recurring))
	pyLib_testSuite.addTest(unittest.makeSuite(test_hpp.AdyenTest_HPP))
	pyLib_testSuite.addTest(unittest.makeSuite(test_payout.AdyenTest_Payout))

	testRunner = unittest.TextTestRunner()
	testRunner.run(pyLib_testSuite)

	

