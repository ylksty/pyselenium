import os
from datetime import datetime

def insert_img(driver, file_name):
    now = datetime.now()
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/test_case')[0]
    print(base)
    file_path = base + "/report/images/" + now.strftime('%Y-%m-%d_%H:%M:%S') + '_' + file_name  + '.jpg'
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = browser()
    driver.get("https://www.baidu.com/")
    insert_img(driver, 'baidu.jpg')
    driver.quit()
