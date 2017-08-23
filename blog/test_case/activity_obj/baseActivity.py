from appium.webdriver.common.touch_action import TouchAction
import abc

class baseActivity(object):
    '''
    页面基础类,用于所有页面的继承
    '''
    def __init__(self, driver):
        self.driver = driver
        self.touchAction = TouchAction(self.driver)
    @abc.abstractmethod
    def open(self):
        """open"""

    @abc.abstractmethod
    def find_element(self, id):
        """Returns the element."""
    def tap_e(self, element):
        self.touchAction.tap(element=element).release().perform()
    def tap_xy(self, x, y):
        self.touchAction.tap(x=x, y=y).release().perform()

    @abc.abstractmethod
    def get_desired_capabilities(self):
        """Returns the desired_capabilities."""