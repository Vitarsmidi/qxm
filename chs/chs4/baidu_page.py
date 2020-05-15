# -*- coding: utf-8 -*-
# @Time : 2020/5/3 18:27
# @Author : qxm
# @FileName: baidu_page.py

from chs.page import BasePage

"""
继承page.BasePage类封装的一些方法，将百度搜索关键字的元素定位封装
"""

class BaiduPage(BasePage):

    base_url = "https://www.baidu.com"  # 提供给BasePage父类open()方法使用

    def search_input(self,search_key):
        self.by_id("kw").send_keys(search_key)

    def search_button(self):
        self.by_id("su").click()
