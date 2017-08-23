from time import sleep
import time
import unittest, random, sys
import logging
from models import function
from appium.webdriver.common.touch_action import TouchAction

from appium import webdriver

class loginTest(unittest.TestCase):
    '''android_登录测试'''

    # 测试首页

    def test_test(self):
        driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', {"platformName": "Android", "platformVersion": "6.0", "appPackage": "cgtz.com.cgtz",
                    "appActivity": ".ui.MainActivity", "deviceName": "deviceName"})

        # function.insert_img(driver, 'hello')
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
        self.assertIsNotNone(el_mine)
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

        sleep(2)
        driver.quit()

if __name__ == "__main__":
    unittest.main()
