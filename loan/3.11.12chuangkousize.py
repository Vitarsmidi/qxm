# coding = utf-8
from selenium import webdriver
import time #引入time库

driver = webdriver.Chrome()
driver.get('http://172.17.255.229/')
driver.maximize_window() #将浏览器最大化显示

driver.find_element_by_id("loginId").send_keys("admin")
driver.find_element_by_id("password").send_keys("123456")
#driver.find_element_by_id("subButton").click()

print ("Start : %s" % time.ctime())
time.sleep( 2 )
print ("End : %s" % time.ctime())

driver.set_window_size(480, 800) #将浏览器大小设置为一定规格
print ("Hello World")
time.sleep( 2 )

driver.quit()
print ("End : %s" % time.ctime())
#“%s”表示输出类型为字符串，“%d”表示输出类型为整型数字,%r不管什么都打印出来;


