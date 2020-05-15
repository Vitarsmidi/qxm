#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time,datetime
import random
import string

url="http://172.17.255.228"
driver = webdriver.Firefox()
driver.get(url+":7080/login")
driver.find_element_by_id("loginId").send_keys("admin")
driver.find_element_by_id("password").send_keys("123456")
time.sleep(6)
##等待输入验证码
driver.find_element_by_id("subButton").click()
time.sleep(5)

driver.execute_script("addTab(\'/product/sporadic/list\',\'散标列表\')")
time.sleep(2)

driver.switch_to.frame("conframe")
time.sleep(1)

zichan=driver.find_element_by_xpath('//td[contains(@data-original-title,"添加车贷资产")]')
driver.execute_script("arguments[0].scrollIntoView(true);",zichan)
time.sleep(1)
driver.find_element_by_xpath('//td[@id="grid-pager_left"]/table/tbody/tr/td[last()]').click()
time.sleep(2)

##借款人信息
def get_random(counts):
    pre = "LLYCHEDAI"
    now = datetime.datetime.now().strftime('%m%d')
    li = string.digits
    sub = ''
    for n in range(0, int(counts)):
        sub += li[random.randint(0, len(li) - 1)]
    return pre + now + sub
driver.find_element_by_id("productName").send_keys(get_random(3))#借款名称
driver.find_element_by_id("amount").send_keys("1100")#借款金额
driver.find_element_by_id("annualRate").send_keys("7.6")#利率
driver.find_element_by_id("addAnnualRate").clear()
driver.find_element_by_id("addAnnualRate").send_keys("0.1")#加息利率
driver.find_element_by_id("deadline").send_keys("6")#期限
driver.find_element_by_id("borrowerName").send_keys(u"杨二")#借款人
driver.find_element_by_id("legalPerson").send_keys(u"企业法人甲")#企业法人

Select(driver.find_element_by_name("repayType")).select_by_visible_text("先息后本")#还款类型
Select(driver.find_element_by_id("productArea")).select_by_visible_text("默认")#指定专区
Select(driver.find_element_by_id("transferStatus")).select_by_visible_text("可转让")#是否转让
driver.find_element_by_id("transferDeadline").send_keys("1")#可转期限

driver.find_element_by_id("minAmount").clear()
driver.find_element_by_id("minAmount").send_keys("100")#最小投资金额
driver.find_element_by_id("maxAmount").clear()
driver.find_element_by_id("maxAmount").send_keys("200000")#最大投资金额
driver.find_element_by_id("increAmount").clear()
driver.find_element_by_id("increAmount").send_keys("1")#递增金额
driver.find_element_by_id("repayAmountPeriod").send_keys("44.68")#期还款金额1
driver.find_element_by_id("repayAmountPeriod2").clear()
driver.find_element_by_id("repayAmountPeriod2").send_keys("0")#期还款金额2

Select(driver.find_element_by_name("status")).select_by_visible_text("初始化")#状态
Select(driver.find_element_by_id("activityStatus")).select_by_visible_text("否")#是否参与活动
Select(driver.find_element_by_id("autoInvest")).select_by_visible_text("可以自动投资")#是否自动投资

driver.find_element_by_id("saleDeadline").clear()
driver.find_element_by_id("saleDeadline").send_keys("3")#售卖期限

#saleDeadline
Select(driver.find_element_by_id("idCardType")).select_by_visible_text("身份证")#证件类型
driver.find_element_by_id("idCardNo").send_keys("130622199408015363")#证件号码

def get_random(counts):
    pre = "JKHTBH"
    now = datetime.datetime.now().strftime('%Y%m%d')
    li = string.digits
    sub = ''
    for n in range(0, int(counts)):
        sub += li[random.randint(0, len(li) - 1)]
    return pre + now + sub
driver.find_element_by_id("contractNumber").send_keys(get_random(4))#合同编号

driver.find_element_by_id("valuationPledge").send_keys("2000")#抵押物估值
driver.find_element_by_id("loanAmount").send_keys("1100")#放款金额
driver.find_element_by_id("poundage").send_keys("16.57")#居间手续费
driver.find_element_by_id("recievedInterest").send_keys("45")#应收借款人利息
driver.find_element_by_id("receivingBank").send_keys("")#收款银行
driver.find_element_by_id("receivingAccount").send_keys("")#收款账户
driver.find_element_by_id("receivingName").send_keys("")#开户名称
driver.find_element_by_id("borrowerUse").send_keys(u"几款用途的撒大借款用途")#借款用途
##担保人信息

driver.find_element_by_id("guaranteeName").clear()
driver.find_element_by_id("guaranteeName").send_keys(u"河南县周龙生态有机畜牧业牧民专业合作社")#担保人
driver.find_element_by_id("guaranteeLegalPerson").clear()
driver.find_element_by_id("guaranteeLegalPerson").send_keys(u"担保人")#担保企业法人

Select(driver.find_element_by_id("gIdCardType")).select_by_visible_text("营业执照")#担保证件类型

driver.find_element_by_id("gIdCardNo").clear()
driver.find_element_by_id("gIdCardNo").send_keys("632324NAa00019X")#担保证件号码

def get_random(counts):
    pre = "DBHTBH"
    now = datetime.datetime.now().strftime('%Y%m%d')
    li = string.digits
    sub = ''
    for n in range(0, int(counts)):
        sub += li[random.randint(0, len(li) - 1)]
    return pre + now + sub
driver.find_element_by_id("gContractNumber").send_keys(get_random(6))#担保合同编号

driver.find_element_by_id("gReceivingBank").send_keys("")#收/付款银行
driver.find_element_by_id("gReceivingAccount").send_keys("")#收/付款账号
driver.find_element_by_id("gReceivingName").send_keys("")#开户名称
driver.find_element_by_name("address").clear()
driver.find_element_by_name("address").send_keys(u"大沙发案发时打完")

##借款信息

jiekuan=driver.find_element_by_xpath('//form[@id="productCarForm"]/div[3]/div/div[2]/span/div[2]/div[3]/div[2]')
driver.execute_script("arguments[0].scrollIntoView(true);",jiekuan)
driver.find_element_by_xpath('//div[@class="note-editable panel-body"]').send_keys(u"的撒开具合法后肺癌哦好急哦盎司附近哦是")#借款信息
time.sleep(2)
##担保措施与项目风险评估
fengkong=driver.find_element_by_xpath('//form[@id="productCarForm"]/div[4]/div/div[2]/div[2]/div[3]/div[3]')
driver.execute_script("arguments[0].scrollIntoView(true);",fengkong)
time.sleep(1)
#driver.find_element_by_xpath('//form[@class="productCarForm"]/div[4]/div/div[2]/div[2]/div[3]/div[3]').clear()
driver.find_element_by_xpath('//div[@class="note-editable panel-body"]').clear()
time.sleep(1)
driver.find_element_by_xpath('//div[@class="note-editable panel-body"]').send_keys(u"未发现借款人异常情况，且本项目是以车辆为质押的借款，如借款到期之后，借款人若无力偿还，担保方将会按合同处置质押物，以保障借款人的权益。")#担保措施与项目风险评估
#上传图片
driver.find_element_by_id("informationFile").send_keys("E:\\biaoti.jpg")#信息认证扫描件
driver.find_element_by_id("informationNoMosaicFile").send_keys("E:\\biaoti.jpg")#信息认证扫描件（非打码）
driver.find_element_by_id("contractFile").send_keys("E:\\biaoti.jpg")#合同扫描件
driver.find_element_by_id("contractMosaicFile").send_keys("E:\\biaoti.jpg")#合同扫描件（非打码）
#上传附件
driver.find_element_by_id("imageRarFile").send_keys("E:\\fujian.rar")#添加影像包
time.sleep(2)
#保存提交

driver.execute_script("arguments[0].scrollIntoView(true);",driver.find_element_by_xpath('//input[@value="保存"]'))
driver.find_element_by_xpath('//input[@value="保存"]').click()