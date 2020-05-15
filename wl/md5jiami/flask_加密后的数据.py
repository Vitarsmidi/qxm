from flask import Flask
from flask import request
from base64 import b64encode

app = Flask(__name__)

@app.route('/user')
def login2():
    """获取用户名和密码，返回 token"""
    id = 'yuz123'
    id_bs64 = b64encode(id.encode('utf-8')) #加密
    id = id_bs64.decode('utf-8')
    return {"code": 1002, "data": {"user": id}}

# yuz123  5d41402abc4b2a76b9719d911017c592
# yuz123  5d41402abc4b2a76b9719d911017c592
# 123456  5d41402abc4b2a76b9719d911017c592
# 888888  5d41402abc4b2a76b9719d911017c592
# 623
# 1230
# 加盐  salt



if __name__ == '__main__':
    app.run(debug=True)