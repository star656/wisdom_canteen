from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation


class addbuttonpage(web_operation):

    sys_manage = (By.XPATH, '//span[contains(text(), "系统管理")]')
    button_manage = (By.XPATH, '//span[contains(text(), "按钮管理")]')
    add_button = (By.XPATH, '//span[contains(text(), "添加")]')

    buttom_name = (By.XPATH,'/html/body/div[2]/div/div[2]/form/div[1]/div/div/input')
    button_logo = (By.XPATH,'//input[@placeholder="请输入按钮标识"]')

    confirm_button = (By.XPATH, '//span[text()="确 定"]')
    toast_text = (By.CLASS_NAME, 'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')
    dialog_text = (By.CLASS_NAME ,'el-dialog__body')


    def input_button_info(self,browser,button_name,button_logo):
        self.find_element_and_send_keys(browser,self.buttom_name,button_name)
        sleep(1)
        self.find_element_and_send_keys(browser,self.button_logo,button_logo)
