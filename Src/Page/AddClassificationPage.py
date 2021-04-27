from time import sleep

from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation
import os


class addclassificationpage(web_operation):

    goods_manage = (By.XPATH, '//span[contains(text(), "商品管理")]')
    classification_list = (By.XPATH, '//span[contains(text(), "分类列表")]')
    add_button = (By.XPATH, '//span[contains(text(), "添加")]')

    classification_number = (By.XPATH, '//input[@placeholder="请输入分类编码"]')
    classification_name = (By.XPATH, '//input[@placeholder="请输入分类名称"]')
    classification_order = (By.XPATH, '//input[@placeholder="请输入分类排序"]')
    upload_photo = (By.CLASS_NAME, 'el-icon-plus')

    save_button = (By.XPATH, '//span[contains(text(), "保 存")]')
    toast_text = (By.CLASS_NAME,'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')
    dialog_text = (By.CLASS_NAME ,'el-dialog__body')

    def input_classification_info(self,browser,classification_number,classification_name,classification_order):
        self.find_element_and_send_keys(browser,self.classification_number,classification_number)
        self.find_element_and_send_keys(browser,self.classification_name,classification_name)
        self.find_element_and_send_keys(browser,self.classification_order,classification_order)

