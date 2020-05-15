# -*- coding: utf-8 -*-
# @Time : 2020/5/08 21:47
# @Author : qxm
# @FileName: baidu_page.py

"""
引入poium库封装baidu测试页面page层，元素定位封装，具体的操作放在另一个文件
"""

from poium import Page, PageElement, PageElements

class BaiduPage(Page):
    search_input = PageElement(id_="kw", describe="搜索框")
    search_button = PageElement(id_="su", describe="搜索按钮")
    settings = PageElement(link_text="设置", describe="设置下拉框")
    search_setting = PageElement(css=".setpref", describe="搜索设置选项")
    save_setting = PageElement(css=".prefpanelgo", describe="保存设置")

    search_input2 = PageElement(id_="k", describe="搜索框") #错误的
    # 定位一组元素
    search_result = PageElements(xpath="//div/h3/a", describe="搜索结果")
