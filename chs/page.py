# -*- coding: utf-8 -*-
# @Time : 2020/4/15 21:23
# @Author : qxm
# @FileName: page.py

import datetime
import random
import string
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import date, timedelta
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
基础Page层，封装一些常用方法
"""


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


   #重写元素定位方法
    def get_element(driver, loc):
        # ele = WebDriverWait(driver, 30).until(lambda x: x.find_element(*loc), message="没有找到元素")
        # return ele
        try:
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located(loc),
                                            message="not found element %s By %s " % loc[::-1])
            return driver.find_element(*loc)
        except TimeoutException as msg:
            print(msg)
            # driver.close()


    #通过title断言进入的页面是否正确。
    #使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True 或 False）
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    # 使用get打开访问链接地址
    # 以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。

    # def _open(self,url, pagetitle):
    #     self.driver.get(url)
    #     self.driver.maximize_window()
    #     # 使用assert进行校验，打开的窗口title是否与配置的title一致。调用on_page()方法
    #     assert self.on_page(pagetitle), u"打开页面失败 %s" % url
    #
    # # # 定义open方法，调用_open()进行打开链接
    # def open(self):
    #     self._open(self.base_url, self.pagetitle)

    # # 定义open方法，打开测试链接
    def open(self,base_url=None):
        if base_url is None :
            self.driver.get(self.base_url)
            self.driver.maximize_window()

        else:
            self.driver.get(base_url)
            self.driver.maximize_window()

    # id定位
    def by_id(self,id_):
        return self.driver.find_element_by_id(id_)

    # name定位
    def by_name(self,name):
        return self.driver.find_element_by_name(name)

    # class定位
    def by_class(self,class_name):
        return self.driver.find_element_by_class_name(class_name)

    # xpath定位
    def by_xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)

    # css定位
    def by_css(self,css):
        return self.driver.find_element_by_css_selector(css)

    # 获取title
    def get_title(self):
        return self.driver.title

    # 获取页面text,用xpath定位
    def get_text(self,xpath):
        return self.by_xpath(xpath).text

    # 获取页面text,用class_name定位
    def get_class_text(self,class_name):
        return self.by_class(class_name).text

    # 用于执行JavaScript脚本
    def js(self, script):
        self.driver.excute_script(script)


    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self, src):
        self.driver.excute_script(src)

    # 重写定义send_keys方法
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print("%s 页面中未能找到 %s 元素" % (self, loc))

    def get_phone(self):
        num_start = ['130', '131', '132', '135', '150', '152', '156', '185', '186', '138', '137', '187', '188', '180',
                     '139']
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 8))
        res = start + end
        return res

    def get_phone2(self):
        num_start = ["4", "5", "6", "8", "9"]
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 7))
        res = start + end
        return res

    def get_phone3(self):
        # num_start = ["4", "5", "6", "8", "9"]
        # start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 7))
        res = end
        return res

    def get_alert(self):
        WebDriverWait(self, 10, 0.5).until(EC.alert_is_present())
        a = self.switch_to.alert
        msg = a.text
        print(msg)
        a.accept()
        return msg

    def get_ID(self):
        # num_start = ["A", "B", "C", "D", "E", "F", "G", "k", "P", "R", "S", "V"]
        num_start = ["A", "B", "C", "D", "E", "F", "G", "k", "P", "R", "S", "V"]
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 6))
        end2 = ''.join(random.sample(string.digits, 1))
        num_end = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        end2 = random.choice(num_end)
        res = start + end + "(" + end2 + ")"
        return res

    def get_date(days=7):
        # 获取7天后的日期, days为具体几天后的日期
        data = (date.today() + timedelta(days=days)).strftime("%Y-%m-%d")
        return data

    def get_date2(days=7):
        # 获取7天后的日期, days为具体几天后的日期
        data = (date.today() + timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
        return data

    def runtime(func):
        def wrapper(*args):
            try:
                starttime = datetime.datetime.now()
                result = func(*args)
                endtime = datetime.datetime.now()
                run_time = (endtime - starttime).seconds
                print("程序运行的时间为:" + str(run_time) + '秒')
                return result
            except Exception as msg:
                print(msg)

        return wrapper






if __name__ == '__main__':
    # print(get_phone())
    # print(type(get_date()))
    # print(get_date2())
    ss = ''.join(random.sample(string.digits, 4))
    name1 = "WDYQ" + ''.join(random.sample(string.digits, 4))
    print(name1)
    print(type(ss))

