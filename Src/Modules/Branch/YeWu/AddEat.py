from time import sleep

from selenium import webdriver

from Src.Common.CSV import csv
from Src.Modules.Common.YeWu.UserLogin import userlogin
from Src.Page.AddEatPage import addeatpage


class addeat(addeatpage,csv):

    def login_and_click_add_eat(self,browser):
        userlogin().user_login_by_branch(browser)
        self.find_element_and_click(browser,self.goods_manage)
        self.find_element_and_click(browser,self.eat_list)
        self.find_element_and_click(browser,self.add_button)
        sleep(2)

    def add_eat_by_testcase_number(self,browser,testcase_number):
        testcase_dict = self.get_testdata_from_csv_by_testcase_number('../TestData/AddEatTestData.csv',testcase_number)

        self.input_info_add_eat(browser,testcase_dict["餐别名称"],testcase_dict["排序"],
                                testcase_dict["起始时间"],testcase_dict["结束时间"])

        self.find_element_and_click(browser,self.save_button)
        sleep(2)

    def login_and_add_eat(self,browser,testcase_number):
        self.login_and_click_add_eat(browser)
        self.add_eat_by_testcase_number(browser,testcase_number)

if __name__ == '__main__':
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get('http://192.168.10.12:19333/index.html#/')
    addeat().login_and_add_eat(browser,'AddEat_001')
