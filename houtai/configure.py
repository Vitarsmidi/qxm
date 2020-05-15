# -*- coding: utf-8 -*-
# @Time : 2018/8/6 15:20
# @Author : sunlin
# @File : configure.py
# @Software: PyCharm
import os
from configobj import ConfigObj
# ConfigParser解析INI文件 需安装configobj 模块

# 获取配置文件值
def getConfig(section, key):
    config_path = 'config.ini'
    config = ConfigObj(config_path, encoding='UTF8')
    value = config[section][key]
    return value


if __name__ == '__main__':
    print(getConfig('SME', 'iphoneType'))
    # dir_work = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(dir_work+r"\houtai\hou.docx")
