class loginTest():
    '''首页测试'''

    def test_test(self):
        po = indexPage(self.driver, base_url='https://www.cgtz.com')
        po.index()
        function.insert_img(self.driver, 'index')

if __name__ == "__main__":
    unittest.main()