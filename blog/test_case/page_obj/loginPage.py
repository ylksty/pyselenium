from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    '''
    用户登录页面
    '''

    url = '/'

    # Action
    cgtz_login_user_loc = (By.XPATH, "//*[@id='topHeader']/div/div/a[1]")

    def cgtz_login(self):
        self.find_element(*self.cgtz_login_user_loc).click()
        sleep(1)

    login_username_loc = (By.XPATH, "//*[@id='LoginForm_username']")
    login_password_loc = (By.XPATH, "//*[@id='LoginForm_password']")
    login_button_loc = (By.XPATH, "//*[@id='submit']")

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一登录入口
    def user_login(self, username="username", password="1111"):
        self.open()
        self.cgtz_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)