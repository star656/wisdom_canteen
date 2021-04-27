import os
from time import sleep

from selenium import webdriver

from Src.Common.CSV import csv
from Src.Modules.Common.YeWu.UserLogin import userlogin
from Src.Page.AddGoodsPage import addgoodspage


class addgoods(addgoodspage,csv):

    def login_and_click_add_goods(self,browser):
        userlogin().user_login_by_branch(browser)
        self.find_element_and_click(browser,self.goods_manage)
        self.find_element_and_click(browser,self.goods_list)
        self.find_element_and_click(browser,self.add_button)
        sleep(2)


    def add_goods_by_textcase_number(self,browser,testcase_number):
        testcase_dict = self.get_testdata_from_csv_by_testcase_number('../TestData/AddGoodsTestData.csv',testcase_number)
        sleep(1)
        self.input_info_and_add_goods(browser,testcase_dict["商品名称"],testcase_dict["商品价格"],
                                      testcase_dict["商品排序"],testcase_dict["商品类别"],testcase_dict["商品描述"])

        if len(testcase_dict["图片路径"]) != 0:
            self.find_element_and_click(browser, self.upload_photo)
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
        sleep(1)

    def login_and_add_goods(self,browser,testcase_number):
        self.login_and_click_add_goods(browser)
        self.add_goods_by_textcase_number(browser, testcase_number),testcase_number


if __name__=="__main__":
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("http://192.168.10.12:19333/index.html#/")
    addgoods().login_and_add_goods(browser,'AddGoods_001')