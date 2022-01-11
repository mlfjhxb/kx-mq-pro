
#实例化一个LWPcookiejar对象
import requests
from http.cookiejar import LWPCookieJar

def write_cookie(self):
    new_cookie_jar = LWPCookieJar(self.username + '.txt')
    #将转换成字典格式的RequestsCookieJar（这里我用字典推导手动转的）保存到LWPcookiejar中
    requests.utils.cookiejar_from_dict({c.name: c.value for c in self.session.cookies}, new_cookie_jar)
    #保存到本地文件
    new_cookie_jar.save('cookies/' + self.username + '.txt', ignore_discard=True, ignore_expires=True)
def read_cookie(self):
    #实例化一个LWPCookieJar对象
    load_cookiejar = LWPCookieJar()
    #从文件中加载cookies(LWP格式)
    load_cookiejar.load('cookies/' + self.username + '.txt', ignore_discard=True, ignore_expires=True)
    #工具方法转换成字典
    load_cookies = requests.utils.dict_from_cookiejar(load_cookiejar)
    #工具方法将字典转换成RequestsCookieJar，赋值给session的cookies.
    self.session.cookies = requests.utils.cookiejar_from_dict(load_cookies)

if __name__ == '__main__':
    url = "http://www.baidu.com"
    response = requests.get(url)
    print(type(response.cookies))
    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    print(cookies)