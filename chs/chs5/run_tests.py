# -*- coding: utf-8 -*-
# @Time : 2020/5/08 22:17
# @Author : qxm
# @FileName: run_test.py

import os
import time
import logging
import pytest
import click
from chs.chs5.conftest import REPORT_DIR
from chs.chs5.config import RunConfig

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python3 run_tests.py  (回归模式，生成HTML报告)
  > python3 run_tests.py -m debug  (调试模式)
  
click 命令行工具开发库，  click提供run,debug两种运行模式
  
logging模块是Python内置的标准模块，主要用于输出运行日志，可以设置输出日志的等级、日志保存路径、日志文件回滚等。
在python中，logging由logger，handler，filter，formater四个部分组成：
logger是提供我们记录日志的方法；handler是让我们选择日志的输出地方，如：控制台，文件，邮件发送等，一个logger添加多个handler；
filter是给用户提供更加细粒度的控制日志的输出内容；formater用户格式化输出日志的信息。
第一种：基础配置，logging.basicConfig(filename="config.log",filemode="w",format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",level=logging.INFO)。
第二种：使用配置文件的方式配置logging,使用fileConfig(filename,defaults=None,disable_existing_loggers=Ture )函数来读取配置文件。
第三种：使用一个字典方式来写配置信息，然后使用dictConfig(dict,defaults=None, disable_existing_loggers=Ture )函数来瓦按成logging的配置.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
filename: 指定日志文件名
filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
 %(levelno)s: 打印日志级别的数值
 %(levelname)s: 打印日志级别名称
 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
 %(filename)s: 打印当前执行程序名
 %(funcName)s: 打印日志的当前函数
 %(lineno)d: 打印日志的当前行号
 %(asctime)s: 打印日志的时间
 %(thread)d: 打印线程ID
 %(threadName)s: 打印线程名称
 %(process)d: 打印进程ID
 %(message)s: 打印日志信息
datefmt: 指定时间格式，同time.strftime()
level: 设置日志级别，默认为logging.WARNING
stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

日志一共分成5个等级，从低到高分别是：DEBUG ,INFO ,WARNING ,ERROR, CRITICAL。
DEBUG：详细的信息,通常只出现在诊断问题上
INFO：确认一切按预期运行
WARNING：一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。
ERROR：更严重的问题,软件没能执行一些功能
CRITICAL：一个严重的错误,这表明程序本身可能无法继续运行
这5个等级，也分别对应5种打日志的方法： debug 、info 、warning 、error 、critical。默认的是WARNING，当在WARNING或之上时才被跟踪。
  
'''


def init_env(now_time):
    """
    初始化测试报告目录
    """
    os.mkdir(REPORT_DIR + now_time)
    os.mkdir(REPORT_DIR + now_time + "/image")


@click.command()
@click.option('-m', default='run', help='输入运行模式：run 或 debug.')
def run(m):
    if m is None or m == "run":
        logger.info("回归模式，开始执行✈✈！")
        now_time = time.strftime("%Y_%m_%d_%H%M%S")
        init_env(now_time)
        html_report = os.path.join(REPORT_DIR, now_time,now_time+ "report.html")
        xml_report = os.path.join(REPORT_DIR, now_time, now_time+"junit-xml.xml")
        pytest.main(["-s", "-v", RunConfig.cases_path,
                     "--html=" + html_report,
                     "--junit-xml=" + xml_report,
                     "--self-contained-html",
                     "--maxfail", RunConfig.max_fail,
                     "--reruns", RunConfig.rerun])
        logger.info("运行结束，生成测试报告♥❤！")
    elif m == "debug":
        print("debug模式，开始执行！")
        pytest.main(["-v", "-s", RunConfig.cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()

