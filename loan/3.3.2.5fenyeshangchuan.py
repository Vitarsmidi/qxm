#!/usr/bin/env python
# coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time ,os #引入time库
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get('http://172.17.255.229/')
driver.maximize_window() #将浏览器最大化显示

driver.find_element_by_id("loginId").clear()
driver.find_element_by_id("loginId").send_keys("qq")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("qxm12345")
time.sleep(5) #输入验证码
#driver.find_element_by_id("subButton").click() #点击登录

#获得登录成功的用户，打印
driver.implicitly_wait(30)
now_user=driver.find_element_by_class_name("user-info").text
print('登录成功', now_user)
time.sleep( 0.5 )

driver.find_element_by_link_text("业务受理").click() #link text,文字链接定位
driver.switch_to_frame("conframe")  #表单切换
time.sleep( 0.5 )
driver.find_element_by_id("searchBtn").click() #搜索查询
time.sleep(0.5)

# #获取所有分页的数量，并打印
# total_pages=len(driver.find_element_by_xpath("//*[@id='grid-pager_center']/table/tbody/tr/td[8]/select"). \
#                 find_elements_by_tag_name("option"))
# print("total page is %s" %(total_pages))
# time.sleep(0.5)
# #再次获取所分页，并执行循环翻页操作
# pages=driver.find_element_by_xpath("//*[@id='grid-pager_center']/table/tbody/tr/td[8]/select").\
#     find_elements_by_tag_name("option")
# for page in pages:
#     page.click()
#     time.sleep(0.5)

driver.find_element_by_id("searchUserName").send_keys("王五")
driver.implicitly_wait(30)
driver.find_element_by_id("searchBtn").click() #搜索查询
print('查询成功......')

time.sleep(0.5)
driver.find_element_by_class_name("fa-check-square-o").click()
#driver.find_element_by_link_text("受理").click() #link text,文字链接定位
# driver.find_element_by_xpath("//*[@id='1']/td[14]/div/button/i").click() #相对路径//
print('已打开受理详情......')
time.sleep(0.5)

# #######通过 JS 隐藏选中的元素##########第一种方法：
# #隐藏文字信息
# driver.execute_script('$("#showOperationBtn").fadeOut();')
# time.sleep(1)
# #隐藏按钮：
# button = driver.find_element_by_id('showOperationBtn')
# driver.execute_script('$(arguments[0]).fadeOut()',button)
# time.sleep(1)
#
# js = "var q=document.body.scrollTop=10000"
# driver.execute_script(js)
# print("ddf")
# time.sleep(1)
# #滚动到底部
# js = "window.scrollTo(0,document.body.scrollHeight)"
# driver.execute_script(js)
# time.sleep(1)
# #滚动到顶部
# js = "window.scrollTo(0,0)"
# driver.execute_script(js)
# print("dddf")
# time.sleep(1)
#
# # 聚焦到某个元素位置
# target =driver.find_element_by_xpath("//*[@id='media-table']/tbody/tr[1]/td[6]/div[1]/button[1]") #相对路径//
# driver.execute_script("arguments[0].scrollIntoView();", target)
# print("ddddf")
# time.sleep(1)
#
# #将页面滚动条拖到底部
# js="var q=document.documentElement.scrollTop=10000"
# # js="var q=document.getElementById('id').scrollTop=0"
# driver.execute_script(js)
# time.sleep(1)
# #将滚动条移动到页面的顶部
# js="var q=document.documentElement.scrollTop=0"
# driver.execute_script(js)
# time.sleep(1)
#
#  # 左右滑动
# # js = "window.scrollTo(100,400);"
# # driver.execute_script(js)

# 借款信息
driver.implicitly_wait(30)
driver.find_element_by_id("repayType").find_elements_by_tag_name("option")[1].click() #
driver.implicitly_wait(30)
driver.find_element_by_id("applyTerm").find_elements_by_tag_name("option")[3].click() #期限
driver.find_element_by_id("purpose").find_elements_by_tag_name("option")[2].click() #
driver.find_element_by_id("salesTeam").find_element_by_xpath("//option[@value='12']").click() #团队经理
driver.implicitly_wait(30)
driver.find_element_by_id("pSalesman").find_element_by_xpath("//option[@value='27']").click() #

# 个人信息输入
driver.implicitly_wait(30)
driver.find_element_by_id('pWechat').clear()
driver.find_element_by_id("pWechat").send_keys('wx123456')
# driver.find_element_by_id('secMobile').clear()
# driver.find_element_by_id("secMobile").send_keys('14800148002')
# driver.find_element_by_id('thirMobile').clear()
# driver.find_element_by_id("thirMobile").send_keys('14800148001')
driver.find_element_by_id('pEmail').clear()
driver.find_element_by_id("pEmail").send_keys('123456@qq.com')
driver.find_element_by_id("pEducation").find_elements_by_tag_name("option")[2].click() #
driver.find_element_by_id('pSalary').clear()
driver.find_element_by_id("pSalary").send_keys('150000')
driver.find_element_by_id("pResideType").find_elements_by_tag_name("option")[3].click() #
driver.find_element_by_id("pMarriage").find_elements_by_tag_name("option")[2].click() #
driver.find_element_by_id("pResidenceType").find_elements_by_tag_name("option")[1].click() #
driver.find_element_by_id('pRegisterProvince').clear()
driver.find_element_by_id("pRegisterProvince").send_keys('广东省') #省
driver.find_element_by_id('pRegisterProvince').clear()
driver.find_element_by_id("pRegisterProvince").send_keys('广东省') #省
driver.find_element_by_id('pRegisterCity').clear()
driver.find_element_by_id("pRegisterCity").send_keys('深圳') #市
driver.find_element_by_id('pRegisterArea').clear()
driver.find_element_by_id("pRegisterArea").send_keys('南山区') #
driver.find_element_by_id('pRegisterAddress').clear()
driver.find_element_by_id("pRegisterAddress").send_keys('科技中二路') #
driver.find_element_by_id('pResideProvince').clear()
driver.find_element_by_id("pResideProvince").send_keys('广东省') #
driver.find_element_by_id('pResideCity').clear()
driver.find_element_by_id("pResideCity").send_keys('深圳') #
driver.find_element_by_id('pResideArea').clear()
driver.find_element_by_id("pResideArea").send_keys('南山区') #
driver.find_element_by_id('pResideAddress').clear()
driver.find_element_by_id("pResideAddress").send_keys('高薪中四道') #

# 职业信息
driver.find_element_by_id('pCompanyName').clear()
driver.find_element_by_id("pCompanyName").send_keys('深圳蚂蚁金服') #企业名称
driver.find_element_by_id("pCompanyType").find_elements_by_tag_name("option")[2].click() #
driver.find_element_by_id('pPosition').clear()
driver.find_element_by_id("pPosition").send_keys('经理') #
js_value = 'document.getElementById("pEntryDate").value="2017-08-08"' #通过js添加时间  入职日期
driver.execute_script(js_value)
driver.find_element_by_id('pCompanyTelephone').clear()
driver.find_element_by_id("pCompanyTelephone").send_keys('13800138005') #
driver.find_element_by_id('pInsuranceNo').clear()
driver.find_element_by_id("pInsuranceNo").send_keys('2184002586988') #社保
driver.find_element_by_id("pIndustry").find_elements_by_tag_name("option")[2].click() #
driver.find_element_by_id("pEmploymentType").find_elements_by_tag_name("option")[1].click() #
driver.find_element_by_id('pCompanyProvince').clear()
driver.find_element_by_id("pCompanyProvince").send_keys('广东省') #
driver.find_element_by_id('pCompanyCity').clear()
driver.find_element_by_id("pCompanyCity").send_keys('深圳市') #
driver.find_element_by_id('pCompanyArea').clear()
driver.find_element_by_id("pCompanyArea").send_keys('南山区') #
driver.find_element_by_id('pCompanyAddr').clear()
driver.find_element_by_id("pCompanyAddr").send_keys('深圳湾科技大厦') #

# 联系人信息
driver.implicitly_wait(30)
driver.find_element_by_name('userContactList[0].contactName').clear()
driver.find_element_by_name("userContactList[0].contactName").send_keys('王一') #
driver.find_element_by_name('userContactList[0].mobile').clear()
driver.find_element_by_name("userContactList[0].mobile").send_keys('15800158001') #
driver.find_element_by_name("userContactList[0].relationType").find_elements_by_tag_name("option")[2].click() #
driver.find_element_by_name('userContactList[0].phoneCheckRemark').clear()
driver.find_element_by_name("userContactList[0].phoneCheckRemark").send_keys('电核备注自动填写') #
driver.find_element_by_name("userContactList[0].alipayCheck").find_elements_by_tag_name("option")[1].click() #
driver.find_element_by_name('userContactList[1].contactName').clear()
driver.find_element_by_name("userContactList[1].contactName").send_keys('王二') #
driver.find_element_by_name('userContactList[1].mobile').clear()
driver.find_element_by_name("userContactList[1].mobile").send_keys('15800158002') #
driver.find_element_by_name("userContactList[1].relationType").find_elements_by_tag_name("option")[2].click() #
driver.find_element_by_name('userContactList[1].phoneCheckRemark').clear()
driver.find_element_by_name("userContactList[1].phoneCheckRemark").send_keys('电核备注自动填写') #
driver.find_element_by_name("userContactList[1].alipayCheck").find_elements_by_tag_name("option")[2].click() #支付宝
#资料上传
driver.implicitly_wait(30)
#定位上传按钮，send_keys添加本地文件
driver.find_element_by_xpath("//*[@id='main-container']//td[text()='身份证明-二代身份证']/..//i[contains(text(),'上传')]").click()
driver.find_element_by_xpath("//input[@type=\"file\"]").send_keys('E:\\tupian\\1.jpg')
time.sleep(0.5)
driver.find_element_by_class_name('layui-layer-btn0').click() #确定
print("身份证已上传.....")

# #打开上传文件页面
# file_path = 'file://*[@id='main-container']//td[text()='身份证明-二代身份证']/..//i[contains(text(),'上传')]'
#    + os.path.abspath('upload_file.html')
# driver.get(file_path)
# #定位上传按钮，添加本地文件
# driver.find_element_by_name("file").send_keys('D:\\selenium_use_case\upload_file.txt')


# AutoIt实现上传
# driver.find_element_by_xpath("//*[@id='main-container']//td[text()='身份证明-二代身份证']/..//i[contains(text(),'上传')]").click()
# driver.find_element_by_xpath("//*[@id='dropzone']/div/span/i").click() #点击打开上传窗口
# os.system("E:\\autoitWork\\businessHandingPics.exe") #调用upfile.exe上传

# 		driver.find_element_by_xpath("//*[@id='main-container']//td[text()='身份证明-二代身份证']/..//i[contains(text(),'上传')]").click()
# 		// *[@id='main-container']//td[text()='身份证明-二代身份证']/..//td[6]
# 		// driver.findElement(By.className("fa-cloud-upload")).click();
# 		// driver.findElement(By.xpath("//i[contains(text(),'上传')]")).click();//
# 		// contains()模糊匹配文本 点击上传

#**资产证明-机动车登记证**#
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='main-container']//td[text()='资产证明-机动车登记证']/..//i[contains(text(),'上传')]").click()
driver.find_element_by_xpath("//input[@type=\"file\"]").send_keys('E:\\tupian\\2.jpg')
time.sleep(0.5)
driver.find_element_by_class_name('layui-layer-btn0').click() #确定
print("机动车登记证已上传.....")
#**资产证明-行驶证**#
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='main-container']//td[text()='资产证明-行驶证']/..//i[contains(text(),'上传')]").click()
driver.find_element_by_xpath("//input[@type=\"file\"]").send_keys('E:\\tupian\\2.jpg')
time.sleep(0.5)
driver.find_element_by_class_name('layui-layer-btn0').click() #确定
print("行驶证已上传.....")
#**资产证明-车辆保单**#
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='main-container']//td[text()='资产证明-车辆保单']/..//i[contains(text(),'上传')]").click()
driver.find_element_by_xpath("//input[@type=\"file\"]").send_keys('E:\\tupian\\1.jpg')
time.sleep(0.5)
driver.find_element_by_class_name('layui-layer-btn0').click() #确定
print("车辆保单已上传.....")
#**资产证明-车辆照片**#
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='main-container']//td[text()='资产证明-车辆照片']/..//i[contains(text(),'上传')]").click()
driver.find_element_by_xpath("//input[@type=\"file\"]").send_keys('E:\\tupian\\2.jpg')
time.sleep(0.5)
driver.find_element_by_class_name('layui-layer-btn0').click() #确定
print("车辆照片已上传.....")

#*保存提交*
driver.implicitly_wait(30)
# driver.find_element_by_id("saveBtn").click() #保存
driver.find_element_by_id("submitBtn").click() #提交
time.sleep(0.5)
driver.find_element_by_class_name('layui-layer-btn0').click() #确定提交
# driver.find_element_by_xpath("//a[contains(text(),'确定')]").click() #确定提交
print("业务受理已提交.....")


#driver.quit()
