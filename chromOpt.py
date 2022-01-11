# coding:utf-8

####headless模式####
import pickle
import time

from lxml import etree
from pandas._libs import json
from selenium import webdriver
from time import sleep
import  requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-infobars')  #禁用浏览器正在被自动化程序控制的提示
    # options.add_argument('--start-maximized')
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument('--blink-settings=imagesEnabled=false')    #不显示图片
    options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    # options.add_argument('--headless')    #不提供可视化   无界面运行（无窗口）
    # options.add_argument('--incognito') # 隐身模式（无痕模式）
    options.add_argument('--window-size=100,768')#设置窗口大小
    options.add_argument('-–hide-scrollbars')#设置隐藏滚动条
    # mobileEmulation = {'deviceName': 'Apple iPhone 4'}
    # options.add_experimental_option('mobileEmulation', mobileEmulation)
    prefs = {'profile.default_content_setting_values' :  {'notifications' : 2}}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(executable_path="C:\mysoft\chromedriver_win32\chromedriver",options=options)
    #设置等待
    wait = WebDriverWait(driver,10,0.5)
    # element =wait.until(EC.presence_of_element_located((By.ID,"kw")),message="")
    #使用匿名函数
    # wait.until(lambda diver:driver.find_element_by_id('kw'))
    # 此处注意，如果省略message=“”，则By.ID外面是三层()
    driver.get('https://blog.csdn.net/liu_xzhen/article/details/89381468')
    sleep(3)

'''
#翻页
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(5)
#使用etree查看是否有下一页元素
page=driver.page_source

#option.add_argument('--headless')    #没有窗口的模式
#option.add_argument('--start-maximized')    #窗口最大化
option.add_argument('--window-size=1024,768')    #设置窗口大小
option.add_argument('--disable-infobars')    #在窗口上不出现‘自动化测试’提示
#==不加载图片
prefs = {"profile.managed_default_content_settings.images": 2}
#==或
prefs = {'profile.default_content_setting_values' : {'images' : 2}}
#禁止chrome弹窗（注意是chrome自带的弹窗，不是网站的弹窗）
prefs = {'profile.default_content_setting_values' :  {'notifications' : 2}}
options.add_experimental_option("prefs", prefs)
#不显示图片
option.add_argument('--blink-settings=imagesEnabled=false')    
#密码提示框
# 设置这两个参数就可以避免密码提示框的弹出
prefs = {} 
prefs[“credentials_enable_service”] = False   
prefs[“profile.password_manager_enabled”] = False 
options.add_experimental_option(“prefs”, prefs) 
#模仿手机
option = webdriver.ChromeOptions()
# 伪装iphone登录
# option.add_argument('--user-agent=iphone')
# 伪装android
option.add_argument('--user-agent=android')
driver = webdriver.Chrome(options=option)
#自己下载的crx路径#加插件
option.add_extension('d:\crx\AdBlock_v2.17.crx')
# 设置下载路径
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": "/path/download"}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
# 设置代理
PROXY = "23.23.23.23:3128" # IP:PORT or HOST:PORT
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://%s' % PROXY)
chrome = webdriver.Chrome(options=options)
chrome.get("http://whatismyipaddress.com")
'''
