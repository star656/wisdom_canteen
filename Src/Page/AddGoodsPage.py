import os
from time import sleep

from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation


class addgoodspage(web_operation):

    goods_manage = (By.XPATH, '//span[contains(text(), "商品管理")]')
    goods_list = (By.XPATH, '//span[contains(text(), "商品列表")]')
    add_button = (By.XPATH, '//span[contains(text(), "添加")]')

    goods_name = (By.XPATH, '//input[@placeholder="请输入商品名称"]')
    goods_price = (By.XPATH, '//input[@placeholder="请输入商品价格"]')
    godds_number = (By.XPATH, '//input[@placeholder="请输入商品排序"]')
    goods_category = (By.XPATH, '//input[@placeholder="商品类别选择"]')
    upload_photo = (By.CLASS_NAME, 'el-icon-plus')
    goods_describe = (By.XPATH, '//textarea[@placeholder="请输入商品描述"]')
    save_button = (By.XPATH,'//span[contains(text(),"保 存")]')

    toast_text = (By.XPATH, 'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')
    dialog_text = (By.CLASS_NAME, 'el-dialog__body')

    def input_info_and_add_goods(self,browser,goods_name,goods_price,goods_number,
                                 goods_category,goods_describe):
        self.find_element_and_send_keys(browser,self.goods_name,goods_name)
        self.find_element_and_send_keys(browser,self.goods_price,goods_price)
        self.find_element_and_send_keys(browser,self.godds_number,goods_number)
        if len(goods_category) != 0:
            self.find_element_and_click(browser, self.goods_category)
            sleep(1)
            self.click_text_by_text_content(browser,goods_category)
        self.find_element_and_send_keys(browser,self.goods_describe,goods_describe)


