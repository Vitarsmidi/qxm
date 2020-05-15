# -*- coding: utf-8 -*-
# @Time : 2020/5/08 21:47
# @Author : qxm
# @FileName: parametrize.py

import sys
import json
from time import sleep
import pytest
from os.path import dirname, abspath

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)
from chs.chs5.page.baidu_page import BaiduPage

"""
 @pytest.mark.parametrize装饰器可以实现测试用例参数化
@pytest.mark.parametrize("参数名",列表数据)
Pytest中装饰器@pytest.mark.parametrize('参数名',list)可以实现测试用例参数化，类似DDT
如：@pytest.mark.parametrize('请求方式,接口地址,传参,预期结果',[('get','www.baidu.com','{"page":1}','{"code":0,"msg":"成功"})',
('post','www.baidu.com','{"page":2}','{"code":0,"msg":"成功"}')])

"""


@pytest.mark.parametrize(
    "name, search_key",
    [("1", "Selenium"),
     ("2", "pytest文档"),
     ("3", "pytest-html"),
     ],
    ids=["case1", "case2", "case3"]
)
def test_baidu_search(name, search_key, browser, base_url):
    page = BaiduPage(browser)
    page.get(base_url)
    page.search_input = search_key
    page.search_button.click()
    sleep(2)
    assert browser.title == search_key + u"_百度搜索"


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
def test_baidu_search2(name, search_key, browser, base_url):
    page = BaiduPage(browser)
    page.get(base_url)
    page.search_input = search_key
    page.search_button.click()
    sleep(2)
    assert browser.title == search_key + u"_百度搜索"
