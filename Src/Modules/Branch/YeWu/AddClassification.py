import os
from time import sleep

from selenium import webdriver

from Src.Common.CSV import csv
from Src.Modules.Common.YeWu.UserLogin import userlogin
from Src.Page.AddClassificationPage import addclassificationpage


class addclassification(addclassificationpage,csv):

    def login_and_click_add_classification(self,browser):
        userlogin().user_login_by_branch(browser)
        self.find_element_and_click(browser,self.goods_manage)
        self.find_element_and_click(browser,self.classification_list)
        self.find_element_and_click(browser,self.add_button)

    def add_classification_by_testcase_number(self,browser,testcase_number):
        testcase_dict = self.get_testdata_from_csv_by_testcase_number('../TestData/AddClassificationTestData.csv',testcase_number)

        self.input_classification_info(browser,testcase_dict["分类编码"],testcase_dict["分类名称"],
                                       testcase_dict["分类排序"])
        if len(testcase_dict["图片路径"]) != 0:
            self.find_element_and_click(browser,self.upload_photo)
            sleep(1)
            os.system(testcase_dict["图片路径"])
            while self.element_to_be_present_in_web_or_not(browser,self.toast_text):
                toast_message = self.find_element_and_get_text(browser,self.toast_text)
                if toast_message == "上传成功!":
                    sleep(2)
                    self.find_element_and_click(browser,self.save_button)
                break
        else:
            self.find_element_and_click(browser, self.save_button)

    def login_and_add_classification(self,browser,testcase_number):
        self.login_and_click_add_classification(browser)
        sleep(2)
        self.add_classification_by_testcase_number(browser,testcase_number)

if __name__=="__main__":
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("http://192.168.10.12:19333/index.html#/")
    addclassification().login_and_add_classification(browser,"AddClassification_001")