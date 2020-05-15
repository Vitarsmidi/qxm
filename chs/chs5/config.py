# -*- coding: utf-8 -*-
# @Time : 2020/5/08 21:00
# @Author : qxm
# @FileName: config.py

"""
配置文件
"""

class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = "./test_dir/"

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "chrome"

    # 配置运行的 URL
    url = "https://www.baidu.com"

    # 失败重跑次数
    rerun = "2"

    # 当达到最大失败数，停止执行
    max_fail = "5"


