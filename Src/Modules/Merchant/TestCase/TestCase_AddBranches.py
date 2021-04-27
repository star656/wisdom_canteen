import unittest

from selenium import webdriver

from Src.Modules.Merchant.YeWu.AddBranches import addbranches


class testcase_addbranches(unittest.TestCase):

    def setUp(self) -> None:
        self.ab = addbranches()
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        url = self.ab.get_info_from_csv_by_key('../../../../Conf/TestEnvironmentConf.csv','URL')
        self.browser.get(url)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_addbranches_001(self):
        try:
            self.ab.login_and_add_branches(self.browser,'AddBranches_001')
            toast_text = self.ab.find_element_and_get_text(self.browser,self.ab.toast_text)
            self.assertEqual('添加成功',toast_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbranches_002(self):
        try:
            self.ab.login_and_add_branches(self.browser,'AddBranches_002')
            toast_text = self.ab.find_element_and_get_text(self.browser,self.ab.toast_text)
            self.assertEqual('添加成功',toast_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbranches_003(self):
        try:
            self.ab.login_and_add_branches(self.browser,'AddBranches_003')
            error_text = self.ab.find_element_and_get_text(self.browser,self.ab.error_text)
            self.assertIn('网点名称不能为空！',error_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbranches_004(self):
        try:
            self.ab.login_and_add_branches(self.browser,'AddBranches_004')
            error_text = self.ab.find_element_and_get_text(self.browser,self.ab.error_text)
            self.assertIn('网点编码不能为空！',error_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbranches_005(self):
        try:
            self.ab.login_and_add_branches(self.browser,'AddBranches_005')
            error_text = self.ab.find_element_and_get_text(self.browser,self.ab.error_text)
            self.assertIn('请选择部门',error_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbranches_006(self):
        try:
            self.ab.login_and_add_branches(self.browser,'AddBranches_006')
            error_text = self.ab.find_element_and_get_text(self.browser,self.ab.error_text)
            self.assertIn('请输入市民卡商户号',error_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbranches_007(self):
        try:
            self.ab.login_and_add_branches(self.browser,'AddBranches_007')
            error_text = self.ab.find_element_and_get_text(self.browser,self.ab.error_text)
            self.assertIn('请输入市民卡终端号',error_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbranches_008(self):
        try:
            self.ab.login_and_add_branches(self.browser,'AddBranches_008')
            error_text = self.ab.find_element_and_get_text(self.browser,self.ab.error_text)
            self.assertIn('网点名称必须是2-30位中文或字母组合',error_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbranches_009(self):
        try:
            self.ab.login_and_add_branches(self.browser,'AddBranches_009')
            error_text = self.ab.find_element_and_get_text(self.browser,self.ab.error_text)
            self.assertIn('市民卡商户号必须是40位以内的数字！',error_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbranches_010(self):
        try:
            self.ab.login_and_add_branches(self.browser,'AddBranches_010')
            error_text = self.ab.find_element_and_get_text(self.browser,self.ab.error_text)
            self.assertIn('市民卡终端号必须是40位以内的数字！',error_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbranches_011(self):
        try:
            self.ab.login_and_add_branches(self.browser,'AddBranches_011')
            dialog_text = self.ab.find_element_and_get_text(self.browser,self.ab.dialog_text)
            self.assertEqual('请选择所在区域！',dialog_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addbranches_012(self):
        try:
            self.ab.login_and_add_branches(self.browser,'AddBranches_012')
            dialog_text = self.ab.find_element_and_get_text(self.browser,self.ab.dialog_text)
            self.assertEqual('添加失败，网点编码已被占用',dialog_text)
        except:
            self.ab.get_web_picture(self.browser,'../TestPicture')
            raise