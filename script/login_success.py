#导包
import unittest
import app
from api.login import LoginAPI
#创建测试类

class login_success(unittest.TestCase):
    #setup 实例化类
    def setUp(self):
        self.login_success=LoginAPI()

    #测试用例
    def test01_login(self):
        response=self.login_success.login({"mobile":"13800000002","password":"123456"})
        app.TOKEN = "Bearer" + response.json().get("data")
        app.headers_data["Authorization"] = app.TOKEN

