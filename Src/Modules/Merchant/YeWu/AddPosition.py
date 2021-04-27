from time import sleep

from selenium import webdriver

from Src.Common.CSV import csv
from Src.Modules.Common.YeWu.UserLogin import userlogin
from Src.Page.AddPositionPage import addpositionpage


class addposition(addpositionpage,csv):

    def login_and_click_add_position(self,browser):
        userlogin().user_login_by_merchant(browser)
        self.find_element_and_click(browser,self.organization_manage)
        self.find_element_and_click(browser,self.position_manage)
        self.find_element_and_click(browser,self.add_button)

    def add_position_by_testcase_number(self,browser,testcase_number):
        testcase_dict = self.get_testdata_from_csv_by_testcase_number('../TestData/AddPositionTestData.csv',testcase_number)
        if len(testcase_dict["部门名称"]) != 0:
            self.find_element_and_click(browser, self.department_name)
            sleep(2)
            self.find_element_and_click(browser, self.department_choice)

        self.input_position_info(browser,
                                 testcase_dict["职位名称"],
                                 testcase_dict["职位描述"])

        if testcase_dict["职位类型"] == "领导":
            self.click_text_by_text_content(browser,testcase_dict["职位类型"])

        self.find_element_and_click(browser,self.save_button)


    def login_and_add_position(self,browser,testcase_number):
        self.login_and_click_add_position(browser)
        sleep(2)
        self.add_position_by_testcase_number(browser,testcase_number)

if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("http://192.168.10.12:19333/index.html#/")
    addposition().login_and_add_position(browser,"AddPosition_001")