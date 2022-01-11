from selenium import webdriver
from time import sleep
import  time
from _datetime import datetime

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

if __name__ == '__main__':

    #设置特殊的 页面加载参数
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('--start-maximized')
    chrome_option.add_argument('--blink-settings=imagesEnabled=false')    #不显示图片
    #options.add_argument('--headless')    #不提供可视化

    driver = webdriver.Chrome(executable_path="C:\mysoft\chromedriver_win32\chromedriver",options=chrome_option)
    # driver = webdriver.Firefox(executable_path="C:\mysoft\chromedriver_win32\geckodriver",chrome_options=chrome_option)
    driver.get('http://sbj.cnipa.gov.cn/sbcx/')
    wait = WebDriverWait(driver,10,0.5)
    element =wait.until(expected_conditions.presence_of_element_located((By.ID,"kw")),message="")
    sleep(1)
    # driver.set_window_size(415,300)
    # driver.maximize_window()

    #我接受 超链
    print()
    bg=datetime.now()
    print('--------begin查询 接受 按钮------',bg)
    # driver.find_element_by_xpath("//div[@class='TRS_Editor']/p/a").click()
    driver.find_element_by_css_selector("div.TRS_Editor > p > a").click()
    ed=datetime.now()
    print('-----end查询 接受 按钮-- total_time:',(ed-bg).seconds)
    sleep(1)

    #商标综合查询 超链
    print()
    print('--------begin查询 商标综合查询 按钮------')
    # driver.find_element_by_xpath("//div[@class='nav']/ul/li[@id='txnS02']").click()
    driver.find_element_by_css_selector("li#txnS02 > a").click()
    ed2=datetime.now()
    print('-----end查询 商标综合查询 按钮,并click--node total_time:',(ed2-ed).seconds)
    sleep(3)

    #商标查询条件页
    print()
    print('--------查询 输入条件框 ------')
    ipt_org= driver.find_element_by_xpath("//div[@class='inputbox']/input[@name='request:hnc']")
    ipt_org.clear()
    ipt_org.send_keys("北龙中网（北京）科技有限责任公司")
    driver.find_element_by_xpath("//div[@class='bottonbox']/input[@id='_searchButton']").click()
    ed3=datetime.now()
    print('--------查询 输入条件框 ,并完成点击<查询>---total_time:',(ed3-ed2).seconds)
    sleep(3)

    #判断是否有验证码提示框 新页面
    search_window=driver.current_window_handle
    window_hds=driver.window_handles
    for win in window_hds:
        if win != search_window:  #处理弹框页面
            print('----准备进行新页面--------')

            driver.switch_to.window(win)
            print('----new window  title: ',driver.title)
            if '出错啦' in driver.page_source:
                print('---出错了页面-----')
                sleep(10)
                driver.close()
            if '请继续' ==driver.title:
                print('----进入到验证码页面-----')
                #设置最小的窗口
                driver.set_window_size(350,300)
                #调整 滚动条
                js = "window.scrollTo(0,150);"
                driver.execute_script(js)
                #截图
                driver.get_screenshot_as_file("d://yzm.png")

    # driver.quit()
