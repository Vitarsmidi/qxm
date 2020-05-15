#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
import SendKeys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlwt
import time

import urllib, httplib,re
import os
from robot.api import logger
import MySQLdb
host='192.168.0.205'
user='hrjrc'
port = 3306
passwd='1qaz2wsx'



def lottery_func(platform, lottery_id,verify):
   
    params = urllib.urlencode({'platform': '%s'%platform, 'lottery_id': '%s'%lottery_id,'verify': '%s'%verify})
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    httpClient = httplib.HTTPConnection('api-and.hrjk-p2p.com', 80, timeout=10)
    httpClient.request('POST', '/lottery', params, headers)
    response = httpClient.getresponse()
    print response.status
    print response.reason
    t= response.read()
    
    print t.decode('raw_unicode_escape')
    stri='status":0'
    if stri in t:
        logger.info("lottery is success")
    else:
        logger.info("lottery is fail")
    return 0


def sel_sql(self):
    conn= MySQLdb.connect(host=host,user=user,port=port,passwd=passwd)
    cur = conn.cursor()
    aa=cur.execute("select id from products_data.data_products order by id desc LIMIT 1")
    info = cur.fetchmany(aa)
    print info
    b=list(info)
    c=b[0]
    d=list(c)
    print d[0]
    cur.close()
    conn.commit()
    conn.close()
    return d[0]


def sele_sql(anumber):
    conn= MySQLdb.connect(host=host,user=user,port=port,passwd=passwd)
    cur = conn.cursor()
    sql = "select id from products_data.data_products where item_number=%s"
    aa=cur.execute(sql,anumber)
    logger.info("sql is %s , item_number is %s"%(sql, anumber))
    info = cur.fetchmany(aa)
    print info
    b=list(info)
    c=b[0]
    d=list(c)
    print d[0]
    cur.close()
    conn.commit()
    conn.close()
    return d[0]



