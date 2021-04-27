from time import sleep

from selenium import webdriver

from Src.Common.CSV import csv
from Src.Modules.Common.YeWu.UserLogin import userlogin
from Src.Page.AddUserPage import adduserpage



class adduser(adduserpage,csv):

    # 登录系统，添加用户
    def login_and_click_add_user(self,browser):
        userlogin().user_login_by_Administrator(browser) #默认账号登录
        self.find_element_and_click(browser, self.sys_manage) #点击系统管理
        self.find_element_and_click(browser, self.user_manage) #点击用户管理
        self.find_element_and_click(browser, self.add_button) #点击添加

    def add_user_by_testcase_number(self,browser,testcase_number):
        testcase_dict = csv().get_testdata_from_csv_by_testcase_number("../TestData/AddUserTestData.csv",testcase_number)

        self.input_info_and_add_user(browser,username=testcase_dict["用户名"],
                                     phone_number=testcase_dict["手机号"],
                                     password=testcase_dict["密码"],
                                     role=testcase_dict["角色"],
                                     uesr_type=testcase_dict["用户类型"])
        if testcase_dict["用户类型"] == "商户" and len(testcase_dict["商户名"]) != 0:
            self.find_element_and_click(browser,self.merchant)
            sleep(2)
            if self.text_to_be_present_in_element_or_not(browser,self.list,testcase_dict["商户名"]):
                self.find_element_and_click(browser,self.merchant_choice[testcase_dict["商户名"]])
            else:
                sleep(2)
                self.find_element_and_click(browser, self.merchant_choice[testcase_dict["商户名"]])
        self.find_element_and_click(browser,self.save_button)

    def login_and_add_user(self,browser,testcase_number):
        self.login_and_click_add_user(browser)
        sleep(2)
        self.add_user_by_testcase_number(browser,testcase_number)

if __name__=="__main__":
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("http://192.168.10.12:19333/index.html#/")
    adduser().login_and_add_user(browser,"AddUser_002")
