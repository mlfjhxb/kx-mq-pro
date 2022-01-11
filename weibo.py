import requests
from selenium import webdriver
import time
from lxml import etree
# -*- coding: UTF-8 -*-

def login_weibo():
    rst= driver.get("http://t.knet.cn")
    time.sleep(10)

    # element=driver.find_element_by_id('loginname')
    # element.send_keys('你的账号名')
    #
    # element=driver.find_element_by_name('password')
    # element.send_keys('你的密码')
    # element=driver.find_element_by_class_name('W_btn_a')
    # element.click()
def search_weibo():
    #查找搜索框并输入信息
    elements=driver.find_elements_by_class_name('W_input')
    elements[0].send_keys('迪丽热巴')
    #点击搜索按钮
    element=driver.find_element_by_class_name('ficon_search')
    element.click()
    time.sleep(10)
    #进入迪丽热巴的微博
    element=driver.find_elements_by_xpath("//a[@href='//weibo.com/u/1669879400']")[0]
    element.click()
    time.sleep(3)
def select_all():
    #定位最新打开的窗口
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    #选择全部按钮，点击
    element=driver.find_element_by_xpath("//li[@class='tab_li tab_li_first']/a")
    element.click()
    time.sleep(10)

def crawel():
    i=0
    file = open("d://img//spider1.txt", "w")
    print('------------crawl---------------')
    while(i!=3):
        #翻页
        js = "window.scrollTo(0, document.body.scrollHeight)"
        driver.execute_script(js)
        time.sleep(5)
        #使用etree查看是否有下一页元素
        page=driver.page_source
        parser = etree.HTMLParser(encoding="utf-8")
        html_parse = etree.HTML(page, parser=parser)
        print(html_parse)
        # result = etree.tostring(html_parse, pretty_print=True,encoding="utf-8")
        pnext=[]
        try:
            pnext=driver.find_element_by_xpath("//a[@class='page next S_txt1 S_line1']")
        except   Exception:
            print('-------未获取到page next')
        else:
            print('-------success获取到page next')
        #存在下一页元素，此时该页全部加载完毕，爬取
        if  pnext!=[]:
            text_list=driver.find_elements_by_xpath("//div[@class='WB_text W_f14']")
            print(text_list)
            for index in range(0,len(text_list)):
                result=text_list[index].text.replace(' ','').replace('\n','')
                if result!='':
                    print('---',i,'--',result)
                    file.write(result+'\n')
            element=driver.find_element_by_class_name('next')
            element.click()
            i=i+1
    file.close()
if __name__ == '__main__':
    # requests.utils.dict_from_cookiejar()
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values' :{'notifications' : 2},
             'profile.managed_default_content_settings.images':2}
    options.add_experimental_option('prefs',prefs)
    options.add_argument('lang=zh_CN.UTF-8')
    driver = webdriver.Chrome(executable_path="C:\mysoft\chromedriver_win32\chromedriver",options=options)
    # driver.maximize_window()

    login_weibo()

    # search_weibo()

    crawel()

