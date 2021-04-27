import sys

sys.path.append(r"D:\Xbx\wisdom_canteen")
from selenium import webdriver
from Src.Common.Send_Email import send_email
from Src.Common.Test_Suite import testsuite_operation
from Src.Modules.Common.YeWu.UserLogin import userlogin
from Src.Common.Sys_Operation import sys_operation
import HTMLTestRunner
import unittest


# report_file = r"E:\work\117\自动化\selenium_117\TestReport"+"\\"+sys_operation().get_shijianchuo()+".html"
# file = open(report_file, "wb")  # 以二进制写的方式打开html文件，如果文件不存在，则创建后再打开
#
# # #使用discover添加用例到测试套件中
# # 将Selenium_Day7目录下，所有已TestCase开头的.py格式的文件内的测试用例一次性添加到测试套件suite3中。
# suite3 = unittest.defaultTestLoader.discover(r"E:\work\117\自动化\selenium_117\Selenium_Day7", pattern="TestCase*.py")
# #实力化HTMLTestRunner下的HTMLTestRunner类的对象，在实例化同时制定报告输出对象，报告的标题和报告的描述
# runner = HTMLTestRunner.HTMLTestRunner(stream=file,title="用户登录模块测试报告", description="实现了3个用例")
# runner.run(suite3)  # 使用HTMLTestRunner类的对象调用run方法，执行套件
# file.close()  # 关闭打开的报



r = testsuite_operation()  # 实例化run_testsuite类对象
suite = r.get_test_suite_by_discover("../TestCase", "TestCase*.py")
r.run_testsuite_to_test_report("../TestReport", suite, report_title="登录模块测试报告",
                               report_description="共6个用例实现了自动化")
send_email().login_and_send_email('自动化测试执行结果', '../TestReport','../../../../Conf/TestEmailServerConf.csv')

