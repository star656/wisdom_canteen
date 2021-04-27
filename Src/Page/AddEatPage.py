from time import sleep

from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation


class addeatpage(web_operation):

    goods_manage = (By.XPATH, '//span[contains(text(), "商品管理") ]')
    eat_list = (By.XPATH, '//span[contains(text(), "餐别列表")]')
    add_button = (By.XPATH, '//span[contains(text() , "添加")]')

    eat_name = (By.XPATH, '//input[@placeholder="请输入餐别名称"]')
    eat_number = (By.XPATH, '//input[@placeholder="请输入排序"]')
    supply_input = (By.XPATH,'//div[3]/div/div/i[@class="el-input__icon el-range__close-icon"]')
    #/html/body/div/div/div[2]/div/div/div/section/section/main/form/div[3]/div/div/i[2]
    supply_start_time = (By.XPATH,'//div[3]/div/div/input[@placeholder="开始时间"]')
    supply_end_time = (By.XPATH, '//div[3]/div/div/input[@placeholder="结束时间"]')
    order_input = (By.XPATH, '//div[4]/div/div/i[@class="el-input__icon el-range__close-icon"]')
    #/html/body/div[1]/div/div[2]/div/div/div/section/section/main/form/div[4]/div/div
    order_start_time = (By.XPATH,'//div[4]/div/div/input[@placeholder="开始时间"]')
    order_end_time = (By.XPATH, '//div[4]/div/div/input[@placeholder="结束时间"]')
    save_button = (By.XPATH, '//span[contains(text(),"保 存")]')

    toast_text = (By.XPATH, 'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')
    dialog_text = (By.CLASS_NAME, 'el-dialog__body')
    clear_button = (By.CLASS_NAME, 'class="el-input__icon el-range__close-icon el-icon-circle-close')


    def input_info_add_eat(self,browser,eat_name,eat_number,start_time,end_time):
        self.find_element_and_send_keys(browser,self.eat_name,eat_name)
        self.find_element_and_send_keys(browser,self.eat_number,eat_number)
        if len(start_time) != 0 or len(end_time)!= 0:
            self.find_element_and_mouse_hover(browser,self.supply_input)
            sleep(2)

            self.find_element_and_send_keys(browser,self.supply_start_time,start_time)
            self.find_element_and_send_keys(browser,self.supply_end_time,end_time)
            sleep(2)
            self.find_element_and_mouse_hover(browser, self.order_input)

            self.find_element_and_send_keys(browser, self.order_start_time, start_time)
            self.find_element_and_send_keys(browser, self.order_end_time,end_time)