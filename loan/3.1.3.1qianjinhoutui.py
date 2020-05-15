# coding = utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
#访问百度首页
first_url= 'http://www.baidu.com'
print( "now access %s" %(first_url))
#“%s”表示输出类型为字符串，“%d”表示输出类型为整型数字,%r不管什么都打印出来;



driver.get(first_url)

#访问新闻页面
second_url='http://news.baidu.com'
print ("now access %s" %(second_url))

driver.get(second_url)

#返回（后退）到百度首页
print ("back to %s "%(first_url))
driver.back() #返回（后退）

#前进到新闻页
print ("forward to %s"%(second_url))
driver.forward() #前进
time.sleep(2)

driver.refresh() #刷新当前页面

driver.quit()

