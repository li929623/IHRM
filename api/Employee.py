#导包
import requests
import app

#创建接口类
class EmployeeAPI:
    #初始化
    def __init__(self):
        self.url_add =  app.BASE_URL + "/api/sys/user"
        self.url_update = app.BASE_URL + "/api/sys/user/{}"
        self.url_get = app.BASE_URL + "/api/sys/user/{}"
        self.url_delete = app.BASE_URL + "/api/sys/user/{}"
    #定义接口调用方法
    #添加用户
    def add_employee(self,employee_add_date):
        url = self.url_add
        return requests.post(url,json=employee_add_date,headers=app.headers_data)
    #更新用户
    def update_employee(self,employee_id,employee_update_date):
        url =self.url_update.format(employee_id)
        return requests.post(url,json=employee_update_date,header=app.headers_data)