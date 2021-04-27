import unittest

from selenium import webdriver

from Src.Modules.Admin.YeWu.AddPermissions import addpermissions


class testcase_addpermissions(unittest.TestCase):
    # 定义前置方法
    def setUp(self):
        self.ap = addpermissions()  # 示例化类loginpage的对象
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()  # 最大化浏览器
        url = self.ap.get_info_from_csv_by_key("../../../../Conf/TestEnvironmentConf.csv", "URL")
        self.browser.get(url)
    # 定义后置方法
    def tearDown(self):
        self.browser.quit()

    def test_addpermissions_001(self):
        try:
            self.ap.login_and_add_permissions(self.browser,'AddPermissions_001')
            toast_text = self.ap.find_element_and_get_text(self.browser,self.ap.toast_text)
            self.assertEqual('添加成功', toast_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addpermissions_002(self):
        try:
            self.ap.login_and_add_permissions(self.browser,'AddPermissions_002')
            toast_text = self.ap.find_element_and_get_text(self.browser,self.ap.toast_text)
            self.assertEqual('添加成功', toast_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addpermissions_003(self):
        try:
            self.ap.login_and_add_permissions(self.browser,'AddPermissions_003')
            error_text = self.ap.find_element_and_get_text(self.browser,self.ap.error_text)
            self.assertIn('权限名称不能为空！', error_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addpermissions_004(self):
        try:
            self.ap.login_and_add_permissions(self.browser,'AddPermissions_004')
            error_text = self.ap.find_element_and_get_text(self.browser,self.ap.error_text)
            self.assertIn('权限路径不能为空！', error_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addpermissions_005(self):
        try:
            self.ap.login_and_add_permissions(self.browser,'AddPermissions_005')
            error_text = self.ap.find_element_and_get_text(self.browser,self.ap.error_text)
            self.assertIn('请选择图标', error_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addpermissions_006(self):
        try:
            self.ap.login_and_add_permissions(self.browser,'AddPermissions_006')
            error_text = self.ap.find_element_and_get_text(self.browser,self.ap.error_text)
            self.assertIn('请选择父功能', error_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addpermissions_007(self):
        try:
            self.ap.login_and_add_permissions(self.browser,'AddPermissions_007')
            error_text = self.ap.find_element_and_get_text(self.browser,self.ap.error_text)
            self.assertIn('权限|功能名称为2-20位中文或字母组合', error_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addpermissions_008(self):
        try:
            self.ap.login_and_add_permissions(self.browser,'AddPermissions_008')
            error_text = self.ap.find_element_and_get_text(self.browser,self.ap.error_text)
            self.assertIn('权限路径不能为空！', error_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addpermissions_009(self):
        try:
            self.ap.login_and_add_permissions(self.browser,'AddPermissions_009')
            dialog_text = self.ap.find_element_and_get_text(self.browser,self.ap.dialog_text)
            self.assertEqual('添加失败，功能名称已经存在！', dialog_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise