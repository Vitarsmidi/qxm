
# -*- coding: utf-8 -*-
# @Time : 2020/5/08 21:47
# @Author : qxm
# @FileName: test_baidu.py

"""
@function python 基本用法

1.pytest test_baidu3.py --junit-xml=./report/log.xml   生成xml文件
2.pytest test_baidu3.py --pastebin=all  生成连接
3.pytest test_baidu3.py --html=./report/report.html  生成html文件

pytest.main(["-v", "-s", "test_baidu.py"])
-q :用来减少测试运行的冗长；-v :用增加测试运行的冗长；-s :用来关闭捕捉，输出打印信息；
"""

import sys
from time import sleep
import pytest
from os.path import dirname, abspath
import json
base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)
# sys.path.insert(0, dirname(dirname(abspath(__file__))))
from chs.chs5.page.baidu_page import BaiduPage


def get_data(file_path):
    """
    读取参数化文件
    :param file_path:
    :return:
    """
    data = []
    with(open(file_path, "r")) as f:
        dict_data = json.loads(f.read())
        for i in dict_data:
            data.append(tuple(i.values()))
    return data


@pytest.mark.parametrize(
    "name, search_key",
    get_data(base_path + "/test_dir/data/data_file.json")
)


class TestSearch:
    """百度搜索"""

    def test_baidu_search_case(self, name,search_key,browser, base_url):
        """
       调用conftest.py中的 base_url()、browser()钩子函数

        名称：百度搜索"pytest"
        步骤：
        1、打开浏览器
        2、输入"pytest"关键字
        3、点击搜索按钮
        检查点：
        * 检查页面标题是否包含关键字。
        """
        page = BaiduPage(browser) #调用BaiduPage类，传入browser驱动
        page.get(base_url)
        page.search_input = search_key
        page.search_button.click()
        sleep(1)
        assert browser.title == search_key + u"_百度搜索"



# class TestSearchSettings:
#     """百度搜索设置"""
#
#     def test_baidu_search_setting(self, browser, base_url):
#         """
#         名称：百度搜索设置
#         步骤：
#         1、打开百度浏览器
#         2、点击设置链接
#         3、在下拉框中"选择搜索"
#         4、点击"保存设置"
#         5、对弹出警告框保存
#         检查点：
#         * 检查是否弹出提示框
#         """
#         page = BaiduPage(browser)
#         page.get(base_url)
#         page.settings.click()
#         page.search_setting.click()
#         sleep(2)
#         page.save_setting.click()
#         alert_text = page.get_alert_text
#         page.accept_alert()
#         assert alert_text == "已经记录下您的使用偏好"


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_baidu.py"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch::test_baidu_search_case"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearchSettings"])
    # pytest.main(["-q", "test_baidu.py"])


