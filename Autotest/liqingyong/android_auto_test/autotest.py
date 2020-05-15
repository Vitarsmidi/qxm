#coding=utf-8
#_name_= 'Tino'
#filename:login.py

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import unittest
import os
import traceback
import random
from PIL import Image
from PIL import ImageEnhance
import pytesseract


p_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #获取当前项目的根路径

class Andr_Auto_Test(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['automationName'] = 'UIAutomator2'
        desired_caps['deviceName'] = 'ce5bdce8'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['noReset'] = True
        desired_caps['app'] = p_path + '\\android_auto_test\\app\\MTJF_v2.8.0_debug228.apk'
#        desired_caps['automationName'] = 'Appium'
        desired_caps["appPackage"] = "com.mintou.finance"
#        desired_caps["appActivity"] = "com.mintou.finance.ui.MainActivity"
        desired_caps["appActivity"] = "com.mintou.finance.ui.LaucherTaskActivity"
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    '''
    #封装获取图片验证码
    def getImgCode(self):
        try:
            driver = self.driver
            driver.save_screenshot("resetpwd.png")          #截取当前界面
            imgelement = driver.find_element_by_id("com.mintou.finance:id/tvLoginImgNumber")          #定位验证码
            location = imgelement.location          #获取验证码x,y轴的坐标
            size = imgelement.size                  #获取验证码的长宽
            coderange = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))   #需要截取的验证码图片坐标
            i = Image.open("resetpwd.png")          #打开当前界面截图
            imgcode = i.crop(coderange)                #使用Image的crop函数，从界面截图中再次截取我们需要的验证码图片区域
            imgcode.save("imgcode.png")
            i2 = Image.open("imgcode.png")
            text = pytesseract.image_to_string(i2).strip()          #使用image_to_string识别验证码
            return text
        except Exception:
            traceback.print_exc()
    '''


    # 获得机器屏幕大小x,y
    def getSize(self):
        driver = self.driver
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return (x, y)

    # 屏幕向上滑动
    def swipeUp(self, t):
        driver = self.driver
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.65)  # 起始y坐标
        y2 = int(l[1] * 0.4)  # 终点y坐标
        driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipeDown(self, t):
        driver = self.driver
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.1)  # 起始y坐标
        y2 = int(l[1] * 0.9)  # 终点y坐标
        driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swipeLeft(self, t):
        driver = self.driver
        l = self.getSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipeRight(self, t):
        driver = self.driver
        l = self.getSize()
        x1 = int(l[0] * 0.1)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.9)
        driver.swipe(x1, y1, x2, y1, t)

    #手势密码  封装：九宫格（012；345；678）手势为：0147
    def gesturepassword(self):
        driver = self.driver
        list_pwd = driver.find_elements_by_class_name("android.widget.RelativeLayout")[1].find_elements_by_class_name("android.view.View")
        TouchAction(driver).press(list_pwd[0]).move_to(list_pwd[0]).wait(100).move_to(list_pwd[1]).wait(100).move_to(list_pwd[4]).wait(100).move_to(list_pwd[7]).release().perform()
        sleep(1)
#        print ("输入手势密码")
        '''如果新注册，或者修改手势密码的时候，需要输入两次手势密码，如果只是登录的话就是一次'''
        try:
            driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'再次绘制解锁图案')]")
            list_pwd = driver.find_elements_by_class_name("android.widget.RelativeLayout")[1].find_elements_by_class_name("android.view.View")
            TouchAction(driver).press(list_pwd[0]).move_to(list_pwd[0]).move_to(list_pwd[1]).wait(100).move_to(list_pwd[4]).wait(100).move_to(list_pwd[7]).release().perform()
        except Exception:
            traceback.print_exc()
            pass

    def test_case(self):

        driver = self.driver

        # 允许权限
        sleep(3)  # 增加延时，防止因弹窗出现过慢而异常
        if driver.page_source.find("appops_warning_hint") != -1:
                driver.find_element_by_id("android:id/button1").click()
        #            driver.switch_to.context("NATIVE_APP")
        else:
                print("NoPermissionMessage")
                pass

        #启动页滑屏
#        sleep(1)       #增加延时，确保应用完全启动
        if driver.page_source.find("image_guide") != -1:
#            WebDriverWait(driver, 30).until(lambda driver:driver.find_element_by_id("com.mintou.finance:id/image_guide"))
            try:
                self.swipeLeft(400)
                sleep(1)
                self.swipeLeft(400)
                sleep(1)
                self.swipeLeft(400)
                sleep(1)
                self.swipeLeft(400)
                sleep(1)
                driver.find_element_by_id("com.mintou.finance:id/btn_begin_use").click()
            except Exception:
                traceback.print_exc("引导页滑动翻页异常")
                pass
        else:
            print ("image_guideNotFound")
            pass


        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/iv_splash"))
        WebDriverWait(driver, 30).until_not(lambda driver: driver.find_element_by_id("com.mintou.finance:id/iv_splash"))

        #点击资产tab中注册按钮
        WebDriverWait(driver, 30).until(lambda driver:driver.find_element_by_id("com.mintou.finance:id/image"))   #头图
        WebDriverWait(driver, 5).until(lambda driver:driver.find_element_by_id("com.mintou.finance:id/assets_rigist")).click()      #点击注册按钮
        WebDriverWait(driver, 30).until(lambda driver:driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'注册')]"))
        driver.find_element_by_id("com.mintou.finance:id/et_input").set_text("18566625484")
        WebDriverWait(driver, 5).until(lambda driver:driver.find_element_by_id("com.mintou.finance:id/btn_next_step")).click()
        WebDriverWait(driver, 15).until(lambda driver:driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'短信验证码将发送到:')]"))
        WebDriverWait(driver, 5).until(lambda driver:driver.find_element_by_id("com.mintou.finance:id/btn_right")).click()
        WebDriverWait(driver, 15).until(lambda driver:driver.find_element_by_id("com.mintou.finance:id/item_login")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'借款人注册')]"))
        driver.find_element_by_id("com.mintou.finance:id/et_input").set_text("18566625484")
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_next_step")).click()
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'短信验证码将发送到:')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_right")).click()
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()



        #点击资产tab立即登录按钮
        WebDriverWait(driver, 30).until(lambda driver:driver.find_element_by_id("com.mintou.finance:id/assets_login")).click()

        #登录界面中点击注册按钮
        WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("com.mintou.finance:id/item_register_2")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'注册')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()   #返回登录界面

        #登录界面中点击忘记密码
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_forgetpass")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'重置登录密码')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()

        # 输入登录手机号
        WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("com.mintou.finance:id/btn_login"))
        driver.find_elements_by_id("com.mintou.finance:id/et_input")[0].set_text("13049408989")
        #输入密码
        driver.find_elements_by_id("com.mintou.finance:id/et_input")[1].set_text("test@123456")
        WebDriverWait(driver, 5).until(lambda driver:driver.find_element_by_id("com.mintou.finance:id/btn_login")).click()

        #输入手势密码
        WebDriverWait(driver, 30).until(lambda driver:driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'设置手势密码')]"))
        self.gesturepassword()
        WebDriverWait(driver, 15).until(lambda driver:driver.find_element_by_id("com.mintou.finance:id/item_total_amount"))   #作判断登录是否成功

        #资产tab顶部客服图标
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_service_kefu")).click()
        WebDriverWait(driver, 45).until(lambda driver:driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '帮助与反馈')]"))   #作判断是否跳转客服页
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'热点问题')]"))
        WebDriverWait(driver, 5).until(lambda driver:driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()    #点击右上角微信图标
        WebDriverWait(driver, 15).until(lambda driver:driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'微信公众号')]"))
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'1.打开微信通信录')]"))
#        driver.find_elements_by_class_name("android.widget.TextView")[3].click()
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()  #微信公众号介绍页中返回
        WebDriverWait(driver, 45).until(lambda driver:driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '帮助与反馈')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'热点问题')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_kefu")).click()     #点击在线客服
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/udesk_conversation"))   #判断是否跳转到客服咨询界面
        WebDriverWait(driver, 30).until(lambda driver:driver.find_element_by_id("com.mintou.finance:id/udesk_bottom_send"))    #判断是否跳转到客服咨询界面
        driver.find_element_by_id("com.mintou.finance:id/udesk_back_linear").click()
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '帮助与反馈')]"))  # 作判断是否返回客服页
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'热点问题')]"))
        driver.find_element_by_id("com.mintou.finance:id/item_call").click()
        WebDriverWait(driver, 15).until(lambda driver:driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'客服热线')]"))
        driver.find_element_by_id("com.mintou.finance:id/btn_left").click()
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '帮助与反馈')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'热点问题')]"))
        driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left").click()
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_total_amount"))   #判断是否返回到资产tab

        #资产tab顶部隐藏按钮
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_open_hiden")).click()
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'***')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_open_hiden")).click()
        WebDriverWait(driver, 15).until_not(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'***')]"))

        #资产tab中总资产
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_total_amount")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'资产概览')]"))    #判断是否跳转
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'可用余额')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()      #点击明细按钮
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'资金明细')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()     #从明细页返回
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'资产概览')]"))    #判断是否返回
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'可用余额')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()      #从资产概览页返回
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_total_amount"))    #判断是否返回到资产tab

        #资产tab中收益栏
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_profit")).click()
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'温馨提示')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_left")).click()     #点击知道了按钮
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_profit"))     #判断是否收起了弹框

        #资产tab中可用余额栏
        WebDriverWait(driver, 5).until(lambda dirver: driver.find_element_by_id("com.mintou.finance:id/ll_assets_banlance")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'资金明细')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()  # 从明细页返回
        WebDriverWait(driver, 15).until(lambda dirver: driver.find_element_by_id("com.mintou.finance:id/ll_assets_banlance"))

        #资产tab中定期项目栏
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_dingqi")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'待收本金(元)')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'持有中')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'投标中')]")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'已结清')]")).click()
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()    #从定期项目中返回
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_dingqi"))

        #资产tab中回款日历栏
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_repayment_calendar")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/indicator"))   #月份滑动栏
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'当月应收本息(元)')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'当月待收本息(元)')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()    #点击回款计划
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'回款计划')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'待收回款总额(元)')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()   #回款计划页中返回
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'回款日历')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()   #回款日历页中返回
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_repayment_calendar"))

        '''
        #资产tab中自动投标栏
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_auto_invest")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'可用余额')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()   #点击页面右上角规则说明按钮
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'自动投标规则')]"))
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'自动投标说明')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'自动投标')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'可用余额')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_min_amount")).click()   #查看单笔最低投资额的提示
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'温馨提示')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_left")).click()
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/edit_single_amount")).set_text("100")   #单笔最低投资设置为100
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_left_amount")).click()    #查看账户保留金额的提示
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'温馨提示')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_left")).click()
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/edit_left_amount")).set_text("0")    #账户保留金额设置为0
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_term")).click()      #点击投资项目期限
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'不限')]"))
        driver.find_element_by_id("com.mintou.finance:id/popup_list").find_elements_by_class_name("android.widget.RelativeLayout")[0].click()    #选择不限期
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/okBtn")).click()     #点击确定按钮
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'5.60%~12.00%')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_repay_type")).click()      #点击还款方式
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'一次性还款')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/okBtn")).click()
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/auto_coupon")).click()     #查看自动使用优惠券的提示
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'温馨提示')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_left")).click()
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/auto_coupon_power")).click()     #打开自动使用优惠券的开关
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_sure")).click()      #点击保存并开启按钮
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()    #自动投标页面中点击返回
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_auto_invest"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'已开启')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_auto_invest")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'关闭自动投标')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_modify_auto")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'保存并开启')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_colse_auto")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'自动投标功能已成功关闭')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_left")).click()
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_auto_invest"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'未开启')]"))
        '''
        #资产tab中优惠券栏
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_coupon")).click()    #点击优惠券栏
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'我的优惠券')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()   #点击使用说明按钮
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'2.每笔投资仅可使用一张优惠劵')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'我的优惠券')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_coupon"))

        #资产tab中推荐奖励栏
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_sumProfitsAmount")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'累计奖励(元)')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'待发奖励(元)')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()     #查看奖励规则说明
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc,'推荐好友说明')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()     #返回推荐奖励页
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'累计奖励(元)')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'待发奖励(元)')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/tv_coupon_bottom")).click()     #点击邀请好友按钮
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_weixin")).click()      #微信好友分享
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_friend")).click()      #朋友圈分享
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_qq")) .click()         #QQ好友分享
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_qq_room")).click()     #QQ空间分享
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_sms"))         #短信分享
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_cancel")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'累计奖励(元)')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()   #返回资产tab
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_sumProfitsAmount"))

        #跳转项目tab
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("//android.widget.CheckBox[contains(@text,'项目')]")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/image"))
        
        #新手专享项目
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/ll_home_item_root")[1]).click()     #点击新手专享的项目
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_profit"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '新手专享')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()     #点击查看协议
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '借款合同')]"))
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '合同编号')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_project_detailinfo")).click()         #点击查看项目详情
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '项目周期')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_introduce")).click()            #点击查看项目说明
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '项目介绍')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_trade_record")).click()      #点击查看交易记录
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/layout_main"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_risk_url")).click()        #点击查看风险提示
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '风险提示')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/image"))
        
        #推荐项目
        self.swipeUp(400)     #向上滑屏
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/home_title_huodong")).click()     #点击页面顶部右侧的活动图标
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '活动中心')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/listview"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_class_name("android.widget.ImageView")[1]).click()       #点击第二个活动banner
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '新手好礼')]"))
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '新手专享好礼01')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '活动中心')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/listview"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '推荐项目')]"))
        WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/item_count")[0]).click()       #查看推荐项目栏更多按钮
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '优选散标')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/page_tab_back")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '推荐项目')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/ll_home_item_root")[3]).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_profit"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()  # 点击查看协议
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '借款合同')]"))
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '合同编号')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_project_detailinfo")).click()  # 点击查看项目详情
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '项目周期')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_introduce")).click()  # 点击查看项目说明
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '项目介绍')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_trade_record")).click()  # 点击查看交易记录
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/layout_main"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_risk_url")).click()  # 点击查看风险提示
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '风险提示')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '推荐项目')]"))
        self.swipeUp(400)
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_foot_more")).click()      #点击推荐项目底部更多按钮
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '优选散标')]"))
        WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/rl_info")[1]).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '优选散标')]"))
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '新手专享')]")).click()    #跳转新手专享tab
        sleep(1)
        WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/rl_info")[1]).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '优选散标')]"))
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '转让专区')]")).click()
        sleep(1)
        WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/item_tv_rate")[1]).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '公允价值')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '优选散标')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/page_tab_back")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '更多项目')]"))
        #转让专区
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/item_count")[0]).click()  # 查看转让专区栏更多按钮
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '优选散标')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/page_tab_back")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '更多项目')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/ll_home_item_root")[5]).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_profit"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '公允价值')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()  # 点击查看协议
#        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '债权转让协议')]"))
#        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '合同编号')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_project_detailinfo")).click()  # 点击查看项目详情
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '借款信息')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_introduce")).click()  # 点击查看项目说明
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '项目介绍')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_trade_record")).click()  # 点击查看交易记录
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/layout_main"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_debt")).click()        #点击查看债权信息
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '债权转让')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_risk_url")).click()  # 点击查看风险提示
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '风险提示')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '更多项目')]"))
        self.swipeUp(400)
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/item_foot_more")[1]).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '优选散标')]"))
        WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/item_tv_rate")[1]).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_remain_amount"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '公允价值')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '优选散标')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/page_tab_back")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '更多项目')]"))
        
        #跳转发现tab
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("//android.widget.CheckBox[contains(@text,'发现')]")).click()
        #判断是否有礼包待领取弹框弹出
        sleep(3)
        if driver.page_source.find("礼包待领取") != -1:
            driver.find_element_by_id("com.mintou.finance:id/action_close").click()
        else:
            print ("账号无待领取的特权礼包")
            pass
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '邀请人')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/ll_more_planner")).click()           #点击邀请人等级栏
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '推荐好友说明')]"))
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '推荐好友说明')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '邀请人')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/ll_leijijiangli")).click()       #点击查看累计奖励
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '推荐奖励')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '累计奖励(元)')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '待发奖励(元)')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()         #查看奖励规则
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '推荐好友说明')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '推荐奖励')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/tv_coupon_bottom")).click()       #点击底部邀请按钮
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_weixin")).click()  # 微信好友分享
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_friend")).click()  # 朋友圈分享
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_qq")).click()  # QQ好友分享
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_qq_room")).click()  # QQ空间分享
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_sms"))  # 短信分享
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_cancel")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '推荐奖励')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '邀请人')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/ll_my_friends")).click()            #点击我的好友栏
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '注册好友(人)')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '已投资好友(人)')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '邀请人')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_call_friend")).click()          #点击邀请好友栏
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '让朋友扫描二维码即可注册')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()         #查看奖励规则
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '推荐好友说明')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '让朋友扫描二维码即可注册')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_weixin")).click()  # 微信好友分享
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_friend")).click()  # 朋友圈分享
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_qq")).click()  # QQ好友分享
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_qq_room")).click()  # QQ空间分享
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '邀请人')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/actionImage")[1]).click()       #点击查看热门活动
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '新手好礼')]"))
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '新手专享好礼01')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '邀请人')]"))
        self.swipeUp(400)
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/ll_member")).click()         #点击会员中心
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/member_level"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '会员服务')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/ll_task")).click()           #点击每日任务
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '新手任务')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '会员服务')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/ll_new_guide")).click()       #点击新手指南
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '新手指南')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '会员服务')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/ll_server_center")).click()      #点击服务
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '客户服务')]"))
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '热点问题')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '会员服务')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '信息披露')]"))


        #跳转我的tab
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("//android.widget.CheckBox[contains(@text,'我')]")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/userInfoContent"))     #作判断是否跳转
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/userInfoContent")).click()       #查看个人信息
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '个人信息')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_head_img")).click()         #设置头像
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '我的相册')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '拍照')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_cancel")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '个人信息')]"))
        try:
            WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_nick_name")).click()        #设置昵称
            WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '设置昵称')]"))
            nickname = '孔子冬游' + str(random.randint(0, 1000))
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/edit_content")).set_text(nickname)
            WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()
            WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '个人信息')]"))
            WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, nickname)]"))
        except Exception:
            traceback.print_exc("昵称设置失败")
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/userInfoContent"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_member")).click()       #点击会员中心
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/member_level"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()     #查看成长说明
        WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '会员等级介绍')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/member_level"))
        #判断是否存在待领取礼包
        if driver.page_source.find("member_gift") != -1:
            driver.find_element_by_id("com.mintou.finance:id/member_gift").click()
            WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_receive")).click()
        else:
            print ("不存在待领取礼包")
            pass
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/privilege_item")[0]).click()        #查看特权详情
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '特权详情')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/member_level"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/privilege_more")).click()      #点击更多特权
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '会员特权')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/member_level"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '积分奖励')]")).click()    #点击积分奖励
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '我的积分')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/member_level"))
#        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '幸运抽奖')]")).click()       #点击幸运抽奖
#        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '幸运抽奖')]"))
#        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
#        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/member_level"))
        self.swipeUp(400)
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/task_head")).click()         #点击任务头部栏
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '任务中心')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/list_task"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/tv_task_more")).click()      #点击任务底部查看更多栏
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '任务中心')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/list_task"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/userInfoContent"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_asset")).click()        #点击我的总资产
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '资产概览')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '总资产(元)')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()     #查看明细
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '资金明细')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '总资产(元)')]"))
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/userInfoContent"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_asset_detail")).click()    #点击资金明细
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/listview"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/userInfoContent"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_bank_card")).click()        #点击银行存管账户
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/bankContent"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_right")).click()     #点击客服图标
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '客户服务')]"))
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '热点问题')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/bankContent"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/userInfoContent"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_risk")).click()         #点击风险评测
        WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_xpath("//android.view.View[contains(@content-desc, '您的投资类型')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/userInfoContent"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/dual_icon_text_help")).click()       #点击帮助与反馈
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '帮助与反馈')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_feedback")).click()         #点击底部意见反馈按钮
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.EditText[contains(@text, '请写下您的宝贵意见或建议')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/edit_input")).set_text("writed by Tino just for test")
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/commit_btn")).click()        #点击保存
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '反馈已收到')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_left")).click()
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '帮助与反馈')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/userInfoContent"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/dual_icon_text_refresh")).click()        #点击版本更新
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '已是最新版本!')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/userInfoContent"))
        #点击设置
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_setting")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '个人信息')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()    #点击左上角返回按钮
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/userInfoContent"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_setting")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_auth_loginpass")).click()      #点击修改登录密码
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '修改登录密码')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '个人信息')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_auth_loginpass")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '修改登录密码')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/et_input")[0]).set_text("test@123456")
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/et_input")[1]).set_text("test@111111")
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/sure")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '修改登录密码成功，请重新登录')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '支持你的从容人生')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/et_input")[0]).set_text("13049408989")
        # 输入新密码
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/et_input")[1]).set_text("test@111111")
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_login")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_total_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("//android.widget.CheckBox[contains(@text,'我')]")).click()
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_setting")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_auth_loginpass")).click()  # 点击修改登录密码
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '修改登录密码')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '个人信息')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_auth_loginpass")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '修改登录密码')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/et_input")[0]).set_text("test@111111")
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/et_input")[1]).set_text("test@123456")
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/sure")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '修改登录密码成功，请重新登录')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '支持你的从容人生')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/et_input")[0]).set_text("13049408989")
        # 输入新密码
        WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_id("com.mintou.finance:id/et_input")[1]).set_text("test@123456")
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_login")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_total_amount"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("//android.widget.CheckBox[contains(@text,'我')]")).click()
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_setting")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_gesture")).click()       #点击设置手势密码
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '修改手势密码')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/gkoModify")).click()         #修改手势密码
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '验证登录密码')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_close")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '修改手势密码')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/cbitCheckBox")).click()      #点击关闭手势轨迹显示
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/gkoModify")).click()  # 修改手势密码
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '验证登录密码')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/editText1")).set_text("test@123456")
        driver.back()
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/sure")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '请绘制新手势密码')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/gesture_close")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '显示手势轨迹')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '个人信息')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/dual_icon_text_about")).click()          #点击关于民投金服按钮
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_about_version"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_about_us")).click()         #查看民投金服介绍
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '公司简介')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_about_version"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_safe")).click()         #查看安全保障
        WebDriverWait(driver, 45).until(lambda driver: driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc, '安全保障')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_about_version"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_phone")).click()        #点击客服热线
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '400-888-6221')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_about_version"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_weixin")).click()       #点击微信公众号
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '复制成功')]"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/item_about_version"))
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/titlebar_tv_left")).click()
        WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '个人信息')]"))
        #退出登录
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("com.mintou.finance:id/btn_logout")).click()
        sleep(5)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



