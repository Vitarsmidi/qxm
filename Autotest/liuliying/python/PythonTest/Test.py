#coding=utf-8
import random
import string
import datetime

def get_random(counts):

    pre = "JKZJHM"
    now = datetime.datetime.now().strftime('%Y%m%d')

    li = string.digits
    sub = ''
    for n in range(0, int(counts)):
        sub += li[random.randint(0, len(li) - 1)]
    return pre + now + sub

print get_random(counts=4)
print 1100//3