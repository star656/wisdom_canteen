from time import sleep

from Src.Common.CSV import csv
from Src.Modules.Common.YeWu.UserLogin import userlogin
from Src.Page.AddRolePage import addrolepage


class addrole(addrolepage,csv):

    def login_and_click_add_role(self,browser):
        userlogin().user_login_by_merchant(browser) #默认账号登录
        self.find_element_and_click(browser, self.sys_manage) #点击系统管理
        self.find_element_and_click(browser, self.role_manage) #点击用户管理
        self.find_element_and_click(browser, self.add_button) #点击添加

    def add_role_by_testcase_number(self,browser,testcase_number):
        testcase_dict = self.get_testdata_from_csv_by_testcase_number("../TestData/AddRoleTestData.csv",testcase_number)
        self.input_role_info(browser,testcase_dict["角色名称"],
                             testcase_dict["角色标识"],
                             testcase_dict["角色描述"])

    def login_and_add_role(self,browser,testcase_number):
        self.login_and_click_add_role(browser)
        sleep(2)
        self.add_role_by_testcase_number(browser,testcase_number)