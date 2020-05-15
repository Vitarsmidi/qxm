# -*- coding: utf-8 -*-
# @Time : 2020/4/2 20:57
# @Author  : qxm
# @FileName: xjkh.py

import os
import string

from random import random # random模块random() 函数生成随机数据
from time import sleep
from selenium import webdriver
from faker import Faker  #需安装faker模块，随机生成数据
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By #common.by.By 模块
import pandas as pd #数据导入及整理的模块

from houtai.configure import getConfig
from houtai.page import get_phone, get_element, get_alert, get_date, get_date2


def input_in():
    f = Faker('zh-cn')
    # starttime = datetime.datetime.now()
    d = webdriver.Chrome()
    d.maximize_window()
    d.implicitly_wait(50)#获取页面元素的超时隐式等待
    d.set_page_load_timeout(50)# 设置页面加载超时

    d.get('http://smeim.vbuat.livibank.com/')
    user = getConfig('SME', 'user')
    password = getConfig('SME', 'password')
    d.find_element_by_id('loginid').send_keys(user)
    d.find_element_by_id('password').send_keys(password)
    # d.find_element_by_xpath('//*[@id="login"]/input[7]').send_keys('sj')
    #d.find_element_by_name("validateCode").send_keys("SJ")
    #d.find_element_by_id('sub').click()
    sleep(6)
    d.implicitly_wait(10)

    get_element(d, (By.XPATH, '/html/body/div[2]/aside[1]/section/ul/li[14]/a/span[1]')).click()#客户管理（绝对路径）
    d.implicitly_wait(10)
    get_element(d, (By.XPATH, '/html/body/div[2]/aside[1]/section/ul/li[14]/ul/li/a/span')).click()#客户配置
    d.switch_to.frame(d.find_element_by_xpath('//*[@id="客户配置"]/iframe'))
    sleep(2)
    d.implicitly_wait(10)
    get_element(d, (By.ID, "add-merchant-basic-info-btton")).click()# 点击新建
    sleep(1)
    d.implicitly_wait(10)
    # name = (f.random_letter() + f.random_letter() + f.random_letter() + f.random_letter()).upper()#随机字母
    # name = ("SME42" + f.numerify()).upper()
    NAME = getConfig('SME', 'enterpriseCode')
    name = (NAME + f.numerify()).upper()
    # n=4101
    # s = str(n + 1)
    # st = s.zfill(4)
    # name = "SME" + str(st)
    # d.find_element_by_id('enterpriseCode').send_keys(name)
    d.find_element_by_xpath('//*[@id ="add-merchant-basic-info-form"]/fieldset[1]/div[1]/div[1]/div[1]/input').send_keys(name)
    sleep(0.5)
    d.find_element_by_id('enterpriseNameCn').send_keys(f.company_prefix() + name)#f.company_prefix()公司名前缀
    d.find_element_by_id('enterpriseNameEn').send_keys(f.month_name() + f.random_element() + f.random_letter())
    #f.random_element()：随机字母，# f.month_name()随机月份名字
    d.find_element_by_id('enterpriseDomesticName').send_keys(f.company())#f.company()公司类 国内企业名称
    d.find_element_by_id('suppliersCode').send_keys(f.random_number(digits=8))
    d.find_element_by_id('brId').send_keys(f.random_number(digits=10))#f.random_number()：随机数字
    d.find_element_by_id('ciId').send_keys(f.random_number(digits=8))
    # get_element(d, (By.XPATH, '//div[@class="city-title city-title1"]')).click()#相对路径索引定位
    get_element(d, (By.XPATH, '//*[@id="registerAddress"]/div[1]')).click()#相对路径索引定位
    sleep(1)
    d.implicitly_wait(5)
    get_element(d, (By.XPATH, '//*[@id="registerAddress"]/div[2]/div[2]/div[1]/a[2]')).click()
    get_element(d, (By.XPATH, '//*[@id="registerAddress"]/div[2]/div[2]/div[2]/a[1]')).click()
    get_element(d, (By.XPATH, '//*[@id="registerAddress"]/div[2]/div[2]/div[3]/a[1]')).click()
    get_element(d, (By.XPATH, '//*[@id="registerAddress"]/div[2]/div[2]/div[4]/a[1]')).click()
    d.find_element_by_id('street').send_keys(f.street_address())#fake.street_address()  # 随机街道
    d.find_element_by_id('registerAddressEn').send_keys("China")#注册地址（英文
    registerCity = d.find_element_by_id('registerCity')
    Select(registerCity).select_by_value('54462')

    js = 'document.getElementById("registerDate").removeAttribute("readonly");'
    d.execute_script(js)
    # re_id = d.find_element_by_id("registerDate")
    # re_id.clear()
    js_value = 'document.getElementById("registerDate").value="2015-12-10"'  # js添加时间
    d.execute_script(js_value)

    enterpriseType = d.find_element_by_id('enterpriseType')
    Select(enterpriseType).select_by_value('2')
    get_element(d, (By.XPATH, '//*[@id="busiAddress"]/div[1]')).click()
    sleep(1)
    get_element(d, (By.XPATH, '//*[@id="busiAddress"]/div[2]/div[2]/div[1]/a[3]')).click()
    get_element(d, (By.XPATH, '//*[@id="busiAddress"]/div[2]/div[2]/div[2]/a[1]')).click()
    d.find_element_by_id('busiAddressStreet').send_keys(f.street_address())
    busiCountry = d.find_element_by_id('busiCountry')
    Select(busiCountry).select_by_value('54462')
    get_element(d, (By.XPATH, '//*[@id="postalAddress"]/div[1]')).click()
    sleep(1)
    get_element(d, (By.XPATH, '//*[@id="postalAddress"]/div[2]/div[2]/div[1]/a[3]')).click()
    get_element(d, (By.XPATH, '//*[@id="postalAddress"]/div[2]/div[2]/div[2]/a[1]')).click()
    d.find_element_by_id('postalAddressStreet').send_keys(f.street_address())
    # d.find_element_by_id('phone1').send_keys("13713587535")
    # d.find_element_by_id('email1').send_keys('834412915@qq.com')
    phone1 = d.find_element_by_id('phone1')
    phone = getConfig('SME', 'phone')
    phone1.send_keys(phone)
    email1 = d.find_element_by_id('email1')
    email = getConfig('SME', 'email')
    email1.send_keys(email)

    js2 = 'document.getElementById("ccraInvalid").removeAttribute("readonly");'
    d.execute_script(js2)
    js_value2 = 'document.getElementById("ccraInvalid").value="%s";' % get_date2()
    d.execute_script(js_value2)

    js3 = 'document.getElementById("tuInvalid").removeAttribute("readonly");'
    d.execute_script(js3)
    js_value3 = 'document.getElementById("tuInvalid").value="%s";' % get_date2()
    d.execute_script(js_value3)

    d.find_element_by_id('crsDeclareAdress').send_keys(f.street_address())
    selec2 = d.find_element_by_id('isGroupUser')
    Select(selec2).select_by_value('2')#是否集团
    connectedParty = d.find_element_by_id('connectedParty')
    Select(connectedParty).select_by_value('2')
    # d.find_element_by_id('groupUserNo').send_keys(f.random_number(digits=7))#集团编号
    # d.find_element_by_id('groupUserName').send_keys(f.company_prefix())
    isGovernmentAgency = d.find_element_by_id('isGovernmentAgency')
    Select(isGovernmentAgency).select_by_value('2')
    isStateOwnedEnterprise = d.find_element_by_id('isStateOwnedEnterprise')
    Select(isStateOwnedEnterprise).select_by_value('1')
    isListedCompany = d.find_element_by_id('isListedCompany')
    Select(isListedCompany).select_by_value('1')
    cra_id = get_element(d, (By.ID, 'cra'))
    Select(cra_id).select_by_value('3')
    # pep_id = get_element(d, (By.ID, 'pep'))
    # Select(pep_id).select_by_value('1')
    str_id = get_element(d, (By.ID, 'str'))
    Select(str_id).select_by_value("1")
    complexStructure = get_element(d, (
    By.XPATH, '//*[@id="add-merchant-basic-info-form"]/fieldset[1]/div[26]/div/div/select'))
    Select(complexStructure).select_by_value('1')

    loanInfoType = get_element(d, (By.ID, 'loanInfoType'))#贷款产品
    value = getConfig('SME', 'loanInfoType')
    if value == "1":
        Select(loanInfoType).select_by_value('1')
    elif value == "2":
        Select(loanInfoType).select_by_value('2')
    selec3 = d.find_element_by_id('indusNature')
    Select(selec3).select_by_value('80')
    sellGoods = d.find_element_by_id('sellGoods')
    Select(sellGoods).select_by_value('1')
    d.find_element_by_id('hkd').send_keys(f.random_number(digits=8))
    employeeNum_id = get_element(d, (By.ID, "employeeNum"))
    Select(employeeNum_id).select_by_value("3")
    d.find_element_by_id('majorBuyers1').send_keys(f.company_prefix())#主要买家
    majorBuyersAddress1 = d.find_element_by_id('majorBuyersAddress1')
    Select(majorBuyersAddress1).select_by_value('54462')
    d.find_element_by_id('majorSuppliers').send_keys(f.company_prefix())
    majorSuppliersAddress = d.find_element_by_id('majorSuppliersAddress')
    Select(majorSuppliersAddress).select_by_value('54462')
    fundSource_id = get_element(d, (By.ID, 'fundSource'))
    Select(fundSource_id).select_by_value("2")
    fundSourceAddress = get_element(d, (By.ID, 'fundSourceAddress'))
    Select(fundSourceAddress).select_by_value("54462")
    predictAnnualFiancialAmt_id = get_element(d, (By.ID, "predictAnnualFiancialAmt"))#预计每年交易金额（HKD）
    Select(predictAnnualFiancialAmt_id).select_by_value("3")
    selec4 = d.find_element_by_id('currency')
    Select(selec4).select_by_value('USD')
    predictAnnualFiancialTimes_id = get_element(d, (By.ID, "predictAnnualFiancialTimes"))
    Select(predictAnnualFiancialTimes_id).select_by_value("2")
    majorReceiptRpymForms_id = get_element(d, (By.ID, 'majorReceiptRpymForms')) #主要收付形式
    Select(majorReceiptRpymForms_id).select_by_value("1")
    majorReceiptRpymChannel_id = get_element(d, (By.ID, "majorReceiptRpymChannel"))
    Select(majorReceiptRpymChannel_id).select_by_value("1")
    payPriod_id = get_element(d, (By.ID, 'payPriod'))#付款账期
    Select(payPriod_id).select_by_value('2')
    openAcctReason_id = get_element(d, (By.ID, 'openAcctReason'))
    Select(openAcctReason_id).select_by_value("1")
    repayFundsSource_id = get_element(d, (By.ID, "repayFundsSource"))
    Select(repayFundsSource_id).select_by_value("1")
    d.find_element_by_id('lastYearTransAmt').send_keys(f.random_number(digits=8))#贸易金额(上一年
    d.find_element_by_id('cooperateYearsJdhk').send_keys(f.random_number(digits=1))
    selec5 = d.find_element_by_id('custStatus')
    Select(selec5).select_by_value('1')

    # d.find_element_by_id('receiptBank').send_keys('招商银行')
    receiptBankCode = d.find_element_by_id('receiptBankCode')#收款银行编码
    Select(receiptBankCode).select_by_value('LIVIHKH0XXX')
    get_element(d, (By.ID, "receiptAcctName")).send_keys(name +"kj")#收款账户名
    d.find_element_by_id('receiptAcct').send_keys(f.credit_card_number())#收款账户号
    # d.find_element_by_xpath(
    #     '//*[@id="add-merchant-basic-info-form"]/fieldset[3]/div[5]/div[1]/div/label[1]/input').click() #交易授权方式
    Authorizer = getConfig('SME', 'add-merchant-basic-info-form')
    if Authorizer == "1":
         d.find_element_by_xpath(
        '//*[@id="add-merchant-basic-info-form"]/fieldset[3]/div[5]/div[1]/div/label[1]/input').click() #1个授权人
    elif Authorizer == "2":
         d.find_element_by_xpath(
        '//*[@id="add-merchant-basic-info-form"]/fieldset[3]/div[5]/div[1]/div/label[2]/input').click() #2个授权人

    d.find_element_by_id('remark').send_keys(f.words())#随机文字
    dianji = d.find_element_by_xpath('//*[@id="wizard"]/div[2]/a[2]')#（下一步）
    dianji.click()#点击控件（下一步）
    sleep(0.5)
    dianji.click()#连续点两次下一步
    sleep(1)
    d.implicitly_wait(10)
    dir_work = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取文件路径
    #os.path.abspath(__file__)当前模块的绝对路径，os.path.dirname可以获取到除文件名以外的路径
    get_element(d, (By.XPATH, '//*[@id="picker1"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    get_element(d, (By.XPATH, '//*[@id="picker2"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    get_element(d, (By.XPATH, '//*[@id="picker3"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    get_element(d, (By.XPATH, '//*[@id="picker4"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    get_element(d, (By.XPATH, '//*[@id="picker5"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    get_element(d, (By.XPATH, '//*[@id="picker6"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    get_element(d, (By.XPATH, '//*[@id="picker7"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    get_element(d, (By.XPATH, '//*[@id="picker8"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    sleep(0.5)
    get_element(d, (By.XPATH, '//*[@id="picker9"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    get_element(d, (By.XPATH, '//*[@id="picker10"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    get_element(d, (By.XPATH, '//*[@id="picker11"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    get_element(d, (By.XPATH, '//*[@id="picker12"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    get_element(d, (By.XPATH, '//*[@id="picker13"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    get_element(d, (By.XPATH, '//*[@id="picker14"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    get_element(d, (By.XPATH, '//*[@id="picker15"]/div[2]/input')).send_keys(dir_work + r"\houtai\atest.pdf")
    sleep(2)
    get_element(d, (By.XPATH, '//*[@id="wizard"]/div[2]/a[2]')).click()#下一步
    d.implicitly_wait(10)
    # try:  # 可能会出现异常的代码，放在try下
    #     get_element(d, (By.XPATH, '//*[@id="layui-layer100001"]/div[3]/a')).click()  # 请上传提示框"确定"
    # except:
    #     print("上传附件无警告提示框")
    # sleep(0.5)
    # d.implicitly_wait(10)
    # get_element(d, (By.XPATH, '//*[@id="wizard"]/div[2]/a[2]')).click()  # 下一步

    ## 新建联系人##
    sleep(0.5)
    d.implicitly_wait(10)
    for i in range(1):#循环执行次数
      get_element(d, (By.XPATH, '//*[@id="add-merchant-user-btton"]')).click()  # 新建
      d.find_element_by_id('userNameCn').send_keys(f.name())  # 中文名称
      d.find_element_by_id('userNameEn').send_keys('samxa')

      js4 = 'document.getElementsByName("birthday")[0].removeAttribute("readonly");'
      d.execute_script(js4)
      re_id4 = d.find_elements_by_name("birthday")
      re_id4[0].clear()
      js_value4 = 'document.getElementsByName("birthday")[0].value="1995-01-15";'
      d.execute_script(js_value4)
      sleep(0.5)
      selec6 = d.find_element_by_id('gender')
      Select(selec6).select_by_value('1')
      selec7 = d.find_element_by_id('nationality')
      Select(selec7).select_by_value('1')
      selec8 = d.find_element_by_id('idType')  # 身份证类型
      Select(selec8).select_by_value('2')
      ssn = f.ssn()  ##随机生成身份证号(18位)
      d.find_element_by_id('idNo').send_keys(ssn)
      phoneZoneNo = get_element(d, (By.ID, "phoneZoneNo"))  # 手机号码区号
      value2 = getConfig('SME', 'phoneZoneNo')
      if value2 == "86":
          Select(phoneZoneNo).select_by_value("86")
      elif value2 == "852":
          Select(phoneZoneNo).select_by_value("852")
      phoneid = d.find_element_by_xpath('//*[@id="phone"]')
      phone = getConfig('SME', 'phone')  # GetConfig接口用于获取配置信息
      phoneid.send_keys(phone)
      emailid = d.find_element_by_id('email')
      email = getConfig('SME', 'email')
      emailid.send_keys(email)
      d.find_element_by_id('originalNameCn').send_keys(f.name())
      d.find_element_by_id('originalNameEn').send_keys('zidonghua')
      d.find_element_by_id('passPharse').send_keys("ABCD")
    # passPharse = (f.random_letter() + f.random_letter() + f.random_letter() + f.random_letter()).upper()
    # d.find_element_by_id('passPharse').send_keys(passPharse)

      UserType = getConfig('SME', 'UserType')
      if UserType == "1":
          userType = d.find_element_by_id('userType')  # 用户类型授权人或管理员
      elif UserType == "2":
          userType = d.find_element_by_id('userTypeForUnsecuredLoan')  # 用户类型其他

      value3 = getConfig('SME', 'userType')
      if value3 == "1":
          Select(userType).select_by_value("1")
      elif value3 == "2":
          Select(userType).select_by_value("2")
      elif value3 == "3":
          Select(userType).select_by_value("3")
      d.find_element_by_id('userAddress').send_keys(f.street_address())
      finalOwner = get_element(d, (By.ID, "finalOwner"))
      Select(finalOwner).select_by_value("1")
      finalController = get_element(d, (By.ID, "finalController"))
      Select(finalController).select_by_value("2")
      finalController2 = get_element(d,
                          (By.XPATH, '//*[@id="add-merchant-user-form"]/fieldset/div[11]/div[2]/div/select'))
      Select(finalController2).select_by_value("1")
    # pep_id2 = d.find_elements_by_id("pep")
    # Select(pep_id2[1]).select_by_value('1')
      str_id2 = d.find_elements_by_id("str")
      Select(str_id2[1]).select_by_value("1")
      staff_id = d.find_elements_by_id("staff")
      Select(staff_id[0]).select_by_value("1")
      sleep(0.5)
      exebtton = d.find_element_by_id('add-merchant-user-exe-btton')#保存
      exebtton.click()
      sleep(0.5)
      exebtton.click()
      sleep(1)
      d.implicitly_wait(10)

# #新建第二个授权人或管理员
#     get_element(d, (By.XPATH, '//*[@id="add-merchant-user-btton"]')).click()  # 新建
#     d.find_element_by_id('userNameCn').send_keys(f.name())  # 中文名称
#     d.find_element_by_id('userNameEn').send_keys('samxa')
#     js4 = 'document.getElementsByName("birthday")[0].removeAttribute("readonly");'
#     d.execute_script(js4)
#     re_id4 = d.find_elements_by_name("birthday")
#     re_id4[0].clear()
#     js_value4 = 'document.getElementsByName("birthday")[0].value="1995-01-15";'
#     d.execute_script(js_value4)
#     sleep(0.5)
#     selec6 = d.find_element_by_id('gender')
#     Select(selec6).select_by_value('1')
#     selec7 = d.find_element_by_id('nationality')
#     Select(selec7).select_by_value('1')
#     selec8 = d.find_element_by_id('idType')  # 身份证类型
#     Select(selec8).select_by_value('2')
#     ssn = f.ssn()  ##随机生成身份证号(18位)
#     d.find_element_by_id('idNo').send_keys(ssn)
#     phoneZoneNo = get_element(d, (By.ID, "phoneZoneNo"))  # 手机号码区号
#     value2 = getConfig('SME', 'phoneZoneNo')
#     if value2 == "86":
#         Select(phoneZoneNo).select_by_value("86")
#     elif value2 == "852":
#         Select(phoneZoneNo).select_by_value("852")
#     phoneid = d.find_element_by_xpath('//*[@id="phone"]')
#     phone = getConfig('SME', 'phone2')  # GetConfig接口用于获取配置信息
#     phoneid.send_keys(phone)
#     emailid = d.find_element_by_id('email')
#     email = getConfig('SME', 'email2')
#     emailid.send_keys(email)
#     d.find_element_by_id('originalNameCn').send_keys(f.name())
#     d.find_element_by_id('originalNameEn').send_keys('zidonghua')
#     d.find_element_by_id('passPharse').send_keys("ABCD")
#
#     UserType = getConfig('SME', 'UserType')
#     if UserType == "1":
#         userType = d.find_element_by_id('userType')  # 用户类型授权人或管理员
#     elif UserType == "2":
#         userType = d.find_element_by_id('userTypeForUnsecuredLoan')  # 用户类型其他
#     value3 = getConfig('SME', 'userType2')
#     if value3 == "1":
#         Select(userType).select_by_value("1")
#     elif value3 == "2":
#         Select(userType).select_by_value("2")
#     elif value3 == "3":
#         Select(userType).select_by_value("3")
#     d.find_element_by_id('userAddress').send_keys(f.street_address())
#     finalOwner = get_element(d, (By.ID, "finalOwner"))
#     Select(finalOwner).select_by_value("1")
#     finalController = get_element(d, (By.ID, "finalController"))
#     Select(finalController).select_by_value("2")
#     finalController2 = get_element(d,
#                                 (By.XPATH, '//*[@id="add-merchant-user-form"]/fieldset/div[11]/div[2]/div/select'))
#     Select(finalController2).select_by_value("1")
#     # pep_id2 = d.find_elements_by_id("pep")
#     # Select(pep_id2[1]).select_by_value('1')
#     str_id2 = d.find_elements_by_id("str")
#     Select(str_id2[1]).select_by_value("1")
#     staff_id = d.find_elements_by_id("staff")
#     Select(staff_id[0]).select_by_value("1")
#     sleep(0.5)
#     exebtton = d.find_element_by_id('add-merchant-user-exe-btton')  # 保存
#     exebtton.click()
#     sleep(0.5)
#     exebtton.click()
#     sleep(1)

    d.find_element_by_xpath('//*[@id="wizard"]/div[2]/a[2]').click()#下一步
    sleep(1)
    d.implicitly_wait(10)
    d.find_element_by_id('auditName').send_keys(f.words())#审核名称
    d.find_element_by_id('approveExplain').send_keys(f.words())
    d.find_element_by_xpath('//*[@id="wizard"]/div[2]/a[3]').click()#提交
    sleep(0.5)
    get_element(d, (By.XPATH, '//*[@id="wizard"]/div[2]/a[3]')).click() # 提交
    print("已提交审批")
    sleep(1)
    d.switch_to.default_content()#    切换到最上层页面
    d.implicitly_wait(10)
    d.find_element_by_xpath('/html/body/div[2]/aside[1]/section/ul/li[5]/a/span[1]').click()#审核管理
    sleep(0.5)
    d.implicitly_wait(10)
    # d.find_element_by_xpath('/html/body/div[2]/aside[1]/section/ul/li[5]/ul/li/a/span').click()
    # dfrma = d.find_element_by_xpath('//*[@id="审核列表"]/iframe')
    # d.switch_to.frame(dfrma)
    get_element(d, (By.XPATH, '/html/body/div[2]/aside[1]/section/ul/li[5]/ul/li/a/span')).click()#审核列表
    d.switch_to.frame(d.find_element_by_xpath('//*[@id="审核列表"]/iframe'))
    sleep(1)
    d.implicitly_wait(10)
    d.find_element_by_xpath('//*[@id="search-approval-control-form"]/fieldset/div[1]/div[2]/input').send_keys(name)
    #find_element与click()连起来使用会使find_element的implicitly_wait失效
    # get_element(d, (By.XPATH, '//*[@id="search-approval-control-btton"]')).click()  # 查询
    chaxun = d.find_element_by_xpath('//*[@id="search-approval-control-btton"]')
    chaxun.click() #点击控件（#查询）
    sleep(2)
    d.implicitly_wait(10)
    d.find_element_by_xpath('//*[@id="approval-control-table"]/tbody/tr[1]/td[9]/a[2]').click()#审批
    sleep(1)
    d.implicitly_wait(10)
    # selec9 = d.find_element_by_id('approvalValueStatusAll')
    # Select(selec9).select_by_value('2')
    # d.find_element_by_name("approvalValueStatus").find_elements_by_tag_name("option")[2].click()  # 审批通过
    # d.find_element_by_name("approvalValueStatus").find_element_by_xpath("//option[@value='2']").click()
    # d.find_element_by_id("approvalValueStatusAll").find_element_by_xpath("//option[2]").click()
    # d.find_element_by_id("approvalValueStatusRefuse").find_element_by_xpath("//option[2]").click()

    # try:  # 可能会出现异常的代码，放在try下
    #     selec10 = d.find_element_by_xpath('//*[@id="approvalValueStatusAll"]')
    #     Select(selec10).select_by_value('1')
    #     # get_element(d, (By.XPATH, '//*[@id="approvalValueStatusAll"]/option[2]')).click()
    # except:
    #     print("命中反洗钱，
    # sleep(1)
    # try:
    #     selec11 = d.find_element_by_xpath('//*[@id="approvalValueStatusAll"]')
    #     Select(selec11).select_by_value('2')
    #     # get_element(d, (By.XPATH, '//*[@id="approvalValueStatusRefuse"]/option[2]')).click()
    # except:
    #     print("未命中反洗钱")


    try:  # 可能会出现异常的代码，放在try下
        selec10 = d.find_element_by_xpath('//*[@id="approvalValueStatusAll"]')
        Select(selec10).select_by_value('1')
        # get_element(d, (By.XPATH, '//*[@id="approvalValueStatusAll"]/option[2]')).click()
    except:
        selec11 = d.find_element_by_xpath('//*[@id="approvalValueStatusAll"]')
        Select(selec11).select_by_value('2')
    else:
        print("未命中反洗钱,审批通过")

    sleep(0.5)
    # d.find_element_by_xpath('//*[@id="approvalValueStatusAll"]/option[2]').click()

    # get_element(d, (By.XPATH, '//*[@id="approval-control-audit-form"]/fieldset/div[8]/div/input')).send_keys("xxxx")
    get_element(d, (By.XPATH, '//*[@id="approval-control-audit-form"]/fieldset/div[8]/div/input')).send_keys(f.words())
    sleep(1)
    d.find_element_by_xpath('//*[@id="approval-control-audit-submit-btton"]').click()
    # sleep(5)
    # d.switch_to.default_content()
    # su = get_alert(d)

    # name_phone = "企业简码:" + name + ",注册手机号码:" + "13714705129" + ",身份证后四位:" + ssn[-4:] + ",pass_pharse:" + pass_pharse
    name_phone = "企业简码:" + name + ",注册手机号码:" + phone + ",身份证后四位:" + ssn[-4:] + ",pass_pharse:" + "ABCD"
    print(name_phone)
    # if su in "Success":
    #     name_phone = "企业简码:" + name + ",注册手机号码:" + phone + ",身份证后四位:" + ssn[-4:] + ",pass_pharse:" + passPharse
    #     print(name_phone)
    with open('name5.txt', 'a+') as b:
        b.write("\n" + name_phone)
    # # endtime = datetime.datetime.now()
    # sleep(0.5)
    d.quit()
    # sleep(10000)


if __name__ == '__main__':
    # try:
    #     for i in range(1):
    w = 1021
    y = 5020
    for i in range(1):
        input_in()
        y += 1
    # except Exception as msg:
    #     print(msg)
