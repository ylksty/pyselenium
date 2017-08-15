import os
import shutil

def del_files(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)
        os.mkdir(dir)

if __name__ == '__main__':
    print('test')
