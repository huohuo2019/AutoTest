import os
import time
import unittest
import sys

from test_case import Test_Login
suite = unittest.TestSuite()
suite.addTest(Test_Login.Login_Test('User_Login'))
if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)