import time
import os
import datetime
import unittest
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
import initialization

class Login_Test(unittest.TestCase):


    def setUp(self):
        initialization.setUp(self)

    def User_Login(self):
        driver=self.driver

        print("**************** 进入登录页面 ****************")
        driver.find_element_by_id('com.modernsky.istv:id/lin_view_me').click()
        time.sleep(1)
        print("**************** 判断是否登陆 ****************")
        #if driver.find_element_by_id('com.modernsky.istv:id/mLogin') :
        try:
            driver.find_element_by_id('com.modernsky.istv:id/loginName')
        except NoSuchElementException:
            driver.find_element_by_id('com.modernsky.istv:id/img_right_one').click()
            driver.find_element_by_id('com.modernsky.istv:id/mLogout').click()
            driver.find_element_by_id('android:id/button1').click()
            driver.find_element_by_id('com.modernsky.istv:id/lin_view_me').click()

        print("**************** 测试验证码登陆 ****************")
        driver.find_element_by_id('com.modernsky.istv:id/mEditPhone').send_keys('13147158922')
        driver.find_element_by_id('com.modernsky.istv:id/mEditPwd').send_keys('111111')
        time.sleep(1)
        driver.find_element_by_id('com.modernsky.istv:id/mLogin').click()
        time.sleep(2)
        driver.find_element_by_id('com.modernsky.istv:id/img_view_me').click()
        driver.find_element_by_id('com.modernsky.istv:id/img_right_one').click()
        driver.find_element_by_id('com.modernsky.istv:id/mLogout').click()
        driver.find_element_by_id('android:id/button1').click()
        driver.find_element_by_id('com.modernsky.istv:id/lin_view_me').click()
        print("**************** 测试密码登陆 ****************")
        driver.find_element_by_id('com.modernsky.istv:id/mChange').click()
        driver.find_element_by_id('com.modernsky.istv:id/mEditPhone').send_keys('13147158922')
        driver.find_element_by_id('com.modernsky.istv:id/mEditPwd').send_keys('hh123456')
        time.sleep(1)
        driver.find_element_by_id('com.modernsky.istv:id/mLogin').click()
        time.sleep(2)
        driver.find_element_by_id('com.modernsky.istv:id/img_view_me').click()
        driver.find_element_by_id('com.modernsky.istv:id/img_right_one').click()
        driver.find_element_by_id('com.modernsky.istv:id/mLogout').click()
        driver.find_element_by_id('android:id/button1').click()
