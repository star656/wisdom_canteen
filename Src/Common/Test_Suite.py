import HTMLTestRunner
import unittest

from Src.Common.Sys_Operation import sys_operation


class testsuite_operation:

    # 实现按照目录将符合一定命名规则的.py文件中的用例添加到测试套件中，并返回套件
    def get_test_suite_by_discover(self, testcase_path,name_rule):
        suite = unittest.defaultTestLoader.discover(testcase_path,pattern=name_rule)
        return suite

    # 实现执行套件，并将测试结果输出到制定目录下的测试报告中
    def run_testsuite_to_test_report(self,report_path,suite,report_title, report_description):
        report_file =report_path  + "\\" + sys_operation().get_shijianchuo() + ".html"
        with open(report_file, "wb") as f:  # 以二进制写的方式打开html文件，如果文件不存在，则创建后再打开
            runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=report_title, description=report_description)
            runner.run(suite)  # 使用HTMLTestRunner类的对象调用run方法，执行套件
              # 关闭打开的报告