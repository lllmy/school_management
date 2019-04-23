import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))
#os.getcwd是当前目录，再dir是school_managment
from core import main
if __name__=='__main__':
    main.main()#main模块的main函数
#这三句话是固定的