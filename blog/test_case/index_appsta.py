from time import sleep
import time
import unittest, random, sys
import logging
from models import function
from appium.webdriver.common.touch_action import TouchAction

from appium import webdriver

class loginTest(unittest.TestCase):
    '''首页测试'''

    # 测试首页

    def test_test(self):
        now = time.strftime("%Y-%m-%d_%H:%M:%S")
        driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', {"platformName": "Android", "platformVersion": "6.0", "appPackage": "cgtz.com.cgtz",
                    "appActivity": ".ui.LoginNewActivity", "deviceName": "deviceName", "time": now})

        print(driver.current_activity)
        # function.insert_img(driver, 'appogin')

        # el = driver.find_element_by_accessibility_id("cgtz.com.cgtz.ui.LoginNewActivity:id/et_phone_num")
        # action = TouchAction(driver)
        # action.tap(el).perform()

        # els = driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        # print(els)
        action = TouchAction(driver)
        action.tap(x=200, y=200).release().perform()
        sleep(1)
        print(driver.current_activity)
        el_button = driver.find_element_by_android_uiautomator('new UiSelector().resourceIdMatches(".*id/tv_login")')
        action.tap(element=el_button).release().perform()
        sleep(1)

        el_phone = driver.find_element_by_android_uiautomator('new UiSelector().resourceIdMatches(".*id/et_phone_num$")')
        driver.set_value(el_phone, '18658870960')
        el_pass = driver.find_element_by_android_uiautomator('new UiSelector().resourceIdMatches(".*id/et_pwd")')
        driver.set_value(el_pass, 'ssssss2')
        action.tap(element=el_button).release().perform()
        sleep(1)
        print(driver.current_activity)

        # sleep(5)

        driver.quit()

        # # 跳转到指定页面并在该页面所以用元素id进行交互
        # driver.get('http://saucelabs.com/test/guinea-pig');
        # div = driver.find_element_by_id('i_am_an_id')
        # # 检查文本是否符合预期
        # assertEqual('I am a div', div.text)
        #
        # # 通过id查找评论框并输入
        # driver.find_element_by_id('comments').send_keys('My comment')
        #
        # # 关闭应用
        # driver.quit()


    # def test_login_1(self):
    #     '''用户名\密码为空登录'''
    #     self.user_login_verify()
    #     po = login(self.driver)
    #     function.insert_img(self.driver, 'user_pawd_empty')

    # def test_login_2(self):
    #     '''用户名正确\密码为空登录'''
    #     self.user_login_verify(username='186588709602')
    #     po = login(self.driver)
    #     function.insert_img(self.driver, 'pawd_empty')

if __name__ == "__main__":
    unittest.main()
