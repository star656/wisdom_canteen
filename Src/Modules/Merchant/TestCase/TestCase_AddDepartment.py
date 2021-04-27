import unittest

from selenium import webdriver

from Src.Modules.Merchant.YeWu.AddDepartment import adddepartment


class testcase_adddepartment(unittest.TestCase):

    def setUp(self) -> None:
        self.ad = adddepartment()
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        url = self.ad.get_info_from_csv_by_key('../../../../Conf/TestEnvironmentConf.csv','URL')
        self.browser.get(url)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_adddepartment_001(self):
        try:
            self.ad.login_and_add_department(self.browser,'AddDepartment_001')
            toast_text = self.ad.find_element_and_get_text(self.browser,self.ad.toast_text)
            self.assertEqual('添加成功！', toast_text)
        except:
            self.ad.get_web_picture(self.browser, '../TestPicture')
            raise

    def test_adddepartment_002(self):
        try:
            self.ad.login_and_add_department(self.browser,'AddDepartment_002')
            toast_text = self.ad.find_element_and_get_text(self.browser,self.ad.toast_text)
            self.assertEqual('请先选择部门！', toast_text)
        except:
            self.ad.get_web_picture(self.browser, '../TestPicture')
            raise

    def test_adddepartment_003(self):
        try:
            self.ad.login_and_add_department(self.browser,'AddDepartment_003')
            error_text = self.ad.find_element_and_get_text(self.browser,self.ad.error_text)
            self.assertIn('部门名称不能为空！', error_text)
        except:
            self.ad.get_web_picture(self.browser, '../TestPicture')
            raise

    def test_adddepartment_004(self):
        try:
            self.ad.login_and_add_department(self.browser,'AddDepartment_004')
            error_text = self.ad.find_element_and_get_text(self.browser,self.ad.error_text)
            self.assertIn('部门名称必须是2-30位中文、字母或数字组合', error_text)
        except:
            self.ad.get_web_picture(self.browser, '../TestPicture')
            raise

    def test_adddepartment_005(self):
        try:
            self.ad.login_and_add_department(self.browser,'AddDepartment_005')
            dialog_text = self.ad.find_element_and_get_text(self.browser,self.ad.dialog_text)
            self.assertIn('部门名称已经存在！', dialog_text)
        except:
            self.ad.get_web_picture(self.browser, '../TestPicture')
            raise

    def test_adddepartment_006(self):
        try:
            self.ad.login_and_add_department(self.browser,'AddDepartment_006')
            dialog_text = self.ad.find_element_and_get_text(self.browser,self.ad.dialog_text)
            self.assertIn('添加成功！', dialog_text)
        except:
            self.ad.get_web_picture(self.browser, '../TestPicture')
            raise