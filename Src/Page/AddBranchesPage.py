from time import sleep

from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation


class addbranchespage(web_operation):

    organization_manage = (By.XPATH, '//span[contains(text(), "组织管理")]')
    branches_manage = (By.XPATH, '//span[contains(text(), "网点管理")]')
    add_button = (By.XPATH, '//span[contains(text(), "添加")]')

    branches_name = (By.XPATH, '//input[@placeholder="请输入网点名称"]')
    branches_number = (By.XPATH, '//input[@placeholder="请输入网点编码"]')
    department_name = (By.XPATH, '//input[@placeholder="请选择部门名称"]')
    department_choice = (By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/ul/li/label/span[1]/span')
    province_choice = (By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div/section/section/main/form/div[4]/div/div/div/label[1]/select')
    city_choice = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/section/section/main/form/div[4]/div/div/div/label[2]/select')
    district_choice = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/section/section/main/form/div[4]/div/div/div/label[3]/select')
    detailed_address = (By.XPATH, '//input[@placeholder="请输入详细地址"]')
    phone_number = (By.XPATH, '//input[@placeholder="请输入电话"]')
    merchant_number = (By.XPATH, '//input[@placeholder="请输入市民卡商户号"]')
    terminal_number = (By.XPATH, '//input[@placeholder="请输入市民卡终端号"]')

    save_button = (By.XPATH, '//span[contains(text(), "保 存")]')

    toast_text = (By.CLASS_NAME, 'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')
    dialog_text = (By.CLASS_NAME ,'el-dialog__body')

    def click_text_by_option_value(self,browser,value):
        ele_tuple = (By.XPATH,'//option[@value="%s"]' %value)
        self.find_element_and_click(browser,ele_tuple)


    def input_branches_info(self,browser,branches_name,branches_number,province,city,district,detailed_address,
                            phone_number,merchant_number,terminal_number):
        self.find_element_and_send_keys(browser,self.branches_name,branches_name)
        self.find_element_and_send_keys(browser,self.branches_number,branches_number)

        if len(province)>0:
            self.find_element_and_click(browser,self.province_choice)
            self.click_text_by_option_value(browser,province)
            if len(city)>0:
                self.find_element_and_click(browser,self.city_choice)
                self.click_text_by_option_value(browser,city)
                if len(district)>0:
                    self.find_element_and_click(browser,self.district_choice)
                    self.click_text_by_option_value(browser,district)

        self.find_element_and_send_keys(browser,self.detailed_address,detailed_address)
        self.find_element_and_send_keys(browser,self.phone_number,phone_number)
        self.find_element_and_send_keys(browser,self.merchant_number,merchant_number)
        self.find_element_and_send_keys(browser,self.terminal_number,terminal_number)