#导包
import requests
#创建接口类
class LoginAPI:
    #初始化
    def __init__(self):
        self.url_login="http://ihrm-test.itheima.net/api/sys/login"
    #定义接口调用方法
    def login(self,login_data):
        return requests.post(url=self.url_login,json=login_data)

