#!/usr/bin/env python
# coding = utf-8
from selenium import webdriver
import unittest, time #引入unittest包 和time
from loan2.bdengji_case import DengJiPage

class Dengji(unittest.TestCase):
   
    def testCase(self):
      # 调用khdj模块chaxun
      DengJiPage.DengJiApi.khdj(self)

    def chaxunCase(self):
      # 调用chaxun模块
      DengJiPage.DengJiApi.chaxun(self)

    def xinzengCase(self):
      # 调用xinzeng模块
      DengJiPage.DengJiApi.xinzeng(self)
      DengJiPage.DengJiApi.xinzengxinxi(self)

    def SubmitCase(self):
      # 调用Submit模块
      DengJiPage.DengJiApi.Submit(self)

    def closeCase(self):
      # 调用quit模块
      DengJiPage.DengJiApi.quit(self)