import unittest

from selenium import webdriver

from Src.Modules.Merchant.YeWu.AddEquipment import addequipment


class testcase_addequipment(unittest.TestCase):

    def setUp(self) -> None:
        self.ae = addequipment()
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        url = self.ae.get_info_from_csv_by_key('../../../../Conf/TestEnvir','URL')
        self.browser.get(url)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_addequipment_001(self):
        try:
            self.ae.login_and_add_equipment(self.browser,'AddEquipment_001')
            toast_info = self.ae.find_element_and_get_text(self.browser,self.ae.toast_text)
            self.assertEqual('添加成功',toast_info)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addequipment_002(self):
        try:
            self.ae.login_and_add_equipment(self.browser,'AddEquipment_002')
            error_text = self.ae.find_element_and_get_text(self.browser,self.ae.error_text)
            self.assertEqual('请选择网点',error_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addequipment_003(self):
        try:
            self.ae.login_and_add_equipment(self.browser,'AddEquipment_003')
            error_text = self.ae.find_element_and_get_text(self.browser,self.ae.error_text)
            self.assertEqual('设备名称不能为空！',error_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addequipment_004(self):
        try:
            self.ae.login_and_add_equipment(self.browser,'AddEquipment_004')
            error_text = self.ae.find_element_and_get_text(self.browser,self.ae.error_text)
            self.assertEqual('设备编号不能为空！',error_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise

    def test_addequipment_005(self):
        try:
            self.ae.login_and_add_equipment(self.browser,'AddEquipment_005')
            dialog_text = self.ae.find_element_and_get_text(self.browser,self.ae.dialog_text)
            self.assertEqual('添加失败，设备编码已被占用',dialog_text)
        except:
            self.ae.get_web_picture(self.browser,'../TestPicture')
            raise