# -*- coding: utf-8 -*-
# @Time : 2020/4/12 17:01
# @Author : qxm
# @FileName: read_json.py

import json

with open("user_info.json","r") as f:
    data =f.read()

users=json.loads(data)
print(users)
