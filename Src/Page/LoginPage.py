from time import sleep

from selenium.webdriver.common.by import By


from Src.Common.CSV import csv
from Src.Common.Web_Operation import web_operation
from selenium import webdriver

class loginpage(web_operation):
    input_username = (By.XPATH,'//input[@placeholder="请输入账号"]')
    input_password = (By.XPATH,'//input[@type="password"]')
    input_code = (By.XPATH,'//input[@placeholder="请输入验证码"]')
    login_button = (By.XPATH,'//button[@type="button"]')

    toast_text = (By.CLASS_NAME,'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')
    user_text = (By.CLASS_NAME, 'el-tooltip user-name')


    def input_info_and_login(self,browser,username,password,code):
        self.find_element_and_send_keys(browser,self.input_username,username)
        self.find_element_and_send_keys(browser,self.input_password,password)
        self.find_element_and_send_keys(browser,self.input_code,code)
        self.find_element_and_click(browser,self.login_button)


if __name__=="__main__":
    browser= webdriver.Firefox()
    browser.maximize_window()
    browser.get("http://192.168.10.12:19333/index.html#/")
    loginpage().input_info_and_login(browser,"13333333333","123456","1234")
    # info_dict = csv().get_info_from_csv_to_dict("../../Conf/TestEnvironmentConf.csv")
    # browser.get(info_dict["URL"])
    # login().input_info_and_login(browser, username=info_dict["UserName"], password=info_dict["Password"],code="1234")
    sleep(3)
    browser.quit()