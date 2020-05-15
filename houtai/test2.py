# coding = utf-8
import unittest, time #引入unittest包 和time库
from selenium import webdriver
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner #引入 HTMLTestRunner 包

driver = webdriver.Chrome()
driver.get('http://vbuat.appgw.livibank.com/mock/repaymentActiveApply?enterpriseCode=SME422&repaymentAmount=10.10&repaymentType=2&businessId=88811211&businessType=1&repaymentBank=nnn&repaymentAccountName=name&repaymentAccount=12348400000002301013&currency=USD&appId=123&token=123')
driver.get('http://vbuat.appgw.livibank.com/mock/repaymentActiveApply?enterpriseCode=SME422&repaymentAmount=11.10&repaymentType=2&businessId=88811211&businessType=1&repaymentBank=nnn&repaymentAccountName=name&repaymentAccount=12348400000002301013&currency=USD&appId=123&token=123')
driver.get('http://vbuat.appgw.livibank.com/mock/repaymentActiveApply?enterpriseCode=SME422&repaymentAmount=12.10&repaymentType=2&businessId=88811211&businessType=1&repaymentBank=nnn&repaymentAccountName=name&repaymentAccount=12348400000002301013&currency=USD&appId=123&token=123')
driver.get('http://vbuat.appgw.livibank.com/mock/repaymentActiveApply?enterpriseCode=SME422&repaymentAmount=13.10&repaymentType=2&businessId=88811211&businessType=1&repaymentBank=nnn&repaymentAccountName=name&repaymentAccount=12348400000002301013&currency=USD&appId=123&token=123')
driver.get('http://vbuat.appgw.livibank.com/mock/repaymentActiveApply?enterpriseCode=SME422&repaymentAmount=14.10&repaymentType=2&businessId=88811211&businessType=1&repaymentBank=nnn&repaymentAccountName=name&repaymentAccount=12348400000002301013&currency=USD&appId=123&token=123')
driver.get('http://vbuat.appgw.livibank.com/mock/repaymentActiveApply?enterpriseCode=SME422&repaymentAmount=15.10&repaymentType=2&businessId=88811211&businessType=1&repaymentBank=nnn&repaymentAccountName=name&repaymentAccount=12348400000002301013&currency=USD&appId=123&token=123')
driver.get('http://vbuat.appgw.livibank.com/mock/repaymentActiveApply?enterpriseCode=SME422&repaymentAmount=16.10&repaymentType=2&businessId=88811211&businessType=1&repaymentBank=nnn&repaymentAccountName=name&repaymentAccount=12348400000002301013&currency=USD&appId=123&token=123')
driver.get('http://vbuat.appgw.livibank.com/mock/repaymentActiveApply?enterpriseCode=SME422&repaymentAmount=17.10&repaymentType=2&businessId=88811211&businessType=1&repaymentBank=nnn&repaymentAccountName=name&repaymentAccount=12348400000002301013&currency=USD&appId=123&token=123')
driver.get('http://vbuat.appgw.livibank.com/mock/repaymentActiveApply?enterpriseCode=SME422&repaymentAmount=18.10&repaymentType=2&businessId=88811211&businessType=1&repaymentBank=nnn&repaymentAccountName=name&repaymentAccount=12348400000002301013&currency=USD&appId=123&token=123')
driver.get('http://vbuat.appgw.livibank.com/mock/repaymentActiveApply?enterpriseCode=SME422&repaymentAmount=19.10&repaymentType=2&businessId=88811211&businessType=1&repaymentBank=nnn&repaymentAccountName=name&repaymentAccount=12348400000002301013&currency=USD&appId=123&token=123')

# driver.maximize_window() #将浏览器最大化显示
time.sleep(3)


