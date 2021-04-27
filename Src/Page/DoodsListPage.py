from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation
from Src.Page.LoginPage import loginpage
import re


class goodslistpage(web_operation):
    goods_manage = (By.XPATH, '//span[contains(text(), "商品管理")]')
    goods_list = (By.XPATH, '//span[contains(text(), "商品列表")]')
    add_button = (By.XPATH, '//span[contains(text(), "添加")]')

    list=(By.CLASS_NAME,'el-table_1_column_3  ')

    def get_goods_list(self,browser,goods_name):

        self.find_element_and_click(browser,self.goods_manage)
        self.find_element_and_click(browser,self.goods_list)
        sleep(2)
        country_list = self.find_elements_and_get_text_list(browser,self.list)
        index= str(country_list.index(goods_name))
        checkbox_XPATH = (By.XPATH,
                          '/html/body/div/div/div[2]/div/div/div/section/section/main/div/div[4]/div[2]/table/tbody/tr[' + index + ']/td[1]/div/label/span/span')
        self.find_element_and_click(browser,checkbox_XPATH)


line_list = ['￥2000元','￥3000元','￥4000元','￥5000元','￥6000元']
list = [ ]
for line in line_list:
    matchObj = re.match( r'￥(.*)元', line)
    if matchObj:
        list.append(matchObj.group(1))
print(list)



# if __name__=='__main__':
#     browser = webdriver.Firefox()
#     browser.maximize_window()
#     browser.get('http://192.168.10.12:19333/index.html#/')
#     loginpage().input_info_and_login(browser,'15555555555','123456','1234')
#     goodslistpage().get_goods_list(browser,"西湖牛肉羹")