from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation
from Src.Page.LoginPage import loginpage


class addmerchantpage(web_operation):

    merchant_manage = (By.XPATH, '//span[contains(text(), "商户管理")]')
    merchant_info = (By.XPATH, '//span[contains(text(), "商户信息")]')
    add_button = (By.XPATH, '//span[contains(text(), "添加")]')

    merchant_name = (By.XPATH,'/html/body/div[2]/div/div[2]/form/div[1]/div/div/input')
    merchant_number = (By.XPATH,'/html/body/div[2]/div/div[2]/form/div[2]/div/div/input')

    confirm_button = (By.XPATH, '//span[text()="确 定"]')

    toast_text = (By.CLASS_NAME, 'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')
    dialog_text = (By.CLASS_NAME ,'el-dialog__body')

    def input_merchant_info(self,browser,merchant_name,merchant_info):

        self.find_element_and_send_keys(browser,self.merchant_name,merchant_name)
        self.find_element_and_send_keys(browser,self.merchant_info,merchant_info)



