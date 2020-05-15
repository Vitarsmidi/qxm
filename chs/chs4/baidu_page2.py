# -*- coding: utf-8 -*-
# @Time : 2020/5/3 18:27
# @Author : qxm
# @FileName: baidu_page.py

from poium import Page,PageElement

"""
poium 是selenium/appium de Page Object测试库 可以简化Page基础层元素的定义

继承poium库中的Page类封装的一些方法，将百度搜索关键字的元素定位封装，poium.Page不用写，直接导入引用
"""

class BaiduPage(Page):

    #poium-操作百度页面用到的元素定位，具体的操作放在另一个文件
    search_input = PageElement(name= "wd")
    search_button = PageElement(id_= "su")

"""
poium支持的8种元素定位
elem_id = PageElement(id_= "xx")
elem_name = PageElement(name= "xx")
elem_class = PageElement(class_name= "xx")
elem_tag = PageElement(tag= "xx")
elem_link_text = PageElement(link_text= "xx")
elem_xpath = PageElement(xpath= '//*[@id="xx"]')
elem_css = PageElement(css= "#id")

定位一组元素
elem_id = PageElements(id_= "xx")


可通过timeout设置元素等待超时时间
search_input = PageElement(id_= "kw",timeout=10)

可通过describe添加元素备注
search_input = PageElement(id_= "kw",describe="搜索框")

"""

