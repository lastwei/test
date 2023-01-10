# -*- coding: utf-8 -*-
import fileinput
import random
import time
import traceback
import  pytest
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import hmac
import hashlib
import base64
import urllib.parse
import urllib.request
import datetime
import json

num = 0
timestamp = str(round(time.time() * 1000))
secret = 'SEC2914dd8cb7020f4ed72ff122fa35c07819c428a40f0f2610e63bc9ee07f151df'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
# https://oapi.dingtalk.com/robot/send?access_token=f06421472e6d5c8ac66a3cde75049b9e52fe5bed6ff72399da89d5543171569c
url = f'https://oapi.dingtalk.com/robot/send?access_token=f06421472e6d5c8ac66a3cde75049b9e52fe5bed6ff72399da89d5543171569c&timestamp={timestamp}&sign={sign}'


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


def get_string():
    '''
    自己想要发送的内容，注意消息格式，如果选择markdown，字符串中应为包含Markdown格式的内容
    例：
    "<font color=#00ffff>昨日销售额：XXX</font> \n <font color=#00ffff>昨日销量：XXX</font>"
    '''
    return "<font color=#00ffff>昨日销售额：XXX</font> \n <font color=#00ffff>昨日销量：XXX</font>"


def main(txt):
    # isAtAll：是否@所有人，建议非必要别选，不然测试的时候很尴尬
    global  num
    num = num +1
    dict = {
        "msgtype": "markdown",
        "markdown": {"title": "测试结果",
                     "text":  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + txt + "@13541008582"
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
def login():
    driver = webdriver.Chrome()
    driver.get("http://192.168.10.1")
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div/div[1]/img')))
    except:
        print("fail!!!")
    # txt = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/div[3]/div/label').text
    # print(txt)
    # user = driver.find_element(By.CLASS_NAME, 'ant-form-item-control').clear()
    # user = driver.find_element(By.CLASS_NAME,'ant-form-item-control').send_keys("user")
    user = driver.find_element(By.ID,'password_login').send_keys("123456")
    button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div/button').click()
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div[2]/div/div[1]')))
    except:
        print("fail!!!")
    return driver
def test_check_internet():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div/div[3]/button[2]').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'ant-modal-body').click()
    a = driver.find_elements(By.CLASS_NAME, "ant-btn-primary")[3].click()
    # for i in a:
    #     print(i.text)
    # while True:
    #     pass
    time.sleep(180)
    driver.close()
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div[2]/div/div[6]').click()
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div[2]/div/div[1]')))
    except:
        print("fail!!!")

    time.sleep(1)
    driver.find_elements(By.CLASS_NAME, 'ant-menu-submenu-title')[1].click()
    time.sleep(1)
    internet = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div[2]/div/div[2]/div/span/div[2]/div/table/tbody/tr[1]/td').text
    print(internet)
    if internet=="已接入互联网":
        print("有网")
        main("successs")
        assert 1
    else:
        print("没网")
        main("fail")
        assert 0
    # user = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/div[3]/div[2]/div/div[2]').click()
    # try:
    #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div[3]/div/span/form/div[1]/div[1]/label')))
    # except:
    #     print("fail!!!")
    #
    # driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/div[3]/div[3]/div/span/form/div[1]/div[2]/div/span/div').click()
    # driver.find_element(By.CLASS_NAME,'ant-select-dropdown-menu-item')[0].click()#选择桥接
    # driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/div[3]/div[3]/div/span/form/div[3]/div[1]/div/div/span/button[2]').click()
    # time.sleep(30)
    # try:
    #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div[2]/div/div[1]')))
    # except:
    #     print("fail!!!")
    # driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div[2]/div/div[1]').click()
    # try:
    #     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div[2]/div/div[1]')))
    # except:
    #     print("fail!!!")
    # internet = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div[3]/div/div[2]/div[1]/label').text
    # if internet != "--------":
    #     print("有网")
    # else:
    #     print("没网")

if __name__ == '__main__':
    while True:
        test_check_internet()
    # pytest.main(["-vs","autoweb.py"])