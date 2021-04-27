from time import sleep

from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation


class addrolepage(web_operation):

    sys_manage = (By.XPATH, '//span[contains(text(), "系统管理")]')
    role_manage = (By.XPATH, '//span[contains(text(), "角色管理")]')
    add_button = (By.XPATH, '//span[contains(text(), "添加")]')

    role_name = (By.XPATH,'//input[@placeholder="请输入角色名称"]')
    role_logo = (By.XPATH,'//input[@placeholder="请输入角色标识"]')
    role_describe = (By.XPATH,'//textarea[@placeholder="请输入角色描述"]')

    save_button = (By.XPATH,'//span[contains(text(), "保 存")]')

    toast_text = (By.CLASS_NAME, 'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')


    def input_role_info(self,browser,role_name,role_logo,role_describe):
        self.find_element_and_send_keys(browser,self.role_name,role_name)
        self.find_element_and_send_keys(browser,self.role_logo,role_logo)
        sleep(1)
        self.find_element_and_send_keys(browser,self.role_describe,role_describe)

