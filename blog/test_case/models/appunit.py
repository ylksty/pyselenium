from .appdriver import androidriver, iosdriver
import unittest

class androidTest(unittest.TestCase):
    driver = {}
    def setUp(self):
        self.driver = androidriver()

    def tearDown(self):
        self.driver.quit()