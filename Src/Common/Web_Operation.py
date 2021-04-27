from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as ec

from Src.Common.Sys_Operation import sys_operation


class web_operation:

    # 实现点击元素方法,参数element表示元素
    def click_element(self, element):
        element.click()
    # 实现给元素输入内容方法,参数element表示元素,value表示你要输入的字符串

    def send_keys_to_element(self, element, value):
        element.clear()
        element.send_keys(value)

    #实现获取元素上文本的方法
    def get_text_from_element(self, element):
        return element.text

    #实现获取元素的属性值的方法
    def get_attribute_value_from_element(self,element, attbiture_name):
        element.get_attribute(attbiture_name)

    #实现示例化动态等待对象的方法
    def get_webdriver_waite_object(self, browser):
        waiter = WebDriverWait(browser, 10)
        return waiter

    #实现动态的定位元素，当元素出现就定位到, browser表示浏览器对象， ele_tuple表示由元素定位方法及标识组成的元祖
    def find_element_by_webdriverwaite(self,browser, ele_tuple):
        waiter = self.get_webdriver_waite_object(browser)
        ele = waiter.until(ec.presence_of_element_located(ele_tuple))
        return ele

    #实现定位元素并点击的方法
    def find_element_and_click(self,browser, ele_tuple):
        ele = self.find_element_by_webdriverwaite(browser, ele_tuple)
        self.click_element(ele)

    # 实现定位元素并输入内容
    def find_element_and_send_keys(self,browser, ele_tuple, value):
        ele = self.find_element_by_webdriverwaite(browser, ele_tuple)
        self.send_keys_to_element(ele, value)

    # 实现定位元素并获取文本的方法
    def find_element_and_get_text(self, browser, ele_tuple):
        ele = self.find_element_by_webdriverwaite(browser, ele_tuple)
        text = self.get_text_from_element(ele)
        return text

    # 实现定位元素并获取文本的方法
    def find_elements_and_get_text_list(self, browser, ele_tuple):
        text_list = []
        ele_list = self.find_elements_by_webdriverwaite(browser, ele_tuple)
        for ele in ele_list:
            text = self.get_text_from_element(ele)
            if len(text) !=0:
                text_list.append(text)
        return text_list

    # 实现定位元素并获取元素属性值
    def find_element_and_get_attribute_value(self, browser, ele_tuple, attbiture_name):
        ele = self.find_element_by_webdriverwaite(browser, ele_tuple)
        attribute_value = self.get_attribute_value_from_element(ele,attbiture_name)
        return attribute_value


    # 判断文本是否在某个元素上，在则返回True，不在返回False
    def text_to_be_present_in_element_or_not(self, browser, ele_tuple, text):
        waiter = self.get_webdriver_waite_object(browser)
        try:
            bool_value = waiter.until(ec.text_to_be_present_in_element(ele_tuple, text))
            return bool_value
        except:
            return False

    # 实现多元素定位
    def find_elements_by_webdriverwaite(self, browser, ele_tuple):
        waiter = self.get_webdriver_waite_object(browser)
        ele_list = waiter.until(ec.presence_of_all_elements_located(ele_tuple))
        return ele_list

    # 实现定位多元素并输入内容
    def find_elements_and_send_keys(self, browser, ele_tuple,index, value):
        ele_list = self.find_elements_by_webdriverwaite(browser, ele_tuple)
        self.send_keys_to_element(ele_list[index], value)

    # 实现定位多元素并点击
    def find_elements_and_click(self, browser, ele_tuple, index):
        ele_list = self.find_elements_by_webdriverwaite(browser, ele_tuple)
        self.click_element(ele_list[index])


    # 判断元素在不在页面上俄
    def element_to_be_present_in_web_or_not(self, browser, ele_tuple):
        ele_list = self.find_elements_by_webdriverwaite(browser, ele_tuple)
        if len(ele_list) == 0:
            return False
        else:
            return True

    # 定义方法，实现截图
    def get_web_picture(self,browser,  picture_path):
        shijianchuo = sys_operation().get_shijianchuo()  # 实例化sys_operation类的对象，调用get_shijianchuo获取时间戳
        file = picture_path +"\\"+shijianchuo+ ".png"
        sleep(2)  # 等页面加载出来再截图
        browser.get_screenshot_as_file(file)

    # 定义方法，实现获取警告窗口对象
    def get_alert_window_object(self,browser):
        waiter = self.get_webdriver_waite_object(browser)  # 获取动态等待的对象
        alert_window = waiter.until(ec.alert_is_present())  #获取告警窗对象
        return alert_window

    #实现点击告警窗口确定
    def get_alert_window_and_accept(self,browser):
        alert_window = self.get_alert_window_object(browser)
        alert_window.accept()

    # 实现点击告警窗口取消
    def get_alert_window_and_dismiss(self, browser):
        asert_window = self.get_alert_window_object(browser)
        asert_window.dismiss()

    #实现按照索引切换网页
    def switch_to_window_by_index(self, browser, index):
        # 获取打开网页的句柄
        hand_list = browser.window_handles
        #按照索引切换
        browser.switch_to.window(hand_list[index])

    #实现动态切入框架
    def switch_to_frame_by_webdriverwait(self, browser, ele_tuple):
        waiter = self.get_webdriver_waite_object(browser)
        waiter.until(ec.frame_to_be_available_and_switch_to_it(ele_tuple))


    # 实现判断网页标题是否等于某段字符串，是返回True，不是返回False
    def title_is_text_or_not(self, browser, text):
        waiter = self.get_webdriver_waite_object(browser)
        bool_value = waiter.until(ec.title_is(text))
        return bool_value

    #实现去除某个元素的某个属性方法
    def remove_attribute_from_element(self, browser, ele_tuple, attributename):
        ele = self.find_element_by_webdriverwaite(browser, ele_tuple)  #定位元素
        js = 'arguments[0].removeAttribute("%s")'%attributename  # 去除元素属性的js语句
        browser.execute_script(js, ele)  # 执行js语句
        return ele

    # 实现去除某个元素的只读属性
    def remove_readonly_from_element(self, browser, ele_tuple):
        ele = self.remove_attribute_from_element(browser, ele_tuple, "readonly")
        return ele

    #实现去除某个元素的只读属性并填写值
    def remove_readonly_from_element_and_sendkeys(self, browser, ele_tuple, value):
        ele = self.remove_readonly_from_element(browser, ele_tuple)
        ele.send_keys(value)

    # 根据按钮名去点击
    def click_button_by_button_name(self, browser, button_name):
        ele_tuple = (By.XPATH, '//button[text()= "%s"]'%button_name)
        self.find_element_and_click(browser, ele_tuple)

    # 根据文本去点击
    def click_text_by_text_content(self,browser,text_content):
        ele_tuple = (By.XPATH, '//span[text() = "%s"]'%text_content)
        self.find_element_and_click(browser,ele_tuple)

    # 根据文本去点击
    def click_text_by_contains_text_content(self, browser, text_content):
        ele_tuple = (By.XPATH, '//span[contains(text(), "%s")]' % text_content)
        self.find_element_and_click(browser, ele_tuple)

    # 定位元素实现鼠标悬停并点击
    def find_element_and_mouse_hover(self,browser,ele_tuple):
        ele = self.find_element_by_webdriverwaite(browser, ele_tuple)
        ActionChains(browser).move_to_element(ele).click(ele).perform()

    # 定位多元素实现鼠标悬停并点击
    def find_elements_and_mouse_hover(self, browser, ele_tuple,index):
        ele_list = self.find_elements_by_webdriverwaite(browser, ele_tuple)
        ActionChains(browser).move_to_element(ele_list[index]).perform()