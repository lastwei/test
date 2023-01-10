import random
import time
import traceback

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login():
    driver = webdriver.Chrome()
    driver.get("http://192.168.10.1")
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div/div[1]/img')))
    except:
        print("fail!!!")

    user = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/div[3]/div/form/div[1]/div[2]/div/span/input').clear()
    user = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/div[3]/div/form/div[1]/div[2]/div/span/input').send_keys()
    # user = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/div[3]/div/form/div[1]/div[2]/div/span/input').send_keys("user")
    # pwd = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/div[3]/div/form/div[3]/div[2]/div/span/span/input').send_keys("123456")
    # button = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/div[3]/div/button').click()
    while True:
        print("1")
    return driver

def lunxun(a):
    driver = webdriver.Chrome()
    try:
        s = driver.get(a)
    except:
        traceback.print_exc()
        pass
    time.sleep(30)
    driver.close()
if __name__ == '__main__':
    list = ["http://www.princeton.edu","http://www.harvard.edu/","http://www.yale.edu/","http://www.caltech.edu/","http://www.stanford.edu/","http://web.mit.edu/","http://www.upenn.edu/","http://www.duke.edu/","http://www.columbia.edu/","http://www.dartmouth.edu/","http://www.uchicago.edu/","http://www.cornell.edu/","http://www.northwestern.edu/","http://www.brown.edu/","http://www.jhu.edu/","http://www.rice.edu/","http://www.vanderbilt.edu/","http://www.emory.edu/","http://www.nd.edu/","http://www.cmu.edu/"]
    while True:
        a = random.randrange(len(list))
        print(list[a])
        lunxun(list[a])
