import unittest
from time import sleep

from selenium import webdriver
from Src.Modules.Common.YeWu.UserLogin import userlogin


class testcase_userlogin(unittest.TestCase):
    # 定义前置方法
    def setUp(self):
        self.ul = userlogin()  # 示例化类loginpage的对象
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()  # 最大化浏览器
        url = self.ul.get_info_from_csv_by_key("../../../../Conf/TestEnvironmentConf.csv", "URL")
        self.browser.get(url)
    # 定义后置方法
    def tearDown(self):
        sleep(2)
        self.browser.quit()

    # 使用用户登录测试用例
    # 实现使用正确用户名和密码登录测试用例
    def test_userlogin_001(self):
        try:
            self.ul.user_login_by_testcase_number(self.browser, "UserLogin_001")
            bool_value = self.ul.title_is_text_or_not(self.browser, "财政厅食堂系统")
            self.assertTrue(bool_value)
        except:
            self.ul.get_web_picture(self.browser,"../TestPicture" )
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    # 实现使用错误账号登录测试用例
    def test_userlogin_002(self):
        try:
            self.ul.user_login_by_testcase_number(self.browser, "UserLogin_002")
            error_text = self.ul.find_element_and_get_text(self.browser, self.ul.error_text)
            self.assertIn("请输入账号", error_text)
        except:
            self.ul.get_web_picture(self.browser,"../TestPicture" )
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    # 实现密码错误登录测试用例
    def test_userlogin_003(self):
        try:
            self.ul.user_login_by_testcase_number(self.browser, "UserLogin_003")
            error_text = self.ul.find_element_and_get_text(self.browser, self.ul.error_text)
            self.assertIn("请输入6位密码", error_text)
        except:
            self.ul.get_web_picture(self.browser,"../TestPicture" )
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass
    #实现账号不填测试
    def test_userlogin_004(self):
        try:
            self.ul.user_login_by_testcase_number(self.browser, "UserLogin_004")
            error_text = self.ul.find_element_and_get_text(self.browser, self.ul.error_text)
            self.assertIn("请输入4位验证码", error_text)
        except:
            self.ul.get_web_picture(self.browser,"../TestPicture" )
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass
    #实现账号不填测试
    def test_userlogin_005(self):
        try:
            self.ul.user_login_by_testcase_number(self.browser, "UserLogin_005")
            toast_text = self.ul.find_element_and_get_text(self.browser, self.ul.toast_text)
            self.assertEqual("手机号或密码错误！", toast_text)
        except:
            self.ul.get_web_picture(self.browser,"../TestPicture" )
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    def test_userlogin_006(self):
        try:
            self.ul.user_login_by_testcase_number(self.browser, "UserLogin_006")
            toast_text = self.ul.find_element_and_get_text(self.browser, self.ul.toast_text)
            sleep(1)
            self.assertIn("用户已被禁用，请联系管理员！", toast_text)
        except:
            self.ul.get_web_picture(self.browser,"../TestPicture" )
            raise
if __name__=="__main__":
    unittest.main()   # 执行这一行相当于执行当前类下所有用例