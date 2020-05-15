# -*- coding: utf-8 -*-
# @Time : 2020/5/7 22:36
# @Author : qxm
# @FileName: assert.py

"""

-- assert 常用断言方法 --


self.assertEqual(self.driver.title, search_key + u"_百度搜索")


now_user = driver.find_element_by_class_name("user-info").text
if now_user == u'当前用户： admin':
    print('登录成功', now_user)
else:
    raise NameError('user name error!')

self.assertIn(now_user,'当前用户： admin') #assertIn(a,b)断言，a is b
print('登录成功', now_user)


1.assertEqual(self, first, second, msg=None)  --判断两个参数相等：first == second

2.assertNotEqual(self, first, second, msg=None)  --判断两个参数不相等：first ！= second

3.assertIn(self, member, container, msg=None)  --判断是字符串是否包含：member in container

4.assertNotIn(self, member, container, msg=None)  --判断是字符串是否不包含：member not in container

5.assertTrue(self, expr, msg=None)   --判断是否为真：expr is True

6.assertFalse(self, expr, msg=None)  --判断是否为假：expr is False

7.assertIsNone(self, obj, msg=None)  --判断是否为None：obj is None

8.assertIsNotNone(self, obj, msg=None)  --判断是否不为None：obj is not None

9.assertIsInstance(obj, cls, msg=None)	--判断obj是cls的实例，不是则fail

10.assertNotIsInstance(obj, cls, msg=None)	--判断obj不是cls的实例，是则fail


　　pytest里面断言实际上就是python里面的assert断言方法，常用的有以下几种

　　1.assert xx判断xx为真

　　2.assert not xx判断xx不为真

　　3.assert a in b 判断b包含a

　　4.assert a == b 判断a等于b

　　5.assert a != b 判断a不等于b


assert expression [, arguments]
assert 表达式 [, 参数]

assert x ==5

a = 1
assert a < 0, '出错了,a大于0 啊'
print('这里不会输出')

a = 1
b = -1
assert a > 0, b < 0
print('正常输出,表达式返回真了') # 输出：正常输出,表达式返回真了


# 断言异常类型type
assert excinfo.type == ZeroDivisionError
# 断言异常value值
assert "division by zero" in str(excinfo.value)



-- 功能 --
def add(a,b):
    return a + b

-- 测试相等
def test_add():
    assert add(3,4) == 7

# 测试不相等
def test_add2():
    assert add(17,22) != 50

# 测试大于
def test_add3():
    assert add(17,22) <= 50

# 测试小于
def test_add4():
    assert add(17,22) >= 50

# 测试相等
def test_in():
    a = "hello"
    b = "he"
    assert b in a


# 测试不相等
def test_not_in():
    a = "hello"
    b = "hi"
    assert b not in a

#用于判断素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


# 判断是否为素数
def test_true():
    assert is_prime(13)


# 判断是否不为素数
def test_true():
    assert not is_prime(7)


"""
