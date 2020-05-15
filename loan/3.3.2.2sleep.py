# coding = utf-8
from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time #引入time库
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome()
driver.get('http://172.17.255.229/')
driver.maximize_window() #将浏览器最大化显示

driver.find_element_by_id("loginId").clear()
driver.find_element_by_id("loginId").send_keys("admin")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456")

#添加智能等待/隱形等待
driver.implicitly_wait(30)  #隱形等待，30秒內找到元素就執行，否則報錯
#driver.find_element_by_id("subButton").click() #点击登录

#显式等待
element=WebDriverWait(driver,5,0.5).until(expected_conditions.visibility_of_all_elements_located(By.ID,'subButton'))
# WebDriverWait(driver,timeout,poll_frequency) timeout最长等待超时时间s  ，poll_frequency检测间隔时间s
#WebDriverWait()一般与until()、until_not()配合使用，until()调用该方法提供的驱动程序作为一个参数，直到返回值为True
#.visibility_of_all_elements_located()判断元素是否存在
#expected_conditions 预期条件判断

#获得登录成功的用户，打印
now_user=driver.find_element_by_class_name("user-info").text
print('登录成功', now_user)

#添加固定休眠时间
time.sleep( 0.5 )

driver.find_element_by_link_text("车辆评估").click() #link text,文字链接定位
driver.switch_to_frame("conframe")  #表单切换
driver.implicitly_wait(30)

driver.find_element_by_id("searchBtn").click() #搜索查询
driver.implicitly_wait(30)

# 打印当前页面上 type 为 checkbox 的个数
print(len(driver.find_elements_by_css_selector('input[type=checkbox]')))
#因为第一个复选框为全选或反选，so要去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop(0).click() #pop（0）：默认获取一组元素的第一个
driver.find_elements_by_css_selector('input[type=checkbox]').pop(1).click() #pop（1）：默认获取一组元素的第二个
time.sleep( 0.5 )

#   #获取对象的属性
# # 选择所有的 type 为 checkbox 的元素并单击勾选
# checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
# #然后循环遍历出 data-node 为594434493的元素，单击勾选
# for checkbox in checkboxes:
#    if checkbox.get_attribute('id') == 'jqg_grid-table_480':
#      checkbox.click()

# # 选择页面上所有的 class 为 cbox 的元素
# inputs = driver.find_elements_by_class_name('cbox') #elements 定位一组元素
# # 然后从中过滤出 tpye 为 checkbox 的元素，单击勾选
# inputs = driver.find_elements_by_tag_name("input")
# for input in inputs:
#   if input.get_attribute('type') == "checkbox":
#     input.click()

# 选择所有的 type 为 checkbox 的元素并单击勾选
# checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
# for checkbox in checkboxes:
#    checkbox.click()
# driver.find_elements_by_css_selector('input[type=checkbox]').pop(0).click()

# def is_select():
#     # 勾选前判断是否勾选
#     t = driver.find_elements_by_css_selector('input[type=checkbox]').is_selected()
#     print(t)
#     driver.find_elements_by_css_selector('input[type=checkbox]').click()
#     driver.find_elements_by_css_selector('input[type=checkbox]').pop(0).click()  # pop（0）：默认获取一组元素的第一个
#
#     #  点击后判断是否勾选
#     r = driver.find_elements_by_css_selector('input[type=checkbox]').is_selected()
#     print(r)

# # 判断是否勾选
# try:
#     driver.find_elements_by_css_selector('input[type=checkbox]').is_selected()
#     print('Test Pass.')
# except Exception as e:
#     print('Test fail', format(e))

driver.find_element_by_id("userName").send_keys("fsad")
driver.implicitly_wait(30)
driver.find_element_by_id("searchBtn").click() #搜索查询
print('查询成功......')
# driver.implicitly_wait(30)

time.sleep( 0.5 )
# driver.find_element_by_xpath("//i[contains(text(),'评估')]").click() #评估
driver.find_element_by_xpath("//td[12]/div/button/i").click() #评估
# driver.find_element_by_class_name('bigger-120').click() #评估
# driver.find_elements_by_css_selector('input[type=button]').click() #评估
print('已进入详情页面......')

driver.implicitly_wait(30)
driver.find_element_by_id("vehicleNum").clear()
driver.find_element_by_id("vehicleNum").send_keys("cp123456")
driver.find_element_by_id("engineNum").clear()
driver.find_element_by_id("engineNum").send_keys("fdj123456")
driver.find_element_by_id("vehicleIdNum").clear()
driver.find_element_by_id("vehicleIdNum").send_keys("fdj123456")
driver.find_element_by_id("transferTimes").clear()
driver.find_element_by_id("transferTimes").send_keys(0)
driver.find_element_by_id("sweptVolume").clear()
driver.find_element_by_id("sweptVolume").send_keys("2.3")
driver.find_element_by_id("seat").clear()
driver.find_element_by_id("seat").send_keys("5")
driver.find_element_by_id("ownership").find_element_by_xpath("//option[@value='1']").click() #下拉框选择
driver.find_element_by_id("envirStandard").find_element_by_xpath("//option[@value='5']").click()
driver.find_element_by_id("evaluatePrice").clear()
driver.find_element_by_id("evaluatePrice").send_keys("990000")
driver.find_element_by_id("vehicleRegistration").clear()
driver.find_element_by_id("vehicleRegistration").send_keys("cldj123456")

driver.find_element_by_id("vehicleBrandId").find_elements_by_tag_name("option")[1].click() #车辆品牌
# s1 = Select(driver.find_element_by_id('vehicleBrandId'))  # 实例化Select
# s1.select_by_value("1")  # 选择value="1"的项  车辆品牌
# # s1.select_by_index(1)  # 选择第o1选项：o1
# # s1.select_by_visible_text("A-奥迪")  # 选择text="A-奥迪"的值，即文本

driver.find_element_by_id("vehicleSeriesId").find_element_by_xpath("//option[@value='2310']").click() #车系名称
driver.find_element_by_id("vehicleModelId").find_element_by_xpath("//option[@value='31927']").click() #车辆型号

#日期控件
js_value = 'document.getElementById("licenseDate").value="2017-08-08"' #通过js添加时间  上牌日期
driver.execute_script(js_value)
# js = "document.getElementById('licenseDate').removeAttribute('readonly')"  # 1.原生js，移除readonly属性
# # 用js去掉元素属性基本思路：先定位到元素，然后用removeAttribute(“readonly”)方法删除属性。
# # js = "$('input[id=txtBeginDate]').removeAttr('readonly')"  # 2.jQuery，移除属性
# # js = "$('input[id=txtBeginDate]').attr('readonly',false)"  # 3.jQuery，设置为false
# # js = "$('input[id=licenseDate]').attr('readonly','')"  # 4.jQuery，设置为空（同3）
# driver.execute_script(js)
# driver.find_element_by_id('licenseDate').clear();
# # driver.find_element_by_id('licenseDate').send_keys('2017-08-08')

# #移除readonly属性，再输入日期
# driver.find_element_by_id('licenseDate').click();
# driver.execute_script("document.getElementById('licenseDate').readOnly=false;");
# driver.find_element_by_id('licenseDate').clear();
# driver.find_element_by_id('licenseDate').send_keys("2018-01-02");

driver.find_element_by_id("registerProvinceId").find_elements_by_tag_name("option")[1].click() #省份
driver.find_element_by_id("registerCityId").find_elements_by_tag_name("option")[1].click() #城市

js_value2 = 'document.getElementById("productDate").value="2016-07-08"' #通过js添加时间  出厂日期
driver.execute_script(js_value2)

driver.find_element_by_id("interiorType").find_elements_by_tag_name("option")[1].click() #内饰
driver.find_element_by_id("surfaceType").find_elements_by_tag_name("option")[2].click()
driver.find_element_by_id("workStateType").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_id("mileage").clear()
driver.find_element_by_id("mileage").send_keys("2") #里程
driver.find_element_by_id("vehicleColorType").find_elements_by_tag_name("option")[10].click() #颜色
driver.find_element_by_id("bubbleWater").find_elements_by_tag_name("option")[0].click()
driver.find_element_by_id("attachment").find_elements_by_tag_name("option")[0].click()
driver.find_element_by_id("accident").find_elements_by_tag_name("option")[0].click()
driver.find_element_by_id("purchasePrice").send_keys("880000") #购买价格
driver.find_element_by_id("evaluateOpinion").clear()
driver.find_element_by_id("evaluateOpinion").send_keys("自动填写详情sdgsdga") #详情
driver.find_element_by_id("isIllegal").find_elements_by_tag_name("option")[1].click() #是否违章

driver.find_element_by_id("subBtnEval").click() #点击评估
driver.implicitly_wait(30)
driver.find_element_by_class_name('layui-layer-btn0').click()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//a[contains(text(),'跳过')]").click() #跳过

driver.find_element_by_id('subBtnVeh').click() #提交
# driver.find_element_by_id("saveBtnVeh").click() #保存
# driver.find_element_by_id("refuseBtnAudit").click() #拒绝
# driver.find_element_by_id("cancelBtnAudit").click() #作废

driver.implicitly_wait(30)
driver.find_element_by_xpath("//a[contains(text(),'确定')]").click() #确定提交
time.sleep(0.5)
driver.find_element_by_xpath("//a[contains(text(),'确定')]").click() #跳过
print('已提交评估......')











#driver.quit()

# #在父亲元件下找到 link 为 Action 的子元素
# menu =driver.find_element_by_id('ownership').find_element_by_link_text('私人')
# #鼠标移动到子元素上
# ActionChains(driver).move_to_element(menu).perform()

# 这里用到了下面几个方法：
#
# find_elements_by_tag_name根据标签名称获得元素列表
#
# get_attribute获取某个属性
#
# is_enabled方法是用于判断是否可用
#
# is_selected方法是用于判断是否选中
#
# is_displayed方法是用于判断是否显示

# pop（）pop（-1）：默认获取一组元素的最后一个
#
# pop（0）：默认获取一组元素的第一个
#
# pop（1）：默认获取一组元素的第二个
#
# pop（2）：默认获取一组元素的第三个


# Select提供了三种选择方法：
# select_by_index(index) ——通过选项的顺序，第一个为 0
# select_by_value(value) ——通过value属性
# select_by_visible_text(text) ——通过选项可见文本
#
# 同时，Select提供了四种方法取消选择：
# deselect_by_index(index)
# deselect_by_value(value)
# deselect_by_visible_text(text)
# deselect_all()
#
# 此外，Select提供了三个属性方法给我们必要的信息：
# options ——提供所有的选项的列表，其中都是选项的WebElement元素
# all_selected_options ——提供所有被选中的选项的列表，其中也均为选项的WebElement元素
# first_selected_option ——提供第一个被选中的选项，也是下拉框的默认值
