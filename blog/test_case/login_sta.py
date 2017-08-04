from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import login

class loginTest(myunit.MyTest):
    '''社区登录测试'''

    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)

    def test_test(self):



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
