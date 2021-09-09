#导包
import unittest
#from script.login_cases import login
import time
from tools.HTMLTestRunner import HTMLTestRunner
import app
from script.Employee_case import employee_add
#组装测试套件
suite =unittest.TestSuite()
suite.addTests(unittest.makeSuite(employee_add))
#指定测试报告路径
report=app.BASE_DIR +"./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
#打开文件流
with open(report,"wb") as f:
    #创建html运行器
    runner =HTMLTestRunner(f,title="api report")
    #执行测试套件
    runner.run(suite)



