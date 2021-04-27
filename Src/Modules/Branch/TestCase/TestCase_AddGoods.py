import unittest
from time import sleep

from selenium import webdriver

from Src.Modules.Branch.YeWu.AddGoods import addgoods


class testcase_addgoods(unittest.TestCase):

    def setUp(self) -> None:
        self.ag = addgoods()
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        url = self.ag.get_info_from_csv_by_key('../../../../Conf/TestEnvironmentConf.csv','URL')
        self.browser.get(url)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_addgoods_001(self):
        try:
            self.ag.login_and_add_goods(self.browser,'AddGoods_001')
            sleep(3)
            toast_text = self.ag.find_element_and_get_text(self.browser,self.ag.toast_text)
            self.assertEqual('添加成功', toast_text)
        except:
            self.ag.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addgoods_002(self):
        try:
            self.ag.login_and_add_goods(self.browser,'AddGoods_002')
            error_text = self.ag.find_element_and_get_text(self.browser,self.ag.error_text)
            self.assertIn('商品名称不能为空！', error_text)
        except:
            self.ag.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addgoods_003(self):
        try:
            self.ag.login_and_add_goods(self.browser,'AddGoods_003')
            error_text = self.ag.find_element_and_get_text(self.browser,self.ag.error_text)
            self.assertIn('商品价格不能为空！', error_text)
        except:
            self.ag.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addgoods_004(self):
        try:
            self.ag.login_and_add_goods(self.browser,'AddGoods_004')
            error_text = self.ag.find_element_and_get_text(self.browser,self.ag.error_text)
            self.assertIn('商品排序不能为空！', error_text)
        except:
            self.ag.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addgoods_005(self):
        try:
            self.ag.login_and_add_goods(self.browser,'AddGoods_005')
            error_text = self.ag.find_element_and_get_text(self.browser,self.ag.error_text)
            self.assertIn('商品类别不能为空！', error_text)
        except:
            self.ag.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addgoods_006(self):
        try:
            self.ag.login_and_add_goods(self.browser,'AddGoods_006')
            dialog_text = self.ag.find_element_and_get_text(self.browser,self.ag.dialog_text)
            self.assertIn('请选择上传图片', dialog_text)
        except:
            self.ag.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addgoods_007(self):
        try:
            self.ag.login_and_add_goods(self.browser,'AddGoods_007')
            error_text = self.ag.find_element_and_get_text(self.browser,self.ag.error_text)
            self.assertIn('商品名称必须是2-30位中文或字母组合', error_text)
        except:
            self.ag.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addgoods_008(self):
        try:
            self.ag.login_and_add_goods(self.browser,'AddGoods_008')
            error_text = self.ag.find_element_and_get_text(self.browser,self.ag.error_text)
            self.assertIn('商品价格必须是大于0的数', error_text)
        except:
            self.ag.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addgoods_009(self):
        try:
            self.ag.login_and_add_goods(self.browser,'AddGoods_009')
            error_text = self.ag.find_element_and_get_text(self.browser,self.ag.error_text)
            self.assertIn('商品排序必须是大于0的整数', error_text)
        except:
            self.ag.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addgoods_010(self):
        try:
            self.ag.login_and_add_goods(self.browser,'AddGoods_010')
            sleep(2)
            toast_text = self.ag.find_element_and_get_text(self.browser, self.ag.toast_text)
            self.assertEqual('上传文件只能是图片格式 !', toast_text)
        except:
            self.ag.get_web_picture(self.browser,'../TestPicture')
            raise

