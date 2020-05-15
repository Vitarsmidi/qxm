from flask import Flask
from flask import request
from base64 import b64encode

app = Flask(__name__)

@app.route('/login')
def login():
    return {"code": 1001, "msg":"success","data": "登陆成功"}


if __name__ == '__main__':
    app.run(debug=True)