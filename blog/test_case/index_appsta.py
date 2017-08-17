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
                    "appActivity": ".ui.MainActivity", "deviceName": "deviceName", "time": now})

        # sleep(1)
        # print('1' + driver.current_activity) # .ui.Guide_activity
        # driver.swipe(start_x=350, start_y=250, end_x=20, end_y=250, duration=200)
        # sleep(1)
        # driver.swipe(start_x=250, start_y=250, end_x=20, end_y=250, duration=200)
        # sleep(1)
        # driver.swipe(start_x=250, start_y=250, end_x=20, end_y=250, duration=200)
        # sleep(1)
        # driver.swipe(start_x=250, start_y=250, end_x=20, end_y=250, duration=200)
        # sleep(1)
        # print('2' + driver.current_activity)

        action = TouchAction(driver)
        el_mine = driver.find_element_by_android_uiautomator('new UiSelector().resourceIdMatches(".*id/layout_main_mine")')
        action.tap(element=el_mine).release().perform() # 点击我的
        print('3' + driver.current_activity) # .ui.Guide_activity
        action.tap(x=200, y=200).release().perform() # 指引点击
        print('4' + driver.current_activity) # .ui.LoginNewActivity
        el_button = driver.find_element_by_android_uiautomator('new UiSelector().resourceIdMatches(".*id/tv_login")')
        action.tap(element=el_button).release().perform() # 点击登录

        el_phone = driver.find_element_by_android_uiautomator('new UiSelector().resourceIdMatches(".*id/et_phone_num")')
        driver.set_value(el_phone, '18658870960') # 输入手机
        el_pass = driver.find_element_by_android_uiautomator('new UiSelector().resourceIdMatches(".*id/et_pwd")')
        driver.set_value(el_pass, 'ssssss2') # 输入密码
        action.tap(element=el_button).release().perform() # 点击登录
        print('5' + driver.current_activity)

        el_asklater = driver.find_element_by_android_uiautomator('new UiSelector().resourceIdMatches(".*id/tv_first_login_left")')
        action.tap(element=el_asklater).release().perform() # 点击以后再说

        sleep(5)

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
