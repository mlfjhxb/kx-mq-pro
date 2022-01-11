# coding:utf-8

####headless模式####
import pickle

from pandas._libs import json
from selenium import webdriver
from time import sleep
import time
import  requests



if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="C:\mysoft\chromedriver_win32\chromedriver")
    driver.get("https://www.ketangpai.com/#/login")
    driver.implicitly_wait(1)
    print('-------1---',driver.get_cookies())

    savedCookies = driver.get_cookies()
    driver2 = webdriver.Chrome(executable_path="C:\mysoft\chromedriver_win32\chromedriver")
    driver2.get("https://www.ketangpai.com/#/main")
    driver2.delete_all_cookies()
    for cookie in savedCookies:
        driver2.add_cookie(cookie)
        # fix the problem-> "errorMessage":"Unable to set Cookie"
        # for k in ('name', 'value', 'domain', 'path', 'expiry'):
        #     if k not in list(cookie.keys()):
        #         if k == 'expiry':
        #             t = time.time()
        #             cookie[k] = int(t) # 时间戳 秒
        #     # fix the problem-> "errorMessage":"Can only set Cookies for the current domain"
        # driver2.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path', 'expiry') if k in cookie})

    driver2.implicitly_wait(1)
    print('-------2---',driver2.get_cookies())

    driver2.get("https://www.ketangpai.com/#/main")
    driver2.implicitly_wait(1)
    print('-------3---',driver2.get_cookies())


    #------------------------------ 读、写cookie -------------
    cookie =driver.get_cookies()
    jsonCookies = json.dumps(cookie)
    print('----dump json:'+jsonCookies)
    open('d://img//aa.json', 'w').write(jsonCookies)

    str=''
    with open('d://img//aa.json','r',encoding='utf-8') as f:
        listCookies=json.loads(f.read())
    print(listCookies)
    cookie = [item["name"] + "=" + item["value"] for item in listCookies]
    print("---------转换成数组: ",cookie)
    cookiestr = '; '.join(item for item in cookie)
    print('--------处理后的cookie: ',cookiestr)
