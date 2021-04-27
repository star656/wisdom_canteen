import unittest

from selenium import webdriver

from Src.Modules.Admin.YeWu.AddUser import adduser


class testcase_adduser(unittest.TestCase):
    # 定义前置方法
    def setUp(self):
        self.ul = adduser()  # 示例化类loginpage的对象
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()  # 最大化浏览器
        url = self.ul.get_info_from_csv_by_key("../../../../Conf/TestEnvironmentConf.csv", "URL")
        self.browser.get(url)
    # 定义后置方法
    def tearDown(self):
        self.browser.quit()


    def test_adduser_001(self):
        try:
            self.ul.login_and_add_user(self.browser, "AddUser_001")
            Toast_info = self.ul.find_element_and_get_text(self.browser, self.ul.toast_text)
            self.assertEqual("操作成功",Toast_info)

        except:
            self.ul.get_web_picture(self.browser,"../TestPicture" )
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass


    def test_adduser_002(self):
        try:
            self.ul.login_and_add_user(self.browser, "AddUser_002")
            Toast_info = self.ul.find_element_and_get_text(self.browser, self.ul.toast_text)
            self.assertEqual("操作成功", Toast_info)
        except:
            self.ul.get_web_picture(self.browser,"../TestPicture" )
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    def test_adduser_003(self):
        try:
            self.ul.login_and_add_user(self.browser, 'AddUser_003')
            error_info = self.ul.find_element_and_get_text(self.browser,self.ul.error_text)
            self.assertIn("用户名不能为空！", error_info)
        except:
            self.ul.get_web_picture(self.browser, "../TestPicture")
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    def test_adduser_004(self):
        try:
            self.ul.login_and_add_user(self.browser, 'AddUser_004')
            error_info = self.ul.find_element_and_get_text(self.browser,self.ul.error_text)
            self.assertIn("手机号码不能为空！", error_info)
        except:
            self.ul.get_web_picture(self.browser, "../TestPicture")
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    def test_adduser_005(self):
        try:
            self.ul.login_and_add_user(self.browser, 'AddUser_005')
            Toast_info = self.ul.find_element_and_get_text(self.browser, self.ul.toast_text)
            self.assertEqual("操作成功", Toast_info)
        except:
            self.ul.get_web_picture(self.browser, "../TestPicture")
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    def test_adduser_006(self):
        try:
            self.ul.login_and_add_user(self.browser, 'AddUser_006')
            error_info = self.ul.find_element_and_get_text(self.browser,self.ul.error_text)
            self.assertIn("请选择角色", error_info)
        except:
            self.ul.get_web_picture(self.browser, "../TestPicture")
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    def test_adduser_007(self):
        try:
            self.ul.login_and_add_user(self.browser, 'AddUser_007')
            error_info = self.ul.find_element_and_get_text(self.browser,self.ul.error_text)
            self.assertIn("请选择用户类型", error_info)
        except:
            self.ul.get_web_picture(self.browser, "../TestPicture")
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    def test_adduser_008(self):
        try:
            self.ul.login_and_add_user(self.browser, 'AddUser_008')
            dialog_info = self.ul.find_element_and_get_text(self.browser,self.ul.dialog_text)
            self.assertEqual("号码已被占用！", dialog_info)
        except:
            self.ul.get_web_picture(self.browser, "../TestPicture")
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    def test_adduser_009(self):
        try:
            self.ul.login_and_add_user(self.browser, 'AddUser_009')
            error_info = self.ul.find_element_and_get_text(self.browser,self.ul.error_text)
            self.assertIn("非法的手机号码！", error_info)
        except:
            self.ul.get_web_picture(self.browser, "../TestPicture")
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    def test_adduser_010(self):
        try:
            self.ul.login_and_add_user(self.browser, 'AddUser_010')
            error_info = self.ul.find_element_and_get_text(self.browser,self.ul.error_text)
            self.assertIn("非法的手机号码！", error_info)
        except:
            self.ul.get_web_picture(self.browser, "../TestPicture")
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    def test_adduser_011(self):
        try:
            self.ul.login_and_add_user(self.browser, 'AddUser_011')
            error_info = self.ul.find_element_and_get_text(self.browser,self.ul.error_text)
            self.assertIn("密码为6~13位字母或数字组合！", error_info)
        except:
            self.ul.get_web_picture(self.browser, "../TestPicture")
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    def test_adduser_012(self):
        try:
            self.ul.login_and_add_user(self.browser, 'AddUser_012')
            dialog_info = self.ul.find_element_and_get_text(self.browser,self.ul.dialog_text)
            self.assertIn("姓名为2-10位中文字符，最多可带一位数字", dialog_info)
        except:
            self.ul.get_web_picture(self.browser, "../TestPicture")
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

    def test_adduser_013(self):
        try:
            self.ul.login_and_add_user(self.browser, 'AddUser_013')
            error_info = self.ul.find_element_and_get_text(self.browser,self.ul.error_text)
            self.assertIn("请选择商户", error_info)
        except:
            self.ul.get_web_picture(self.browser, "../TestPicture")
            raise  # 再抛一次异常。如果不抛出异常，即使脚本执行失败也会被判断为pass

if __name__=="__main__":
    unittest.main()   # 执行这一行相当于执行当前类下所有用例