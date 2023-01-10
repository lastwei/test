# -*- coding: utf-8 -*-
import time
import hmac
import hashlib
import base64
import urllib.parse
import urllib.request
import datetime
import json

import pytest

num = 0
def send_request(url, datas):
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    sendData = json.dumps(datas)
    sendDatas = sendData.encode("utf-8")
    request = urllib.request.Request(url=url, data=sendDatas, headers=header)
    opener = urllib.request.urlopen(request)
    # 输出响应结果
    print(opener.read())

@pytest.fixture(scope="class")
def get_string():
    '''
    自己想要发送的内容，注意消息格式，如果选择markdown，字符串中应为包含Markdown格式的内容
    例：
    "<font color=#00ffff>昨日销售额：XXX</font> \n <font color=#00ffff>昨日销量：XXX</font>"
    '''
    return "123"

@pytest.mark.usefixtures("get_string")
class Testmain():
    def send_request(url, datas):
        header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }
        sendData = json.dumps(datas)
        sendDatas = sendData.encode("utf-8")
        request = urllib.request.Request(url=url, data=sendDatas, headers=header)
        opener = urllib.request.urlopen(request)
        # 输出响应结果
        print(opener.read())

    def test_main(self,get_string):
        timestamp = str(round(time.time() * 1000))
        secret = 'SEC2914dd8cb7020f4ed72ff122fa35c07819c428a40f0f2610e63bc9ee07f151df'
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        # https://oapi.dingtalk.com/robot/send?access_token=f06421472e6d5c8ac66a3cde75049b9e52fe5bed6ff72399da89d5543171569c
        url = f'https://oapi.dingtalk.com/robot/send?access_token=f06421472e6d5c8ac66a3cde75049b9e52fe5bed6ff72399da89d5543171569c&timestamp={timestamp}&sign={sign}'
        # isAtAll：是否@所有人，建议非必要别选，不然测试的时候很尴尬
        global num
        num = num + 1
        dict = {
            "msgtype": "markdown",
            "markdown": {"title": "测试结果",
                         "text": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + get_string +"已执行次数："+ str(num) + "@13541008582"
                         },
            "at": {
                "atMobiles": ["13541008582"],
                "isAtAll": False
            }
        }

        #把文案内容写入请求格式中
        # dict["markdown"]["text"] = get_string()
        print(dict)
        send_request(url, dict)
@pytest.fixture(scope="class")
def test_01():
    a = 6
    b = 6
    return (a, b)


@pytest.fixture(scope="class")
def test_02():
    print("你是第二个执行")


@pytest.mark.usefixtures("test_02")
class TestNum:
    def test_03(self, test_01):
        a = test_01[0]
        b = test_01[1]
        assert a == b
        print("断言成功")
if __name__=="__main__":
    pytest.main(["-s","robot_123.py::Testmain","--count=3","--capture=sys","--html=report.html","--self-contained-html"])
