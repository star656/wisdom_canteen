import unittest

from selenium import webdriver

from Src.Modules.Admin.YeWu.AddRole import addrole


class testcase_addrole(unittest.TestCase):
    # 定义前置方法
    def setUp(self):
        self.addrole = addrole()  # 示例化类loginpage的对象
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()  # 最大化浏览器
        url = self.addrole.get_info_from_csv_by_key("../../../../Conf/TestEnvironmentConf.csv", "URL")
        self.browser.get(url)
    # 定义后置方法
    def tearDown(self):
        self.browser.quit()

    def test_addrole_001(self):
        try:
            self.addrole.login_and_add_role(self.browser,"AddRole_001")
            toast_info = self.addrole.find_element_and_get_text(self.browser,self.addrole.toast_text)
            self.assertEqual("添加成功",toast_info)
        except:
            self.addrole.get_web_picture(self.browser, "../TestPicture")
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    def test_addrole_002(self):
        try:
            self.addrole.login_and_add_role(self.browser,'AddRole_002')
            error_info = self.addrole.find_element_and_get_text(self.browser,self.addrole.error_text)
            self.assertIn('角色名称不能为空！',error_info)
        except:
            self.addrole.get_web_picture(self.browser, '../TestPicture')
            raise

    def test_addrole_003(self):
        try:
            self.addrole.login_and_add_role(self.browser,'AddRole_003')
            error_info = self.addrole.find_element_and_get_text(self.browser,self.addrole.error_text)
            self.assertIn('角色标识不能为空！',error_info)
        except:
            self.addrole.get_web_picture(self.browser, '../TestPicture')
            raise

    def test_addrole_004(self):
        try:
            self.addrole.login_and_add_role(self.browser,'AddRole_004')
            error_info = self.addrole.find_element_and_get_text(self.browser,self.addrole.error_text)
            self.assertIn('角色描述不能为空！',error_info)
        except:
            self.addrole.get_web_picture(self.browser, '../TestPicture')
            raise

    def test_addrole_005(self):
        try:
            self.addrole.login_and_add_role(self.browser,'AddRole_005')
            error_info = self.addrole.find_element_and_get_text(self.browser,self.addrole.error_text)
            self.assertIn('角色名称为2-10位中文或字母组合',error_info)
        except:
            self.addrole.get_web_picture(self.browser, '../TestPicture')
            raise

    def test_addrole_006(self):
        try:
            self.addrole.login_and_add_role(self.browser,'AddRole_006')
            error_info = self.addrole.find_element_and_get_text(self.browser,self.addrole.error_text)
            self.assertIn('角色标识为2-16位字母组合',error_info)
        except:
            self.addrole.get_web_picture(self.browser, '../TestPicture')
            raise
    def test_addrole_007(self):
        try:
            self.addrole.login_and_add_role(self.browser,'AddRole_007')
            error_info = self.addrole.find_element_and_get_text(self.browser,self.addrole.error_text)
            self.assertIn('角色描述为2-200位的中文或字母组合',error_info)
        except:
            self.addrole.get_web_picture(self.browser, '../TestPicture')
            raise