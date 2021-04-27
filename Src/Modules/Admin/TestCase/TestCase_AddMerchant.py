import unittest

from selenium import webdriver

from Src.Modules.Admin.YeWu.AddMerchant import addmerchant


class testcase_addmerchant(unittest.TestCase):

    def setUp(self) -> None:
        self.am = addmerchant()
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        url = self.am.get_info_from_csv_by_key('../../../../Conf/TestEnvironmentConf.csv','URL')
        self.browser.get(url)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_addmerchant_001(self):
        try:
            self.am.login_and_add_merchant(self.browser,'AddMerchant_001')
            toast_text = self.am.find_element_and_get_text(self.browser,self.am.toast_text)
            self.assertEqual('添加成功！', toast_text)
        except:
            self.am.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addmerchant_002(self):
        try:
            self.am.login_and_add_merchant(self.browser,'AddMerchant_002')
            error_text = self.am.find_element_and_get_text(self.browser,self.am.error_text)
            self.assertIn('商户名不能为空！',error_text)
        except:
            self.am.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addmerchant_003(self):
        try:
            self.am.login_and_add_merchant(self.browser,'AddMerchant_003')
            error_text = self.am.find_element_and_get_text(self.browser,self.am.error_text)
            self.assertIn('商户编号不能为空！',error_text)
        except:
            self.am.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addmerchant_004(self):
        try:
            self.am.login_and_add_merchant(self.browser,'AddMerchant_004')
            error_text = self.am.find_element_and_get_text(self.browser,self.am.error_text)
            self.assertIn('商户名称为4-32位中文或字母组合',error_text)
        except:
            self.am.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addmerchant_005(self):
        try:
            self.am.login_and_add_merchant(self.browser,'AddMerchant_005')
            error_text = self.am.find_element_and_get_text(self.browser,self.am.error_text)
            self.assertIn('商户编号必须是8-15位的数字',error_text)
        except:
            self.am.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addmerchant_006(self):
        try:
            self.am.login_and_add_merchant(self.browser,'AddMerchant_006')
            dialog_text = self.am.find_element_and_get_text(self.browser,self.am.dialog_text)
            self.assertEqual('添加失败，商户名称已经存在！',dialog_text)
        except:
            self.am.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addmerchant_007(self):
        try:
            self.am.login_and_add_merchant(self.browser,'AddMerchant_007')
            dialog_text = self.am.find_element_and_get_text(self.browser,self.am.dialog_text)
            self.assertEqual('添加失败，商户号已经存在！',dialog_text)
        except:
            self.am.get_web_picture(self.browser,'../TestPicture')
            raise