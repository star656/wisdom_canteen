from time import sleep

from selenium import webdriver

from Src.Common.CSV import csv
from Src.Modules.Common.YeWu.UserLogin import userlogin
from Src.Page.AddDepartmentPage import adddepartmentpage


class adddepartment(adddepartmentpage,csv):


    def login_and_click_add_department(self,browser):
        userlogin().user_login_by_merchant(browser)
        self.find_element_and_click(browser,self.organization_manage)
        self.find_element_and_click(browser,self.department_manage)

    def add_department_by_testcase_number(self,browser,testcase_number):
        testcase_dict = self.get_testdata_from_csv_by_testcase_number('../TestData/AddDepartmentTestData.csv',testcase_number)
        if len(testcase_dict["上级部门"]) > 0:
            self.find_element_and_click(browser,self.department)
            self.find_element_and_click(browser,self.add_button)
            self.find_element_and_send_keys(browser,self.department_name,testcase_dict["部门名称"])
            sleep(2)
            self.find_element_and_click(browser,self.confirm_button)
        else:
            self.find_element_and_click(browser, self.add_button)


    def login_and_add_department(self,browser,testcase_number):
        self.login_and_click_add_department(browser)
        sleep(3)
        self.add_department_by_testcase_number(browser,testcase_number)


if __name__=="__main__":
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("http://192.168.10.12:19333/index.html#/")
    adddepartment().login_and_add_department(browser,'AddDepartment_001')
