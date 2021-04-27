import unittest
from time import sleep

from selenium import webdriver

from Src.Modules.Branch.YeWu.AddClassification import addclassification


class testcase_addclassification(unittest.TestCase):

    def setUp(self) -> None:
        self.ac = addclassification()
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        url = self.ac.get_info_from_csv_by_key('../../../../Conf/TestEnvironmentConf.csv','URL')
        self.browser.get(url)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_addclassification_001(self):
        try:
            self.ac.login_and_add_classification(self.browser,'AddClassification_001')
            sleep(3)
            toast_text = self.ac.find_element_and_get_text(self.browser,self.ac.toast_text)
            self.assertEqual('添加成功',toast_text)
        except:
            self.ac.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addclassification_002(self):
        try:
            self.ac.login_and_add_classification(self.browser,'AddClassification_002')
            error_text = self.ac.find_element_and_get_text(self.browser,self.ac.error_text)
            self.assertIn('分类编码不能为空！',error_text)
        except:
            self.ac.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addclassification_003(self):
        try:
            self.ac.login_and_add_classification(self.browser,'AddClassification_003')
            error_text = self.ac.find_element_and_get_text(self.browser,self.ac.error_text)
            self.assertIn('分类名称不能为空！',error_text)
        except:
            self.ac.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addclassification_004(self):
        try:
            self.ac.login_and_add_classification(self.browser,'aAddClassification_004')
            error_text = self.ac.find_element_and_get_text(self.browser,self.ac.error_text)
            self.assertIn('分类排序不能为空！',error_text)
        except:
            self.ac.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addclassification_005(self):
        try:
            self.ac.login_and_add_classification(self.browser,'AddClassification_005')
            error_text = self.ac.find_element_and_get_text(self.browser,self.ac.error_text)
            self.assertIn('分类名称必须是2-30位中文或字母组合',error_text)
        except:
            self.ac.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addclassification_006(self):
        try:
            self.ac.login_and_add_classification(self.browser,'AddClassification_006')
            error_text = self.ac.find_element_and_get_text(self.browser,self.ac.error_text)
            self.assertIn('分类排序必须是大于0的整数',error_text)
        except:
            self.ac.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addclassification_007(self):
        try:
            self.ac.login_and_add_classification(self.browser,'AddClassification_007')
            dialog_text = self.ac.find_element_and_get_text(self.browser,self.ac.dialog_text)
            self.assertIn('请选择上传图片',dialog_text)
        except:
            self.ac.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addclassification_008(self):
        try:
            self.ac.login_and_add_classification(self.browser,'AddClassification_008')
            toast_text = self.ac.find_element_and_get_text(self.browser,self.ac.toast_text)
            self.assertEqual('上传文件只能是图片格式 !',toast_text)
        except:
            self.ac.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addclassification_009(self):
        try:
            self.ac.login_and_add_classification(self.browser,'AddClassification_009')
            dialog_text = self.ac.find_element_and_get_text(self.browser,self.ac.dialog_text)
            self.assertIn('添加失败，分类编码已被占用',dialog_text)
        except:
            self.ac.get_web_picture(self.browser,'../TestPicture')
            raise