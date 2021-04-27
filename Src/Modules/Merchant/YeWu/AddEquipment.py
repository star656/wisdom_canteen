from time import sleep

from selenium import webdriver

from Src.Common.CSV import csv
from Src.Modules.Common.YeWu.UserLogin import userlogin
from Src.Page.AddEquipmentPage import addequipmentpage


class addequipment(addequipmentpage,csv):

    def login_and_click_add_equipment(self,browser):
        userlogin().user_login_by_merchant(browser)
        self.find_element_and_click(browser,self.equipment_manage)
        self.find_element_and_click(browser,self.equipment_list)
        self.find_element_and_click(browser,self.add_button)

    def add_equipment_by_testcase_number(self,browser,testcase_number):
        testcase_dict = self.get_testdata_from_csv_by_testcase_number('../TestData/AddEquipmentTestData.csv',testcase_number)

        self.input_equipment_info(browser,testcase_dict["网点名称"],testcase_dict["设备名称"],testcase_dict["设备编号"])
        sleep(2)
        self.find_element_and_click(browser,self.save_button)

    def login_and_add_equipment(self,browser,testcase_number):
        self.login_and_click_add_equipment(browser)
        sleep(2)
        self.add_equipment_by_testcase_number(browser,testcase_number)

if __name__=="__main__":
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("http://192.168.10.12:19333/index.html#/")
    addequipment().login_and_add_equipment(browser,"AddEquipment_001")