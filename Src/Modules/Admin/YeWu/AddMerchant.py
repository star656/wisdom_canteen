from time import sleep

from selenium import webdriver

from Src.Common.CSV import csv
from Src.Modules.Common.YeWu.UserLogin import userlogin
from Src.Page.AddMerchantPage import addmerchantpage


class addmerchant(addmerchantpage,csv):

    def login_and_click_add_merchant(self,browser):
        userlogin().user_login_by_Administrator(browser)
        self.find_element_and_click(browser,self.merchant_manage)
        self.find_element_and_click(browser,self.merchant_info)
        self.find_element_and_click(browser,self.add_button)

    def add_button_by_testcase_number(self,browser,testcase_number):
        testcase_dict = self.get_testdata_from_csv_by_testcase_number("../TestData/AddMerchantTestData.csv",testcase_number)

        self.input_merchant_info(browser,
                                 testcase_dict["商户名称"],
                                 testcase_dict["商户编号"])

        self.find_element_and_click(browser, self.confirm_button)

    def login_and_add_merchant(self, browser, testcase_number):
        self.login_and_click_add_merchant(browser)
        sleep(2)
        self.add_button_by_testcase_number(browser,testcase_number)

if __name__=='__main__':
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get('http://192.168.10.12:19333/index.html#/')
    addmerchant().login_and_add_merchant(browser,'AddMerchant_001')