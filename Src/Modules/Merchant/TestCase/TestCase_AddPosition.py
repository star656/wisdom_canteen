import unittest

from selenium import webdriver

from Src.Modules.Merchant.YeWu.AddPosition import addposition


class testcase_addposition(unittest.TestCase):

    def setUp(self) -> None:
        self.ap = addposition()
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        url = self.ap.get_info_from_csv_by_key('../../../../Conf/TestEnvironmentConf.csv','URL')
        self.browser.get(url)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_addposition_001(self):
        try:
            self.ap.login_and_add_position(self.browser,'AddPosition_001')
            toast_text = self.ap.find_element_and_get_text(self.browser,self.ap.toast_text)
            self.assertEqual('添加成功', toast_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addposition_002(self):
        try:
            self.ap.login_and_add_position(self.browser,'AddPosition_002')
            error_text = self.ap.find_element_and_get_text(self.browser,self.ap.error_text)
            self.assertIn('请选择部门', error_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addposition_003(self):
        try:
            self.ap.login_and_add_position(self.browser,'AddPosition_003')
            error_text = self.ap.find_element_and_get_text(self.browser,self.ap.error_text)
            self.assertIn('职位名称不能为空！', error_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addposition_004(self):
        try:
            self.ap.login_and_add_position(self.browser,'AddPosition_004')
            error_text = self.ap.find_element_and_get_text(self.browser,self.ap.error_text)
            self.assertIn('职位描述不能为空！', error_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addposition_005(self):
        try:
            self.ap.login_and_add_position(self.browser,'AddPosition_005')
            dialog_text = self.ap.find_element_and_get_text(self.browser,self.ap.dialog_text)
            self.assertEqual('职位名称必须是2-30位中文字符、字母或数字组合', dialog_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addposition_006(self):
        try:
            self.ap.login_and_add_position(self.browser,'AddPosition_006')
            error_text = self.ap.find_element_and_get_text(self.browser,self.ap.error_text)
            self.assertIn('职位描述必须是2-200位的中文或字母组合', error_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addposition_007(self):
        try:
            self.ap.login_and_add_position(self.browser,'AddPosition_007')
            dialog_text = self.ap.find_element_and_get_text(self.browser,self.ap.dialog_text)
            self.assertEqual('指定的部门下已存在该职位！', dialog_text)
        except:
            self.ap.get_web_picture(self.browser,'../TestPicture')
            raise