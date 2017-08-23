from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./activity_obj")
from models import appunit, function
from activity_obj.androidLoginNewActivity import androidLoginNewActivity
from activity_obj.androidMainActivity import androidMainActivity

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class loginTest(appunit.androidTest):
    def user_login_locle(self, username="", password=""):
        androidLoginNewActivity(self.driver).user_login(username, password)
    # def test_a_login_usernull(self):
    #     '''用户名为空登录'''
    #     # 用户名为空登录
    #     self.user_login_locle()
    #     activity = self.driver.current_activity
    #     self.assertEqual('.ui.LoginNewActivity', activity)
    # def test_b_login_passnull(self):
    #     '''密码为空登录'''
    #     self.user_login_locle(username='18658870960', password='')
    #     activity = self.driver.current_activity
    #     self.assertEqual('.ui.LoginNewActivity', activity)
    # def test_c_login_passerr(self):
    #     '''用户名正确\密码错误登录'''
    #     self.user_login_locle('18658870960', 'ssssss22')
    #     activity = self.driver.current_activity
    #     self.assertEqual('.ui.LoginNewActivity', activity)
    def test_z_login(self):
        '''正常登录'''
        self.user_login_locle('18658870960', 'ssssss2')
        androidMainActivity(self.driver).click_tv_first_login_left()
        self.driver.wait_activity('.ui.MainActivity', 10)
        activity = self.driver.current_activity
        self.assertEqual('.ui.MainActivity', activity)

if __name__ == "__main__":
    unittest.main()
