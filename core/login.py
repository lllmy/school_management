import hashlib
from conf import settings
from lib.mylogger import Logger

def get_pwd(user,pwd):
    # Manager  123456
    # Teacher  900420
    # Student  987654
    m=hashlib.md5(user.encode('utf-8'))
    m.update(pwd.encode('utf-8'))
    return m.hexdigest()
def login():
    i=0
    while i<3:
        username=input('username: ').strip()
        password=input('password: ').strip()
        password=get_pwd(username,password)
        f = open(settings.userinfo_path)
        for line in f:
            user, pwd, role = line.strip().split('|')
            if user == username and pwd == password:
                print('\033[1;32m登陆成功\33[0m')
                Logger.logger.info('%s登陆成功'%user)
                f.close()
                return username, role
        else:
            print('\033[1;31m登录失败,还有%s次机会\033[0m' % (2 - i))
            f.close()
        i += 1
if __name__=='__main__':
    login()
