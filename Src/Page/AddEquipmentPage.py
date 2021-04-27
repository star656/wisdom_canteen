from time import sleep

from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation


class addequipmentpage(web_operation):

    equipment_manage = (By.XPATH, '//span[contains(text(), "设备管理")]')
    equipment_list = (By.XPATH, '//span[contains(text(), "设备列表")]')
    add_button = (By.XPATH, '//span[contains(text(), "添加")]')

    branches_name = (By.XPATH, '//input[@placeholder="网点选择"]')
    branches_list = (By.CLASS_NAME, 'el-scrollbar')
    equipment_name = (By.XPATH, '//input[@placeholder="请输入设备名称"]')
    equipment_number = (By.XPATH, '//input[@placeholder="请输入设备编号"]')

    save_button = (By.XPATH, '//span[contains(text(), "保 存")]')

    toast_text = (By.CLASS_NAME, 'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')
    dialog_text = (By.CLASS_NAME ,'el-dialog__body')

    def input_equipment_info(self,browser,branches_name,equipment_name,equipment_number):
        if len(branches_name)>0:
            self.find_element_and_click(browser,self.branches_name)
            if self.text_to_be_present_in_element_or_not(browser,self.branches_list,branches_name):
                self.click_text_by_text_content(browser,branches_name)
            else:
                sleep(2)
                self.click_text_by_text_content(browser, branches_name)
        self.find_element_and_send_keys(browser,self.equipment_name,equipment_name)
        self.find_element_and_send_keys(browser,self.equipment_number,equipment_number)

