#coding:utf-8
import time

from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

if __name__ == '__main__':
    url="https://passport.ctrip.com/user/member/fastOrder"

    # Chrome,此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(executable_path="C:\mysoft\chromedriver_win32\chromedriver",options=options)
    driver.maximize_window()

    driver.get(url)
    time.sleep(5)

    sour=driver.find_element(By.CLASS_NAME,'cpt-drop-btn') #获取滑块
    ele=driver.find_element(By.CLASS_NAME,'cpt-bg-bar') #获取整个滑块框

    print('--bg bar--',ele.size,ele.location['x'])

    action = ActionChains(driver)
    action.click_and_hold(on_element=sour).perform()
    print('--btn--',sour.size,sour.location['x'])
    time.sleep(0.15)
    ActionChains(driver).move_to_element_with_offset(to_element=sour, xoffset=30, yoffset=0).perform()
    time.sleep(1)
    print(30,sour.location['x'],sour.location['y'])
    ActionChains(driver).move_to_element_with_offset(to_element=sour, xoffset=100, yoffset=0).perform()
    time.sleep(0.5)
    print(100,sour.location['x'],sour.location['y'])
    ActionChains(driver).move_to_element_with_offset(to_element=sour, xoffset=190, yoffset=0).release().perform()
    print(190,sour.location['x'],sour.location['y'])