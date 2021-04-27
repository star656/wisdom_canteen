from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation
from Src.Page.LoginPage import loginpage


class addpermissionspage(web_operation):

    sys_manage = (By.XPATH, '//span[contains(text(), "系统管理")]')
    permissions_manage = (By.XPATH, '//span[contains(text(), "权限管理")]')
    add_button = (By.XPATH, '//span[contains(text(), "添加")]')

    permissions_name = (By.XPATH,'//input[@placeholder="请输入权限名称"]')
    permissions_level = {
        "1级菜单":(By.XPATH,'//span[contains(text(),"1级菜单")]'),
        "2级菜单":(By.XPATH,'//span[contains(text(),"2级菜单")]')
    }
    permissions_path = (By.XPATH,'//input[@placeholder="请输入权限路径"]')
    permissions_number = (By.XPATH,'//input[@aria-valuemin="1"]')
    permissions_icon = (By.CLASS_NAME,'icon-upload')
    icon_style = {
        "数据": (By.XPATH,'//img[@alt="shuju"]'),
        "日志": (By.XPATH,'//img[@alt="rizhi"]'),
        "商户": (By.XPATH,'//img[@alt="shanghu"]'),
        "卡片": (By.XPATH,'//img[@alt="kapian"]'),
        "机具": (By.XPATH,'//img[@alt="jiju"]'),
        "操作": (By.XPATH,'//img[@alt="caozao"]'),
        "规则": (By.XPATH,'//img[@alt="guize"]'),
        "充值": (By.XPATH,'//img[@alt="chongzhi"]'),
        "点单": (By.XPATH,'//img[@alt="diandan"]'),
        "账单": (By.XPATH,'//img[@alt="zhangdan"]'),
        "系统": (By.XPATH,'//img[@alt="xitong"]'),
        "设备": (By.XPATH,'//img[@alt="shebei"]')
    }
    confirm_button = (By.XPATH,'//span[text()="确 定"]')

    father_permissions = (By.XPATH,'//input[@placeholder="选择父级"]')

    save_button = (By.XPATH,'//span[contains(text(), "保 存")]')

    toast_text = (By.CLASS_NAME, 'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')
    dialog_text = (By.CLASS_NAME ,'el-dialog__body')

    def input_permisstions_info(self,browser,permisstions_name,level,path,number):

        self.find_element_and_send_keys(browser,self.permissions_name,permisstions_name)
        self.find_element_and_click(browser,self.permissions_level[level])
        self.find_element_and_send_keys(browser,self.permissions_path,path)
        if len(number) > 1:
            self.find_element_and_send_keys(browser,self.permissions_number,number)



if __name__=="__main__":
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("http://192.168.10.12:19333/index.html#/")
    loginpage().input_info_and_login(browser, "13333333333", "123456", "1234")
    sleep(3)
    addpermissionspage().input_permisstions_info(browser,"测试","1级菜单","test","3")