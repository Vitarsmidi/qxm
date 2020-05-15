# -*- coding: utf-8 -*-
# @Time : 2020/5/08 22:47
# @Author : qxm
# @FileName: conftest.py

import os
import pytest
# from py.xml import html
from py._xmlgen import html # 用于为 py.test 结果生成HTML报告的插件
from selenium import webdriver
from selenium.webdriver import Remote  #Remote远程控制
from selenium.webdriver.chrome.options import Options as CH_Options  # Chrome配置
from selenium.webdriver.firefox.options import Options as FF_Options
from chs.chs5.config import RunConfig

"""
基本配置层，本地测试配置文件

钩子函数：通过我们自定义功能，挂载到其它功能上。

from selenium.webdriver.chrome.options import Options as CH_Options  # Chrome配置
#Chrome配置无头模式 ,即无（无界面启动），使用Chrome内核
ch_options = Options()
ch_options.add_argument("--headless")  # => 为Chrome配置无头模式 

@pytest.fixture()装饰器用于声明函数是一个fixture。如果测试函数的参数列表中包含fixture名，那么pytest会检测到，
  并在测试函数运行之前执行fixture。
  
fixture包含一个scope的可选参数，用于控制fixture执行配置和销毁逻辑的频率。
@pytest.fixture()的scope参数有四个值：
 1.scope='function' 函数级别的fixture每个测试函数 只运行一次。配置代码在测试用例运行之前运行，销毁代码在测试用例运行之后执行,默认值;
 2.scope='class'  类级别的fixture每个测试类只运行一次，不管测试类中有多少个类方法都可以共享这个fixture
 3.scope='module' 模块级别的fixture每个模块只运行一次，不管模块里有多少个测试函数，类方法或其他fixture都可以共享这个fixture;
 4.scope='session'会话级别的fixture每次会话只运行一次。pytest会话中的所有测试函数、方法都可以共享这个fixture

用@pytest.mark.usefixtures('fixture1','fixture2')标记测试函数或类。


"""


# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 当前目录
REPORT_DIR = BASE_DIR + "/report/"
driver = None


# 定义基本测试环境，设置测试钩子函数  @pytest.fixture  scope='function'在每个测试函数前运行一次
@pytest.fixture(scope='function')
def base_url():
    return RunConfig.url


# 设置用例描述表头
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.pop()


# 设置用例描述表格
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.pop()

#错误截图配置
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item,call):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = description_html(item.function.__doc__)
    # report.description = str(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            case_path = report.nodeid.replace("::", "_") + ".png"
            if "[" in case_path:
                case_name = case_path.split("-")[0] + "].png"
            else:
                case_name = case_path
            capture_screenshots(case_name)  #调用capture_screenshots函数进行截图
            #添加img标签，通过src 指定图片路径
            img_path = "image/" + case_name.split("/")[-1]
            if img_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_path
                extra.append(pytest_html.extras.html(html)) #在末尾附加
        report.extra = extra


def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]

    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html


def capture_screenshots(case_name):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    global driver
    file_name = case_name.split("/")[-1]
    new_report_dir = new_report_time()
    if new_report_dir is None:
        raise RuntimeError('没有初始化测试目录')
    image_dir = os.path.join(REPORT_DIR, new_report_dir, "image", file_name)
    driver.save_screenshot(image_dir)


def new_report_time():
    """
    获取最新报告的目录名（即运行时间，例如：2018_11_21_17_40_44）
    """
    files = os.listdir(REPORT_DIR)
    files.sort()
    try:
        return files[-1]
    except IndexError:
        return None


# 启动浏览器  钩子函数 @pytest.fixture  scope='session'在每次会话运行一次
@pytest.fixture(scope='session', autouse=True)
def browser():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver

    if RunConfig.driver_type == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif RunConfig.driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif RunConfig.driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")   # 为Chrome配置无头模式
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif RunConfig.driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)

    elif RunConfig.driver_type == "grid":
        # 通过远程节点运行
        driver = Remote(command_executor='http://localhost:4444/wd/hub',
                        desired_capabilities={
                              "browserName": "chrome",
                        })
        driver.set_window_size(1920, 1080)

    else:
        raise NameError("driver驱动类型定义错误！")

    return driver


# 关闭浏览器  @pytest.fixture  scope='session'在每次会话运行一次
@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")


if __name__ == "__main__":
    capture_screenshots("test_dir/test_baidu_search.test_search_python.png")
