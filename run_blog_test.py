from HTMLTestRunner import HTMLTestRunner
import unittest, sys
import time
import shutil
sys.path.append("./models")
from models import funs

def remove_dir(dir):
     shutil.rmtree(dir)

if __name__ == '__main__':
    funs.del_files('./blog/report/images')
    funs.del_files('./blog/report/logs')
    # now = time.strftime("%Y-%m-%d_%H:%M:%S")
    now = time.strftime("%Y-%m-%d")
    filename = './blog/report/logs/' + now + '_' + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='cgtz测试报告',
                            description='环境win7 浏览器:chrome')
    discover = unittest.defaultTestLoader.discover('./blog/test_case',
                                                   pattern='*_appsta.py')
    runner.run(discover)
    fp.close()
