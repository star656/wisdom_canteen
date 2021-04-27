import unittest

from selenium import webdriver

from Src.Modules.Merchant.YeWu.AddEmployees import addemployees


class testcase_addemployees(unittest.TestCase):

    def setUp(self) -> None:
        self.ae = addemployees()
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        url = self.ae.get_info_from_csv_by_key('../../../../Conf/TestEnvironmentConf.csv','URL')
        self.browser.get(url)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_addemployees_001(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_001')
            toast_text = self.ae.find_element_and_get_text(self.browser,self.ae.toast_text)
            self.assertEqual('添加成功', toast_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_002(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_002')
            toast_text = self.ae.find_element_and_get_text(self.browser,self.ae.toast_text)
            self.assertEqual('请先选择部门！', toast_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_003(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_003')
            toast_text = self.ae.find_element_and_get_text(self.browser,self.ae.toast_text)
            self.assertEqual('添加成功', toast_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_004(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_004')
            error_text = self.ae.find_element_and_get_text(self.browser,self.ae.error_text)
            self.assertIn('请输入中文名称', error_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_005(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_005')
            error_text = self.ae.find_element_and_get_text(self.browser,self.ae.error_text)
            self.assertIn('请选择性别', error_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_006(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_006')
            error_text = self.ae.find_element_and_get_text(self.browser,self.ae.error_text)
            self.assertIn('手机号不能为空', error_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_007(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_007')
            error_text = self.ae.find_element_and_get_text(self.browser,self.ae.error_text)
            self.assertIn('请输入卡号', error_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_008(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_008')
            error_text = self.ae.find_element_and_get_text(self.browser,self.ae.error_text)
            self.assertIn('员工工号为2-8位数字', error_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_009(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_009')
            error_text = self.ae.find_element_and_get_text(self.browser,self.ae.error_text)
            self.assertIn('员工中文名必须是2-10位中文,可加一位数字', error_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_010(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_010')
            error_text = self.ae.find_element_and_get_text(self.browser,self.ae.error_text)
            self.assertIn('英文名为4-30个英文字母', error_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_011(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_011')
            error_text = self.ae.find_element_and_get_text(self.browser,self.ae.error_text)
            self.assertIn('非法的手机号码！', error_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_012(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_012')
            error_text = self.ae.find_element_and_get_text(self.browser,self.ae.error_text)
            self.assertIn('非法的身份证号！', error_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_013(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_013')
            error_text = self.ae.find_element_and_get_text(self.browser,self.ae.error_text)
            self.assertIn('卡号必须是40位以内的数字！', error_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_014(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_014')
            dialog_text = self.ae.find_element_and_get_text(self.browser,self.ae.dialog_text)
            self.assertEqual('卡号是20位以内的数字组合！', dialog_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addemployees_015(self):
        try:
            self.ae.login_and_add_employees(self.browser,'AddEmployees_015')
            dialog_text = self.ae.find_element_and_get_text(self.browser,self.ae.dialog_text)
            self.assertEqual('电话号码在本商户已被登记！', dialog_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise