from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation
from Src.Page.LoginPage import loginpage


class adduserpage(web_operation):

    sys_manage = (By.XPATH,'//span[contains(text(), "系统管理")]')
    user_manage = (By.XPATH,'//span[contains(text(), "用户管理")]')
    add_button = (By.XPATH,'//span[contains(text(), "添加")]')

    username = (By.XPATH,'//input[@placeholder="请输入用户名称"]')
    phone_number = (By.XPATH,'//input[@placeholder="请输入手机号"]')
    user_password = (By.XPATH,'//input[@placeholder="请输入密码"]')
    user_role = (By.XPATH,'//input[@placeholder="选择角色"]')
    list = (By.CLASS_NAME,'el-scrollbar')
    role_choice = {
        "网点": (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li/span'),
        "陕西省财政厅角色" : (By.XPATH,'//span[contains(text(), "陕西省财政厅角色")]'),
        "系统管理员" : (By.XPATH,'//span[contains(text(), "系统管理员")]')
    }
    user_type = (By.XPATH,'//input[@placeholder="选择用户类型"]')
    type_choice = {
        "管理员" : (By.XPATH,'//span[text()="管理员"]'),
        "商户": (By.XPATH, '//span[text()="商户"]'),
        "网点": (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[3]/span')
    }
    merchant = (By.XPATH,'//input[@placeholder="选择商户"]')
    merchant_choice = {
        "陕西省财政厅" : (By.XPATH,'//span[text()="陕西省财政厅"]')
    }
    branch = (By.XPATH, '//input[@placeholder="选择网点"]')

    save_button = (By.XPATH,'//span[contains(text(),"保 存")]')

    toast_text = (By.CLASS_NAME,'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')
    dialog_text = (By.CLASS_NAME ,'el-dialog__body')

    def input_info_and_add_user(self,browser,username,phone_number,password,role,uesr_type):
        self.find_element_and_send_keys(browser,self.username,username)
        self.find_element_and_send_keys(browser,self.phone_number,phone_number)
        self.remove_readonly_from_element_and_sendkeys(browser,self.user_password,password)
        if len(role) !=0:
            self.find_element_and_click(browser,self.user_role)
            sleep(2)
            if self.text_to_be_present_in_element_or_not(browser,self.list,role):
                self.find_element_and_click(browser,self.role_choice[role])
            else:
                sleep(2)
                self.find_element_and_click(browser, self.role_choice[role])
        if len(uesr_type) != 0:
            self.find_element_and_click(browser,self.user_type)
            sleep(2)
            if self.text_to_be_present_in_element_or_not(browser,self.list,uesr_type):
                self.find_element_and_click(browser,self.type_choice[uesr_type])
            else:
                sleep(2)
                self.find_element_and_click(browser, self.type_choice[uesr_type])

if __name__=="__main__":
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("http://192.168.10.12:19333/index.html#/")
    loginpage().input_info_and_login(browser, "13333333333", "123456", "1234")
    sleep(3)
    adduserpage().input_info_and_add_user(browser,"张三","13333333336","123456","陕西省财政厅角色","商户",)