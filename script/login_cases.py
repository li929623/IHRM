#导包
import json
import unittest
from api.login import LoginAPI
from parameterized import parameterized
import app
#构建测试数据
def build_data():
    test_data=[]
    #指定文件路径
    json_file=app.BASE_DIR +"/data/login.json"
    #打开json文件
    with open(json_file,encoding="utf-8") as f:
        #读取json字符串
        json_data =json.load(f)
        for case_data in json_data:
            login_data=case_data.get("login_data")
            status_code=case_data.get("status_code")
            message=case_data.get("message")
            test_data.append((login_data,status_code,message))
            print("test_data={}".format(login_data,status_code,message))
    return test_data
#定义测试类
class login(unittest.TestCase):
    #前置处理
    def setUp(self):
        #实例化接口
        self.login_api=LoginAPI()
    #后置处理
    # def tearDown(self):
    #     pass
    #定义测试用例
    #登录
    @parameterized.expand(build_data)
    def test01_login(self,login_data,status_code,message):
        #调用登录接口登录
        response=self.login_api.login(login_data)
        print(response.json())
        #断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(message,response.json().get("message"))
        #获取token
        app.TOKEN="Bearer"+response.json().get("data")
        app.headers_data["Authorization"]=app.TOKEN


