# -*- coding: utf-8 -*-
# @Time : 2020/4/15 21:18
# @Author : qxm
# @FileName: configure.py

from configobj import ConfigObj
# ConfigParser解析INI文件 需安装configobj 模块

"""
解析ConfigINI文件
"""

# 获取配置文件值
def getConfig(section, key):
    config_path = 'config.ini'
    config = ConfigObj(config_path, encoding='UTF8')
    value = config[section][key]
    return value


if __name__ == '__main__':
    print(getConfig('Chedai'))
