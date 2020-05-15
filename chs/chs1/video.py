# -*- coding: utf-8 -*-
# @Time : 2020/4/8 23:20
# @Author : qxm
# @FileName: video.py

from time import sleep
from selenium import webdriver

driver =webdriver.Chrome()
driver.get("http://videojs.com/")
driver.maximize_window()
video = driver.find_element_by_id("preview-player_html5_api")
#返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;",video)
# execute_script 调用js方法 ，arguments[0] 去arguments对象的第一个值，currentSrc返回当前音频的url
print(url)

driver.implicitly_wait(10)

#播放视频 load()加载,play()播放,pause()暂停
print("start")
driver.execute_script("arguments[0].play()",video)
sleep(5) #播放5s

#暂停
print("stop")
driver.execute_script("arguments[0].pause()",video)

# driver.quit()