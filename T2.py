import json
#导包
import logging

import requests
from selenium import webdriver
#创建类
class spider():
    # 定义属性
    def __init__(self):
        self.url = "http://www.baidu.com"
    #定义方法
    def write_keep(self):
        # 打开谷歌
        driver = webdriver.Chrome(executable_path="C:\mysoft\chromedriver_win32\chromedriver")
        # 设置隐式等待
        driver.implicitly_wait(2)
        #窗口最大化
        # driver.maximize_window()
        # 打开百度贴吧网址
        driver.get("http://www.baidu.com")
        # cookies_dict = requests.utils.dict_from_cookiejar(driver.get_cookies())
        # logging.info(cookies_dict)
        #打开文件
        file = open("d://img//hxb.txt", "w")
        #抓取元素保存到文件中
        for i in range(1, 4):
            ele = driver.find_element_by_xpath("//li[@class='hotsearch-item odd']").text
            print(i,ele)
            # 去掉字符间可能存在的空格
            ss = ''.join(ele.split())
            # 写入文件
            file.write(str(i) + "  " + ss + "\n")
            # 关闭文件
        file.close()

        driver.close()
#类的实例化与调用
if __name__ == '__main__':
    spider1 = spider()
    spider1.write_keep()

