# coding:utf-8
import datetime
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://onewechat.bnu.edu.cn/ncov/wap/default/index"

def open(ids,pwd):
    driver = webdriver.Edge()
    time.sleep(1)
    driver.get(url)
    time.sleep(1)

    inputTag = driver.find_element(By.CSS_SELECTOR, '[placeholder="账号"]')
    inputTag.send_keys(ids)
    time.sleep(1)
    inputTag = driver.find_element(By.CSS_SELECTOR, "[placeholder='密码']")
    inputTag.send_keys(pwd)
    time.sleep(1)

    # btn=driver.find_element(By.CLASS_NAME, "login-btn")
    try:
        btn=driver.find_element(By.CLASS_NAME, "login-btn")
    except(selenium.common.exceptions.NoSuchElementException):
        btn=driver.find_element(By.CLASS_NAME, "btn")
    except:
        print("Error occurred")
    btn.click()
    time.sleep(2)

    js = "var q=document.documentElement.scrollTop=800"
    driver.execute_script(js)
    inputTag = driver.find_element(By.CSS_SELECTOR, "[placeholder='点击获取地理位置']")
    inputTag.click()
    time.sleep(5)

    driver.execute_script(js)
    submit = driver.find_element(By.LINK_TEXT,"提交信息（Submit）")
    submit.click()
    time.sleep(2)
    
    xpath = "//div[@class='wapcf-btn wapcf-btn-ok']"
    try:
        affirm = driver.find_element(By.XPATH, xpath)
    except(selenium.common.exceptions.NoSuchElementException):
        xpath = "//div[@class='wapat-btn wapat-btn-ok']"
        affirm = driver.find_element(By.XPATH, xpath)
        print("already clock-in")
    except:
        print("Error occurred")
    affirm.click()
    time.sleep(1)
    driver.close()
    print(f"finished,id={ids},pwd={pwd}\n")

if __name__=="__main__":
    id_lcy="201911081218"
    pwd_lcy="LCYrr013428"
    id_xjd="201911081217"
    pwd_xjd="xjd3364755764"
    print("start auto clock-in")
    while True:
        now = datetime.datetime.now()
        now_str = str(now)[11:16]
        # print(now_str)
        if(now_str=="00:00"):
            print(now_str)
            open(id_lcy,pwd_lcy)
            open(id_xjd,pwd_xjd)
        time.sleep(0.5)
