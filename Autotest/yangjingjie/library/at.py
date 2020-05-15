# -*- coding:utf-8 -*-
import SendKeys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlwt
import time
import random,string
import urllib, httplib,re
import os
from robot.api import logger
import MySQLdb

host='172.17.255.228'
user='root'
port = 3306
passwd='123456'



def auto():
    url = 'http://172.17.255.220:7080/product/sporadic/list'
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    browser.get(url)
    browser.maximize_window()
    browser.find_element_by_id("loginId").send_keys("admin")
    browser.find_element_by_id("password").send_keys("123456")
    time.sleep(7)
    browser.find_element_by_xpath('//button[@id="subButton"]').click()
    WebDriverWait(browser,15,0.3).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="menuUL"]/li[1]/a')))
    browser.get(url)

def GenPassword():
    length=8
    numOfNum = random.randint(1,length-1)
    numOfLetter = length - numOfNum

    slcNum = [random.choice(string.digits) for i in range(numOfNum)]
    slcLetter = [random.choice(string.ascii_letters) for i in range(numOfLetter)]
    slcChar = slcNum + slcLetter
    random.shuffle(slcChar)
    genPwd = ''.join([i for i in slcChar])
    return genPwd



def GenProductname():
    length=5
    numOfNum = random.randint(1,length-1)
    numOfLetter = length - numOfNum

    slcNum = [random.choice(string.digits) for i in range(numOfNum)]
    slcLetter = [random.choice(string.ascii_letters) for i in range(numOfLetter)]
    slcChar = slcNum + slcLetter
    random.shuffle(slcChar)
    genPwd = ''.join([i for i in slcChar])
    genproductname="转让YANG"+genPwd.encode('utf8')
    product=genproductname.decode('utf8','ignore')
    return product


def PaperProductname():
    length=5
    numOfNum = random.randint(1,length-1)
    numOfLetter = length - numOfNum

    slcNum = [random.choice(string.digits) for i in range(numOfNum)]
    slcLetter = [random.choice(string.ascii_letters) for i in range(numOfLetter)]
    slcChar = slcNum + slcLetter
    random.shuffle(slcChar)
    genPwd = ''.join([i for i in slcChar])
    genproductname="银票YANG"+genPwd.encode('utf8')
    product=genproductname.decode('utf8','ignore')
    return product


def sele_sql(pname):
    conn= MySQLdb.connect(host=host,user=user,port=port,passwd=passwd,charset="utf8")
    cur = conn.cursor()
    sql = "select id from mtbill.product where productname = %s"
    aa=cur.execute(sql,pname)
    logger.info("sql is %s "%(sql))
    info = cur.fetchmany(aa)
    b=list(info)
    c=b[0]
    d=list(c)
    cur.close()
    conn.commit()
    conn.close()
    return d[0]


def sel_sms(phone):
    conn= MySQLdb.connect(host=host,user=user,port=port,passwd=passwd,charset="utf8")
    cur = conn.cursor()
    sql = "select smsparam from mtbill.sms_record where receiveMobiles = %s limit 1"
    aa=cur.execute(sql,phone)
    info = cur.fetchmany(aa)
    b=info[0]
    for c in b:
        d=c.encode("utf-8")
    e=eval(d)
    sms=e['code']
    cur.close()
    conn.commit()
    conn.close()
    return sms

def getmobile():
    length=8
    numOfNum = random.randint(1,length-1)
    slcNum = [random.choice(string.digits) for i in range(length)]
    random.shuffle(slcNum)
    genPwd = ''.join([i for i in slcNum])
    genproductname="137"+genPwd
    mobile=genproductname

    return mobile


def update_product(prid):
    a=prid
    conn= MySQLdb.connect(host=host,user=user,port=port,passwd=passwd,charset="utf8")
    cur = conn.cursor()
    sql = "update mtbill.product set valuedate = NOW()  where id = %s"
    cur.execute(sql,a)
    sql = "update mtbill.product set lastmodifydate = DATE_SUB(NOW(),INTERVAL 15 MINUTE)  where id = %s"
    cur.execute(sql,a)
    conn.commit()
    conn.close()


def update_repay(pid):
    a=pid
    conn= MySQLdb.connect(host=host,user=user,port=port,passwd=passwd,charset="utf8")
    cur = conn.cursor()
    sql = "UPDATE mtbill.product set valueDate = DATE_SUB(DATE_SUB(NOW(),INTERVAL 1 DAY),INTERVAL 1 month)  , expireDate = DATE_ADD(DATE_SUB(DATE_SUB(NOW(),INTERVAL 1 DAY),INTERVAL 1 month),INTERVAL 4 month) where originalProductId = %s"
    cur.execute(sql,a)
    sql = "update mtbill.invest set investDate = DATE_SUB(DATE_SUB(NOW(),INTERVAL 1 DAY),INTERVAL 1 month),valueDate =DATE_SUB(DATE_SUB(NOW(),INTERVAL 1 DAY),INTERVAL 1  month),expireDate = DATE_ADD(DATE_SUB(DATE_SUB(NOW(),INTERVAL 1 DAY),INTERVAL 1 month),INTERVAL 4 month) where originalProductId = %s"
    cur.execute(sql,a)
    sql = "update mtbill.product_repay_plan set repayDate = DATE_ADD(DATE_SUB(DATE_SUB(NOW(),INTERVAL 1 DAY),INTERVAL 1 month),INTERVAL 1 month) where repayPeriod = 1 and originalProductId = %s"
    cur.execute(sql,a)
    sql = "update mtbill.product_repay_plan set repayDate = DATE_ADD(DATE_SUB(DATE_SUB(NOW(),INTERVAL 1 DAY),INTERVAL 1 month),INTERVAL 2 month) where repayPeriod = 2 and originalProductId = %s"
    cur.execute(sql,a)
    sql = "update mtbill.product_repay_plan set repayDate = DATE_ADD(DATE_SUB(DATE_SUB(NOW(),INTERVAL 1 DAY),INTERVAL 1 month),INTERVAL 3 month) where repayPeriod = 3 and originalProductId = %s"
    cur.execute(sql,a)
    sql = "update mtbill.product_repay_plan set repayDate = DATE_ADD(DATE_SUB(DATE_SUB(NOW(),INTERVAL 1 DAY),INTERVAL 1 month),INTERVAL 4 month) where repayPeriod = 4 and originalProductId = %s"
    cur.execute(sql,a)
    sql = "update mtbill.invest_repay_plan set repayDate = DATE_ADD(DATE_SUB(DATE_SUB(NOW(),INTERVAL 1 DAY),INTERVAL 1 month),INTERVAL 1 month) where originalRepayPeriod = 1 and originalProductId = %s"
    cur.execute(sql,a)
    sql = "update mtbill.invest_repay_plan set repayDate = DATE_ADD(DATE_SUB(DATE_SUB(NOW(),INTERVAL 1 DAY),INTERVAL 1 month),INTERVAL 2 month) where originalRepayPeriod = 2 and originalProductId = %s"
    cur.execute(sql,a)
    sql = "update mtbill.invest_repay_plan set repayDate = DATE_ADD(DATE_SUB(DATE_SUB(NOW(),INTERVAL 1 DAY),INTERVAL 1 month),INTERVAL 3 month) where originalRepayPeriod = 3 and originalProductId = %s"
    cur.execute(sql,a)
    sql = "update mtbill.invest_repay_plan set repayDate = DATE_ADD(DATE_SUB(DATE_SUB(NOW(),INTERVAL 1 DAY),INTERVAL 1 month),INTERVAL 4 month) where originalRepayPeriod = 4 and originalProductId = %s"
    cur.execute(sql,a)
    conn.commit()
    conn.close()


def sele_ivid(pidd):
    conn= MySQLdb.connect(host=host,user=user,port=port,passwd=passwd,charset="utf8")
    cur = conn.cursor()
    sql = "select id from mtbill.invest where originalProductId = %s limit 1"
    aa=cur.execute(sql,pidd)
    logger.info("sql is %s "%(sql))
    print "sql is %s "%(sql)
    info = cur.fetchmany(aa)
    print info
    b=list(info)
    print b
    c=b[0]
    print c
    d=list(c)
    print d
    print d[0]
    cur.close()
    conn.commit()
    conn.close()
    return d[0]

