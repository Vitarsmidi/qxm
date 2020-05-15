#!/usr/bin/env python
# coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

##BasePage封装所有页面都公用的方法，初始化例如driver, Find_Element
# #实例化BasePage类时，最先执行__init__方法，该方法的入参，就是BasePage类的入参, __init__方法不能有返回值，只能返回None.
class BasePage(object):
    def __init__(self, selenium_driver, base_url,pagetitle):
        self.driver = selenium_driver
        self.base_url = base_url
        self.pagetitle = pagetitle

    #通过title断言进入的页面是否正确。
    #使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True 或 False）
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    # 使用get打开访问链接地址
    # 以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。

    def _open(self,url, pagetitle):
        self.driver.get(url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的窗口title是否与配置的title一致。调用on_page()方法
        assert self.on_page(pagetitle), u"打开开页面失败 %s" % url

    # # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.base_url, self.pagetitle)

    # 重写元素定位方法
    def find_element(self, *loc):  # *loc任意数量的位置参数（带单个星号参数）
        # return self.driver.find_element(*loc)
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))  # 入参本身是元组不需要加*
            return self.driver.find_element(*loc)
            # 若入参为元组的元素，需要加*。
            # WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
        except:
            print("%s 页面未能找到 %s 元素" % (self, loc))

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


