#!/usr/bin/env python
# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import loan3.BasePage

#继承BasePage类
class DengJiPage(loan3.BasePage.BasePage):

   ##定位器，登录元素定位
   khdj = (By.LINK_TEXT, '客户登记')
   searchUserName = (By.ID, 'searchUserName')
   searchBtn = (By.ID, 'searchBtn') #查询
   addBtn = (By.ID, 'addBtn') #新增
   userName = (By.ID, 'userName') #新增用户名
   mobile = (By.ID, 'mobile')
   applyAmount = (By.ID, 'applyAmount')
   idCard = (By.ID, 'idCard')
   source = (By.ID, 'source')
   idCardType = (By.ID, 'idCardType')
   purpose = (By.ID, 'purpose')
   submitOrder = (By.CLASS_NAME, 'submitOrder') #提交 class ="submitOrder"
   definite = (By.CLASS_NAME, 'layui-layer-btn0') #确定提交
   definite2 = (By.CLASS_NAME, 'layui-layer-btn0')

   ##页面操作，通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
   # 点击'客户登记'：调用send_keys对象，点击登录
   def click_khdj(self):
     self.find_element(*self.khdj).click()

   # 输入用户名：调用send_keys对象，输入用户名
   def input_searchUserName(self, searchUserName):
     self.find_element(*self.searchUserName).clear()
     self.find_element(*self.searchUserName).send_keys(searchUserName) #searchUserName在DengJiCase定义

   # 点击查询：调用send_keys对象，点击查询
   def click_searchBtn(self):
       self.find_element(*self.searchBtn).click()

   # 点击新增：调用send_keys对象
   def click_addBtn(self):
       self.find_element(*self.addBtn).click()

   # 输入用户名：调用send_keys对象，输入用户名
   def input_userName(self, userName):
     self.find_element(*self.userName).clear()
     self.find_element(*self.userName).send_keys(userName) #userName在DengJiCase定义

   # 输入mobile
   def input_mobile(self, mobile):
     self.find_element(*self.mobile).clear()
     self.find_element(*self.mobile).send_keys(mobile)

   # 输入applyAmount
   def input_applyAmount(self, applyAmount):
     self.find_element(*self.applyAmount).clear()
     self.find_element(*self.applyAmount).send_keys(applyAmount)

   # 输入idCard
   def input_idCrd(self, idCard):
     self.find_element(*self.idCard).clear()
     self.find_element(*self.idCard).send_keys(idCard)

   # 输入source
   def input_source(self):
     self.find_element(*self.source).find_elements_by_tag_name("option")[1].click()#客户来源
     # self.find_element(*self.source).find_element_by_xpath("//option[@value='1']").click()

   # 输入idCardType
   def input_idCardType(self):
     self.find_element(*self.idCardType).find_elements_by_tag_name("option")[1].click()#证件类型

   # 输入purpose
   def input_purpose(self):
     self.find_element(*self.purpose).find_elements_by_tag_name("option")[1].click()#

   # 输入submitOrder
   def input_submitOrder(self):
     self.find_element(*self.submitOrder).click() #提交

   # 输入definite
   def input_definite(self):
     self.find_element(*self.definite).click() ##确定提交

   # definite2
   def input_definite2(self):
     self.find_element(*self.definite2).click() ##确定


