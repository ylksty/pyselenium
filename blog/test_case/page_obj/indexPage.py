from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class indexPage(Page):
    '''
    首页
    '''

    url = '/'

    def index(self):
        self.open()
        print('2333')