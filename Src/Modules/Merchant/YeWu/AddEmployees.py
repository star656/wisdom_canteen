from time import sleep

from Src.Common.CSV import csv
from Src.Modules.Common.YeWu.UserLogin import userlogin
from Src.Page.AddEmployeesPage import addemployeespage


class addemployees(addemployeespage,csv):

    def login_and_click_add_employees(self,browser):
        userlogin().user_login_by_merchant(browser)
        self.find_element_and_click(browser,self.organization_manage)
        self.find_element_and_click(browser,self.employees_manage)

    def add_employees_by_testcasst_number(self,browser,testcase_number):
        testcase_dict = self.get_testdata_from_csv_by_testcase_number('../TestData/AddEmployeesTestData.csv',testcase_number)
        if len(testcase_dict["部门"]) != 0:
            self.find_element_and_click(browser,self.department_choice)
            self.find_element_and_click(browser,self.add_button)
            self.input_employees_info(browser,testcase_dict["员工工号"],testcase_dict["姓名"],
                                      testcase_dict["英文名"],testcase_dict["入职时间"],testcase_dict["手机号"],
                                      testcase_dict["身份证号"],testcase_dict["卡号"])
            if testcase_dict["性别"] == '男' or testcase_dict["性别"] == "女":
                self.click_text_by_text_content(browser,testcase_dict["性别"])
            self.find_element_and_click(browser,self.save_button)
        else:
            self.find_element_and_click(browser, self.add_button)

    def login_and_add_employees(self,browser,testcase_number):
        self.login_and_click_add_employees(browser)
        sleep(2)
        self.add_employees_by_testcasst_number(browser,testcase_number)