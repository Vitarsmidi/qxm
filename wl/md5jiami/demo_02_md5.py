
"""
md5 和 sha1 是摘要算法，注意不是加密算法。

摘要算法又称哈希算法、散列算法。把任意长度的数据转换为一个长度固定的数据串。

MD5特征
1.不可逆，即只加密，不能解密
2.长度固定
3.哈希/散列算法

主要所用是验证和原始数据是否一致：
1，防盗版。 https://zh.snipaste.com/download.html# 下载会提供 sha1 值，如果你下载的软件 hash 和他
提供的值不一样，则证明是盗版。
2，数据库校验。   存储的密码是hash后的数据。
3，为了防止撞库，可以加盐。salt 不被别人知道，就不能破解。


实例：
md5.digest() 得到的是 32位 byte
import hashlib
m = hashlib.md5()
m.update(b"hello yuz")
m.digest()
b'\xbf\xb3\xf4q-\x0b\x04\xe84\x8a?\xb5\xfa\x0b\x9b\xc2'

hash.hexdigest() 得到的是32位字符串
hash.hexdigest()
bfb3f4712d0b04e8348a3fb5fa0b9bc2


sha1 算法：
SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
s = hashlib.sha1()
s.update(b"hello yuz")
s.digest()



# 加盐, 不要透露你的 salt
pwd = '8888' + 'the salt'
hash.update(pwd.encode('utf-8'))
hash.digest()
b'\xb7\xd7h\xa2\xd5!\x01\xe6\x0fW8A\xb5\x15\xbd\xdb'

"""
import hashlib
# md5

hash = hashlib.md5()
hash.update(b"hello yuz")
hash_str = hash.digest()
print(hash_str)    # b'\xbf\xb3\xf4q-\x0b\x04\xe84\x8a?\xb5\xfa\x0b\x9b\xc2'

# hexdigest 得到的是字符串
hash = hashlib.md5()
hash.update(b"hello yuz")
hash_str = hash.hexdigest()
print(hash_str) #bfb3f4712d0b04e8348a3fb5fa0b9bc2


# sha1 算法
s = hashlib.sha1()
s.update(b"hello yuz")
sha_str = s.hexdigest()
print(sha_str) #9ff13b4143bb9df6df4923066be16f1e8ffe1b7d


# 加盐
salt = 'the salt'
pwd = 'hello yuz'

salt_pwd = pwd + salt
hash.update(salt_pwd.encode('utf-8'))
hash_str = hash.hexdigest()
print(hash_str)  #1b5263fe5b8b8c0cf318316651c67d13


# 加盐
salt = 'the salt'
pwd = '8888'

salt_pwd = pwd + salt
hash.update(salt_pwd.encode('utf-8'))
hash_str = hash.hexdigest()
print(hash_str)  #9fad7a8cc14c51a5b574c00be4d6ae58

