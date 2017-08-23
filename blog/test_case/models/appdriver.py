from appium.webdriver import Remote
import os

def androidriver () :
    # driver = Remote('http://0.0.0.0:4723/wd/hub', {"platformName": "Android", "platformVersion": "6.0", "appPackage": "cgtz.com.cgtz", "appActivity": ".ui.MainActivity", "deviceName": "deviceName"})
    driver = Remote('http://0.0.0.0:4723/wd/hub', get_android_desired_capabilities('cgtz_V4.0.1_test.apk'))
    return driver

def iosdriver () :
    driver = 0
    return driver

def get_android_desired_capabilities(app):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.0',
        'deviceName': 'Android Emulator',
        'app': os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/apps/' + app)),
        'newCommandTimeout': 60,
        'appActivity': '.ui.MainActivity'
    }
    return desired_caps