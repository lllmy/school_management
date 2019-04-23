import sys
#尽管main和login是在同一个包下边，但是程序是基于start执行的，所以要导入
from core import login
from core.manager import Manager
from core.teacher import Teacher
from core.student import Student
def main():
    ret=login.login()
    if ret:
        user,role=ret
        cls=getattr(sys.modules[__name__],role)#就找到了一个类
        #是当我自己执行的时候就是我的函数的名字，但是当模块导入的时候就是模块名
        #然后进行实例化：
        obj=cls(user)
        while True:
            for num,item in enumerate(cls.operate_lst,1):
                print(num,item[0])
            num = int(input('请输入你要操作的序号：'))
            getattr(obj,cls.operate_lst[num-1][1])()



