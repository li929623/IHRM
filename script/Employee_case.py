import requests
from api.Employee import EmployeeAPI
import app
import unittest
import json
from parameterized import parameterized

#提取token
data={"mobile":"13800000002","password":"123456"}
response=requests.post("http://ihrm-test.itheima.net/api/sys/login",json=data)
token=response.json()["data"]
app.TOKEN="Bearer "+token
app.headers_data["Authorization"]=app.TOKEN
print(app.TOKEN)
app.headers_data={
    "Content-Type":"application/json",
    "Authorization":app.TOKEN
}
print(app.headers_data)
#构造数据
def build_data():
    test_data=[]
    data_file=app.BASE_DIR+"/data/employee_add.json"
    with open (data_file,encoding="utf-8") as f:
        #json格式
        json_data=json.load(f)
        for case_data in json_data:
            employee_add_date=case_data.get("employee_add_date")
            message=case_data.get("message")
            test_data.append((employee_add_date,message))
            print ("test_data={}".format(employee_add_date,message))
    return test_data

class employee_add(unittest.TestCase):
    def setUp(self) -> None:
        #实例化对象
        employee_ID=None
        self.employee_add_api=EmployeeAPI()

    @parameterized.expand(build_data)
    def test01_add(self,employee_add_date,message):
        response=self.employee_add_api.add_employee(employee_add_date)
        print(response.json())
        self.assertEqual(message,response.json().get("message"))
        #取值employee_ID
        #if response.json()["data"] is not None:
        if response.json()["data"] is not None:
            employee_add.employee_ID=response.json()["data"]["id"]
            print(employee_add.employee_ID)


            @parameterized.expand(build_data)
            def test02_update(self,employee_updata_date,message):
                response=self.employee_update_api.update_employee(employee_add.employee_ID,employee_updata_date)
                print(response.json())
                self.assertEqual(message,response.json()["message"])



