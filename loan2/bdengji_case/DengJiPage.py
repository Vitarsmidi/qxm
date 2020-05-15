#!/usr/bin/env python
# coding = utf-8
import unittest, time
from loan2.bdengji_case import DengJiData #导入函数

# 通过两个变量，来接收调用函数
User,UserName,Mobile,Amount,IdCard= DengJiData.data()

class DengJiApi(unittest.TestCase):

   def khdj(self):
     driver = self.driver
     driver.implicitly_wait(30)
     driver.find_element_by_link_text("客户登记").click()  # link text,文字链接定位
     print('已打开客户登记......')
     time.sleep(0.5)

   def chaxun(self):
     driver = self.driver
     driver.implicitly_wait(30)
     driver.find_element_by_id("searchUserName").clear()
     driver.find_element_by_id("searchUserName").send_keys(User)
     driver.find_element_by_id("searchBtn").click()  # 搜索查询
     print('查询成功......')
     time.sleep(0.5)

   def xinzeng(self):
     driver = self.driver
     driver.implicitly_wait(30)
     driver.find_element_by_id("addBtn").click()  # 新增
     print('已打开新增窗口......')
     time.sleep(0.5)

   def xinzengxinxi(self):
     driver = self.driver
     driver.implicitly_wait(30)
     driver.find_element_by_id("userName").clear()
     driver.find_element_by_id("userName").send_keys(UserName)
     driver.find_element_by_id("mobile").clear()
     driver.find_element_by_id("mobile").send_keys(Mobile)
     driver.find_element_by_id("applyAmount").clear()
     driver.find_element_by_id("applyAmount").send_keys(Amount)
     driver.find_element_by_id("idCard").clear()
     driver.find_element_by_id("idCard").send_keys(IdCard)
     driver.find_element_by_id("source").find_element_by_xpath("//option[@value='1']").click()  # 下拉框选择
     # driver.find_element_by_id("vehicleBrandId").find_elements_by_tag_name("option")[1].click()  # 车辆品牌
     driver.find_element_by_id("idCardType").find_element_by_xpath("//option[@value='1']").click()  # 下拉框选择
     driver.find_element_by_id("purpose").find_element_by_xpath("//option[@value='1']").click()  # 下拉框选择
     print('新增信息填写完成......')
     time.sleep(0.5)

   def Submit(self):
     driver = self.driver
     driver.implicitly_wait(30)
     driver.find_element_by_class_name("submitOrder").click()
     time.sleep(0.5)
     driver.implicitly_wait(30)
     driver.find_element_by_class_name("layui-layer-btn0").click()
     time.sleep(0.5)
     driver.implicitly_wait(30)
     driver.find_element_by_class_name("layui-layer-btn0").click()
     print('已提交新增......')
     time.sleep(0.5)

   def quit(self):
     self.driver.quit()

