import os
import time
import unittest
from selenium import webdriver
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


def setUp(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.1'
    desired_caps['deviceName'] = 'af2cf409'
    desired_caps['appPackage'] = 'com.modernsky.istv'
    desired_caps['appActivity'] = 'com.modernsky.istv.ui.activity.LoadingActivity'
    desired_caps['noReset'] = True

    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(3)


def Login(self):
    driver=self.driver
    driver.find_element_by_id('com.modernsky.istv:id/lin_view_me').click()
    time.sleep(1)
    try:
        driver.find_element_by_id('com.modernsky.istv:id/txt_bar_title')
    except NoSuchElementException:
        driver.find_element_by_id('com.modernsky.istv:id/mChange').click()
        driver.find_element_by_id('com.modernsky.istv:id/mEditPhone').send_keys('13147158922')
        driver.find_element_by_id('com.modernsky.istv:id/mEditPwd').senf_keys('hh123456')
        driver.find_element_by_id('com.modernsky.istv:id/mLogin').click()