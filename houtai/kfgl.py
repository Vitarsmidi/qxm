# coding = utf-8
import unittest, time #引入unittest包 和time库
from selenium import webdriver
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner #引入 HTMLTestRunner 包
from time import sleep

driver = webdriver.Chrome()
driver.get('http://smeim.vbuat.livibank.com/')
driver.maximize_window() #将浏览器最大化显示
sleep(1)
driver.find_element_by_id("loginid").clear()
driver.find_element_by_name("loginid").send_keys("uattest19")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("uatP@ssw0rd")
driver.find_element_by_name("validateCode").send_keys("SJ")
driver.find_element_by_id("sub").click()
time.sleep(2)
driver.implicitly_wait(10)
driver.find_element_by_link_text("客户管理").click()  # link text,文字链接定位
driver.implicitly_wait(10)
driver.find_element_by_link_text("客户配置").click()  # link text,文字链接定位
driver.implicitly_wait(10)
# driver.switch_to_frame("conframe")  # 表单切换find_element_by_class_name()
driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
# driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@src='http://smeim.vbuat.livibank.com/merchantBasicInfo/list']"))
time.sleep(5)
driver.find_element_by_id("add-merchant-basic-info-btton").click()  # 点击新建
time.sleep(1)
driver.find_element_by_id("enterpriseNameEn").send_keys("411kj")
# driver.find_element_by_id("enterpriseCode").send_keys("4353452")
driver.find_element_by_id("suppliersCode").send_keys("ID2253452")
driver.find_element_by_id("brId").send_keys("4353452")
driver.find_element_by_id("ciId").send_keys("4354353")
driver.find_element_by_id("street").send_keys("望京路望京大厦103")#注册地址
driver.find_element_by_id("registerAddressEn").send_keys("China")#注册地址（英文）registerCity
# driver.find_element_by_id("registerCity").find_element_by_xpath("//option[@value='1']").click()  # 注册地
driver.find_element_by_id("registerCity").find_elements_by_tag_name("option")[1].click() # 注册地
# driver.find_element_by_id("vehicleBrandId").find_elements_by_tag_name("option")[1].click()  #
# 去掉js属性
js = 'document.getElementById("registerDate").removeAttribute("readonly");'
driver.execute_script(js)
# js添加时间
js_value = 'document.getElementById("registerDate").value="2015-12-10"'
driver.execute_script(js_value)
# driver.find_element_by_id("enterpriseType").find_element_by_xpath("//option[@value='1']").click()  # 企业类型
driver.find_element_by_id("enterpriseType").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("busiCountry").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("busiAddressStreet").send_keys("望京路望京大厦103")#
driver.find_element_by_id("postalAddressStreet").send_keys("望京路望京大厦103")#
driver.find_element_by_id("phone1").send_keys("13713587535")#
driver.find_element_by_id("email1").send_keys("834412915@qq.com")#

js = 'document.getElementById("ccraInvalid").removeAttribute("readonly");'
driver.execute_script(js)
# js添加时间
js_value = 'document.getElementById("ccraInvalid").value="2020-12-10"'
driver.execute_script(js_value)

js = 'document.getElementById("tuInvalid").removeAttribute("readonly");'
driver.execute_script(js)
# js添加时间
js_value = 'document.getElementById("tuInvalid").value="2020-12-10"'
driver.execute_script(js_value)

driver.find_element_by_id("crsDeclareAdress").send_keys("北京")
driver.find_element_by_id("isGroupUser").find_elements_by_tag_name("option")[2].click()
driver.find_element_by_id("connectedParty").find_elements_by_tag_name("option")[2].click()
driver.find_element_by_id("isGovernmentAgency").find_elements_by_tag_name("option")[2].click()
driver.find_element_by_id("isStateOwnedEnterprise").find_elements_by_tag_name("option")[2].click()
driver.find_element_by_id("isListedCompany").find_elements_by_tag_name("option")[2].click()
driver.find_element_by_id("cra").find_elements_by_tag_name("option")[3].click()
driver.find_element_by_id("str").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_name("complexStructure").find_elements_by_tag_name("option")[2].click()

driver.find_element_by_id("loanInfoType").find_elements_by_tag_name("option")[1].click()#贷款产品
driver.find_element_by_id("indusNature").find_element_by_xpath("//option[@value='80']").click()
driver.find_element_by_id("sellGoods").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("hkd").send_keys("85000000")
driver.find_element_by_id("employeeNum").find_elements_by_tag_name("option")[2].click()
driver.find_element_by_id("majorBuyers1").send_keys("天猫")#主要买家
driver.find_element_by_id("majorBuyersAddress1").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("majorSuppliers").send_keys("dj")
driver.find_element_by_id("majorSuppliersAddress").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("fundSource").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("fundSourceAddress").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("predictAnnualFiancialAmt").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("currency").find_element_by_xpath("//option[@value='USD']").click()
driver.find_element_by_id("predictAnnualFiancialTimes").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("majorReceiptRpymForms").find_element_by_xpath("//option[@value='1']").click()
driver.find_element_by_id("majorReceiptRpymChannel").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("payPriod").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("openAcctReason").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("repayFundsSource").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("lastYearTransAmt").send_keys("6000000")#贸易金额(上一年
driver.find_element_by_id("cooperateYearsJdhk").send_keys("3")
driver.find_element_by_id("custStatus").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("receiptBankCode").find_element_by_xpath("//option[@value='LIVIHKH0XXX']").click()
# driver.find_element_by_name("loanAuditMode").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_xpath(
    '//*[@id="add-merchant-basic-info-form"]/fieldset[3]/div[5]/div[1]/div/label[1]/input').click()  # 交易授权方式
time.sleep(1)
print('已自动填充客户信息完毕......')
# driver.quit()


