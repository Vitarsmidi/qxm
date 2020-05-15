# -*- coding: utf-8 -*-
# @Time : 2020/4/24 9:36
# @Author : qxm
# @FileName: sumiao.py

from PIL import Image, ImageDraw, ImageFont,ImageOps,ImageFilter  #图像操作库PIL，常用三个模块Image，ImageDraw，ImageFont

img=Image.open('ss.jpg') #读取图片

def dodge(a,b,alpha): # # 图像组成：红绿蓝（RGB）三原色组成 r：red红色 g：green绿色 b：blue蓝色 a：alpha透明度 0～255
    return min(int(a*255/(256-b*alpha)),255)
def draw(img,blur=25,alpha=1.0):
    img1=img.convert('L') #将图片转为灰色
    img2=img1.copy()
    img2=ImageOps.invert(img2)

    for i in range(blur): #模糊度
        img2=img2.filter(ImageFilter.BLUR)
    width,height=img1.size
    for x in range(width):
        for y in range(height):
            a =img1.getpixel((x,y))
            b =img2.getpixel((x,y))
            img1.putpixel((x,y),dodge(a,b,alpha))
    img1.show()
    img1.save('ssnew.jpg')
draw(img)