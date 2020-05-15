# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 20:37
# @Author  : sunlin
# @File    : page.py
# @Software: PyCharm
import datetime
import random
import string
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from datetime import date, timedelta
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


def get_element(driver, loc):
    # ele = WebDriverWait(driver, 30).until(lambda x: x.find_element(*loc), message="没有找到元素")
    # return ele
    try:
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(loc), message="not found element %s By %s " % loc[::-1])
        return driver.find_element(*loc)
    except TimeoutException as msg:
        print(msg)
        # driver.close()


def get_phone():
    num_start = ['130', '131', '132', '135', '150', '152', '156', '185', '186', '138', '137', '187', '188', '180',
                 '139']
    start = random.choice(num_start)
    end = ''.join(random.sample(string.digits, 8))
    res = start + end
    return res


def get_phone2():
    num_start = ["4", "5", "6", "8", "9"]
    start = random.choice(num_start)
    end = ''.join(random.sample(string.digits, 7))
    res = start + end
    return res

def get_phone3():
    # num_start = ["4", "5", "6", "8", "9"]
    # start = random.choice(num_start)
    end = ''.join(random.sample(string.digits, 7))
    res =  end
    return res



def get_alert(driver):
    WebDriverWait(driver, 10, 0.5).until(EC.alert_is_present())
    a = driver.switch_to.alert
    msg = a.text
    print(msg)
    a.accept()
    return msg


def get_ID():
    # num_start = ["A", "B", "C", "D", "E", "F", "G", "k", "P", "R", "S", "V"]
    num_start = ["A", "B", "C", "D", "E", "F", "G", "k", "P", "R", "S", "V"]
    start = random.choice(num_start)
    end = ''.join(random.sample(string.digits, 6))
    end2 = ''.join(random.sample(string.digits, 1))
    num_end = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    end2 = random.choice(num_end)
    res = start + end + "("+end2 +")"
    return res


def get_date(days=7):
    # 获取7天后的日期, days为具体几天后的日期
    data = (date.today() + timedelta(days=days)).strftime("%Y-%m-%d")
    return data


def get_date2(days=7):
    # 获取7天后的日期, days为具体几天后的日期
    data = (date.today() + timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
    return data


def runtime(func):
    def wrapper(*args):
        try:
            starttime = datetime.datetime.now()
            result = func(*args)
            endtime = datetime.datetime.now()
            run_time = (endtime - starttime).seconds
            print("程序运行的时间为:" + str(run_time) + '秒')
            return result
        except Exception as msg:
            print(msg)

    return wrapper


if __name__ == '__main__':
    # print(get_phone())
    # print(type(get_date()))
    # print(get_date2())
    ss = ''.join(random.sample(string.digits, 4))
    name1 = "WDYQ" + ''.join(random.sample(string.digits, 4))
    print(name1)
    print(type(ss))
    print(get_ID())
