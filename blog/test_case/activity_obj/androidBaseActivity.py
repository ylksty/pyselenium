from .baseActivity import baseActivity

class androidBaseActivity(baseActivity):
    '''
    页面基础类,用于所有页面的继承
    '''
    def find_element(self, id):
        return self.driver.find_element_by_android_uiautomator('new UiSelector().resourceIdMatches(".*id/' + id + '")')
    def tap(self, element):
        self.touchAction.tap(element=element).release().perform()

    def get_desired_capabilities(app):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '4.2',
            'deviceName': 'Android Emulator',
            'app': '../../apps/' + app,
            'newCommandTimeout': 240
        }
        return desired_caps
    def editClear(self, driver, el):
        el.click()
        driver.keyevent(123)
        textLength = len(str(el.text))
        for i in range(0, textLength):
            driver.keyevent(67)