from time import sleep

from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation


class addpositionpage(web_operation):

    organization_manage = (By.XPATH, '//span[contains(text(), "组织管理")]')
    position_manage = (By.XPATH, '//span[contains(text(), "职位管理")]')
    add_button = (By.XPATH, '//span[contains(text(), "添加")]')

    department_name = (By.XPATH,'//input[@placeholder="请选择部门名称"]')
    department_choice = (By.XPATH,'/html/body/div[2]/div[1]/div[1]/div[1]/ul/li/label/span[1]')

    position_name = (By.XPATH,'//input[@placeholder="请输入职位名称"]')
    position_describe = (By.XPATH, '//input[@placeholder="请输入职位描述"]')

    save_button = (By.XPATH, '//span[contains(text(), "保 存")]')
    toast_text = (By.CLASS_NAME, 'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')
    dialog_text = (By.CLASS_NAME ,'el-dialog__body')

    def input_position_info(self,browser,position_name,position_describe):

        self.find_element_and_send_keys(browser,self.position_name,position_name)
        self.find_element_and_send_keys(browser,self.position_describe,position_describe)