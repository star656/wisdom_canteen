from Src.Common.CSV import csv
from Src.Modules.Common.YeWu.UserLogin import userlogin
from Src.Page.AddPermissionsPage import addpermissionspage
from selenium import webdriver
from time import sleep
import threading

class addpermissions(addpermissionspage,csv):

    def login_and_click_add_perminssions(self,browser):
        userlogin().user_login_by_Administrator(browser)
        self.find_element_and_click(browser, self.sys_manage)  # 点击系统管理
        self.find_element_and_click(browser, self.permissions_manage)  # 点击权限管理
        self.find_element_and_click(browser, self.add_button)  # 点击添加

    def add_permissions_by_testcase_number(self,browser,testcase_number):
        testcase_dict = self.get_testdata_from_csv_by_testcase_number("../TestData/AddPermissionsTestData.csv",testcase_number)
        self.input_permisstions_info(browser,
                                     testcase_dict["权限名称"],
                                     testcase_dict["权限等级"],
                                     testcase_dict["权限路径"],
                                     testcase_dict["权限序列"])

        if testcase_dict["权限等级"] == "1级菜单" and len(testcase_dict["图标样式"]) != 0 :
            self.find_element_and_click(browser,self.permissions_icon)
            self.find_element_and_click(browser,self.icon_style[testcase_dict["图标样式"]])
            self.find_element_and_click(browser,self.confirm_button)
        elif testcase_dict["权限等级"] == "2级菜单" :
            self.find_element_and_click(browser,self.father_permissions)
            sleep(2)
            if len(testcase_dict["父权限"]) != 0:
                self.click_text_by_text_content(browser,testcase_dict["父权限"])
            if len(testcase_dict["功能"]) != 0:
                funtions_list = testcase_dict["功能"].split("，")
                for funtion in funtions_list:
                    self.click_text_by_text_content(browser, funtion)
                    # t = threading.Thread(target=self.click_text_by_text_content(browser, funtion))
                    # t.start()
        sleep(2)
        self.find_element_and_click(browser, self.save_button)

    def login_and_add_permissions(self,browser,testcase_number):
        self.login_and_click_add_perminssions(browser)
        self.add_permissions_by_testcase_number(browser,testcase_number)

if __name__=="__main__":
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("http://192.168.10.12:19333/index.html#/")
    addpermissions().login_and_add_permissions(browser,"AddPermissions_002")
