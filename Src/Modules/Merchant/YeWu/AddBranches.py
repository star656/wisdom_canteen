from time import sleep

from selenium import webdriver

from Src.Common.CSV import csv
from Src.Modules.Common.YeWu.UserLogin import userlogin
from Src.Page.AddBranchesPage import addbranchespage


class addbranches(addbranchespage,csv):

    def login_and_click_add_branches(self,browser):
        userlogin().user_login_by_merchant(browser)
        self.find_element_and_click(browser,self.organization_manage)
        self.find_element_and_click(browser,self.branches_manage)
        self.find_element_and_click(browser,self.add_button)


    def add_branches_by_testcase_number(self,browser,testcase_number):
        testcase_dict = self.get_testdata_from_csv_by_testcase_number('../TestData/AddBranchesTestData.csv',testcase_number)
        sleep(2)
        self.input_branches_info(browser,testcase_dict["网点名称"],testcase_dict["网点编码"],
                                 testcase_dict["省"],testcase_dict["市"],testcase_dict["区"],
                                 testcase_dict["详细地址"],testcase_dict["电话号码"],testcase_dict["商户号"],
                                 testcase_dict["终端号"])
        if len(testcase_dict["部门名称"]) != 0:
            self.find_element_and_click(browser,self.department_name)
            sleep(2)
            self.find_element_and_click(browser,self.department_choice)
        self.find_element_and_click(browser,self.save_button)

    def login_and_add_branches(self,browser,testcase_number):
        self.login_and_click_add_branches(browser)
        sleep(2)
        self.add_branches_by_testcase_number(browser,testcase_number)


if __name__=="__main__":
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("http://192.168.10.12:19333/index.html#/")
    addbranches().login_and_add_branches(browser,"AddBranches_002")
