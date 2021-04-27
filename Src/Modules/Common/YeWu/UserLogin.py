from Src.Common.CSV import csv
from Src.Page.LoginPage import loginpage


class userlogin(loginpage,csv):
    # 按照用例编号实现登录
    def user_login_by_testcase_number(self, browser,testcase_number):
        td_dict = self.get_testdata_from_csv_by_testcase_number("../TestData/UserLoginTestData.csv", testcase_number)
        self.input_info_and_login(browser, username=td_dict["账号"], password=td_dict["密码"],code=td_dict["验证码"])


    # 使用管理员账号登录
    def user_login_by_Administrator(self, browser):
        info_dict = self.get_info_from_csv_to_dict("../../../../Conf/TestEnvironmentConf.csv")
        self.input_info_and_login(browser, username=info_dict["UserName"],password=info_dict["Password"],code="1234")

    # 使用商户账号登录
    def user_login_by_merchant(self,browser):
        in_dict = self.get_info_from_csv_to_dict('../../../../Conf/TestMerchantConf.csv')
        self.input_info_and_login(browser,username=in_dict["UserName"],password=in_dict["Password"],code="1234")

    #使用网点账户登录
    def user_login_by_branch(self,browser):
        in_dict = self.get_info_from_csv_to_dict('../../../../Conf/TestBranchConf.csv')
        self.input_info_and_login(browser, username=in_dict["UserName"], password=in_dict["Password"], code="1234")