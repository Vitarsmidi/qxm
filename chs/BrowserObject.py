# -*- coding: utf-8 -*-
# @Time : 2020/5/7 14:41
# @Author : qxm
# @FileName: BrowserObject.py

from time import sleep
from selenium import webdriver
import unittest, os, sys


class UseBrowser(object):

    def setupChrome(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def setupFirfox(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def setupIE(self):
        self.driver = webdriver.Ie()
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True


    def teardownBrowser(self):
        self.driver.close()

