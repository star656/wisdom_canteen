from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation


class addemployeespage(web_operation):

    organization_manage = (By.XPATH, '//span[contains(text(), "组织管理")]')
    employees_manage = (By.XPATH, '//span[contains(text(), "员工管理")]')
    add_button = (By.XPATH, '//span[contains(text(), "添加")]')
    department_choice = (By.CLASS_NAME, 'org-tree-node')

    employees_number = (By.XPATH, '//input[@placeholder="请输入员工工号"]')
    chinese_name = (By.XPATH, '//input[@placeholder="请输入员工中文名称"]')
    english_name = (By.XPATH, '//input[@placeholder="请输入员工英文名称"]')
    induction_time = (By.ID, 'hiredate')
    phone_number = (By.XPATH, '//input[@placeholder="请输入员工电话"]')
    id_number = (By.XPATH, '//input[@placeholder="请输入员工身份证号"]')
    card_number = (By.XPATH, '//input[@placeholder="请输入卡号"]')

    save_button = (By.XPATH, '//span[contains(text(), "保 存")]')
    toast_text = (By.CLASS_NAME, 'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')
    dialog_text = (By.CLASS_NAME ,'el-dialog__body')

    def input_employees_info(self,browser,employees_number,chinese_name,
                             english_name,induction_time,phone_number,id_number,card_number):
        self.find_element_and_send_keys(browser,self.employees_number,employees_number)
        self.find_element_and_send_keys(browser,self.chinese_name,chinese_name)
        self.find_element_and_send_keys(browser,self.english_name,english_name)
        if len(induction_time) > 0:
            self.find_element_and_send_keys(browser,self.induction_time,induction_time)
        self.find_element_and_send_keys(browser,self.phone_number,phone_number)
        self.find_element_and_send_keys(browser,self.id_number,id_number)
        self.find_element_and_send_keys(browser,self.card_number,card_number)