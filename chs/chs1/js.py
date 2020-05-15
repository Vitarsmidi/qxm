# -*- coding: utf-8 -*-
# @Time : 2020/4/8 22:49
# @Author : qxm
# @FileName: js.py

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.set_window_size(800,600)

driver.find_element_by_id("kw").send_keys("中国")
driver.find_element_by_id('su').click()

# js ="window.scrollTo(1000,1500);"
# js="var q=document.documentElement.scrollTop=10000"
# js = "var q=document.body.scrollTop=10000"

# driver.execute_script(js)

#通过js控制时间控件，输入时间
js = 'document.getElementById("registerDate").removeAttribute("readonly");'
driver.execute_script(js)
# re_id = d.find_element_by_id("registerDate")
# re_id.clear()
js_value = 'document.getElementById("registerDate").value="2015-12-10"'  # js添加时间
driver.execute_script(js_value)