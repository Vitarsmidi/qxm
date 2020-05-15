"""
Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

base64, 每次得到的结果都是固定的。

因为，Base64将三个字节转化成四个字节，因此Base64编码后的文本，会比原文本大出三分之一左右。

优点：速度快，ascii字符，肉眼不可理解
缺点：编码比较长，非常容易被破解，仅适用于加密非关键信息的场合

在 python 当中， encode 参数必须是 byte 类型
base64.b64encode(b"hello world")

decode 参数可以是字符串，也可以是 byte 类型：
base64.b64encode("aGVsbG8gd29ybGQ=")
base64.b64encode(b"aGVsbG8gd29ybGQ=")


中文处理：
byte_str = "你好， yuz".encode('utf-8')
encode_str = base64.b64encode(byte_str)

解码：
decode_str = base64.b64decode('5L2g5aW977yMIHl1eg==')
decode_str.decode("utf-8")


/ + 等特殊字符的处理, 在url当中是特殊符号，要转换
encode_str = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd++//'

urlsafe模式：
encode_str = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(encode_str)  # b'abcd--__'


"""

import base64

# 编码
byte_str = "I like you".encode('utf-8')
encode_str = base64.b64encode(byte_str)
print(encode_str)   # SSBsaWtlIHlvdQ==

# 解码
decode_str = base64.b64decode("SSBsaWtlIHlvdQ==")
print(decode_str.decode("utf-8"))


byte_str2 = "123456".encode('utf-8')
encode_str2 = base64.b64encode(byte_str2)
print(encode_str2)   # MTIzNDU2==

decode_str2 = base64.b64decode("MTIzNDU2")
print(decode_str2.decode("utf-8"))


# 解码
decode_str3 = base64.b64decode("aGVsbG/kuK3mloflkowv5oCO5LmI5Yqed29ybGQ=")
print("decode_str3:"+decode_str3.decode("utf-8"))

# 中文处理
byte_str = "你好， yuz".encode('utf-8')
encode_str = base64.b64encode(byte_str)
print(encode_str)  #5L2g5aW977yMIHl1eg==

# 中文解码
decode_str = base64.b64decode('5L2g5aW977yMIHl1eg==')
print(decode_str.decode("utf-8"))

# / + 等特殊字符的处理
encode_str = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(encode_str)    # b'abcd++//'
# // 在url当中是路径，不要使用
encode_str = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(encode_str)  # b'abcd--__'


