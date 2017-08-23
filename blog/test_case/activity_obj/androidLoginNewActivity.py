from .androidBaseActivity import androidBaseActivity

class androidLoginNewActivity(androidBaseActivity) :
    login_username_loc = 'et_phone_num'
    login_password_loc = 'et_pwd'
    login_button_loc = 'tv_login'

    tag_mine = 'layout_main_mine'

    # 点击我的
    def click_tag_mine(self):
        el_tag_mine = self.find_element(self.tag_mine)
        self.tap_e(element=el_tag_mine)

    # 点击指引
    def click_guide(self):
        self.tap_xy(x=200, y=200)

    # 登录用户名
    def login_username(self, username):
        el_phone = self.find_element(self.login_username_loc)
        self.editClear(self.driver, el_phone) # 清空
        self.driver.set_value(el_phone, username) # 输入手机

    # 登录密码
    def login_password(self, password):
        el_pass = self.find_element(self.login_password_loc)
        self.editClear(self.driver, el_pass) # 清空
        self.driver.set_value(el_pass, password) # 输入密码

    # 登录按钮
    def login_button(self):
        el_button = self.find_element(self.login_button_loc)
        self.tap_e(element=el_button) # 点击登录

    # 定义统一登录入口
    def user_login(self, username="", password=""):
        self.click_tag_mine()
        self.click_guide()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
