from .androidBaseActivity import androidBaseActivity

class androidMainActivity(androidBaseActivity) :
    main_tv_first_login_left_loc = 'tv_first_login_left'

    # 点击以后再说
    def click_tv_first_login_left(self):
        el_tag_mine = self.find_element(self.main_tv_first_login_left_loc)
        self.tap_e(element=el_tag_mine)

