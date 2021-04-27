from selenium.webdriver.common.by import By

from Src.Common.Web_Operation import web_operation


class adddepartmentpage(web_operation):

    organization_manage = (By.XPATH, '//span[contains(text(), "组织管理")]')
    department_manage = (By.XPATH, '//span[contains(text(), "部门管理")]')
    add_button = (By.XPATH, '//span[contains(text(), "新增")]')

    department_name = (By.XPATH,'//input[@placeholder="请输入部门名称"]')
    confirm_button = (By.XPATH, '/html/body/div[2]/div/div[3]/div/button[2]/span')

    department = (By.CLASS_NAME,'el-tree-node__content')
    dialog_title = (By.CLASS_NAME, 'el-dialog__title')

    toast_text = (By.CLASS_NAME, 'el-message__content')
    error_text = (By.CLASS_NAME, 'el-form-item__error')
    dialog_text = (By.CLASS_NAME ,'el-dialog__body')