import unittest

from selenium import webdriver

from Src.Modules.Admin.YeWu.AddButton import addbutton


class testcase_addbutton(unittest.TestCase):

    def setUp(self):
        self.ab = addbutton()
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        url = self.ab.get_info_from_csv_by_key('../../../../Conf/TestEnvironmentConf.csv','URL')
        self.browser.get(url)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_addbutton_001(self):
        try:
            self.ab.login_and_add_button(self.browser,'AddButton_001')
            toast_text = self.ab.find_element_and_get_text(self.browser,self.ab.toast_text)
            self.assertEqual('添加成功！',toast_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbutton_002(self):
        try:
            self.ab.login_and_add_button(self.browser,'AddButton_002')
            error_text = self.ab.find_element_and_get_text(self.browser,self.ab.error_text)
            self.assertIn('按钮名称不能为空！',error_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbutton_003(self):
        try:
            self.ab.login_and_add_button(self.browser,'AddButton_003')
            error_text = self.ab.find_element_and_get_text(self.browser,self.ab.error_text)
            self.assertIn('按钮标识不能为空！',error_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbutton_004(self):
        try:
            self.ab.login_and_add_button(self.browser,'AddButton_004')
            dialog_text = self.ab.find_element_and_get_text(self.browser,self.ab.dialog_text)
            self.assertEqual('按钮名称已存在，不可添加！',dialog_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbutton_005(self):
        try:
            self.ab.login_and_add_button(self.browser,'AddButton_005')
            dialog_text = self.ab.find_element_and_get_text(self.browser,self.ab.dialog_text)
            self.assertEqual('按钮标识已存在，不可添加！',dialog_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbutton_006(self):
        try:
            self.ab.login_and_add_button(self.browser,'AddButton_006')
            error_text = self.ab.find_element_and_get_text(self.browser,self.ab.error_text)
            self.assertIn('按钮名称为2-10位中文字母组合',error_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbutton_007(self):
        try:
            self.ab.login_and_add_button(self.browser,'AddButton_007')
            error_text = self.ab.find_element_and_get_text(self.browser,self.ab.error_text)
            self.assertIn('按钮标识为2-20位字母组合',error_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise