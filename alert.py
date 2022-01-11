# -*- coding=utf-8 -*-
# 导入模块
from selenium import webdriver
from time import sleep
#1.引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains


if __name__=='__main__':

    # browser = webdriver.Chrome(executable_path ="C:\mysoft\chromedriver_win32\chromedriver")
    driver =webdriver.Firefox(executable_path ="C:\mysoft\chromedriver_win32\geckodriver")
    driver.implicitly_wait(1)
    driver.get('http://www.baidu.com')

    #-------=========================================== 获取断言信息
    # 打印当前页面title
    title = driver.title
    print('搜索页的title=[%s]',title)
    # 打印当前页面URL
    now_url = driver.current_url
    print('当前搜索的url=[%s]',now_url)

    #-------=========================================== 控制浏览器操作
    #3.刷新浏览器
    driver.refresh()
    #4.设置浏览器的大小
    driver.set_window_size(1400,800)

    #-------=========================================== 定位元素
    element= driver.find_element_by_id("s-usersetting-top")
    #-------=========================================== 鼠标事件
    #3.对定位到的元素执行鼠标悬停操作
    ActionChains(driver).move_to_element(element).perform()
    #找到链接
    elem1=driver.find_element_by_link_text("搜索设置")
    elem1.click()
    #通过元素选择器找到id=sh_2,并点击设置
    elem2=driver.find_element_by_id("sh_1")
    elem2.click()
    #保存设置
    elem3=driver.find_element_by_class_name("prefpanelgo")
    elem3.click()
    #弹出框 确认
    driver.switch_to.alert.accept()
    sleep(1)

    #-------=========================================== 键盘事件
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    sleep(2)
    # 获取结果数目
    searchTotal = driver.find_element_by_class_name('nums').text
    print('搜索的结果统计如下：\n [%s]',searchTotal)

    #-------=========================================== 定位一组元素
    #1.定位一组元素
    elements = driver.find_elements_by_xpath('//div/h3/a')
    print('获取的a链结果类型为：%s',type(elements))
    #2.循环遍历出每一条搜索结果的标题
    for t in elements:
        print("====",t.text)
        # element=driver.find_element_by_link_text(t.text) #或者 t.click()
        sleep(1)

    driver.quit()



