from _datetime import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="C:\mysoft\chromedriver_win32\chromedriver")
    wait = WebDriverWait(driver,10,0.5)
    # element =wait.until(expected_conditions.presence_of_element_located((By.ID,"kw")),message="")
    driver.maximize_window()
    driver.get("https://www.ketangpai.com/#/login")
    time.sleep(1)
    user=driver.find_element_by_xpath("//input[@placeholder='请输入邮箱/手机号/账号']")
    pwd=driver.find_element_by_xpath("//input[@placeholder='请输入密码']")
    user.clear()
    user.send_keys("hxb_success@126.com")
    pwd.clear()
    pwd.send_keys("Hxb.js123")
    '''
    有时会出现找到元素，但是无法click的问题，使用script进行替换
    '''
    btn=driver.find_element_by_xpath("//div[@class='go-register text-right font14 flex-align flex-between']//span")
    print(btn.text)
    ActionChains(driver).click(btn).perform()
    js2 = "document.getElementsByClassName('el-button el-button--primary')[0].click()"
    driver.execute_script(js2)
    print('------login cookie---------')
    print(driver.get_cookies())
    time.sleep(1)
    # driver.find_element_by_css_selector("li#txnS02 > a").click()

    cks=driver.get_cookies()
    print('--------driver2----------')
    driver2 = webdriver.Chrome(executable_path="C:\mysoft\chromedriver_win32\chromedriver")
    driver2.maximize_window()
    driver2.get("https://www.ketangpai.com/#/main")
    driver2.delete_all_cookies()

    for ck in cks:
        driver2.add_cookie(ck)
    '''
    #遍历savedCookies中的两个元素
    for cookie in cks:
        print('key----')
        print(cookie)
        #k代表着add_cookie的参数cookie_dict中的键名，这次我们要传入这5个键
        for k in {'name', 'value', 'domain', 'path', 'expiry'}:
            #cookie.keys()属于'dict_keys'类，通过list将它转化为列表
            if k not in list(cookie.keys()):
                #saveCookies中的第一个元素，由于记录的是登录前的状态，所以它没有'expiry'的键名，我们给它增加
                if k == 'expiry':
                    t = time.time()
                    # cookie[k].append(t)
        #将每一次遍历的cookie中的这五个键名和键值添加到cookie
        # driver2.add_cookie({k: cookie[k] for k in {'name', 'value', 'domain', 'path', 'expiry'}})
        driver2.add_cookie(cookie)
  '''
    print(driver2.get_cookies())
    driver2.refresh()
    print('-----cookie2',driver2.get_cookies())


