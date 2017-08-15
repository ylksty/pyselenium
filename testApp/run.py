from HTMLTestRunner import HTMLTestRunner
import unittest, sys
import time
import shutil
sys.path.append("./models")
from models import funs

def remove_dir(dir):
     shutil.rmtree(dir)

if __name__ == '__main__':
    funs.del_files('./app/report/images')
    funs.del_files('./app/report/logs')
    now = time.strftime("%Y-%m-%d_%H:%M:%S")
    filename = './app/report/logs/' + now + '_' + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='cgtzApp测试报告',
                            description='andorid')
    discover = unittest.defaultTestLoader.discover('./app/test_case',
                                                   pattern='*_sta.py')
    runner.run(discover)
    fp.close()