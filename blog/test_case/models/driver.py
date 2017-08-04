from selenium.webdriver import Remote
#from selenium import webdriver

def browser () :
    # driver = webdriver.Chrome('/usr/bin/chromedriver')
    host = '127.0.0.1:4444'
    dc = {'plantform': 'ANY',
          'browserName': 'chrome',
          'version': '',
          'javascriptEnabled': True
          }
    driver = Remote(command_executor='http://' + host + '/wd/hub', desired_capabilities=dc)
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get("https://www.baidu.com")
    print(dr.title)
    dr.quit()